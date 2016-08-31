#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
_autorotate
-----------

:copyright: 2016-08-30 by hbldh <henrik.blidh@nedomkull.com>

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import io

from PIL import Image, ExifTags
from PIL.Image import open as imopen
import piexif

__all__ = ["autorotate", "autopil_open",
           "monkey_patch",
           "update_exif_for_rotated_image",
           "save_with_exif_info", "ImDirectException"]

EXIFKEYS = {ExifTags.TAGS.get(k): k for k in ExifTags.TAGS}

# Py2/Py3 compatability.
try:
    string_types = basestring,
    text_type = unicode
    binary_type = str
except NameError:
    string_types = str,
    text_type = str
    binary_type = bytes


class ImDirectException(Exception):
    """Simple exception class for the module."""


def autorotate(image):
    """Rotate and return an image according to its Exif information.

    ROTATION_NEEDED = {
        1: 0,
        2: 0 (Mirrored),
        3: 180,
        4: 180 (Mirrored),
        5: -90 (Mirrored),
        6: -90,
        7: 90 (Mirrored),
        8: 90,
    }

    :param :py:class:`~PIL.Image.Image` image: PIL image to rotate
    :return: A :py:class:`~PIL.Image.Image` image.

    """
    orientation_value = image._getexif().get(EXIFKEYS.get('Orientation'))
    if orientation_value is None:
        raise ImDirectException("No orientation available in Exif tag.")
    if orientation_value in (2, 4, 5, 7):
        image = image.transpose(Image.FLIP_LEFT_RIGHT)

    if orientation_value in (1, 2):
        i = image
    elif orientation_value in (3, 4):
        i = image.transpose(Image.FLIP_TOP_BOTTOM)
    elif orientation_value in (5, 6):
        i = image.transpose(Image.ROTATE_270)
    elif orientation_value in (7, 8):
        i = image.transpose(Image.ROTATE_90)
    else:
        i = image

    return i


def update_exif_for_rotated_image(exif):
    """Modifies the Exif tag if rotation has been performed.

    0th, 1st
    --------
    ImageWidth = 256
    ImageLength = 257
    XResolution = 282
    YResolution = 283
    TileWidth = 322
    TileLength = 323

    Exif
    ----
    PixelXDimension = 40962
    PixelYDimension = 40963

    :param dict exif: The parsed Exif tag
    :return: The modified Exif dict.

    """
    orientation_value = exif.get('0th', ).get(
        piexif.ImageIFD.Orientation, exif.get('1st', ).get(
            piexif.ImageIFD.Orientation, None))

    if orientation_value is not None:
        # Update orientation.
        exif['0th'][piexif.ImageIFD.Orientation] = 1
        if exif.get('1st', {}).get(piexif.ImageIFD.Orientation) is not None:
            exif['1st'][piexif.ImageIFD.Orientation] = 1

        # If 90 or 270 degree rotation, x dimensions are now y dimensions,
        # so flip all such properties.
        if orientation_value > 4:
            for exif_tag in ['0th', '1st']:
                if exif.get(exif_tag) is not None:
                    x, y = (exif.get(exif_tag).get(piexif.ImageIFD.ImageWidth),
                            exif.get(exif_tag).get(piexif.ImageIFD.ImageLength))
                    if x is not None and y is not None:
                        exif[exif_tag][piexif.ImageIFD.ImageWidth] = y
                        exif[exif_tag][piexif.ImageIFD.ImageLength] = x

                    x, y = (exif.get(exif_tag).get(piexif.ImageIFD.XResolution),
                            exif.get(exif_tag).get(piexif.ImageIFD.YResolution))
                    if x is not None and y is not None:
                        exif[exif_tag][piexif.ImageIFD.XResolution] = y
                        exif[exif_tag][piexif.ImageIFD.YResolution] = x

                    x, y = (exif.get(exif_tag).get(piexif.ImageIFD.TileWidth),
                            exif.get(exif_tag).get(piexif.ImageIFD.TileLength))
                    if x is not None and y is not None:
                        exif[exif_tag][piexif.ImageIFD.TileWidth] = y
                        exif[exif_tag][piexif.ImageIFD.TileLength] = x
            if exif.get('Exif') is not None:
                x, y = (exif.get('Exif').get(piexif.ExifIFD.PixelXDimension),
                        exif.get('Exif').get(piexif.ExifIFD.PixelYDimension))
                if x is not None and y is not None:
                    exif['Exif'][piexif.ExifIFD.PixelXDimension] = y
                    exif['Exif'][piexif.ExifIFD.PixelYDimension] = x

    # TODO: Update the thumbnail as well!

    return exif


