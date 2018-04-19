============
Installation
============

Install with `conda <http://continuum.io/downloads>`_
-----------------------------------------------------

We recommend making sure you have the latest versions of conda and Anaconda
before installing mBuild:

::

    $ conda update conda anaconda

mBuild can be installed from the ``mosdef`` channel. The ``omnia`` and
``conda-forge`` channels should also be specified for installation of
dependencies.

::

    $ conda install -c conda-forge -c omnia -c mosdef mbuild

Alternatively you can add all the required channels to your ``.condarc``
after which you can simply install without specifying the channels::

    $ conda config --add channels mosdef
    $ conda config --add channels omnia
    $ conda config --add channels conda-forge
    $ conda install mbuild

.. note::
    The `MDTraj website <http://mdtraj.org/latest/new_to_python.html>`_ makes a
    nice case for using Python and in particular the
    `Anaconda scientific python distribution <http://continuum.io/downloads>`_
    to manage your numerical and scientific Python packages.

Install an editable version from source
-------------------
::

    $ git clone https://github.com/mosdef-hub/mbuild
    $ cd mbuild
    $ pip install -e .

To make your life easier, we recommend that you use a pre-packaged Python
distribution like `Continuum's Anaconda <https://store.continuum.io/>`_
in order to get all of the dependencies.

Testing your installation (source installation only)
----------------------------------------------------

mBuild uses ``pytest`` for unit testing. To run them simply run the
following while in the base directory::

    $ conda install pytest
    $ pytest -v

