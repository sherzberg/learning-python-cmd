What is this?
=============

This is just a repo to learn the 
`Python Cmd library <http://docs.python.org/2/library/cmd.html>`_. 
I have a need to be able to dynamically generate a command line utilites base on 
a module api. So this will be an area to POC that out.

I used bits and pieces from `this blog post <http://blog.fogcreek.com/cheeky-python-a-redis-cli>`_.

How do I run this?
==================

You need to install:

1. Python (I tested it with 2.7 cpython, 3.3 cpython, and pypy)

Next run the command:

::

    $ python platform-cmd.py
    (platform) help
    ... #see output
    (platform) help machine
    ... #see output
    (platform) processor
    (platform) quit
    $ 

