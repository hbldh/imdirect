imdirect
========

|Build Status| |Coverage Status|

Determine the determine_orientation of a camera image from it EXIF tag.


Installation
------------

::

    pip install git+https://www.github.com/hbldh/imdirect

Usage
-----

.. code:: python

   In [1]: import imdirect

   In [2]: imdirect.determine_orientation('2016-08-28 15.11.44.jpg')
   Out[2]: 6

   In [3]: imdirect.get_rotation_needed('2016-08-28 15.11.44.jpg')
   Out[3]: 90


Tests
~~~~~

TBD.

.. |Build Status| image:: https://travis-ci.org/hbldh/imdirect.svg?branch=master
   :target: https://travis-ci.org/hbldh/imdirect
.. |Coverage Status| image:: https://coveralls.io/repos/github/hbldh/imdirect/badge.svg?branch=master
   :target: https://coveralls.io/github/hbldh/imdirect?branch=master


