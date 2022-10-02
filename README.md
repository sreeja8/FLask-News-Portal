# Flask-News-Portal

This is a news portal app where general audience can see multiple news articles posted by multiple editors. There is also the Editor's corner through which editors can login to the site and add or remove news as per their requirement. This website has been developed in flask.

#### Home Page :
which displays news posted by different editors along with the editor/author of each news. Regular audience are able to view this page as well as Editors.
#### Editor's Corner : 
Editors will click on this and will be routed to Login and Signup page. Only Editors can login/signup on the portal.
#### Login :
Editor login page, also has a redirection to sign up page if an editor has not yet signed up. Editors can post news only if they have logged in to this website.
#### Sign up :
Sign up page for editors.
#### Editor's News :
Logged in editor can add or delete news to his profile. This news gets stored into the database along with author/editor details such as name, time, etc.
#### Logout :
Logout functionality for editors.

### APIs

`/`: `GET` call renders the home page to any user that has all news added by all editors.

`/login`: `GET` call renders the login page to the user.
          `POST` call logs in the user.

`/logout`: `GET` call logs the editor out.

`/editor_corner/sign-up`: `GET` call renders the sign-up page to the user.
                          `POST` call commits the user account to the database and redirects the user to login post successful account creation.
                     
 
`/editor_news`: `GET` call renders only the news previously added by the logged in editor.
                 `POST` call commits the news added by the logged in user.
                 
`/delete-note`: `POST` call helps editor to delete his own news.

## **Demo**

![2022-09-29 16-44-46-79](https://user-images.githubusercontent.com/112502713/193017778-ad6ad5d6-0a5b-4a92-9604-6871cb25322b.gif)
