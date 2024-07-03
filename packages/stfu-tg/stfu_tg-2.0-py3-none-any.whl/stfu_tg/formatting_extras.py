from .formatting import Bold
from .doc import Element, EscapedStr


class Title(Element):
    item: Element
    prefix: Element
    postfix: Element
    bold: bool

    def __init__(
            self,
            item: Element | str,
            prefix: Element | str = '[',
            postfix: Element | str = ']',
            bold: bool = True
    ):
        self.item = EscapedStr.if_needed(item)
        self.prefix = EscapedStr.if_needed(prefix)
        self.postfix = EscapedStr.if_needed(postfix)
        self.bold = bold

    def __str__(self) -> str:
        text = f"{self.prefix}{self.item}{self.postfix}"

        if self.bold:
            text = str(Bold(text))

        return text
