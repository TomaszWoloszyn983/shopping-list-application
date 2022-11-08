# Shopping List Application

## Welcome to the project.

The subject of the project is the shopping list. 
The application allows adding items to buy to the list, editing, deleting the items form the list, as well as marking them as done/bought.

** **
## Contents:
1. [Project Overview](#project-overview)
2. [User Stories](#user-stories)
3. [Features](#features)
    * [Home Page](#home-page)
    * [Item Class](#item-class)
4. [Future Features](#future-features)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [References and Credits](#references-and-credits)



## User Stories:

### Non-registered user
    - As a non-registered user I would like to be able to create quick and simple shopping list.
    - As a non-registered user I would like to save my shopping list in a database so it will be accessible wherever I am.
    - As a non-registered user I would like to mark items as bought, so the bought items will be separated from items to buy.
    - As a non-registered user I would like to mark items as bought, so the bought items will be separated from items to buy.
    - As a non-registered user I would like to edit or delete items.
    - As a non-registered user I would like to clear the list with one click after my shoppings are done, so I don't have to delete each item separately.


### Registered user
    - As a registered user I would like to be able to log in to get access to additional functions.
    - As a registered user I would like to be able to create more than just one list, so I can create separate lists for different occasions and different users.
    - As a registered user I would like to add items to favourite so I can easier add them to my shopping list.
    - As a registered user I would like to be able to mark items as urgent so they can be highlighted on the list and easier spotted.
    - As a registered user I would like to be able to share my list with another users.
    - As a registered user I would like to be able to assign price to items so I can know the assumed price of all items on the list.
    - As a registered user I would like to be able to print the shopping list, so I can use the list when I have no mobile devices with me.


### As the application creator
    - I want to make the site user friendly
    - 

- **Must do:**
    - Create class Item and the model section for Items.
    - Add, edit, delete item functions.
    - Marking item as bought and sorting the list.
    - Register and Login/logout functions that allow the register user to get access to additional functions (more about additional functions in the Could do section)
    - Create a table in Postgres database for added items that will contain Columns for: Id, Name, quantity, urgent, bought.
    - Adding each item to the list in Database, so they can be suggested during the future search.
    - Create a responsive layout with Materialize, Bootstrap or Material Desing Bootstrap.
    - Create a separate templates for each CRUD function that will inherit from the base template.
    - Deploy to Heroku. Create Procfile and Requirements.txt file.
    
- **Could do:**
    - Add additional columns for Item attributes such as: price, favorite.
    - Add item to the favourite. Create the Favourite Item column in Database. Favorite item suggested during the search and have predefined price.



- ***Additional Item's attributtes available only for register users***

    - Favorite. Favorite item could be suggested during the search and it can have a predefined price.
    - Price: Summed up value of all items could be displayed at the bottom of the list.
    - Category that will contain different icons for each category
    - Shopping counter showing how many times the item was added to the shopping list.

## Project Overview


## Features

The application includes following sections. Although accessibilty of those sections depends on whether the user is logged in or not.

### **Home Page**
Home Page contain a short introduction to the application.
In case of unlogged in user it displays a default Shopping List where the user can add, delete or update the list. 
In case of logged in user the Home Page displays last three list previously created by the user. There is also a button which redirects the user to the lists page where he can add more list and to manage already existing lists.

### **Lists Page**
This page is only accessible for logged in users and it allows users to create new lists and to manage existing lists.

### **Items Page**
This page is only accessible for logged in users and it allows users to create new items and to edit or delete items, as well as assigning items to lists.

### **Header** this section contains the list of events taking place in 

### **Navigation bar**
  All sections are clearly and simply arranged inside the navigation bar which allows for an easy access to each section. 

### **Shopping List Section** 

### **Login/logout Section** 

### **Footer**  


- **Add Item** 

- **Item Section** 
    Contains information about item that is added to the shopping list.

## Item class:

    - Id
    - Name
    - Quantity
    - Bought
    - Urgent
    - Favourite

## Future Features

## Technologies used:
    * Python - an interpreted, object-oriented, high-level programming language.
    * Django
    * Materialize
    * Html5
    * CSS
    * Github
    * Gitpod

## Testing

## Errors

### Model Error
When I click on items list, instead of diplaying the items list I get an error:

ProgrammingError at /admin/list/item/
column list_item.list_name_id does not exist
LINE 1: ...g", "list_item"."quantity", "list_item"."bought", "list_item...

![Help section image](images/errors/er1.jpg)

![Help section image](images/errors/er2.jpg)

The same thing happens when I try to delete any list in my application.

![Help section image](images/errors/er4.jpg)

![Help section image](images/errors/er5.jpg)

The source of the error seems to be the underlined line of code, where I try to assign the Item object to a List. 
I try to use List as the foreign key, but the system expects to find list_name_id

![Help section image](images/errors/er6.jpg)


P.S. Item model displays in the admin panel when I click the 'add' button, but when I try to 'save' the Item the error mentioned above show up.

![Help section image](images/errors/er3.jpg)

    ### Checkbox issue

![Help section image](images/errors/issue_no_checkboxes2.jpg)

## Deployment

### Local Deployment

## References and Credits:

 - Tutorial on differences between MVC and MVT - https://www.youtube.com/watch?v=zhrLVCjNbyk

- Vibhor Chandels YouTube channel on Agile methodology - https://www.youtube.com/watch?v=C2boBomE4aM&list=PLxO4vxvvorbtqmkL7sYi0Qc4kX-0RE9fp
- Mark Shead YouTube channel on Agile -  https://www.youtube.com/c/MarkShead

- How to create Modals using Materialize YouTube tutorial - https://www.youtube.com/watch?v=GAQoVIgjeZA&list=TLPQMjkxMDIwMjJbjtPeibmcMA&index=2

- How to create a nice login form using Materialize YouTube tutorial - https://www.youtube.com/watch?v=2lbiRNNnAx8&t=1s

- Solution how to fix not displaying checkboxes i materialize - https://stackoverflow.com/questions/54500348/django-checkbox-not-showing-up-in-html

## Credits: