#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
_piexif
-------

:copyright: 2016-08-30 by hbldh <henrik.blidh@nedomkull.com>

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import piexif

from ._exceptions import ImDirectException
from ._util import ROTATION_NEEDED


def determine_orientation(image):
    """Get the EXIF orientation value.

    :param str image:
    :return: Integer representing the orientation. (See table in documetnation.)

    """
    d = piexif.load(image)
    orientation_value = d.get('0th', ).get(piexif.ImageIFD.Orientation,
        d.get('1st', ).get(piexif.ImageIFD.Orientation, None))
    return orientation_value


def get_rotation_needed(image):
    """Get the number of degrees needed to adjust rotate image.

    :param str image:
    :return: Degrees to rotate image.

    """
    orientation_value = determine_orientation(image)
    if orientation_value is None:
        raise ImDirectException("No orientation available in EXIF tag.")
    return ROTATION_NEEDED.get(orientation_value)