def autopil_open(fp, mode="r"):
    """Opens, identifies the given image file, and rotates it if it is a JPEG.

    Note that this method does NOT employ the lazy loading methodology that
    the PIL Images otherwise use. This is done to avoid having to save new

    :param fp: A filename (string), pathlib.Path object or a file object.
       The file object must implement :py:meth:`~file.read`,
       :py:meth:`~file.seek`, and :py:meth:`~file.tell` methods,
       and be opened in binary mode.
    :param mode: The mode.  If given, this argument must be "r".
    :returns: An :py:class:`~PIL.Image.Image` object.
    :exception IOError: If the file cannot be found, or the image cannot be
       opened and identified.

    """
    img = imopen(fp, mode)
    if img.format == 'JPEG':
        # Read Exif tag on image.
        if isinstance(fp, string_types):
            exif = piexif.load(binary_type(fp))
        else:
            fp.seek(0)
            exif = piexif.load(fp.read())
        # If orientation field is missing or equal to 1, nothing needs to be done.
        orientation_value = exif.get('0th', {}).get(piexif.ImageIFD.Orientation)
        if orientation_value is None or orientation_value == 1:
            return img
        # Otherwise, rotate the image and update the exif accordingly.
        img_rot = autorotate(img)
        exif = update_exif_for_rotated_image(exif)

        # Now, lets restore the output image to PIL.JpegImagePlugin.JpegImageFile class
        # with the correct update Exif information.
        # Save image as JPEG to get a correct byte representation of the image and then read it back.
        with io.BytesIO() as bio:
            img_rot.save(bio, format='jpeg', exif=piexif.dump(exif))
            bio.seek(0)
            img_rot_new = imopen(bio, mode)
            # Since we use a BytesIO we need to avoid the lazy loading of the PIL image, hence
            # loading the data it explicitly here.
            img_rot_new.load()
        img = img_rot_new

    return img


def monkey_patch(enabled=True):
    """Monkey patching PIL.Image.open method

    :param bool enabled: If the monkey patch should be activated or deactivated.

    """
    if enabled:
        Image.open = autopil_open
    else:
        Image.open = imopen


def save_with_exif_info(img, *args, **kwargs):
    """Saves an image using PIL, preserving the exif information.

    Wraps :py:method:`~PIL.Image.Image.save`.

    :param :py:class:`~PIL.Image.Image` img: The PIL
    :param args: The arguments for the `save` method of the Image class.
    :param kwargs: The keywords for the `save` method of the Image class.

    """
    if 'exif' in kwargs:
        exif = kwargs.pop('exif')
    else:
        exif = img.info.get('exif')
    img.save(*args, exif=exif, **kwargs)


def _PIL_determine_orientation(image):
    """Get the Exif orientation value.

    :param :py:class:`~PIL.Image.Image` image:
    :return: Integer representing the orientation. (See table in documentation.)

    """
    try:
        orientation_value = image._getexif().get(
            EXIFKEYS.get('Orientation'))
    except AttributeError:
        raise ImDirectException("This image has no Exif data.")

    return orientation_value


def _piexif_determine_orientation(image_path):
    """Get the Exif orientation value.

    :param str image_path: The path to the JPEG image.
    :return: Integer representing the orientation. (See table in documentation.)

    """
    d = piexif.load(image_path)
    orientation_value = d.get('0th', ).get(piexif.ImageIFD.Orientation,
        d.get('1st', ).get(piexif.ImageIFD.Orientation, None))

    return orientation_value
