import html
from abc import ABC
from typing import Any, List


class Element(ABC):
    def __repr__(self):
        return f'<{self.__class__.__name__}>'

    def __add__(self, other):
        return Doc(self, other)

    def to_str(self, *args):
        return str(self)


class EscapedStr(Element, str):
    def __new__(cls, object: Any):
        return super().__new__(cls, html.escape(str(object), quote=False))

    @staticmethod
    def if_needed(item: Element | str) -> Element:
        return item if isinstance(item, Element) else EscapedStr(item)


class Doc(Element, List[Element]):
    # Contains child items
    # Also an abstract class for other arguments that contains child elements.

    def __init__(self, *items: Element | str):
        super().__init__(
            EscapedStr.if_needed(item) for item in items if item
        )

    def __str__(self) -> str:
        return '\n'.join(str(items) for items in self)

    def __iadd__(self, other: Element | str):  # type: ignore
        self.append(EscapedStr.if_needed(other))
        return self

    def __repr__(self):
        return f'<{self.__class__.__name__}>({self})'
