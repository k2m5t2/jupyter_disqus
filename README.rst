Jupyter_Disqus Package
=======================

.. image:: https://travis-ci.org/vwxyzjn/jupyter_disqus.svg?branch=master
    :target: https://travis-ci.org/vwxyzjn/jupyter_disqus

.. image:: https://codecov.io/gh/vwxyzjn/jupyter_disqus/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/vwxyzjn/jupyter_disqus

.. image:: https://badge.fury.io/py/jupyter-disqus.svg
    :target: https://badge.fury.io/py/jupyter-disqus

Introduction
---------------------------

You may use this package to inject and display `Disqus <https://disqus.com/>`_ in your jupyter notebook, which might be helpful for couple use cases. For example, if you are doing a tutorial or a demonstration, ``Jupyter_Disqus`` allows you to answer questions that other people may have. Also, you may get some helpful feedback from the audience as well.

Demo
-----------------------

.. image:: https://github.com/vwxyzjn/jupyter_disqus/raw/master/demo.gif
    :target: https://github.com/vwxyzjn/jupyter_disqus/raw/master/demo.gif


Installation
-------------------------

::

  $ pip install jupyter_disqus


Usage
----------------------

.. code-block:: python

    from jupyter_disqus import inject
    # make sure to run this in a cell of your jupyter notebook
    inject(
        page_url="https://costahuang.me/SC2AI/",
        page_identifier="1f527ae5-5a59-4dc3-9bb0-d77c2ccf5cab",  # unique identifier
        site_shortname="costahuang"                              # your disqus site shortname
    )

Authors: Costa Huang
