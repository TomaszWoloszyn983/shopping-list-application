# Testing


##  Responsiveness
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
    
    <!-- Link to the test
         https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Ftomaszwoloszyn983.github.io%2Fswap-puzzle-game -->

- JAVASCRIPT
    <!-- * No errors were detected when passing through the [jshint](https://jshint.com/) validator.

    ![Javascript Validation](documentation/images/validation_js.jpg) -->

- PYTHON


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


- Although the game is also responsive on every type of mobile devices as Tablets or Smart Phones, most of the devices using touch screen don't support Drag and Drop technology.
    **On every mobile device I've tested the game, the drag and drop functionality did NOT work properly**. Even connecting a mouse for the test using a recommended adapter, did not solve the problem and the tiles were still unable to drag.
    That's why it is NOT recommended to use mobile devices for this game.

    ![Mobile phone](documentation/images/resp_mobile_2.jpg)
    ![Mobile phone](documentation/images/mobile_issue.jpg)
    
    ![Mobile phone](documentation/images/resp_mobile_4.jpg)

 


## **Unfixed Bugs**
- The main unfixed bug is the lack of support for mobile devices, such as smart phones using touch screens.
- There are no other bugs that I am aware of.