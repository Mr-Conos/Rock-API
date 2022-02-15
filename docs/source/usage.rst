Usage
=======

Here you will learn how to best use Rock API and take full advantage of 
the features it has to offer.

.. contents::
  :local:
  :depth: 3
  
Base URL
----------

.. code-block::

       https://mrconos.pythonanywhere.com/rock/
       
Searching For Rocks
---------------------

+--------+---------------+---------------------------+
| Type   | URL           | Parameters                |
+========+===============+===========================+
| GET    | `/<rock name>`| rock name                 |
+--------+---------------+---------------------------+

.. warning::
    Rock names must be lowercase and the exact name of the rock you are searching for.

Random Rocks
--------------

+--------+---------------+---------------------------+
| Type   | URL           | Parameters                |
+========+===============+===========================+
| GET    | `/random`     | none                      |
+--------+---------------+---------------------------+


Rock Count
--------------

+--------+---------------+---------------------------+
| Type   | URL           | Parameters                |
+========+===============+===========================+
| GET    | `/count`      | none                      |
+--------+---------------+---------------------------+


Rate Rocks
--------------

**NEW URL**

.. code-block::

       https://mrconos.pythonanywhere.com/rate/

+--------+---------------+---------------------------+
| Type   | URL           | Parameters                |
+========+===============+===========================+
| PATCH  | `/<rock name>`| rating : int              |
+--------+---------------+---------------------------+


**Python Example**


.. code-block:: python
  
  import requests

  BASE = "https://mrconos.pythonanywhere.com/"

  response = requests.patch(BASE + "rate/" + "test", {"rating":0})
  print(response.json())

