# Testing


##  **Responsiveness**
- The project was responsive tested on https://ui.dev/amiresponsive and it is responsive for every type of devices such as desktop computers, laptops, tablets and smart phones.

![Am I Responsive](documentation/images/components/AmIResponsive.jpg)

## **Code Validator Testing**
- HTML
    * No errors were detected when passing through the [W3C validator](https://validator.w3.org/nu/).
    ![html_validation](documentation/images/testing/nu_html_checker1.jpg).
    * Link to the validation testing for my Html file:
    https://validator.w3.org/nu/?doc=https%3A%2F%2Ftomaszwoloszyn983.github.io%2Fswap-puzzle-game

- CSS
    * No errors were detected when passing through the [jigsaw.w3 validator](https://jigsaw.w3.org/css-validator). 

         ![css_validation](documentation/images/testing/w3c_css_checker1.jpg)
    
   

- JAVASCRIPT
   
No test yet.

- PYTHON

No test yet.

## **Browsers compatibility**
- The Web Page is compatibile with every tested browser, such as:
    * Google Chrome:

         ![Google Chrome](documentation/images/resp_chrome.jpg)

    * Microsoft Edge: 
    
       ![Microsoft Edge](documentation/images/resp_edge.jpg)

    * Avast Browser: 

        ![Avast Browser](documentation/images/resp_avast.jpg)

    * Netbox Browser:

        ![Netbox Browser](documentation/images/resp_netbox.jpg)

## **Lighthouse Inspection reports**
 - There are some issues when the page is opening using Google Chrome browser.

    * ![Google Chrome inspection](documentation/images/testing/light_1.jpg)

    However inspecting the page in Incognito Mode without any browser extensions shows results as follows

    * ![Google Chrome inspection](documentation/images/testing/light_2.jpg)

    Making Lighthouse inspections using different browsers show very similar results. 
    
    * ![Microsoft Egde inspection](documentation/images/testing/light_3.jpg)

    This is an example of Lighthouse inspection in Microsort Edge browser made using inPrivate mode.

## **Testing Functionalities:**

User Stories Tests:
* As a user I can mark an Item on the list as Urgent so that the Item will be moved to the top of the list or highlighted with a different color
* As a the application user I can create and add items to the shopping list so that the items can be displayed and marked as Done/Bought
* As a an application user I can mark an item as Bought so that the item will be moved to the botton of the list or removed from the list
* As a user I can register and login so that I can receive access to additional functions.
* As a user I can **Edit items already added to the list ** so that udpade items names and change quantity of the items
* As a user I can remove items from the list so that I don't have to store unwanted items on my shopping list
* As a user I can **remove all existing items at one click ** so that I can quickly remove one list and build a new one.

### Home Page:



![Microsoft Egde inspection](documentation/images/testing/home_page0.jpg)

### **Authentication:**

The user is able to register an account. After creating the account the user is able to Login and Logout from his account.
Logged in users gets access to all the application functions.

### Register a new account:

To create a new account enter the Register page and fill up the form which includes:
- User Name
- Email
- Password
- Repeated Password

![Microsoft Egde inspection](documentation/images/testing/register_page.jpg)

After filling up the form correctly and clicking "Sign Up" button the account is created 
and the user is redirected to the Home Page where the information about successful
register hould be dispayed.

![Microsoft Egde inspection](documentation/images/testing/register1.jpg)

![Microsoft Egde inspection](documentation/images/testing/register2.jpg)

### Login:

Users who already have their accounts can login in the Login Page.

![Microsoft Egde inspection](documentation/images/testing/login_page1.jpg)

Filling up the form correctly and clicking "Sign Up" button redirects the user to the Home Page.
Entering invalid data or not entering required data displays wqrning message.

![Microsoft Egde inspection](documentation/images/testing/logged_in_home.jpg)


### Logout:

To being logout the user should go to the Logout Page and after clicking "Sign Out" he is logged out and redirected to the Home Page.
Also information about being logged out is displayed.

![Microsoft Egde inspection](documentation/images/testing/logout_page.jpg)


![Microsoft Egde inspection](documentation/images/testing/logout.jpg)

### **Testing Lists functionalities:**

Creating shopping lists is one of the main functions of this application.


### Add List

To create a new List go to the Lists Page and click "Add New List" button.

![Microsoft Egde inspection](documentation/images/testing/add_list1.jpg)

After naming the new list click "Create List" button to create the list.

![Microsoft Egde inspection](documentation/images/testing/add_list2.jpg)
![Microsoft Egde inspection](documentation/images/testing/add_list3.jpg)

If the list name was successfully validated the user will be redirected to the Lists view page.

![Microsoft Egde inspection](documentation/images/testing/add_list4.jpg)

In case of unsuccessful validation a warning message is desplayed.

![Microsoft Egde inspection](documentation/images/testing/add_list5.jpg)

Also a handled Integrity Error can occured during adding a new List.

More information about the error in the Bugs and Errors section [here](README.md#7-bugs-and-errors).

![Microsoft Egde inspection](documentation/images/testing/add_list_integrity_error.jpg)

### Show Lists

Created lists are displayed in the Lists Page.

### Edit List

To change the list name click the "Edit" button on the list card. Enter the new name and submit changes clicking the "Submit Changes" button.
In case of successful validation the user will be redirected to the Lists page.
If the input in validated successfully a warning message is displayed.

![Microsoft Egde inspection](documentation/images/testing/edit_list1.jpg)

![Microsoft Egde inspection](documentation/images/testing/edit_list2.jpg)

![Microsoft Egde inspection](documentation/images/testing/edit_list3.jpg)

### Delete List

To delete a list click the "Delete" button on the list card. A confirmation window will be displayed.

Clicking "Yes" button the user submits deleting the list and its all items from the database.

Clicking "No" cancels hte operation and redirects the user back to the Lists Page.

![Microsoft Egde inspection](documentation/images/testing/delete_list2.jpg)

Deleting the list redirects the user to the Lists Page.

![Microsoft Egde inspection](documentation/images/testing/delete_list.jpg)


### **Testing Items functionalities:**

Adding and managing items is the main function this application. In this section I'm going to test Add, Edit and Delete functions as well as changing items status from "to buy" to "bought"

### Add Item

### Edit Item

### Delete Itme

### Show Items


 ### Item Functionalities Testings


## **Unfixed Bugs**
