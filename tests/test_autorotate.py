#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`test_monkey_patching`
=======================

.. moduleauthor:: hbldh <henrik.blidh@swedwise.com>
Created on 2016-08-31, 11:23

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import os
from itertools import chain

from PIL import Image
import imdirect

this_dir = os.path.dirname(os.path.abspath(__file__))


def test_autorotate_1():
    """Test rotation of real image with orientation value = 6"""
    # TODO: Bad test, should be removed or improved.
    image_path = os.path.join(this_dir, 'testfile_6.jpg')

    img = Image.open(image_path)
    assert img.width == 300
    assert img.height == 225
    assert img._getexif().get(274) == 6

    img_rot = imdirect.autorotate(img)
    assert img_rot.width == 225
    assert img_rot.height == 300
    assert not hasattr(img_rot, '_getexif')


def test_imdirect_open_with_string_path():
    image_path = os.path.join(this_dir, 'testfile_6.jpg')

    img = Image.open(image_path)
    assert img.width == 300
    assert img.height == 225
    assert img._getexif().get(274) == 6

    img_rot = imdirect.imdirect_open(image_path)
    assert img_rot.width == 225
    assert img_rot.height == 300
    assert img_rot._getexif().get(274) == 1


def test_imdirect_open_with_filelike():
    image_path = os.path.join(this_dir, 'testfile_6.jpg')
    with open(image_path, 'rb') as f:
        img = Image.open(f)
    assert img.width == 300
    assert img.height == 225
    assert img._getexif().get(274) == 6

    with open(image_path, 'rb') as f:
        img_rot = imdirect.imdirect_open(f)
    assert img_rot.width == 225
    assert img_rot.height == 300
    assert img_rot._getexif().get(274) == 1


def test_rotate_1(base_img, image_with_rotation_value_1):
    """Test rotation of image with orientation = 1"""
    rotated_img = imdirect.autorotate(image_with_rotation_value_1)
    x = list(rotated_img.getdata())
    assert x == list(chain(*base_img))


def test_rotate_2(base_img, image_with_rotation_value_2):
    """Test rotation of image with orientation = 2"""
    rotated_img = imdirect.autorotate(image_with_rotation_value_2)
    x = list(rotated_img.getdata())
    assert x == list(chain(*base_img))


def test_rotate_3(base_img, image_with_rotation_value_3):
    """Test rotation of image with orientation = 3"""
    rotated_img = imdirect.autorotate(image_with_rotation_value_3)
    x = list(rotated_img.getdata())
    assert x == list(chain(*base_img))


def test_rotate_4(base_img, image_with_rotation_value_4):
    """Test rotation of image with orientation = 4"""
    rotated_img = imdirect.autorotate(image_with_rotation_value_4)
    x = list(rotated_img.getdata())
    assert x == list(chain(*base_img))


def test_rotate_5(base_img, image_with_rotation_value_5):
    """Test rotation of image with orientation = 5"""
    rotated_img = imdirect.autorotate(image_with_rotation_value_5)
    x = list(rotated_img.getdata())
    assert x == list(chain(*base_img))


def test_rotate_6(base_img, image_with_rotation_value_6):
    """Test rotation of image with orientation = 6"""
    rotated_img = imdirect.autorotate(image_with_rotation_value_6)
    x = list(rotated_img.getdata())
    assert x == list(chain(*base_img))


def test_rotate_7(base_img, image_with_rotation_value_7):
    """Test rotation of image with orientation = 7"""
    rotated_img = imdirect.autorotate(image_with_rotation_value_7)
    x = list(rotated_img.getdata())
    assert x == list(chain(*base_img))


def test_rotate_8(base_img, image_with_rotation_value_8):
    """Test rotation of image with orientation = 8"""
    rotated_img = imdirect.autorotate(image_with_rotation_value_8)
    x = list(rotated_img.getdata())
    assert x == list(chain(*base_img))


