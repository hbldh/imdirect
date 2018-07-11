#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
conftest
"""

import io
from itertools import chain

import pytest
from PIL import Image
from PIL.Image import open as pil_open
import piexif


@pytest.fixture()
def base_img():
    return [
        [0, 0, 255, 255, 255, 255, 0, 0],
        [0, 0, 255, 0, 0, 0, 0, 0],
        [0, 0, 255, 255, 255, 0, 0, 0],
        [0, 0, 255, 0, 0, 0, 0, 0],
        [0, 0, 255, 0, 0, 0, 0, 0],
        [0, 0, 255, 0, 0, 0, 0, 0],
    ]


def _save_with_exif_and_return_PIL_image(mat, orientation_value):
    i = Image.new('L', (len(mat[0]), len(mat)))
    i.putdata(list(chain(*mat)))
    exif = {'0th': {piexif.ImageIFD.Orientation: orientation_value}}
    with io.BytesIO() as b:
        i.save(b, format='jpeg', exif=piexif.dump(exif), quality=100, subsampling=0)
        b.seek(0)
        i = pil_open(b)
        i.load()
    i.putdata(list(chain(*mat)))
    return i


@pytest.fixture()
def image_with_rotation_value_1():
    mat = [
        [0, 0, 255, 255, 255, 255, 0, 0],
        [0, 0, 255, 0, 0, 0, 0, 0],
        [0, 0, 255, 255, 255, 0, 0, 0],
        [0, 0, 255, 0, 0, 0, 0, 0],
        [0, 0, 255, 0, 0, 0, 0, 0],
        [0, 0, 255, 0, 0, 0, 0, 0],
    ]
    return _save_with_exif_and_return_PIL_image(mat, 1)


@pytest.fixture()
def image_with_rotation_value_2():
    mat = [
        [0, 0, 255, 255, 255, 255, 0, 0][::-1],
        [0, 0, 255, 0, 0, 0, 0, 0][::-1],
        [0, 0, 255, 255, 255, 0, 0, 0][::-1],
        [0, 0, 255, 0, 0, 0, 0, 0][::-1],
        [0, 0, 255, 0, 0, 0, 0, 0][::-1],
        [0, 0, 255, 0, 0, 0, 0, 0][::-1],
    ]
    return _save_with_exif_and_return_PIL_image(mat, 2)


@pytest.fixture()
def image_with_rotation_value_3():
    mat = [
        [0, 0, 0, 0, 0, 255, 0, 0],
        [0, 0, 0, 0, 0, 255, 0, 0],
        [0, 0, 0, 0, 0, 255, 0, 0],
        [0, 0, 0, 255, 255, 255, 0, 0],
        [0, 0, 0, 0, 0, 255, 0, 0],
        [0, 0, 255, 255, 255, 255, 0, 0]
    ]
    return _save_with_exif_and_return_PIL_image(mat, 3)


@pytest.fixture()
def image_with_rotation_value_4():
    mat = [
        [0, 0, 0, 0, 0, 255, 0, 0][::-1],
        [0, 0, 0, 0, 0, 255, 0, 0][::-1],
        [0, 0, 0, 0, 0, 255, 0, 0][::-1],
        [0, 0, 0, 255, 255, 255, 0, 0][::-1],
        [0, 0, 0, 0, 0, 255, 0, 0][::-1],
        [0, 0, 255, 255, 255, 255, 0, 0][::-1]
    ]
    return _save_with_exif_and_return_PIL_image(mat, 4)


@pytest.fixture()
def image_with_rotation_value_5():
    mat = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [255, 255, 255, 255, 255, 255],
        [255, 0, 255, 0, 0, 0],
        [255, 0, 255, 0, 0, 0],
        [255, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    return _save_with_exif_and_return_PIL_image(mat, 5)


@pytest.fixture()
def image_with_rotation_value_6():
    mat = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [255, 0, 0, 0, 0, 0],
        [255, 0, 255, 0, 0, 0],
        [255, 0, 255, 0, 0, 0],
        [255, 255, 255, 255, 255, 255],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    return _save_with_exif_and_return_PIL_image(mat, 6)


@pytest.fixture()
def image_with_rotation_value_7():
    mat = [
        [0, 0, 0, 0, 0, 0][::-1],
        [0, 0, 0, 0, 0, 0][::-1],
        [255, 0, 0, 0, 0, 0][::-1],
        [255, 0, 255, 0, 0, 0][::-1],
        [255, 0, 255, 0, 0, 0][::-1],
        [255, 255, 255, 255, 255, 255][::-1],
        [0, 0, 0, 0, 0, 0][::-1],
        [0, 0, 0, 0, 0, 0][::-1],
    ]
    return _save_with_exif_and_return_PIL_image(mat, 7)


@pytest.fixture()
def image_with_rotation_value_8():
    mat = [
        [0, 0, 0, 0, 0, 0][::-1],
        [0, 0, 0, 0, 0, 0][::-1],
        [255, 255, 255, 255, 255, 255][::-1],
        [255, 0, 255, 0, 0, 0][::-1],
        [255, 0, 255, 0, 0, 0][::-1],
        [255, 0, 0, 0, 0, 0][::-1],
        [0, 0, 0, 0, 0, 0][::-1],
        [0, 0, 0, 0, 0, 0][::-1],
    ]
    return _save_with_exif_and_return_PIL_image(mat, 8)
