from PIL import Image, ImageDraw
from math import log, log2

MAX_ITER = 100


def mandelbrot(c):
    """_summary_

    Args:
        c (_type_): _description_

    Returns:
        _type_: _description_
    """
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z * z + c
        n += 1

    if n == MAX_ITER:
        return MAX_ITER

    return n + 1 - log(log2(abs(z)))


class MandelbrotFractal:
    def __init__(self, width=600, height=400) -> None:
        self.width = width
        self.height = height

        self.re_start = -2
        self.re_end = 1
        self.im_start = -1
        self.im_end = 1

        self.palette = []

        self.image = Image.new("RGB", (self.width, self.height), (0, 0, 0))
        self.draw_img = ImageDraw.Draw(self.image)

    def draw(self):
        pass

    def save(self, path="output.png"):
        self.image.save(path, "PNG")


class MandelbrotFractalBW(MandelbrotFractal):
    def __init__(self) -> None:
        super().__init__()

    def draw(self):
        """_summary_

        Args:
            path (str, optional): _description_. Defaults to 'output.png'.
        """

        for x in range(0, self.width):
            for y in range(0, self.height):

                c = complex(
                    self.re_start + (x / self.width) * (self.re_end - self.re_start),
                    self.im_start + (y / self.height) * (self.im_end - self.im_start),
                )
                m = mandelbrot(c)
                color = 255 - int(m * 255 / MAX_ITER)
                self.draw_img.point([x, y], (color, color, color))


class MandelbrotFractalColor(MandelbrotFractal):
    def __init__(self) -> None:
        super().__init__()

        self.image = Image.new("HSV", (self.width, self.height), (0, 0, 0))
        self.draw_img = ImageDraw.Draw(self.image)

    def draw(self):

        for x in range(0, self.width):
            for y in range(0, self.height):
                c = complex(
                    self.re_start + (x / self.width) * (self.re_end - self.re_start),
                    self.im_start + (y / self.height) * (self.im_end - self.im_start),
                )
                m = mandelbrot(c)
                hue = int(255 * m / MAX_ITER)
                saturation = 255
                value = 255 if m < MAX_ITER else 0
                self.draw_img.point([x, y], (hue, saturation, value))

    def save(self, path="output.png"):
        self.image.convert("RGB").save(path, "PNG")
