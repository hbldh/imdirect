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

.. code:: python

   In [1]: import imdirect

   In [2]: from PIL import Pillow

   In [3]: img = Image.open('2016-08-28 15.11.44.jpg')

   In [4]: imdirect.determine_orientation(img)
   Out[4]: 6

   In [5]: img
   Out[5]: <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=4032x3024 at 0x7F3DFD950990>

   In [6]: imdirect.autorotate(i)
   Out[6]: <PIL.Image.Image image mode=RGB size=4032x3024 at 0x7F3DFD89CED0>

:copyright: 2016-08-30 by hbldh <henrik.blidh@nedomkull.com>

"""

import re

from ._exceptions import ImDirectException
from ._pil import autorotate, determine_orientation

__all__ = ['autorotate', 'determine_orientation', 'ImDirectException']

# Version information.
__version__ = '0.2.0'
version = __version__  # backwards compatibility name
try:
    version_info = [int(x) if x.isdigit() else x for x in
                    re.match('^([0-9]+)\.([0-9]+)[\.]*([0-9]*)(.*)$',
                             __version__, re.DOTALL).groups()]
except Exception:
    version_info = ()
