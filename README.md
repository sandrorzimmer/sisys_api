# API for Search Info System - SISYS

* SISYS is an achronym for Search Info System. It is a tool designed to store pieces of information that are frequently needed by users.

* For example: an engineer who writes documents for different companies that contain very similar pieces of text. He can use SISYS to store that structured texts and easily find them as needed.

* That was the inspiration to develop this tool.

* This project, specifically, shows the backend for SISYS, using an API REST created using Django REST framework.

* To make an easier understanding, from now on we will call every piece of information stored in the system simply as "info".

## What is an info?

* Info is a plain text, like a paragraph, for example.
* For each info we can attribute tags.
* Every user of the system can create as many tags as necessary. Then, it is possbile to attach some of these tags to an info.

## Structure of SISYS

There are three main parts in the system:

1. User profile

Every user will create their own tags and infos. This information is personal and the users will only have access to their own data.

It is only possible to create an info or a tag if there is a user logged in and this user will be the owner of the data.

A user should insert an **email** and a **password** to be created.

2. Info

An info is composed by a **title**, a **text** and, optionally, some **tags** attached.

When an info is created, it has a field called *created_on* which is automatically filled with the current date and time. It registers when the info was created.

Thers is a second date and time field, called *updated_on*, that can be filled when the user changes the info content.

3. Tag

A tag can be used to categorize groups of info or to make easier looking for some kind of information. Users will choose if and how they will use it.

To create a tag is only necessary define the its **name** in a text field.

## API endpoints

- sisys/profile

    - GET - Show current user profile (*id*, *email* and *name*).

    - POST - Create new user profile (*email*, *name* and *password*)

- sisys/profile/<profile_id>

    - GET - Show a specific user profile, but only show current user profile. Any other id will return *404 - Not found*.

    - PUT - update current user profile.

    - PATCH - partially update current user profile.

    - DELETE - delete current user profile.
    
- sisys/tag

    - GET - show all tags from current user.
  
    - POST - create a new tag for current user.

- sisys/tag/<tag_id>

    - GET - show specific tag from current user. If tried a tag_id from other user, it will return *404 - Not found*.

    - PUT - update specific tag from current user.

    - PATCH - partially update specific tag from current user.

    - DELETE - delete specific tag from current user.

- sisys/info

    - GET - show all infos from current user.
  
    - POST - create a new info for current user.

- sisys/info/<info_id>

    - GET - show specific info from current user. If tried a info_id from other user, it will return *404 - Not found*.

    - PUT - update specific info from current user.

    - PATCH - partially update specific info from current user.

    - DELETE - delete specific info from current user.