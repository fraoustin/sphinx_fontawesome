sphinx fontawesome
##################

It is a extension for sphinx.

Add directive for use fontawesome 

Installation
------------

::

    pip install sphinx_fontawesome


Or

::

    git clone https://github.com/fraoustin/sphinx_fontawesome.git
    cd sphinx_fontawesome
    python setup.py install

Use
---

In your conf.py

::

    import sphinx_fontawesome
    extensions = ['sphinx_fontawesome']

In your rst file, you can use

* directive

::

   .. fa:: check

* role

::

   :fa:`check`
   :fa:`check lg`
   :fa:`square-o`

* substitution

::

    |check|
    |square-o|

If you change in your conf.py a value of prolog_rst, and you use subsitution you
can add in prolog_rst sphinx_fontawesome.prolog

::

    prolog_rst = sphinx_fontawesome.prolog + "my prolog"
