# Testing


##  **Responsiveness**
- The project was responsive tested on https://ui.dev/amiresponsive and it is responsive for every type of devices such as desktop computers, laptops, tablets and smart phones.

![Am I Responsive](documentation/images/components/AmIResponsive.jpg)

## **Code Validator Testing**

- **HTML**

    * No errors were detected when passing through the [W3C validator](https://validator.w3.org/nu/).

        ![html_validation](documentation/images/testing/nu_html_checker1.jpg).

    * Link to the validation testing for my Html file:
    https://validator.w3.org/nu/?doc=https%3A%2F%2Ftw-shopping-list.herokuapp.com%2F

- **CSS**
    * No errors were detected when passing through the [jigsaw.w3 validator](https://jigsaw.w3.org/css-validator). 

         ![css_validation](documentation/images/testing/w3c_css_checker1.jpg)
    
   

- **JAVASCRIPT**
   
No test yet.

- **PYTHON**

No test yet.

## **Browsers compatibility**

- The Web Page is compatibile with every tested browser and fully responsive in the full range of screen sizes:

    * **Google Chrome:**

    ![Google Chrome](documentation/images/testing/chrome1.jpg)

    ![Google Chrome](documentation/images/testing/chrome2.jpg)


    * **Microsoft Edge:**
    
    ![Microsoft Edge](documentation/images/testing/ms_edge1.jpg)

    ![Microsoft Edge](documentation/images/testing/ms_edge2.jpg)


    * **Avast Browser:** 

    ![Avast Browser](documentation/images/testing/avast1.jpg)

    ![Avast Browser](documentation/images/testing/avast2.jpg)


    * **Netbox Browser:**

    ![Netbox Browser](documentation/images/testing/netbox1.jpg)

    ![Netbox Browser](documentation/images/testing/netbox2.jpg)


    * **Mobile Devices:**

    ![Mobile Devices](documentation/images/testing/mobile_view1.jpg)
    ![Mobile Devices](documentation/images/testing/mobile_view2.jpg)
    ![Mobile Devices](documentation/images/testing/mobile_view3.jpg)

## **Lighthouse Inspection reports**
 - There are some issues when the page is opening using Google **Chrome browser**.
    
    However the page inspection in Incognito Mode without any browser extensions shows results as follows

![Google Chrome inspection](documentation/images/testing/lighthouse_chrome.jpg)

    Results are similar for all the pages. 

    Although there are some differences between displaying the page on different browsers.

**Microsoft Edge:**

![Microsoft Egde inspection](documentation/images/testing/lighthoue_edge.jpg)

And a less popular **Netbox Browser**:

![Netbox inspection](documentation/images/testing/lighthouse_netbox.jpg)


## **Testing Functionalities:**

User Stories Tests:
* As a user I can mark an Item on the list as Urgent so that the Item will be moved to the top of the list or highlighted with a different color
* As a the application user I can create and add items to the shopping list so that the items can be displayed and marked as Done/Bought. [Link to tests](#add-item)
* As a an application user I can mark an item as Bought so that the item will be moved to the botton of the list or removed from the list [Link to tests](#item-functionalities-testings)
* As a user I can register and login so that I can receive access to additional functions. [Link to test](#authentication)
* As a user I can Edit items already added to the list so that udpade items names and change quantity of the items [Link to test](#edit-item)
* As a user I can remove items from the list so that I don't have to store unwanted items on my shopping list [Link to test](#delete-item)
* As a user I can remove all existing items at one click so that I can quickly remove one list and build a new one. [Link to test](#clear-list)

### Home Page:

![Home Page](documentation/images/testing/home_page0.jpg)

### **Authentication:**

The user is able to register an account. After creating the account the user is able to Login and Logout from his account.
Logged in users gets access to all the application functions.

### Register a new account:

To create a new account enter the Register page and fill up the form which includes:
- User Name
- Email
- Password
- Repeated Password

![Register](documentation/images/testing/register_page.jpg)

After filling up the form correctly and clicking "Sign Up" button the account is created 
and the user is redirected to the Home Page where the information about successful
register hould be dispayed.

![Register](documentation/images/testing/register1.jpg)

![Register](documentation/images/testing/register2.jpg)

### Login:

Users who already have their accounts can login in the Login Page.

![Login](documentation/images/testing/login_page1.jpg)

Filling up the form correctly and clicking "Sign Up" button redirects the user to the Home Page.
Entering invalid data or not entering required data displays wqrning message.

![Login](documentation/images/testing/logged_in_home.jpg)


### Logout:

To being logout the user should go to the Logout Page and after clicking "Sign Out" he is logged out and redirected to the Home Page.
Also information about being logged out is displayed.

![Logout](documentation/images/testing/logout_page.jpg)


![Logout](documentation/images/testing/logout.jpg)

### **Testing Lists functionalities:**

Creating shopping lists is one of the main functions of this application.


### Add List

To create a new List go to the Lists Page and click "Add New List" button.

![Add List](documentation/images/testing/add_list1.jpg)

After naming the new list click "Create List" button to create the list.

![Add List](documentation/images/testing/add_list2.jpg)
![Add List](documentation/images/testing/add_list3.jpg)

If the list name was successfully validated the user will be redirected to the Lists view page.

![MAdd List](documentation/images/testing/add_list4.jpg)

In case of unsuccessful validation a warning message is displayed.

![Add List](documentation/images/testing/add_list5.jpg)

Also a handled Integrity Error can occured during adding a new List.

More information about the error in the Bugs and Errors section [here](README.md#7-bugs-and-errors).

![Add List](documentation/images/testing/add_list_integrity_error.jpg)

### Show Lists

Created lists are displayed in the Lists Page.

### Edit List

To change the list name click the "Edit" button on the list card. Enter the new name and submit changes clicking the "Submit Changes" button.
In case of successful validation the user will be redirected to the Lists page.
If the input in validated successfully a warning message is displayed.

![Edit List](documentation/images/testing/edit_list1.jpg)

![Edit List](documentation/images/testing/edit_list2.jpg)

![Edit List](documentation/images/testing/edit_list3.jpg)

### Delete List

To delete a list click the "Delete" button on the list card. A confirmation window will be displayed.

Clicking "Yes" button the user submits deleting the list and its all items from the database.

Clicking "No" cancel the operation and redirects the user back to the Lists Page.

![Delete List](documentation/images/testing/delete_list2.jpg)

Deleting the list redirects the user to the Lists Page where information about deleting list is displayed.

![Delete List](documentation/images/testing/delete_list.jpg)


### **Testing Items functionalities:**

Adding and and manipulationg items is the main function this application. In this section I'm going to test Add, Edit and Delete functions as well as changing items status from "to buy" to "bought".


### Add Item

To create a new Item go to the Lists Page and click "Add Item" button.
Fill up the form which includes:

Required field
- Item Name
- Quantity (with default value 1)

Optional fields:
- Price
- Description
- Favourite checkbox
- Urgent checkbox

After filling up the form click "Add Item" button to create the item and add it to the list.

If the all form fields were successfully validated the user will be redirected to the List view.

In case of unsuccesful validation a warning message is displayed.

![Add Item](documentation/images/testing/add_item1.jpg)
![Add Item](documentation/images/testing/add_item_2.jpg)

### Edit Item

To update Item informations go to the Lists Page and click over the item card and click "Edit Item" button.
Override the information in the form and click "Submit" button:

![Add Item](documentation/images/testing/edit_item1.jpg)

If the all form fields were successfully validated the user will be redirected to the List view.

In case of unsuccesful validation a warning message is displayed.

![Add Item](documentation/images/testing/edit_item2.jpg)

### Delete Item

To delete an item click over the item card to display function button click the "Delete" button. A confirmation window will be displayed.

Clicking "Yes" button the user submits deleting the item.

Clicking "No" cancel the operation and redirects the user back to the Lists view.

![Add Item](documentation/images/testing/del_item1.jpg)

![Add Item](documentation/images/testing/del_item2.jpg)

Deleting the item redirects the user to the Lists view where information about deleting the item is displayed.

![Add Item](documentation/images/testing/del_item3.jpg)



### Clear List

To delete all the items from the list click "Delete All" button.
A confirmation window will be displayed.

Clicking "Yes" button the user submits deleting the items.

Clicking "No" cancel the operation and redirects the user back to the List view.

![Add Item](documentation/images/testing/clear_list2.jpg)

![Add Item](documentation/images/testing/clear_list.jpg)


 ### Item Functionalities Testings

To move item to the "bought items list" click round green button on the left side of the item card.
The "bought" items list will be created and the clicked item will be moved to the list.

Bought items can be moved back to the items to buy list when clicked again.

 ![Add Item](documentation/images/testing/mark1.jpg)

 ![Add Item](documentation/images/testing/mark2.jpg)

 ![Add Item](documentation/images/testing/mark3.jpg)


## **Unfixed Bugs**
* The only unfixed bug is possibility of dublicating slugs. Full description of the bug [here](README.md#7-bugs-and-errors).
* There are no other bugs that I am aware of.