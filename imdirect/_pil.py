#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
_pil
----

:copyright: 2016-08-30 by hbldh <henrik.blidh@nedomkull.com>

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import


from PIL import Image, ExifTags

from ._util import ROTATION_NEEDED
from ._exceptions import ImDirectException


EXIFKEYS = {ExifTags.TAGS.get(k): k for k in ExifTags.TAGS}


def autorotate(image):
    """Rotate and return an image according to its Exif information.

    :param :class:`PIL.Image.Image` image: PIL image to rotate
    :return: A :class:`PIL.Image.Image` image.

    """
    orientation_value = image._getexif().get(
        EXIFKEYS.get('Orientation'))
    if orientation_value is None:
        raise ImDirectException("No orientation available in EXIF tag.")
    if orientation_value in (2, 4, 5, 7):
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
    return image.rotate(ROTATION_NEEDED.get(orientation_value))


def determine_orientation(image):
    """Get the EXIF orientation value.

    :param :class:`PIL.Image.Image` or str image:
    :return: Integer representing the orientation. (See table in documentation.)

    """
    if isinstance(image, Image.Image):
        try:
            orientation_value = image._getexif().get(
                EXIFKEYS.get('Orientation'))
        except AttributeError:
            raise ImDirectException("This image has no Exif data.")
    else:
        orientation_value = determine_orientation(Image.open(image))
    return orientation_value
