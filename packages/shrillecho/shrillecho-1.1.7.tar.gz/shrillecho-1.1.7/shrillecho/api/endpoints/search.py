from typing import List
from shrillecho.api.endpoints.endpoint import Endpoint
from shrillecho.api.endpoints.endpoint_urls import SPOTIFY_URLS
from shrillecho.types.artist_types import Artist
from shrillecho.types.search_types import SearchResult


class SearchEndpoint(Endpoint):

    async def search_item(
        self, query: str, query_type: List[str], **kwargs
    ) -> SearchResult:

        url = SPOTIFY_URLS.SEARCH.ITEM

        return await self._request_handler.make_request(
            method="GET",
            url=url,
            query_params={**{"q": query, "type": query_type}, **kwargs},
            response_type=SearchResult,
        )
