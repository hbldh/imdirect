#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
run
---

:copyright: 2016-08-30 by hbldh <henrik.blidh@nedomkull.com>

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from PIL import Image
import imdirect

image_path = 'tests/testfile_6.jpg'

img = Image.open(image_path)
print("{0}, Orientation: {1}".format(img, img._getexif().get(274)))

imdirect.monkey_patch()
img_autorotated = Image.open(image_path)
print("{0}, Orientation: {1}".format(
    img_autorotated, img_autorotated._getexif().get(274)))
imdirect.monkey_patch(False)

from imdirect import imdirect_open
img = imdirect_open(image_path)
print("{0}, Orientation: {1}".format(img, img._getexif().get(274)))


