from .doc import Element, Doc, EscapedStr
from .formatting import Bold


class KeyValue(Element):
    title: Element
    value: Element
    suffix: Element

    def __init__(
            self,
            title: Element | str,
            value: Element | str,
            suffix: Element | str = ': ',
            title_bold: bool = True
    ):
        self.title = Bold(title) if title_bold else EscapedStr.if_needed(title)
        self.value = EscapedStr.if_needed(value)
        self.suffix = EscapedStr.if_needed(suffix)

    def __str__(self) -> str:
        return f'{self.title}{self.suffix}{self.value}'


class HList(Doc):
    prefix: Element
    divider: Element

    def __init__(
            self,
            *args: Element | str,
            prefix: Element | str = '',
            divider: Element | str = ' '
    ):
        super().__init__(*args)

        self.prefix = EscapedStr.if_needed(prefix)
        self.divider = EscapedStr.if_needed(divider)

    def __str__(self) -> str:
        text = ''
        for idx, item in enumerate(self):
            if idx > 0:
                text += str(self.divider)
            if self.prefix:
                text += str(self.prefix)
            text += str(item)

        return text
