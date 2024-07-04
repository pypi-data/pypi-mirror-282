from typing import List
from neo4j import GraphDatabase

from shrillecho.types.artist_types import Artist

# uri = "bolt://localhost:7687"
# username = "neo4j"
# password = "Zxasqw12"

# driver = GraphDatabase.driver(uri, auth=(username, password))

# def create_and_relate_artist(main_artist, other_artists):

#     def create_and_relate_artists(tx, main_artist: Artist, other_artists: List[Artist]):

#         main_artist_query = "MERGE (main:Artist {name: $main_artist}) RETURN main"
#         tx.run(main_artist_query, main_artist=main_artist.name)

#         for artist in other_artists:
#             # For each artist in the list, create or find the artist node and create a RELATED_TO relationship
#             artist_query = """
#             MERGE (other:Artist {name: $artist})
#             WITH other
#             MATCH (main:Artist {name: $main_artist})
#             MERGE (main)-[:RELATED_TO]->(other)
#             """
#             tx.run(artist_query, main_artist=main_artist.name, artist=artist.name)


#     with driver.session() as session:
#         session.execute_write(create_and_relate_artists, main_artist, other_artists)


class NeoController:

    def __init__(
        self,
        uri: str = "bolt://localhost:7687",
        username: str = None,
        password: str = None,
    ):
        if not (username and password):
            raise Exception("Provide authentication details!")

        self.__driver = GraphDatabase.driver(uri, auth=(username, password))

    def create_artist(self, tx, artist_name):
        query = "MERGE (a:Artist {name: $artist_name}) " "RETURN a"
        tx.run(query, artist_name=artist_name)

    def create_relationship(self, tx, artist_name, related_artist_name):
        query = (
            "MATCH (a:Artist {name: $artist_name}) "
            "MATCH (b:Artist {name: $related_artist_name}) "
            "MERGE (a)-[:RELATED_TO]->(b)"
        )
        tx.run(query, artist_name=artist_name, related_artist_name=related_artist_name)

    def set_unrelated_artist(self, tx):
        query = (
            "MATCH (a:Artist) "
            "WHERE NOT (a)-[:RELATED_TO]->() "
            "REMOVE a:Artist "
            "SET a:UnrelatedArtist, a.color = 'red'"
        )
        tx.run(query)

    def add_artists_with_relationships(self, artist_data):
        with self.__driver.session() as session:
            for artist in artist_data:
                artist_name = artist["name"]
                related_artists = artist["related"]
                session.write_transaction(self.create_artist, artist_name)
                for related_artist in related_artists:
                    session.write_transaction(self.create_artist, related_artist)
                    session.write_transaction(
                        self.create_relationship, artist_name, related_artist
                    )
            # Set unrelated artists after all nodes and relationships are created
            session.write_transaction(self.set_unrelated_artist)
