
<!-- TOC ignore:true -->
# LitList - Online Book Management 

![LitList Mockup](/static/docs/litlist_mockup.png)
<a href='https://pp4-litlist-dee1a055f48d.herokuapp.com/'>LitList</a> is a browser based book management system for users to register the books they have in their own home library for easy overview, management and sharing.

The site provides a user-friendly interface that enables users to create, edit, delete, and view their books in an easy and intuitive way. The users full library is shown in a limited overview where the user can also click on each book for further details.


> Note: The current form is an MVP (Minimum Viable Product) of the project. Further development will bring more functionality, better design and more intuitive navigation. In regards to design, the color scheme currently on the project was an early draft that due to personal health never was made time to alter, thus the amount of contrast errors. I am aware of these and they are on the list of things to edit in the future.

<br>

# Index

- [Features](#features)
    - [Future Features](#future-features)
- [Development](#development)
    - [Wireframe mockups](#wireframe-mockups)
    - [Database](#database)
    - [Technologies used](#technologies-used)
- [Deployment](#deployment)
- [Testing](#testing)
    - [Manual Feature Testing](#manual-feature-testing)
    - [Lighthouse validation](#lighthouse-validation)
    - [Python validation](#python-code-validation)
    - [HTML validation](#html-validation)
    - [CSS validation](#css-validation)
    - [Responsiveness](#responsiveness)
- [Credits](#credits)

<br>

# Features
What follows is a description of all parts and functions of the app:

### Account Registration
In order to use the site, a user must register for the site. I have chosen to use Django-Allauth for this, in hopes of adding social media login functionality down the road.
For now, a user can register using a username/email and password.

![Account Registration](/static/docs/scr-registration.png)


### User Library
The main purpose of this webapp is for users to be able to keep track and easily manage the books they own, and be able to access their at-home library titles from anywhere they go. The User Library is therefor the main feature of this project.

Here, users can register their books in two different ways. By clicking [Add Book](/static/docs/scr-lib-addbook.png), which gives a full form with all the book details they might want to register, including review and book description, or by clicking the [Quick Add](/static/docs/scr-lib-quickadd.png) button which brings up a "light version" of the add book form with only the vital pieces of information.

![User Library](/static/docs/scr-lib-table.png)

### Search, Filter and Sort
Within the User Library View, the user can search for book titles, authors and series (as shown on the image) to find more exact matches to what they are looking for.
The user can also choose to sort the books (alphabetically) by any of the details included in the library table.

![Search Function](/static/docs/scr-lib-search.png)

### Book Details Page
Although the user can see the most important book information in the Library View, the table would be incredibly big and difficult to manage if it included everything.
Thus, Each book has its own Details page (accessed by clicking the book title in the library table). Here, all the registered book details will show up.
From here, the user can also choose to edit or delete a book.

![Book Details View](/static/docs/scr-lib-bookdetails.png)

### User Profile
To make the site more interesting and personal, I have included a way for a user to setup a user profile.
With information such as profile picture, bio, book site links and a wishlist, the user can feel certain that their mark on the site is made personal and memorable.
When looking at ones own profile, there is an [Edit Profile](/static/docs/scr-profile-edit.png) button in the bottom right, which opens the form to add, remove or edit profile information.

![User Profile](/static/docs/scr-profile-own.png)
<br>

#### Privacy Settings
Within the Edit Profile Form, the user has an option to make their profile (and all subsequent pages such as library) private. If another user tries to enter their page, they will be given an error.
![Privacy Switch](/static/docs/scr-profile-private.png)
![Private Profile](/static/docs/scr-profile-hidden.png)


## Future Features 
These are features that were considered, but not implemented into the MVP version of this project.
- Friend Requests between Users
- Site Translation (To Swedish first and foremost)
- List 5-Star Reads on User Profiles
- Social accounts integration in site registration
- Google Books / Goodreads API Integration
- Password reset

<br>

# Development
This project was created with all of the methods and theories we've learned so far in the course in mind. In accordance with agile methodology and MoSCoW prioritization I set up a project board which you can find [here](https://github.com/users/ArcLiz/projects/3), that I have been working by to a large extent. 

The board is made up of User Stories that I settled on after brainstorming session, in which I had help from my mother (who is an incredible book collector and the inspiration for the project) and friends from the bookish online communities I am a part of. I read and own many books myself, but I felt I needed the input of other readers and book collectors to create the most usable tool possible.

On the board, you'll see that the user stories are labeled according to the MoSCoW prioritization theories and also broken down into acceptance criteria which I have tried to work by in developing the project and its features and functions. 

I find setting the board up, with user stories and acceptance criteria, to be quite difficult. This due to me personally having issues with breaking what I feel are big concepts down into small sentences and steps. However, I do find that once the steps are properly done and thought out, it is easier to work by them rather than with my "big concept ideas". It is a learning curve with theories and methodologies that I can see the purpose of, even if its difficult for me.
<br>

## Wireframe mockups
As this project at core is a modernization of an old project of my stepfathers (listed in the credits section), I did not originally feel the need to create in depth wireframes. I sketched the 3 different "main views" of the site with pen and paper but have made them presentable for the scope of the documentation of this project as shown below.

**Main Library View**
![Library Wireframe](/static/docs/wireframe-library.png)
<br>
**Book Details View**
![Book Details Wireframe](/static/docs/wireframe-bookdetails.png)
<br>
**User Profile View**
![Profile Wireframe](/static/docs/wireframe-profile.png)


## Database

![Schema](/static/docs/database_schema.png)

## Technologies used

- **Django** - Used as the project Framework
- **PostgreSQL** - Used for project database (via ElephantSQL)
- **Cloudinary** - Used as cloud storage of all static files
- **HTML** - Used for base structure and layout
- **CSS/JavaScript** - (Bootstrap 5) - Used for design and responsiveness of the project
- **Font Awesome** - Used for Icons throughout the site
- **Git** - Used for version control during the different project stages.
- **GitHub** - Used to store the code throughout the development
- **Heroku** - Used to deploy the project

### Supporting Libraries
`django-crispy-forms` - used for nicer forms throughout the site<br>
`django-allauth` - used for authorization (account creation and management)<br>
`django-resized` - used to control image upload sizes<br>
`django-richtextfield` - used to give users the ability to format their profile bio<br>
`django-tables2` - used to easily customize the table used for user library<br>

<br>

# Deployment

The project was deployed using Heroku. The steps to deploy are as follows:

### Heroku Deployment - Project Creation and Settings<br>
1. Sign up or Log in to [Heroku](https://heroku.com/)
2. Once in your dashboard, select "New" and then "Create New App"
3. Give your project a name (must be unique), select your region and confirm "create app"<br>

You'll now be taken to the Heroku Deployment Tab. In order to use the Code Institute mock terminal template for your deployed project, you'll need to do the following:

4. Navigate to the "Settings" tab
5. Click "Reveal Config Vars" to add any and all hidden variables and passwords (that most likely reside in your `env.py` or similar)

### Heroku Deployment - Deploying a Github Repository<br>
1. Navigate to the "Deployment" tab
2. Select "GitHub - Connect" under Deployment method and follow the steps necessary to connect your GitHub account
3. Select your GitHub account from the droplist, enter your repository name and click search
4. Choose "Connect" at the correct repository to connect the repo to your Heroku app
5. Further down on the Deployment page, you'll find "Automatic deploys" and "Manual deploy"
    * For automatic, choose the branch you wish to deploy and click "Enable Automatic Deploys".<br> This allows Heroku to automatically rebuild your app when your Github repository is updated
    * For manual, choose the branch you wish to deploy and click "Deploy Branch"
6. Once Heroku is finished with the build process you will be notified with a "Your App Was Successfully Deployed" message and a link to the app

### Forking the GitHub Repository<br>

If you wish to make a copy of the repository to your own GitHub account, you can do so by "Forking" it.<br>
This will give you a full working copy of the project, but ensures that no changes you make affect the original repository.
1. Navigate to the GitHub repository while logged into your account
2. In your top right, click the Fork button
3. Chose the name you want to give your version of the repository *(automatically filled in as the original project name)*
4. Click the green "Create fork" button

### Cloning the GitHub Repository<br>

If you wish to download a local version of the repository to be worked on, you can do that too. That is referred to as "Cloning".<br>
The steps to cloning the repository are as follows:
1. Navigate to the GitHub repository while logged into your account
2. Click the <>Code dropdown button
3. Make sure that HTTPS is chosen, then copy the repository link to the clipboard<br>
*Git must be installed for the next steps to work*<br>
4. Open the IDE you're working in
5. Type "git clone (the url link you just copied)" into the terminal

The project will now be on your local machine to use or save. This can be a good way to back up versions of your own work too.

> Note: In order to install all the required support libraries, you will need to run the command `pip install -r requirements.txt`
This should be done _after_ setting up a virtual environment on your machine. You can find how to do that [here](https://code.visualstudio.com/docs/python/environments) for Python in VSCode or by googling for tutorials on your specific Code Editor.

<br>


# Testing

## Manual Feature Testing

| Test Object           | Action                                  | Expected Outcome                                                                                                                 | Result |
| --------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------ |
| User Registration     | Enter incorrect form data               | No account to be created, user warning about incorrect data                                                                      | PASS   |
| User Registration     | Enter correct form data                 | Account successfully created, user redirected to profile setup                                                                   | PASS   |
| User Login            | Enter incorrect form data               | No login, warn user about incorrect details                                                                                      | PASS   |
| User Login            | Enter correct form data                 | Login and redirect user to User Profile                                                                                          | PASS   |
| User Logout           | Click Logout button                     | Redirected to "Are you sure you wish to log out?" page                                                                           | PASS   |
| User Logout           | Logout Confirmation Clicked             | Redirected to index                                                                                                              | PASS   |
| User Library          | All Books Table                         | User can see all their books in a table (pagination on 20+)                                                                      | PASS   |
| User Library          | Search function                         | User can search titles, authors and series (whole and partial) and get the limited search result back                            | PASS   |
| User Library          | Reset Search function                   | If user library is in limited view (due to search), the search button is turned into a Reset button to remove the search filters | PASS   |
| User Library          | Sort by any table column                | User can sort (alphabetically) per each column in the table                                                                      | PASS   |
| User Library          | Reset Sorting                           | User can reset the sorting to original by clicking Reset sort in the bottom right of the table                                   | PASS   |
| User Library          | Pagination                              | User can see pagination if they have above 20 books and pagination works as intended                                             | PASS   |
| User Library          | Add Book Button                         | Button takes user to the Add Book Form                                                                                           | PASS   |
| User Library          | Add Book Form                           | User can fill in all relevant book details to add a book to their library                                                        | PASS   |
| User Library          | Quick Add Button                        | Button takes user to the Quick Add Form                                                                                          | PASS   |
| User Library          | Quick Add Form                          | User can fill in the important book details to quickly add a book to their library                                               | PASS   |
| User Library          | Book Details Page                       | Book Details for the selected book are shown properly                                                                            | PASS   |
| User Library          | Edit Book Button                        | Button takes user to a pre-populated "Add Book Form"                                                                             | PASS   |
| User Library          | Edit Book Form                          | Form is pre-populated with existing details and if user changes any details, the book details are updated accordingly            | PASS   |
| User Library          | Delete Book Button                      | Button takes user to a warning/confirmation page                                                                                 | PASS   |
| User Library          | Delete Book Confirmed                   | If user confirms deletion, the book is removed from user library                                                                 | PASS   |
| User Library          | Back Button                             | Button takes user back to library view                                                                                           | PASS   |
| User Profile (own)    | View Profile when profile exists        | User Profile is shown                                                                                                            | PASS   |
| User Profile (own)    | View Profile when profile doesn't exist | User is prompted to setup Profile                                                                                                | PASS   |
| User Profile (own)    | Edit Profile Button                     | Visible in the bottom right corner and opens Edit Profile Form                                                                   | PASS   |
| User Profile (own)    | Edit Profile Form                       | Form to edit profile information, upload avatar and setup User Wishlist                                                          | PASS   |
| Profile Privacy       | Edit Profile Form Option                | In the top of the edit profile form, the user can choose to set their profile (and subsequent subpages) to private               | PASS   |
| User Search           | Search for other users                  | User can search for other users by username, either whole or partial. Results are shown on the same page                         | PASS   |
| User Search           | Search Results                          | User Search Results are shown as the full username as a clickable link to their profile                                          | PASS   |
| User Profile (others) | View Public Profile                     | User Profile is shown with extra information and link to library                                                                 | PASS   |
| User Profile (others) | View Private Profile                    | Redirected to a "This profile is private" page                                                                                   | PASS   |
| User Library (others) | View Public Library                     | Library View just as ones personal library without the add/quick add buttons                                                     | PASS   |
| User Library (others) | Book Details Page                       | Book Details page just as ones personal books without the edit/delete buttons                                                    | PASS   |

## Lighthouse validation

 The site has been run through the Lighthouse tester in Google Chrome DevTools and received very varied scores and as such, I have included both the top and bottom marks to show that I am indeed aware of the issues.

![Lighthouse](/static/docs/test-lighthouse.png)
![Lighthouse](/static/docs/test-lighthouse-low.png)


<br>

## Python Code Validation
I purposefully did not test every single file, as django creates many that I've not touched, or at least done very little to.

However, below, you'll see the results from the CI Python Linter for the files that I have written in their entirety. I made the judgement that the code would not be easier to read by making more row breaks, and as such, I have left the long lines as they were.

![Python Code Validation](/static/docs/test-pylint.png)

## HTML Validation

All pages passed HTML Validation without issues, aside from where text is created from models, especially using RichTextFields (User Bio and Wishlist for example).
<br>

## CSS Validation

The project includes very little custom CSS, as it is mainly built with Bootstrap 5.
These are the validator results for the snippets of custom CSS used.

![W3C CSS Validation](/static/docs/test-w3c-css.png)

## Responsiveness
This site is built using Bootstrap 5 and its native responsivity classes. However, due to the nature of this project, it is never the less best used on a bigger screen, or at least horizontal screen, whether mobile, tablet or desktop. 

Future versions of the project will include an even more limited table view for the user library on mobile versions to improve mobile usability.

The site is tested on numerous screen sizes using developer tools in google chrome, as well as iPhone 12, iPad 2019, MacBook Air M1 and a Windows Desktop.
<br>

# Credits
- [Original Library Project](https://biblioteket.lovene.se/library.php?val=1) by Stefan Larsson (Larssonline) that was the inspiration to this project 
- [Daisy Mc Girr's YouTube series](https://www.youtube.com/@IonaFrisbee/) on Django
- Python Django - The Practical Guide (Udemy Course) by Maximilian Schwarzmüller
- Bootstrap 5 From Scratch (Udemy Course) by Brad Traversy