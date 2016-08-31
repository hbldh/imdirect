#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
imdirect
========

The orientation of the photographed
object or scene with respect to the digital camera is encoded in the resulting
image's `Exif <https://en.wikipedia.org/wiki/Exif>`_ data (given that it is
saved as a JPEG).

When working with such digital camera images, this orientation might
lead to problems handling the image and is very often desired to be
counteracted. This module is a small extension to ``Pillow``, adding an
autorotate method that can be used for addressing this issue.

It will eventually feature a ``PIL.Image.Image`` subclass that autorotates
internally and updates and ports Exif data when saving the image to new file.

Usage
-----

Demonstration of the monkey patching and how it works.

.. code:: python

   from PIL import Image
   img = Image.open('2016-08-28 15.11.44.jpg')
   # Print image as string and the EXIF orientation.
   print(img)
   print("Orientation: {0}".format(img._getexif().get(274)))

   import imdirect
   img_autorotated = Image.open('2016-08-28 15.11.44.jpg')
   print(img_autorotated)
   print("Orientation: {0}".format(img_autorotated._getexif().get(274)))

The output of the above:

.. code:: python

   <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=4032x3024 at 0x7FC3238AC810>
   Orientation: 6
   <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3024x4032 at 0x7FC323875250>
   Orientation: 1

:copyright: 2016-08-30 by hbldh <henrik.blidh@nedomkull.com>

"""

import re

from ._autorotate import *


# Version information.
__version__ = '0.3.0.dev1'
version = __version__  # backwards compatibility name
try:
    version_info = [int(x) if x.isdigit() else x for x in
                    re.match('^([0-9]+)\.([0-9]+)[\.]*([0-9]*)(.*)$',
                             __version__, re.DOTALL).groups()]
except Exception:
    version_info = ()
