Rock API Quickstart
=====================

Here you will learn how to use the Rock API to access information about rocks. This tutorial will go over the following methods.

.. contents::
  :local:
  :depth: 3
  
Python
---------

This method will use the `requests library <https://pypi.org/project/requests>`_. 

First, install requests:

.. code-block:: python

  pip install requests
  
Now, use the following code in your Python file:

.. code-block:: python

   import requests

   url = "rockapi.apiworks.tech/rock/random"

   payload={}
   headers = {}

   response = requests.request("GET", url, headers=headers, data=payload)

   print(response.text)
   
Let's go over what this code does. 

#. We import the requests library.
#. We define the API URL.
#. We define an empty dictionary for both **payload** and **headers**, as they are not required to use this request.
#. The requests library creates a **GET** request with **url**, **headers**, and **data** parameters.
#. We print the response.

NodeJS
---------

This method will use the `requests library <https://www.npmjs.com/package/request>`_. 

First, install requests:

.. code-block:: javascript

  npm install request
  
Now, use the following code in your NodeJS file:

.. code-block:: javascript

  var request = require('request');
  var options = {
    'method': 'GET',
    'url': 'rockapi.apiworks.tech/rock/random',
    'headers': {
    }
  };
  request(options, function (error, response) {
    if (error) throw new Error(error);
    console.log(response.body);
  });

   
Let's go over what this code does. 

#. We import the requests library.
#. We define the API URL and method.
#. Run the request function with the **options** dictionary.
#. We print the response or throw an error if one occurs.
