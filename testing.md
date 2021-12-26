# Read and Recommend Website - Testing in detils

[The Website In Action](https://read-and-recommend.herokuapp.com/)       
[Main README.md file](README.md)

## Validation

- [HTML Validation](https://validator.w3.org/)    was used to validate all the HTML files.
  * **Important Note** on the pages with jinja template, the W3c validator throws many errors in regards to the syntax and variable names inserted by jinja template.          
  For instance:
    - It does not allow curly craces in "href", "src" and "action" attributes and it considers it as an error.
    - It does not accept variable names inserted in for loops in the "ul" elements.
    - It does not allow the code wrapped in curly braces to be palced in an element such as "a" and it considers it as "bad value".      
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) was used to validate the code in my style.css file.        
- The website has been tested with the Lighthouse for each page separately and on both desktop and mobile devices and, required actions have been taken to improve the functionality of the website as much as possible.
- Lighthouse was also used to check the overall performance of the website and as a way to improve the website performance.
                                  

| Known Issues | Causes |            
| ----------- | ----------- |
| The javascript does not run on IE 10 and earlier versions and as such the application does not run properly. | This is a browser issue on old versions of IE that do not have scripting enabled by default. |
| The back button on books.html does not return to the same scroll position on the previous page on Chrome, Edge and Opera but perfectly works on Safari and Firefox.| According to my inquiry about this issue, this is a browser issue which has been reported by many users but have not been fixed yet.|
| The back to top button does not always land on top of the footer as intended when resizing the window without reloading the page. | This happens because the bottom position of the button is defined with javascript on ready document state. |
     
   

| Bugs | Solutions |            
| ----------- | ----------- |   
| The back to top button did not always land on top of the footer as it intended when resizing the window without reloading the page. | This was solved by wrapping the variable that defines the footer's height in setInterval() function which runs every 500 miliseconds. |
| One of the challenges I faced in this project was styling the active links that point to a python view. The issue was originated from the fact that every time a link was clicked the whole page is refreshed and as a result, the applied style to the active links would disappear in a blink. | The issue was solved by using a built-in flask request.path attribute which was used to achieve this. |




## Client stories testing:

The potential common paths through the website:

- Home > Sign-Up
- Home > Sign-In 
- Home > Book 
- Home > Profile
- Book > Shopping Link
- Profile > Edit Profile
- Profile > Edit Book
- Profile > Add a Book
              

Each of these possible paths is achievable by simply navigating through the navigation bar or the links embedded in the footer.
### Testing client stories from UX section of [README.md](README.md)

1. 
2. 
3. 
4. 
5. 
   


## Manual (logical) testing of all elements and functionality on every page.      

###  Navigation Bar





###  Sticky back-to-top button
 - Verify that the button shows up in the right position on every page.
 - Click on the button to confirm that the button works.
 - Open the page in the "Developer Tool", choose a mobile device and ensure that the size and spacing of the button change properly-



### Footer
 - Confirm that footer code is identical on all HTML pages.


## Further Testing
 - I have tested the website on the following internet browsers and no serious issue was found:

     - Google Chrome
     - Safari
     - Firefox
     - IE
     - Edge
     - Opera


- I have tested the website on the following devices:

     - iPhone X/12/12 pro (On physical devices)
     - Galaxy S21 (On physical device)
     - iPad (On physical devices)
     - iPad Pro (Chrome Developer Tools)
     - iPad mini (Chrome Developer Tools)
     - Galaxy Note 3 (Chrome Developer Tools)
     - Galaxy S III (Chrome Developer Tools)
     - Laptops
 