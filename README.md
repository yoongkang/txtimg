# TxtImg

A library to easily create text-based images (e.g. images that primarily contain text).

This is just a thin layer on top of Pillow.

## Installation

This is compatible with Python 3.6 and above.

Run the following command to install:

```
$ pip install txtimg
```

## Example

```python
from txtimg import TxtImg

text = """
What did Sushi A say to Sushi B?

What's up B? (WASABI)
"""

t = TxtImg()
img = t.generate_from_text(text)
img.save("wasabi.png")
```

## Configuration

You can specify parameters to the `TxtImg` constructor:


* font - Font used for your text. This is a PIL ImageFont object
* base_img - You can specify a base image to use, rather than the default white background. This is a PIL Image object.
* horizontal_margin - Horizontal margin in pixels
* vertical_margin - Vertical margin in pixels
* chars_per_row - Number of characters per row
* txt_color - A tuple representing the RGB values, e.g. (255, 0, 0) for red.


