#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
run
-----------

:copyright: 2016-08-30 by hbldh <henrik.blidh@nedomkull.com>

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from PIL import Image
import imdirect

img = Image.open('2016-08-28 15.11.44.jpg')
# Print image as string and the EXIF orientation.
print(img)
print("Orientation: {0}".format(img._getexif().get(274)))

imdirect.monkey_patch()
img_autorotated = Image.open('2016-08-28 15.11.44.jpg')
print(img_autorotated)
print("Orientation: {0}".format(img_autorotated._getexif().get(274)))

