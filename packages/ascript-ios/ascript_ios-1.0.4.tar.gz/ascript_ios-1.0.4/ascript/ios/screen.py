from PIL.Image import Image

from ascript.ios import system


def capture(png_filename=None, format='pillow') -> bytes | Image:
    return system.client.screenshot(png_filename, format)
