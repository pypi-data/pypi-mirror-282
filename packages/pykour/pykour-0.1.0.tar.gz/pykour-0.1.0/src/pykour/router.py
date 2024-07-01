from __future__ import annotations
from http import HTTPStatus
from typing import Any, Callable, Dict, Union


class Route:
    def __init__(self, path: str, method: str, handler: Any):
        self.path = path
        self.method = method
        self.handler = handler
        self.variables: Dict[str, str] = {}

    def set_variables(self, variables: Dict[str, str]):
        self.variables = variables


class Node:
    def __init__(self, part: str, is_wild: bool = False):
        self.part = part
        self.children: list[Node] = []
        self.is_wild = is_wild
        self.route_map: Dict[str, Route] = {}

    def insert(self, pattern: str, route: Route):
        parts = pattern.strip("/").split("/")

        node = self
        for part in parts:
            child = node.match_child(part)
            if not child:
                child = Node(
                    part,
                    part.startswith(":") or part.startswith("*") or part.startswith("{"),
                )
                node.children.append(child)
            node = child

        node.route_map[route.method] = route

    def search(self, path: str, method: str):
        parts = path.strip("/").split("/")
        variables = {}

        node = self
        for part in parts:
            child = node.match_child(part)
            if not child:
                return None, {}
            if child.is_wild:
                var_name = child.part.lstrip(":*{").rstrip("}")
                variables[var_name] = part
            node = child

        route = node.route_map.get(method)
        return route, variables

    def match_child(self, part: str):
        for child in self.children:
            if child.part == part or child.is_wild:
                return child
        return None


class Router:
    def __init__(self, prefix: str = ""):
        self.root = Node("")
        self.prefix = prefix.rstrip("/")

    def get(self, path: str, status_code: HTTPStatus = HTTPStatus.OK) -> Callable:
        return self.route("GET", path, status_code)

    def post(self, path: str, status_code: HTTPStatus = HTTPStatus.CREATED) -> Callable:
        return self.route("POST", path, status_code)

    def put(self, path: str, status_code: HTTPStatus = HTTPStatus.OK) -> Callable:
        return self.route("PUT", path, status_code)

    def delete(self, path: str, status_code: HTTPStatus = HTTPStatus.NO_CONTENT) -> Callable:
        return self.route("DELETE", path, status_code)

    def options(self, path: str, status_code: HTTPStatus = HTTPStatus.OK) -> Callable:
        return self.route("OPTIONS", path, status_code)

    def head(self, path: str, status_code: HTTPStatus = HTTPStatus.OK) -> Callable:
        return self.route("HEAD", path, status_code)

    def trace(self, path: str, status_code: HTTPStatus = HTTPStatus.OK) -> Callable:
        return self.route("TRACE", path, status_code)

    def patch(self, path: str, status_code: HTTPStatus = HTTPStatus.OK) -> Callable:
        return self.route("PATCH", path, status_code)

    def route(self, method: str, path: str, status_code: int) -> Callable:
        def decorator(func):
            self.add_route(path, method, (func, status_code))
            return func

        return decorator

    def add_route(self, path: str, method: str, handler: Any):
        if self.prefix:
            full_path = f"/{self.prefix}{path}"
        else:
            full_path = path
        route = Route(full_path, method, handler)
        self.root.insert(full_path, route)

    def add_router(self, router: Router):
        for child in router.root.children:
            self._merge_nodes(self.root, child, self.prefix)

    def get_route(self, path: str, method: str) -> Union[Route, None]:
        if self.prefix:
            if not path.startswith(f"/{self.prefix}"):
                return None
            path = path[len(self.prefix) + 1 :]
        route, variables = self.root.search(path, method)
        if route:
            route.set_variables(variables)
        return route

    def exists(self, path: str, method: str) -> bool:
        return self.get_route(path, method) is not None

    def _merge_nodes(self, parent: Node, child: Node, prefix: str):
        if prefix:
            full_part = f"{prefix}/{child.part}".strip("/")
        else:
            full_part = child.part.strip("/")

        existing_child = parent.match_child(full_part)
        if existing_child:
            for method, route in child.route_map.items():
                existing_child.route_map[method] = route
            for grandchild in child.children:
                self._merge_nodes(existing_child, grandchild, full_part)
        else:
            new_node = Node(full_part, child.is_wild)
            new_node.route_map = child.route_map.copy()
            parent.children.append(new_node)
            for grandchild in child.children:
                self._merge_nodes(new_node, grandchild, full_part)
