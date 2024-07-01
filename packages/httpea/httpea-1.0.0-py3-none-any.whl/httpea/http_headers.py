from __future__ import annotations

from typing import Generator, KeysView, Optional, Sequence, Union, ValuesView


def _parseparam(s: str):
    while s[:1] == ";":
        s = s[1:]
        end = s.find(";")
        while end > 0 and (s.count('"', 0, end) - s.count('\\"', 0, end)) % 2:
            end = s.find(";", end + 1)
        if end < 0:
            end = len(s)
        f = s[:end]
        yield f.strip()
        s = s[end:]


def parse_header(line: str):
    parts = _parseparam(";" + line)
    key = parts.__next__()
    pdict = {}
    for p in parts:
        i = p.find("=")
        if i >= 0:
            name = p[:i].strip().lower()
            value = p[i + 1 :].strip()
            if len(value) >= 2 and value[0] == value[-1] == '"':
                value = value[1:-1]
                value = value.replace("\\\\", "\\").replace('\\"', '"')
            pdict[name] = value
    return key, pdict


def _normalize_header_name(name: str) -> str:
    """
    According to rfc https://www.ietf.org/rfc/rfc2616.txt header names are case insensitive,
    thus they can be normalized to ease usage of Headers class.
    :param name:
    :return:
    """
    name = name.lower()
    if name.startswith("http_"):
        name = name[5:]

    return name.replace("_", "-")


def _normalize_headers(headers: dict) -> dict:
    normalized = {}
    for name, value in headers.items():
        if isinstance(value, list):
            normalized[_normalize_header_name(name)] = [str(item) for item in value]
        else:
            normalized[_normalize_header_name(name)] = [str(value)]

    return normalized


class HttpHeaders:
    """
    Dict-like object containing http headers. Header names are case-insensitive, and
    their values are internally stored as sequences to conform RFC-2616 standard.
    .. _RFC-2616 Section 4.2: https://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html#sec4.2
    """

    def __init__(self, headers: Optional[dict] = None):

        headers = {} if headers is None else headers
        self._headers = _normalize_headers(headers)

    def set(self, name: str, value: str) -> None:
        """
        Appends new value to the header, if header does not exist it will get created.
        """
        normalized_name = _normalize_header_name(name)
        if normalized_name not in self._headers:
            self._headers[normalized_name] = []

        self._headers[normalized_name].append(value)

    def override(self, name: str, value: Union[str, list]) -> None:
        normalized_name = _normalize_header_name(name)
        self._headers[normalized_name] = value if isinstance(value, list) else [value]

    def get(self, name: str, default: str = "") -> Union[str, Sequence[str]]:
        if name in self:
            return self.__getitem__(name)
        return default

    def __setitem__(self, name: str, value: Sequence[str]) -> None:
        """
        Sets value for header. Value must be valid sequence of strings.
        """
        self._headers[_normalize_header_name(name)] = value

    def __getitem__(self, name: str) -> Union[str, Sequence[str]]:
        """
        Returns string if header is unique otherwise sequence of strings is returned.
        """
        value = self._headers.get(_normalize_header_name(name), None)
        if value is None:
            return ""

        if len(value) == 1:
            return value[0]

        return value

    def __contains__(self, name: str) -> bool:
        return _normalize_header_name(name) in self._headers

    def items(self) -> Generator:
        for key, values in self._headers.items():
            if len(values) == 1:
                yield key, values[0]
                continue
            for value in values:
                yield key, value

    def values(self) -> ValuesView[Union[str, Sequence[str]]]:
        return self._headers.values()

    def keys(self) -> KeysView[str]:
        return self._headers.keys()

    def __repr__(self) -> str:
        return str(self._headers)

    def __eq__(self, other) -> bool:
        if not isinstance(other, HttpHeaders):
            return False

        return self._headers == other._headers

    def __copy__(self) -> HttpHeaders:
        copy = HttpHeaders.__new__(HttpHeaders)
        copy._headers = {
            key: [item for item in value] for key, value in self._headers.items()
        }

        return copy


__all__ = ["HttpHeaders", "parse_header"]
