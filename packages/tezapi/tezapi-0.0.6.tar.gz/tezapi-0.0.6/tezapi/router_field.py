from aiohttp.web_request import Request

from .middleware import Middleware
from .routes import Route


class Router:

    def __init__(self, prefix: str):
        self.middlewares: list[Middleware] = []
        self.routes = []
        self.prefix = prefix

    def _add_route(self, path, handler, method: str, **kwargs):
        route = {'method': method, 'path': path, 'handler': handler}
        route.update(kwargs)
        self.routes.append(route)

    def get(self, path: str):
        def wrapper(func):
            async def decorated(request: Request):
                route = Route(func)
                return await route(request)

            self._add_route(self.prefix + path, decorated, 'GET', name=func.__name__)
            return decorated

        return wrapper

    def post(self, path: str):
        def wrapper(func):
            async def decorated(request: Request):
                route = Route(func)
                return await route(request)

            self._add_route(self.prefix + path, decorated, 'GET', name=func.__name__)
            return decorated

        return wrapper

    def delete(self, path: str):
        def wrapper(func):
            async def decorated(request: Request):
                route = Route(func)
                return await route(request)

            self._add_route(self.prefix + path, decorated, 'GET', name=func.__name__)
            return decorated

        return wrapper

    def put(self, path: str):
        def wrapper(func):
            async def decorated(request: Request):
                route = Route(func)
                return await route(request)

            self._add_route(self.prefix + path, decorated, 'GET', name=func.__name__)
            return decorated

        return wrapper

    def middleware(self, path: str = '*', method: str = '*'):
        def wrapper(func):
            async def decorated(request: Request):
                route = Route(func)
                return await route(request)

            self.middlewares.append(Middleware(decorated, self.prefix + path, method))
            return decorated

        return wrapper
