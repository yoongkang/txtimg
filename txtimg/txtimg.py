from PIL import ImageFont, Image, ImageDraw
import textwrap
import io
import math
from pathlib import Path


class TxtImg:
    def __init__(
        self,
        font: ImageFont = None,
        base_img: Image = None,
        horizontal_margin=40,
        vertical_margin=20,
        chars_per_row=80,
        txt_color=(0, 0, 0),
    ) -> None:
        self.font = font or self._default_font()
        self.base_img = base_img
        self.chars_per_row = chars_per_row
        self.horizontal_margin = horizontal_margin
        self.vertical_margin = vertical_margin
        self.txt_color = txt_color

    def generate_from_text(self, txt: str) -> Image:
        formatted_text = self._format_text(txt)
        img = self.base_img or self._default_img(formatted_text)
        draw = ImageDraw.Draw(img)
        draw.multiline_text(
            (self.horizontal_margin, self.vertical_margin),
            formatted_text,
            font=self.font,
            fill=self.txt_color,
        )
        return img

    def _format_text(self, txt: str) -> list:
        paragraphs = txt.split("\n\n")
        wrapped_paragraphs = [
            textwrap.wrap(p, width=self.chars_per_row) for p in paragraphs
        ]
        return "\n\n".join(["\n".join(x) for x in wrapped_paragraphs])

    def _default_font(self) -> ImageFont:
        filename = str((Path(__file__).parent / "fonts/Roboto-Regular.ttf").absolute())
        return ImageFont.truetype(filename, size=16)

    def _default_img(self, formatted_text) -> Image:
        dimensions = self._img_dimensions(formatted_text)
        return Image.new(mode="RGB", size=dimensions, color=(255, 255, 255))

    def _img_dimensions(self, formatted_text) -> tuple:
        width, height = self.font.getsize_multiline(formatted_text)
        return (
            width + 2 * (self.horizontal_margin),
            height + 2 * (self.vertical_margin),
        )
