# Our Gallery

## Introduction

My Our Gallery project is a fun online gallery blog for art lovers. It allows users to discuss the art with each other by leaving comments and liking the art pieces.

The admin of the site will be able to create new posts to show different pieces of art, they will be able to read what they have posted, update the posts and delete them if and when necessary. This shows the use of CRUD functionality in the project. The users will also be able to create, read, update and delete their comments making use of this functionality for both the users and admin of the site.

<img src="images/responsive.png" alt="Live website image"> 

[Click here to go to the live website!](https://ourgalleryyy.onrender.com) 

1. [Wireframes](#wireframes)
2. [User Stories](#user-stories)
3. [Objectives](#objectives)
4. [Features](#features)
    - [Navigation Bar](#navigation-bar)
    - [Links](#links)
    - [News Posts](#news-posts)
    - [Gallery Posts](#gallery-posts)
    - [Comments](#comments)
    - [Like](#like)
    - [Message](#message)
    - [Register](#register)
    - [Login](#login)
    - [Logout](#logout)
5. [Testing](#testing)
    - [HTML](#html)
    - [CSS](#css)
    - [Python](#python)
    - [Manual Testing](#manual-testing)
6. [Bugs](#bugs)
7. [Deployment](#deployment)
8. [Credits](#credits)

## Wireframes

### Home 
<img src="images/wire-home.png" alt="wireframe for home page">

### Gallery
<img src="images/wire-gallery.png" alt="wireframe for gallery page">

### Gallery Details
<img src="images/wire-gallery-det.png" alt="wireframe for gallery details page">

### News
<img src="images/wire-news.png" alt="wireframe for news page">

### News Details
<img src="images/wire-news-det.png" alt="wireframe for news details page">



## User Stories

I used the GitHub projects board to log my user stories to help me manage my project. 
This helped me break the project down into smaller tasks that would be more manageable by moving them into the in-progress section whilst I focused on them. once a task was complete, I could move it into the done section to help me see my progress.

<img src="images/userstory1.png" alt="user stories">
<img src="images/userstory2.png" alt="user stories">
<img src="images/userstory3.png" alt="user stories">
<img src="images/userstory4.png" alt="user stories">

## Objectives

- I want to create a page where the user can see multiple pieces of art so that they can select which ones they want to read more about.
    - Was this achieved?
        -  Yes
    - How was this achieved?
        -  I created a gallery that uses a view class called PostList, this allows the user to see multiple posts images and their titles on one page before looking into them in further detail.

- I want the users to be able to select an art piece then be taken to a page all about that piece of art.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - In the post model there is a slug field, this means that each post can have their own URL, so when the user clicks on the title they are taken to the posts individual page to see more detail on that piece.

- I want the users to be able to register for an account on the site.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - I used allauth to create three pages one to log in, one to log out and one to register as a user.

- When the user has an account, I want the users to be able to like a piece.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - In views.py I created a class called PostLike, it has an if statement that toggles the like button inside, so it checks if a logged in user has already liked a post and if yes, when it clicked it unlikes the post or if not then when clicked it likes it.

- I also want the users to be able to see how many likes a piece already has.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - in models.py within the post class i defined number of likes and returned self.likes.count() so that it would add the amount 0f likes up and return it to the page.

- when the user has an account, I want the users to be able to comment on a piece of art.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - In models.py I defined everything I need to make a comment in the Comment class, created a form in forms.py and used that within the post details view.

- I also want the users to be able to read other comments left on the art.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - In views.py post details view I rendered the comment form so if a user’s comment has been approved it can show in the post details html pages.

- I want the admin to be able to create, read, update and delete posts of art pieces on the site.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - when adding /admin to the end of the home URL the admin can login and create new posts.

- I want the admin to be able to approve or disapprove comments on the site to filter unwanted comments.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - In the admin.py file within the class commentadmin I added an action of approve comment, this allows the admin to approve a comment when they are logged into the admin panel.

## Features

### Navigation Bar

- The navigation bar contains the links needed to use the website easily. This changes how it looks depending on a couple of things, if the user is logged in or out but also depending on the size of the screen it is being viewed on.
<img src="images/nav-f.png" alt="Navigation function">
<img src="images/drop.png" alt="Navigation function">
<img src="images/dropin.png" alt="Navigation function">

### Links

- On the home page I have two links that are used to take the user to the two main pages on the site.

<img src="images/home-func.png" alt="link function">

### News Posts

- Each news post contains a link in its title, these links take the user to the relevent news post detail page to read more. 

<img src="images/news-func.png" alt="news post function">

- If the user is an admin they will see the options to delete or edit a news post.
<img src="images/news-f.png" alt="news post function">

- If the user is an admin they can edit a news post.
<img src="images/news-edit.png" alt="news post edit function">

### Gallery Posts

-  Each gallery post contains a link in its title, these links take the user to the relevant gallery post detail page to read more. 

<img src="images/gallery-func.png" alt="gallery post function">

- If the post belongs to this user they will see the options to edit or delete the post.
<img src="images/gallery.png" alt="gallery post function">

- The post edit page allows the user that owns the post to make changes.
<img src="images/post-edit.png" alt="gallery post edit function">

### Comments

- Within each gallery post details page there is a comment section, this allows the user to interact with the site, and have conversations about the art shown.

<img src="images/comment.png" alt="comment function">

- If the comment belongs to the user they will see the options to edit or delete the comment.
<img src="images/comment-f.png" alt="comment function">

- If edit is clicked by the user they will be taken to the edit comment page to change their comment.
<img src="images/edit-comment.png" alt="comment edit function">

### Like

- On each gallery post in their details page you have the ability to like or dislike a post

<img src="images/like.png" alt="like function">

### Message

- when a user logs in or out they will see a message pop up and automatically leave after a few seconds.

<img src="images/message.png" alt="message function">

### Register

- The register function allows the user to create a profile so that they can log in and out of the site.

<img src="images/register.png" alt="register function">

### Login

- The login function allows the user to log into their account so that they can like a post or leave a comment.

<img src="images/login.png" alt="login function">

### Logout

- the log out function allows the user to sign out after they are finished on the site.

<img src="images/logout.png" alt="logout function">

## Testing

### HTML

HTML was tested using the official [W3C validator](https://validator.w3.org/nu/) 

The following errors/warnings were found:

<img src="images/html-home.png" alt="Testing html for home page">
<img src="images/hmtl-home1.png" alt="Testing html for home page">

1. lang missing from <html> tag.
    - To fix this i just added lang="en" to the <html> tag.

Retested: Warning cleared

2. An image must have an alt attribute.
    - For both of these errors I added and alt attribute to the images that have details of the image just in case the image doesn't load.

Retested: Error cleared

3. Element div not allowed as child on ul.
    - I Added an li around the dropdown div.

Retested: Error cleared

<img src="images/html-gallery.png" alt="Testing html for gallery page">

1. An image must have an alt attribute.
    - I had made the same mistake of forgetting to add an alt attribute on the gallery page so followed the same process to fix these errors.

Retested: Error cleared

<img src="images/html-news-det.png" alt="Testing html for news detail pages">

1. Bad value on image element
    - To fix this I put it into the CSS style sheet.

2. The font element is obsolete 
    - I didn’t recognise this code so I searched for the code it gave me on the error page in my base.html and news_detail.html files and no results were found, I’m unsure where it has pulled this code from, and I believe the third error is also in relation to this.

<img src="images/html-gallery-det.png" alt="Testing html for gallery detail pages">

1. Element div not allowed as child of element h2 
    - I didn't recognise this code so I searched for h2 in my base.html and news_detail.html files and no results were found.

2. No p element in scope but a p end tag seen.
    - i searched for a stray </p> but none were found in either file.



### CSS
 
CSS was tested using the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/)

No errors were found:

<img src="images/css-home.png" alt="Testing css for home page">
<img src="images/css-gallery.png" alt="Testing CSS for gallery page">
<img src="images/css-gallery-det.png" alt="Testing CSS for gallery details pages">
<img src="images/css-news.png" alt="Testing CSS for news page">
<img src="images/css-news-det.png" alt="Testing CSS for news details pages">

### Python
 
Python was tested using the official [PEP8](http://pep8online.com/)

The following errors were found:

<img src="images/py.png" alt="Testing python">

To fix these all I had to do was extend the code onto the next line, all of these errors were caused by comments.

### Manual Testing 

Component | Function | Does it work? | Fixed? 
--------- | --------- | ----------------- | ------ |
Logo | Takes user to home page | Yes | N/A
Navbar: Home | Takes user to home page | Yes | N/A
Navbar: News| Takes user to news page | Yes | N/A
Navbar: Gallery | Takes user to gallery  | Yes | N/A
Navbar: My Account | Show user drop down menu, if user is not signed in it should show login, register. If user is an admin it should show add news, add post and log out. if loged in but not admin user should see log out and add post. | Yes | N/A
Navbar: Register | Takes user to the sign up page  | Yes | N/A
Navbar: Login | Takes user to the login page  | Yes | N/A
Navbar: logout | Takes user to the log out page  | Yes | N/A
Navbar: Add post | Takes user to the add post page  | Yes | N/A
Navbar: Add news | Takes admin to the add news page  | Yes | N/A
Home: see the latest exhibition | Take user to news page | Yes | N/A
Home: Head over to gallery | Take user to gallery page | Yes | N/A
News: News post slug links | Takes user to relevant news post details page  | Yes | N/A
News: Edit | If user is an admin they should see an edit button which will take them to the edit news page  | Yes | N/A
News: Delete | If user is an admin they should see an delete button which will delete that news article | Yes | N/A
News Detail: Edit | If user is an admin they should see an edit button which will take them to the edit news page  | Yes | N/A
News Detail: Delete | If user is an admin they should see an delete button which will delete that news article | Yes | N/A
Gallery: Post slug link | Takes user to relevant post details page | Yes | N/A
Gallery: Edit | If user is creator of post they should see an edit button which will take them to the edit their post | Yes | N/A
Gallery: Delete | If user is creator of the post they should see an delete button which will delete that post | Yes | N/A
Post Detail: Edit | If user is creator of post they should see an edit button which will take them to the edit their post | Yes | N/A
Post Detail: Delete | If user is creator of the post they should see an delete button which will delete that post | Yes | N/A
Post Detail: like and unlike button | Allows user to like or unlike a post when logged in  | Yes | N/A
Post Detail: Submit button | Allows user to leave a comment for the admin to validate and eventually for everyone to view on the page  | Yes | N/A
Post Detail: Login | if user is not logged in the will see a message asking them to login if they want to make a comment, this should take them to login page | Yes | N/A
Add News: Choose file | This should allow the admin to pick a picture for their news post | Yes |N/A
Add News: Cancel | This should redirect the admin to home page | Yes |N/A
Add News: Add Article | This should allow the admin to add a news post | Yes |N/A
Add Post: Choose file | This should allow the user to pick a picture for their post | Yes |N/A
Add Post: Cancel | This should redirect the user to home page | Yes |N/A
Add Post: Add Post | This should allow the user to add a post | Yes |N/A
Register: Sign up button | Allows user to sign up  | Yes | N/A
Register: Sign in | This link will take the user to the dign in page | Yes | N/A
Login: Sign in button | Allows user to sign in  | Yes | N/A
Login: Sign up | Takes user to sign up page | Yes | N/A
Logout: Sign out button | Allows user to sign out  | Yes | N/A


## Bugs

I ran into this error message:

<img src="images/error.png" alt="error message">

I realised that I was missing news/ from my news/< slug:slug >/ in my urls.py file, when I changed that it worked but my page wasn't rendering correctly.

This is how it rendered:	

<img src="images/render.png" alt="image of how page was rendering incorrectly">

I originally had written return render(request, "news_detail.html")
so I tried this:

<img src="images/fix2.png" alt="image of how I tried to fix">

This didnt work so I also tried:

<img src="images/fix.png" alt="image of how I tried to fix">

Then I noticed a spelling error in the first attempt I had written new_detail.html when I was supposed to write news_detail.html and then it all worked.

## Deployment

- Create a new app on heroku 
- In resources add heroku postgres
- In settings review config vars, copy the DATABASE_URL
- In gitpod make a file called env.py, use this to store our environment variables.
- make sure env.py is in gitignore file
- Add your secret key environment variable to both the env.py file and heroku config vars
- Reference the env file in the settings.py file.
- Add the secret key environment variable to settings.py.
- Highlight database section and comment it out, 
replace with the following:
DATABASES = {
   'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
- run migrations

## Credits

Thankyou to tutor support for helping me figure out my bug.

The run through project was helpful for getting me through this project I went back to see how classes were used throughout the making.

Gallery images from: https://www.istockphoto.com/

News content: https://visitlondon.com/things-to-do/whats-on/art-and-exhibitions/top-10-exhibitions

Am I responsive: http://ami.responsivedesign.is/
