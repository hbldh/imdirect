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

from PIL import Image
import autopil

this_dir = os.path.dirname(os.path.abspath(__file__))


def test_autorotate_1():
    image_path = os.path.join(this_dir, 'testfile_6.jpg')

    img = Image.open(image_path)
    assert img.width == 300
    assert img.height == 225
    assert img._getexif().get(274) == 6

    img_rot = autopil.autorotate(img)
    assert img_rot.width == 225
    assert img_rot.height == 300
    assert not hasattr(img_rot, '_getexif')


def test_autopil_open_with_string_path():
    image_path = os.path.join(this_dir, 'testfile_6.jpg')

    img = Image.open(image_path)
    assert img.width == 300
    assert img.height == 225
    assert img._getexif().get(274) == 6

    img_rot = autopil.autopil_open(image_path)
    assert img_rot.width == 225
    assert img_rot.height == 300
    assert img_rot._getexif().get(274) == 1


def test_autopil_open_with_filelike():
    image_path = os.path.join(this_dir, 'testfile_6.jpg')
    with open(image_path, 'r') as f:
        img = Image.open(f)
    assert img.width == 300
    assert img.height == 225
    assert img._getexif().get(274) == 6

    with open(image_path, 'r') as f:
        img_rot = autopil.autopil_open(f)
    assert img_rot.width == 225
    assert img_rot.height == 300
    assert img_rot._getexif().get(274) == 1
