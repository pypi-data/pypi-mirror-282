from __future__ import annotations

from typing import Any, Dict
from urllib.parse import unquote_plus


def build_dict_from_path(path: str, value) -> Dict[str, Any]:
    """
    Creates dictionary representing passed path with given value.
    For example: [some][path] will be turned to {"some":{"path": value}} dict.
    :param path:
    :param value:
    :return:
    """
    starting_bracket = path.find("[")
    if starting_bracket == 0:
        raise ValueError("Path cannot start with [")
    if path[-1:] != "]":
        return {path: value}
    parsed_path = [path[:starting_bracket]]
    parsed_path = parsed_path + path[starting_bracket + 1 : -1].split("][")

    for part in parsed_path:
        if "[" in part or "]" in part:
            return {path: value}

    def _create_leaf(_parsed_path: list):
        if len(_parsed_path) == 1:
            if not _parsed_path[0]:
                return [value]

            return {_parsed_path[0]: value}
        if not _parsed_path[0]:
            return [_create_leaf(_parsed_path[1:])]

        return {_parsed_path[0]: _create_leaf(_parsed_path[1:])}

    return _create_leaf(parsed_path)


def deep_merge(base: Dict[str, Any], extension: Dict[str, Any]) -> Dict[str, Any]:
    for key in extension:
        if key in base:
            if isinstance(base[key], dict) and isinstance(extension[key], dict):
                base[key] = deep_merge(base[key], extension[key])
            elif isinstance(base[key], list) and isinstance(extension[key], list):
                base[key] = base[key] + extension[key]
            elif isinstance(extension[key], list):
                base[key] = [base[key]] + extension[key]
            elif isinstance(extension[key], dict):
                base[key] = {"": base[key], **extension[key]}
            else:
                base[key] = [base[key], extension[key]]
        else:
            base[key] = extension[key]
    return base


def parse_qs(query: str) -> Dict[str, Any]:
    """
    Parse query string with json forms support, more available in the following link
    https://www.w3.org/TR/html-json-forms/
    :param query:
    :return:
    """
    result: Dict[str, Any] = {}
    if query == "":
        return result

    for item in query.split("&"):
        (name, value) = item.split("=")
        value = parse_qs_value(value)
        name = unquote_plus(name)
        if "[" in name:
            result = deep_merge(result, build_dict_from_path(name, value))
        elif name in result:
            if isinstance(result[name], list):
                result[name].append(value)
            else:
                result[name] = [result[name], value]
        else:
            result[name] = value

    return result


def parse_qs_value(value: str) -> Any:
    value = unquote_plus(value)
    if value == "true":
        return True

    if value == "false":
        return False

    if len(value) > 1 and value[0] == "0" and value[1] != ".":
        return value

    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value)
    except ValueError:
        pass

    return value


class HttpQueryString(dict):
    def __init__(self, string: str):
        self._str = string
        super().__init__(parse_qs(string))

    def __getitem__(self, key) -> Any:
        return self.get(key)

    def __repr__(self):
        return self._str

    def __str__(self) -> str:
        return self._str

    def __eq__(self, other) -> bool:
        if not isinstance(other, HttpQueryString):
            return False

        return other._str == self._str


__all__ = ["HttpQueryString", "build_dict_from_path", "parse_qs", "parse_qs_value"]
