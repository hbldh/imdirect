#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
imdirect
--------

:copyright: 2016-08-29 by hbldh <henrik.blidh@nedomkull.com>

EXIF  Orientation Value Row #0 is   Column #0 is
======================= =========   ============
1                       Top         Left side
2                       Top         Right side
3                       Bottom      Right side
4*                      Bottom      Left side
5*                      Left side   Top
6                       Right side  Top
7*                      Right side  Bottom
8                       Left side   Bottom

References:
-----------
http://www.impulseadventure.com/photo/exif-determine_orientation.html

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import piexif


class ImDirectException(Exception):
    """Simple exception class for the module."""


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
    return {
        1: 0,
        8: -90,
        3: 180,
        6: 90
    }.get(orientation_value)
