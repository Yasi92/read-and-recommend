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
                                  


| Bugs | Solutions |            
| ----------- | ----------- |   
| The back to top button did not always land on top of the footer as it intended when resizing the window without reloading the page. | This was solved by wrapping the variable that defines the footer's height in setInterval() function which runs every 500 miliseconds. |
| One of the challenges I faced in this project was styling the active links that point to a python view. The issue was originated from the fact that every time a link was clicked the whole page is refreshed and as a result, the applied style to the active links would disappear in a blink. | The issue was solved by using a built-in flask request.path attribute which was used to achieve this. |



| Known Issues | Causes |            
| ----------- | ----------- |
| The javascript does not run on IE 10 and earlier versions and as such the application does not run properly. | This is a browser issue on old versions of IE that do not have scripting enabled by default. |
| The back button on books.html does not return to the same scroll position on the previous page on Chrome, Edge and Opera but perfectly works on Safari and Firefox.| According to my inquiry about this issue, this is a browser issue which has been reported by many users but have not been fixed yet.|
| The back to top button does not always land on top of the footer as intended when resizing the window without reloading the page. | This happens because the bottom position of the button is defined with javascript on ready document state. |
     
  

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
              

Each of these possible paths has been tested repeatedly.
### Testing client stories from UX section of [README.md](README.md)

1. As a first-time visitor, I would like to find a worth reading book.
- I browse the book list on the home page until I find something interesting, click on the book once found it, read the description and information provided on the page, click on the "G0 Get It" button to head to the store.
2. As a first-time visitor, I would like to find out more about my favorite book and read other readers' reviews.
- I type the book title in the search box embedded in the navigation bar to find my favorite book.
- I select the related category of my favorite book, scroll the page down to find my intended book.
3. As a first-time visitor, I would like to become a member of the community to be able to add my favorite book to the website.
- I navigate to the sign-up page and create an account, following that I will be navigated to the profile page where I can see the "Add a Book" button on top of the page as well as in the navigation bar. Finally, I enter the requested data in each field and the book I intend will be added to the website. I will be provided with a feedback message confirming that I added the book.
4. As a returning visitor, I would like to edit my profile and info.
- I log in to my account, click on the edit-profile button to get navigated to the edit profile page. On the edit-profile page, I see a pre-filled form with my account detail where I can update any field I intend and submit the form to modify my profile. I will be provided with a feedback message confirming that I updated my profile.
5. As a returning visitor, I would like to write a review about a book I have recently read/purchased from the online store.
- I first log in to my account, then I will look for the book I am looking for, after having it found I scroll down the page until I see the review form, fill out the form, and submit it. I will be provided with a feedback message thanking me for the review.
6. As a returning visitor, I would like to check out all the best seller books on the website and find out more about them.
- I navigate to the home page, click on the "Best seller" link on the collection bar and then I can see all the best seller books.
7. As a returning visitor, I would like to delete a review I left on a book.
- I log in to my account, navigate to my profile page, find the review I am looking for in the "Added reviews" section and click on the delete button. I will be provided with a feedback message confirming that I deleted the review.
- I log in to my account, type the book title on which I left the review, click on the book once it is found, scroll down the page to the review section, find my added review among other reviews (Which is pretty distinguishable since there is a red "Delete" button on the review I added) and finally, click on the "Delete" button. I will be provided with a feedback message confirming that I deleted the review.
8. As a returning visitor, I would like to edit a book I added to the website.
- I log in to my account, navigate to the profile page, scroll down the page until I find the intended book, click on the "Edit" button, I will be navigated to a page with a pre-filled form with the book details and from there I will be able to modify any field I want and finally click on the "Submit button". I will be provided with a feedback message confirming that I edited the book.
- I log in to my account, type the book title I want to edit in the search box, click on the book, from the book detail page I can see an "Edit" button, I click on that, and next I will be navigated to a page with a pre-filled form with the book details and from there I will be able to modify any field I want and finally click on the "Submit button". I will be provided with a feedback message confirming that I Edited the book.
9. As a returning visitor, I would like to Remove a book I added to the website.
- I log in to my account, navigate to the profile page, scroll down the page until I find the intended book, click on the "Delete" button which opens to modal confirming if I am sure I want to delete the book, I click on "Yes" button and the book will be removed. I will be provided with a feedback message confirming that I deleted the book.
- I log in to my account, type the book title I want to edit in the search box, click on the book, from the book detail page I can see an "Delete" button, I click on that, and next I will be navigated to a page with a pre-filled form with the book details and from there I will be able to modify any field I want and finally click on the "Submit button".
10. As a visitor, I would like to filter the books by the category I am looking for.
- I navigate to the home page (whether I am logged in or not), select the category from the collection bar, and then I can see all the books with the category I am interested in.

   


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
 