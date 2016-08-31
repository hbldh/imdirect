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
import autopil

img = Image.open('2016-08-28 15.11.44.jpg')
print("{0}, Orientation: {1}".format(img, img._getexif().get(274)))

autopil.monkey_patch()
img_autorotated = Image.open('2016-08-28 15.11.44.jpg')
print("{0}, Orientation: {1}".format(img_autorotated, img_autorotated._getexif().get(274)))

autopil.monkey_patch(False)

from autopil import autorotate_open
img = autorotate_open('2016-08-28 15.11.44.jpg')
print("{0}, Orientation: {1}".format(img, img._getexif().get(274)))
