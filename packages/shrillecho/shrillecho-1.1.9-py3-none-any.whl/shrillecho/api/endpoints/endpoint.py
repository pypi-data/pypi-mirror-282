from abc import ABC
import math
from typing import Dict, List
from shrillecho.api.api_request_handler import SpotifyApiRequestHandler
from shrillecho.api.task_scheduler import TaskScheduler


class Endpoint(ABC):
    def __init__(self, api_request_handler):
        self._request_handler: SpotifyApiRequestHandler = api_request_handler
        self._task_scheduler: TaskScheduler = TaskScheduler()

    @staticmethod
    def _format_url_params(url_template: str, map: dict):
        url = url_template
        for key, value in map.items():
            placeholder = f"{{{key}}}"
            url = url.replace(placeholder, str(value))
        return url

    @staticmethod
    def _generate_pagination_batch_urls(initial_item) -> List[Dict[str, int]]:

        if not hasattr(initial_item, "total"):
            raise AttributeError("initial_item must have a .total attribute")

        query_param_dicts: List[dict] = []
        limit = 50
        pages = math.ceil(initial_item.total / limit)
        for page in range(1, pages):
            query_param_dicts.append({"limit": 50, "offset": limit * page})
        return query_param_dicts

    async def batch_get(
        self, url: str, response_type, initial_item, batch_size, **kwargs
    ):

        query_param_offsets = self._generate_pagination_batch_urls(
            initial_item=initial_item
        )

        tasks = [
            (
                self._request_handler._req_proxy,
                ("GET", url, response_type, {**query_params, **kwargs}),
            )
            for query_params in query_param_offsets
        ]

        self._task_scheduler.load_tasks(tasks)

        return await self._task_scheduler.execute_tasks(
            batch_size=batch_size, unpack=True
        )
