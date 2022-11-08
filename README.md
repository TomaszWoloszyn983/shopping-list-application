# Shopping List Application

## Welcome to the project.

The subject of the project is the shopping list. 
The application allows adding items to buy to the list, editing, deleting the items form the list, as well as marking them as done/bought.

** **

## User Stories:

### First time user
    - As a first time user I would like to be able to create quick and simple shopping list.
    - As a first time user I would my shopping list to be accessible wherever I am.

### Returning user
    - As an returning user I would like to be able to register and log in to get additional functionalities for ma shopping lists.

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

- **Item class:**

    - Id
    - Name
    - Quantity
    - Bought
    - Urgent

- ***Additional Item's attributtes available only for register users***

    - Favorite. Favorite item could be suggested during the search and it can have a predefined price.
    - Price: Summed up value of all items could be displayed at the bottom of the list.
    - Category that will contain different icons for each category
    - Shopping counter showing how many times the item was added to the shopping list.

** **
## Features

The application includes following sections. Although accessibilty of those sections depends on whether the user is logged in on not.

- **Home Page** 

    * **Navigationbar**
  All sections are clearly and simply arranged inside the navigation bar which allows for an easy access to each section. 

    * **Header** this section contains the list of events taking place in 

    * **Shopping List Section** 

    * **Login/logout Section** 

    * **Footer**  

- **Add Item** 

- **Item Section** 
    Contains information about item that is added to the shopping list.

## Future Features

## Technologies used:
    * Python - an interpreted, object-oriented, high-level programming language.
    * Django
    * Materialize
    * Html5
    * CSS

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