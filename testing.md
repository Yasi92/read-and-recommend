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
| When testing the edit_book function, noticed that it does not check if the book title already exists in the database before updating the book and as a result, there was a high chance of duplicated books on the website. | I fixed this by adding a line of code before updating the book collection in the database which queries all the books with the same title and resets the form if there is one. |
| When testing the "edit_profile" and "edit_book" function in app.py, noticed that there is a bug in the code when I try to update any other fields than the title and username fields in the form. This happened since I was trying to avoid a duplicate username and title in those functions and as such I would have reset the form if the title and username had already existed in the database. The main issue was that all the fields in the form were pre-filled and given a value from the database and, consequensntly the if statement would consider an untouched title and username as new data which already existed in the database. | I got around this issue by adding extra "elif" statements that check if the username and title from the database are equal to the value from the form and in that case, they won't be considered as "exsisting_user" and "exsisting_book" and this will allow to update the other fields. | 




| Known Issues | Causes |            
| ----------- | ----------- |
| The javascript does not run on IE 10 and earlier versions and as such the application does not run properly. | This is a browser issue on old versions of IE that do not have scripting enabled by default. |
| The back button on books.html does not return to the same scroll position on the previous page on Chrome, Edge and Opera but perfectly works on Safari and Firefox.| According to my inquiry about this issue, this is a browser issue which has been reported by many users but have not been fixed yet.|
| The back to top button does not always land on top of the footer as intended when resizing the window without reloading the page. | This happens because the bottom position of the button is defined with javascript on ready document state. |
| The python code in some functions such as "edit_form" and "edit_profile" may be quite verbose and I believe it could have been more "DRY". | This has not been fixed as I believe it requires more experience and time to debug. |
     
  

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
- Click on every single link on the navigation bar to assure they are all properly wired up.
- Check the page URL and make sure it shows the right path name. (http://read-and-recommend.herokuapp.com/get_books)
- Check the accessibility to the links that are supposed to be visible on the two different states of logged In/Out.
- Hover over every single link to make sure they have the proper style.
- Click on the links and make sure the active style is applied to them until another link is clicked.
- Change the screen size from desktop to tablet to verify that the navigation bar is responsive and switches from the inline menu to the burger icon dropdown menu at the appropriate place.
- Click on the burger icon to make sure the menu opens from the right side of the screen.
- Check the search box size and function on the home page.
- Type a book title that is known it exists and make sure it will be displayed.
- Type an author name and make sure it displays all the books from that author.
- Type a title or an author name which is known it does not exist in the database and make sure the "No Results found" text displays on the screen.
- Click on the reset button and make sure it resets the searches and displays all books.


### Home page
- Click on every collection bar link and make sure they display the books from the right category.
- Check the page URL and make sure it shows the right path name as expected. (http://read-and-recommend.herokuapp.com/get_books/get_categories/history)
- Make sure the active style is applied to the links on click.
- Resize the window size and make sure that the links have proper position and padding on the iPad and mobile screen.
- Scroll down the page and check the layout of the book cards on the home page.
- Click on the book cards and make sure they navigate to the corresponding book detail page.
- Hover over the book cards and make sure they have the applied style.
- Resize the window in the iPad and mobile screen size to make sure all sections are responsive and the layout changes on different screen sizes.


### Book Detail page
- Click on the back button and make sure it returns to the previous home page on the same scroll position.
(As explained above, this does not always work properly on Chrome and Edge browsers and it is considered as a browser incompatibility)
- Check the page URL and make sure it shows the right path name as expected and that the book is triggered by its ObjectId. (http://read-and-recommend.herokuapp.com/get_book/61b89fed83b47941f2028fbd)
- Click on a book from the best seller category and make sure the best seller badge displays on top of the book title.
- Click on a book from non best seller category and make sure the best seller badge does not display.
- Click on the "Go Get It" button and make sure it navigates to the store in a new tab.
- Find a book that was added by the user and make sure the "Delete" and "Edit" buttons are displayed in the section.
- Click on the "Edit" button and make sure it navigates to the edit book page.
- Click on the "Delete" button on the added books and make sure before the deletion it opens a delete confirmation modal. 
- Make sure the modal triggers the right book to delete.
- Ignore the deletion and make sure it returns safely to the profile page.
- Submit the deletion and make sure the feedback message pops up on the page informing the book was deleted.
- Find another book that was not added by the user and make sure the "Delete" and "Edit" buttons are not accessible.
- Click on the "Read More" text on the book description and make sure it expands the description text.
- Try to write a review in the review form and submit it when the user is not logged in and make sure it returns to the login page with a feedback message asking the user to login first.
- Try to submit a review when the user is logged in and make sure that the review is submitted successfully and the user is provided with a feedback message thanking them for their feedback.
- After submitting a review, scroll down the page and make sure your review is displayed in the review section with correct data.
- Check if the time for the added review is shown in a format of time ago properly.
- Check a book with more than 4 reviews and make sure the reviews are displayed in slices of 4 and the "Load More" button is shown underneath the reviews.
- Click on the "Load More" button and make sure more reviews in slices of 4 will be displayed and that the button fades out once there are no more reviews to display..
- Check a book with less than 4 reviews and make sure all the reviews are displayed and the "Load More" button does not show.
- Resize the window in the iPad and mobile screen size to make sure all sections are responsive and the layout changes on different screen sizes.



### Edit Book Page
- Check the page URL and make sure it shows the right path name as expected and that the book is triggered by its ObjectId to be edited. For instance(http://192.168.1.13:8000/edit_book/61b10198aed1435538424f4e)
- Make sure the form is already pre-filled by the book details.
- Try to change the book title to an already existing title and make sure it displays a feedback message informing that the book title already exists, without updating the book.
- Try To change any field from the form and submit the form. Make sure the book is updated as expected and it redirects to the book detail page with the updated data.
- Try to uncheck the best seller check box and make sure that after the submission the best seller badge is removed from the title. 
- Try to modify any field on the form except the title and make sure it updates the form accordingly.
- Resize the window in the iPad and mobile screen size to make sure all sections are responsive and the layout changes on different screen sizes.




### Profile Page
- Make sure your account details are displayed correctly on the profile page.
- Check the page URL and make sure the username is displayed after the profile path. For instance (http://read-and-recommend.herokuapp.com/profile/zahra)
- Click on the "Edit Profile" button and make sure it navigates to the edit profile page with a pre-filled form with the user's account info.
- Click on the "Add a Book" button and make sure it navigates to the Add a book page.
- Scroll down the page and check the list of the books added by the user.
- Click on any part of the added book such as its image, title, or author, and make sure it navigates to the book detail page.
- Click on the "Edit" button on the added books and make sure it works.
- Click on the "Delete" button on the added books and make sure before the deletion it opens a delete confirmation modal. 
- Make sure the modal triggers the right book to delete.
- Ignore the deletion and make sure it returns safely to the profile page.
- Submit the deletion and make sure the feedback message pops up on the page informing the book was deleted.
- Login with a user account with more than 6 added books and make sure the added book list on the profile page displays in slices of 6 and that the "Load More" button is visible.
- Click on the "Load more" button and make sure it displays more added books in slices of 6 and that the button fades out once there are no more books to display.
- Login with a user account with less than 6 added books and make sure that all the added books are displayed and the "Load More" button is not visible.
- Login with a user account with more than 4 added reviews and make sure the review list on the profile page displays in slices of 4 and that the "Load More" button is visible.
- Click on the "Load more" button and make sure it displays more reviews from the user in slices of 4 and that the button fades out once there are no more reviews to display.
- Login with a user account with less than 4 added reviews and make sure that all the reviews are displayed and the "Load More" button is not visible.
- Make sure a "Delete" button is featured on every review added by the user.
- Check the time of the added review is correctly shown in a format of time ago.
- Click on the "Delete" button on the review section and make sure before the deletion it opens a delete confirmation modal. 
- Make sure the modal triggers the right review to delete.
- Ignore the deletion and make sure it returns safely to the profile page.
- Submit the deletion and make sure the feedback message pops up on the page informing the review was deleted.
- Resize the window in the iPad and mobile screen size to make sure all sections are responsive and the layout changes on different screen sizes.


### Edit Profile Page
- Check the page URL and make sure the user is triggered to be edited by its ObjectId. For instance (http://192.168.1.13:8000/edit_profile/61c331f5cd6335d6a47fcc2f)
- Make sure all fields on the edit profile page are pre-filled with the user's account info.
- Change the username to an already existing username and make sure it returns a feedback message informing that the username already exists in the database and that nothing will be changed in that case.
- Change the username to a new username and make sure the feedback message pops up on the page informing that the profile has been updated. 
- Check if after updating the username, it redirects to the profile page with the updated username and that the profile name updates correspondingly in the URL path.
- Check if after updating the username, all the books and reviews added by the user are updated accordingly in the review and book collections.
- Try to click on the "Save" button without making any change to the profile info and make sure it returns to the profile page without any feedback message.
- Click on the "Cancel" button and make sure it returns to the profile page without any changes to the account info.
- Try to change other fields in the form such as location and/or email address and check if the feedback message pops up and the data has been updated on the profile page.
- Resize the window in the iPad and mobile screen size to make sure all sections are responsive and the layout changes on different screen sizes.



### Add a Book Page
- Click on every single field and make sure they have the applied active style.
- Try to submit the form with every field empty at a time and make sure it shows the validation error message.
- Fill out the form accordingly and submit it. Next check if the book is successfully added with the correct detail and a feedback message pops up informing the book has been added.
- Resize the window in the iPad and mobile screen size to make sure all sections are responsive and the layout changes on different screen sizes.



### Sign In page
- Sign Out the account and make sure the feedback message pops up on the window informing that you have been logged out.
- Sig out the account and make sure you are navigated to the login page.
- Click on every field to assure that the active style is applied to the fields and that the labels jump up and make space for the input value.
- Click on the "log In" button and make sure you are navigated to your profile page.
- Check the "Register Account" link underneath the "Log In" button and make sure it navigates to the Sign Up page.
- Try to log in with an incorrect username and/or password and make sure you won't be logged in and that a feedback message pops up on the window informing that the "Username/Password is incorrect".
- Resize the window in the iPad and mobile screen size to make sure all sections are responsive and the layout changes on different screen sizes and that the image card won't be displayed on mobile screen.


### Sign Up page
- Click on every field to assure that the active style is applied to the fields and that the labels jump up and make space for the input value.
- Try to create an account and leave a field blank to check if the validation error messages pop up.
- Try to create a username that already exists in the database and make sure a message pops up on the page informing that the username already exists.
- Try to fill out the form correctly and click on the "Register" button and make sure you are navigated to your profile page with a feedback message informing that you have registered successfully.
- Try to create a password and then add a non-matching password in the confirm password field and make sure the error message pops up.
- Check the "Log In" link underneath the "Register" button and make sure it navigates to the Sign In page.
- Resize the window in the iPad and mobile screen size to make sure all sections are responsive and the layout changes on different screen sizes and that the image card won't be displayed on the mobile screen.


###  Sticky back-to-top button
- Verify that the button shows up in the right position on every page.
- Click on the button to confirm that the button works.
- Open the page in the "Developer Tool", choose a mobile device and ensure that the size and spacing of the button change properly.
- Click on the button and make sure that the animation effect works properly and the page scrolls to the top smoothly.



### Footer
- Confirm that footer code is identical on all HTML pages.
- Try to log in and check the footer on every single page to make sure that the links embedded in the footer updates accordingly.
- Try to log out and check the quick access links in the footer alters according to the navigation bar links on different pages.
- Resize the window in the iPad and mobile screen size to make sure all sections are responsive and the layout changes on different screen sizes.
- From the home page, check if all the book collection links are accessible from the footer as well, and check every link separately.



### Custom 404 Page
- Try to change the path name in the URL manually to a random name and make sure that the custom 404 page appears on the screen informing you that the page is not found.
- Click on the "Let's Go Home" button and make sure it returns you to the home page.



### Custom 500 Page
- From the home page click on a book card and then from the URL try to change the book id in the URL path to something random. Make sure that the custom 500 page appears on the screen informing you that something went wrong.
- Click on the "Let's Go Back" button and make sure it returns you to the home page.
- **Note** that this is something that you can examine only if the Debugger is False in your flask app.


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
 