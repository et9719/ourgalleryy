# Our Gallery

## Introduction

My Our Gallery project is a fun online gallery blog, it allows users to discus the art with eachother by leaving comments and liking the art pieces.

The admin of the site will be able to create new posts to show differnt pieces of art, they will be able to read what they have posted, upate the posts and delete them if and when nessasary. This shows the use of CRUD functionality in the project. The users will also be able to create, read, update and delete their comments making use of this functionality for both the users and admin of the site.

<img src=" <!--Add Live Web Image--> " alt="Live website image"> 

[Click here to go to the live website!](<!--Add Website Link-->) 

1. [Wireframes](#wireframes)

2. [User Stories](#user-stories)
3. [Objectives](#objectives)

4. [Features](#features)
  
## Wireframes

### Home 
<img src="static/images/" alt="wireframe for home page">
<img src="static/images/" alt="wireframe for mobile home page">

## User Stories

I used the GitHub projects board to log my user stories to help me manage my project. 
This helped me break the project down into smaller tasks that would be more manageable by moving them into the in progrss section whilst I focused on them. once a task was complete I could move it into the done section to help me see my progress.


<img src="static/#" alt="user stories">
<img src="static/#" alt="user stories">
<img src="static/#" alt="user stories">
<img src="static/#" alt="user stories">

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
        - In the post model there is a slug field, this means that each post can have their own url, so when the user clicks on the title they are taken to the posts individual page to see more detail on that piece.

- I want the users to be able to register for an account on the site.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - I used allauth to create three pages one to log in, one to log out and one to register as a user.

- When the user has an account I want the users to be able to like a piece.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - In views.py I created a class called PostLike, it has an if statement that toggles the like button inside so it checks if a logged in user has already liked a post and if yes, when it clicked it unlikes the post or if not then when clicked it likes it.

- I also want the users to be able to see how many likes a piece already has.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - in models.py within the post class i defined number of likes and returned self.likes.count() so that it would add the amount 0f likes up and return it to the page.

- when the user has an account I want the users to be able to comment on a piece of art.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - In models.py I defined everything I need to make a comment in the Comment class, created a form in forms.py and used that within the post details view.

- I also want the users to be able to read other comments left on the art.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - In views.py post details view I rendered the comment form so if a users comment has been approved it can show in the post details html pages.

- I want the admin to be able to create, read, update and delete posts of art pieces on the site.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - when adding /admin to the end of the home url the admin can login and create new posts.

- I want the admin to be able to approve or disapprove comments on the site to filter unwanted comments.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - In the admin.py file within the class commentadmin I added an action of approve comment, this allows the admin to approve a comment when they are logged into the admin pannel.

## Features





images from : https://www.istockphoto.com/


gallery content: https://visitlondon.com/things-to-do/whats-on/art-and-exhibitions/top-10-exhibitions