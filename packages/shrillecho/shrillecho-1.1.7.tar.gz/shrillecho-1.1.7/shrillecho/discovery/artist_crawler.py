import asyncio
from collections import deque
from dataclasses import asdict
import json
from typing import List, Set, Tuple

from pymongo import MongoClient
from shrillecho.api.api_client import SpotifyClient
from shrillecho.controllers.artist_controller import ArtistController
from shrillecho.types.artist_types import Artist
from shrillecho.utility.artist_utils import ArtistUtils
from shrillecho.utility.cache import Mongo
from shrillecho.utility.neo4j import NeoController


class Mongo:
    def __init__(self, domain: str, port: str, db: str = None):
        self._mongo_client = MongoClient(f"mongodb://{domain}:{port}/")
        self._db = self._mongo_client[db]

    def insert_document(self, collection_name: str, document: dict):
        collection = self._db[collection_name]
        collection.insert_one(document)

    def initialise_artist_state(self, artist: Artist) -> List[Artist]:
        collection = self._db["graph_state"]
        document = collection.find_one({"_id": artist.id})
        if not document:

            new_artist_state = {"_id": artist.id, "exp": [], "unexp": [asdict(artist)]}

            if collection.insert_one(new_artist_state):
                print("inserted new artist state okay")
            else:
                print("insertion failure")
                exit(1)

    def update_array(self, artist: Artist, array_type: str, new_array) -> List[Artist]:
        collection = self._db["graph_state"]
        collection.update_one(
            {"_id": artist.id},
            {"$set": {array_type: [asdict(item) for item in new_array]}},
        )

    def pop_unexplored(self, artist: Artist) -> Artist:
        collection = self._db["graph_state"]

        unexplored = collection.find_one_and_update(
            {"_id": artist.id}, {"$pop": {"unexp": -1}}, return_document=True
        )

        return Artist.from_json(json.dumps(unexplored))

    def get_explored_states(self, artist: Artist):
        collection = self._db["graph_state"]

        state = collection.find_one({"_id": artist.id})
        if state:

            return {
                "exp": [Artist.from_json(json.dumps(a)) for a in state["exp"]],
                "unexp": [Artist.from_json(json.dumps(a)) for a in state["unexp"]],
            }
        else:

            data = {"_id": artist.id, "exp": [], "unexp": [asdict(artist)]}

            collection.insert_one(data)

            return {
                "exp": [],
                "unexp": [Artist.from_json(json.dumps(a)) for a in data["unexp"]],
            }


class ArtistCrawler:

    def __init__(self, sp: SpotifyClient):
        self._sp = sp
        self._neo = NeoController(username="neo4j", password="Zxasqw12")
        self._mongo = Mongo("localhost", "27017", "shrillecho")

    # async def bfs_related(self, start: Artist, max_depth: int = 2) -> List[Artist]:

    #     unexpanded, expanded = self._mongo.get_graph_state()
    #     # unexpanded: deque[Tuple[Artist, int]] = deque([(start, 0)])

    #     while unexpanded:

    #         cur_artist, depth = unexpanded.popleft()

    #         if cur_artist.id not in expanded and depth <= max_depth:

    #             related_artists: List[Artist] = await self._sp.artists.related(artist_id=cur_artist.id)
    #             expanded.add(cur_artist.id)

    #             for artist in related_artists:
    #                 if depth + 1 < max_depth and artist.id not in expanded:
    #                     unexpanded.append((artist, depth + 1))

    #     return await ArtistUtils.fetch_several_artists(sp=self._sp,artist_ids=list(expanded))

    def get_full_list(self, expanded, unexpanded) -> List[Artist]:
        expanded_list = list(expanded)
        expanded_list.extend(list(set(unexpanded)))
        return expanded_list

    async def related(self, artist: str) -> List[Artist]:
        return await self._sp.artists.related(artist_id=artist)

    async def bfs_related_state(
        self, start: Artist, cursor: Artist = 0, limit: int = 50
    ) -> List[Artist]:
        graph_state = self._mongo.get_explored_states(artist=start)

        expanded = set(graph_state["exp"])
        unexpanded = deque(graph_state["unexp"])

        while True:

            batch: List[Artist] = []

            for _ in range(0, min(len(unexpanded), 50)):
                cur_artist: Artist = unexpanded.popleft()
                batch.append(cur_artist)

            if any(batch) not in expanded:

                related_artists: List[List[Artist]] = await asyncio.gather(
                    *[self.related(ba.id) for ba in batch]
                )
                flatten_related = [
                    item for sublist in related_artists for item in sublist
                ]

                for item in batch:
                    expanded.add(item)

                for artist in flatten_related:
                    if artist not in expanded:
                        unexpanded.append((artist))

            self._mongo.update_array(artist=start, array_type="exp", new_array=expanded)
            self._mongo.update_array(
                artist=start, array_type="unexp", new_array=unexpanded
            )
