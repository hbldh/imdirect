#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PIL extension performing automatic rotation of opened JPEG images.

Description
-----------

The orientation of the photographed object or scene with respect to the
digital camera is encoded in the resulting image's Exif [1]_ data
(given that it is saved as a JPEG). When working with such digital
camera images, this orientation might lead to problems handling the
image and is very often desired to be counteracted.

This module is a small extension to `Pillow <https://pillow.readthedocs.io/en/3.3.x/>`_ that
`monkey patches <https://en.wikipedia.org/wiki/Monkey_patch>`_
the `PIL.Image.open <http://pillow.readthedocs.io/en/3.3.x/reference/Image.html#PIL.Image.open>`_ method
to automatically rotate the image [2]_ (by lossless methods) and update
the Exif tag accordingly, given that image is a JPEG.

The package also features a save method that includes the Exif data
by default when saving JPEGs.

Installation
------------

::

    pip install git+https://www.github.com/hbldh/imdirect

Usage
-----

Demonstration of the monkey patching and how it works:

.. code:: python

   >>> from PIL import Image
   >>> import imdirect
   >>> img = Image.open('image.jpg')
   >>> print("{0}, Orientation: {1}".format(img, img._getexif().get(274)))
   <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=4032x3024 at 0x7F44B5E4FF10>, Orientation: 6
   >>> imdirect.monkey_patch()
   >>> img_autorotated = Image.open('image.jpg')
   >>> print("{0}, Orientation: {1}".format(img_autorotated, img_autorotated._getexif().get(274)))
   <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3024x4032 at 0x7F44B5DF5150>, Orientation: 1


The package can also be used without monkey patching, by applying the
``imdirect.imdirect_open`` method directly:

.. code:: python

   >>> from imdirect import imdirect_open
   >>> img = imdirect_open('image.jpg')

or by using the ``imdirect.autorotate`` on a ``PIL.Image.Image`` object:

.. code:: python

   >>> from PIL import Image
   >>> import imdirect
   >>> img = Image.open('image.jpg')
   >>> img_rotated = imdirect.autorotate(img)

The last method does not return a ``PIL.JpegImagePlugin.JpegImageFile``,
but can still be used if the Exif information of the original image is
undesired.

Tests
~~~~~

Tests can be run with `pytest <http://doc.pytest.org/en/latest/>`_:

.. code:: sh

   Testing started at 13:28 ...
   ============================= test session starts ==============================
   platform linux2 -- Python 2.7.12, pytest-3.0.1, py-1.4.31, pluggy-0.3.1
   rootdir: /home/hbldh/Repos/imdirect, inifile:
   collected 4 items

   test_autorotate.py ...
   test_monkey_patching.py .

   =========================== 4 passed in 0.08 seconds ===========================

"""

import re

from ._autorotate import *


# Version information.
__version__ = '0.5.0'
version = __version__  # backwards compatibility name
try:
    version_info = [int(x) if x.isdigit() else x for x in
                    re.match('^([0-9]+)\.([0-9]+)[\.]*([0-9]*)(.*)$',
                             __version__, re.DOTALL).groups()]
except Exception:
    version_info = ()
