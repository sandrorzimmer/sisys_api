# API for Search Info System - SISYS

* SISYS is an achronym for Search Info System. It is a tool designed to store pieces of information that are frequently requested by users.

* For example: an engineer who writes documents for different companies that contain very similar pieces of text. He can use SISYS to store that structured texts and easily find them as needed.

* That was the inspiration to develop this tool.

* This project, specifically, shows the backend for SISYS, using an API REST created using Django REST framework.

* To make an easier comprehension, from now on we will call every piece of information stored in the system as "info".

## What is an info?

* Info is a plain text, like a paragraph, for example.
* For each info we can attribute tags.
* Every user of the system can create as many tags as necessary. Then, it is possbile to attach some of these tags to an info.

## Structure of SISYS

There are three main parts in the system:

1. User profile
2. Info
3. Tag