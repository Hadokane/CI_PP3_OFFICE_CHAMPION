# **OFFICE CHAMPION**

*FIGHT YOUR FRIENDS - CRUSH YOUR COLLEAGUES - BECOME THE OFFICE CHAMPION!*

---

![UI](officechampion/static/assets/images/docs/herolgt.png)

The last update to this file was: **07 March 2023**

---

**Developer Links:**

*(Right-click to open in a new tab/window)*

[Developer - HK_Dev](https://github.com/Hadokane "Hadokane - Github")

[Commit Log](https://github.com/Hadokane/CI_PP3_OFFICE_CHAMPION/commits/main)

**Live Website Link:**

[Live Website - Heroku](https://officechampion.herokuapp.com/ "Office Champion")

**Repository Pages:**

[All HTML Pages - Templates](https://github.com/Hadokane/CI_PP3_OFFICE_CHAMPION/blob/b9e1855fe978f3ab382c4b423dad2887c409c35b/officechampion/templates)

[Repository page - style.css](https://github.com/Hadokane/CI_PP3_OFFICE_CHAMPION/blob/b9e1855fe978f3ab382c4b423dad2887c409c35b/officechampion/static/css/style.css)

[Repository page - scripts.js](https://github.com/Hadokane/CI_PP3_OFFICE_CHAMPION/blob/b9e1855fe978f3ab382c4b423dad2887c409c35b/officechampion/static/js/script.js)

[Repository page - models.py](https://github.com/Hadokane/CI_PP3_OFFICE_CHAMPION/blob/b9e1855fe978f3ab382c4b423dad2887c409c35b/officechampion/models.py)

[Repository page - routes.py](https://github.com/Hadokane/CI_PP3_OFFICE_CHAMPION/blob/b9e1855fe978f3ab382c4b423dad2887c409c35b/officechampion/routes.py)

**Additional Documents**

[Testing Document - Automatic, Manual & User](https://github.com/Hadokane/CI_PP3_OFFICE_CHAMPION/blob/b9e1855fe978f3ab382c4b423dad2887c409c35b/TESTING.md)

**PROVIDED TEST ACCOUNT**

[Provided Test Account](#provided-test-account) - Sign in using these provided details and view an example of an active user profile.

*(Provided for review/examination purposes)*

---

# Academic Project Aims

I am currently pursuing my **Diploma in Web App Development** from [Code Institute](https://codeinstitute.net/ "Code Institute").

The academic aim of this project is to demonstrate my newly developed skills and knowledge of Python by developing a full-stack website with a backend capable of providing full C.R.U.D. functionality to its user.

As the site owner, I will achieve this goal by providing a database project that "gamifies" the concept of "Employee of the Month," allowing users to straightforwardly Create, Read, Update and Delete their data in a manner that directly meets user expectations.

I intend to display the above throughout the project via my: coding, comments, commits, and the explanation provided by this README and its accompanying TESTING document.

Additional functionality has been provided by the framework [Materialize 1.0.0](https://materializecss.com/) for CSS styling & [Flask](https://flask.palletsprojects.com/en/2.2.x/) for its templating functionality while utilising [Jinja](https://jinja.palletsprojects.com/en/3.0.x/).

Great care has been taken, to ensure that the website is designed to meet best practice standards, and is responsive on all screen resolutions.

The website has been tested on a variety of devices and screen resolutions: from mobiles; to tablets; and 4k monitors. It also has proven compatibility with all popular web browsers.

---

# Table of Contents

1. [User Experience (UX)](#user-experience---ux)
    - [Strategy Plane](#strategy-plane)
    - [Scope Plane](#scope-plane)
        - [Features Required](#features-required)
        - [Road Map](#road-map)
    - [Structure Plane](#structure-plane)
    - [Skeleton Plane](#skeleton-plane)
        - [Wireframes](#wireframes)
        - [Database Schema](#database-schema)
    - [Surface Plane](#surface-plane)
1. [Testing](#testing)
    - [Provided Test Account](#provided-test-account)
1. [Deployment](#deployment)
    - [Creating The Gitpod-Workspace](#creating-the-gitpod-workspace)
    - [Forking The Github Repository](#forking-the-github-repository)
    - [Deploying With Heroku](#deploying-with-heroku)
    - [Deploying With ElephantSQL](#deploying-with-elephantsql)
    - [Gitpod CLI Inputs](#gitpod-cli-terminal-inputs)
    - [PostgreSQL Inputs](#postgresql-inputs)
1. [Credits](#credits)
    - [Languages Used](#languages-used)
    - [Frameworks Libraries & Programs Used](#frameworks-libraries-and-programs-used)
    - [Validators Used](#validators-used)
    - [Technologies Used](#technologies-used)
    - [Imagery Used](#imagery-used)
    - [Acknowledgements](#acknowledgements)

---

# User Experience - UX

As with my previous projects I have chosen to arrange my UX analysis following the framework of Jesse James Garrett's philosophy of the "5 Planes," as discussed in his book [The Elements of User Experience](https://www.amazon.co.uk/Elements-User-Experience-User-Centered-Design/dp/0321683684/ref=asc_df_0321683684/?tag=googshopuk-21&linkCode=df0&hvadid=311000051962&hvpos=&hvnetw=g&hvrand=10376246921916888236&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007448&hvtargid=pla-432330338546&psc=1&th=1&psc=1).

I decided to utilise this methodology to establish a clear and achievable list of goals for my project to follow. 

These goals will be divided between meeting the needs of the user - both first-time and returning - along with meeting the needs of the site owner.

I will maintain a clear, justified development path, and establish a defined priority of tasks and elements for integration. Ensuring the project avoids "feature creep," at this early development stage and maintains a clear initial scope.

---

# Strategy Plane

In this section, I will define clear goals that will be represented by a list of both user and website owner stories. These will serve as a definitive reference point for defining the necessary features and functions of the website.

In a later section, I will revisit these stories and see if/how the project has addressed each goal, justifying my explanations with imagery and proof cases.

Each subheading below provides these initial goal lists, with added explanations on where/how I expect to meet these goals throughout the development of the project.

---
## User Stories:

### **As a First-Time user, I want to:**
---

1. Be able to sign up for an account.
    
    1. Does it prompt me if my username is already taken?
    
    2. Does it let me know if my password is okay?
        
        - Do both password boxes match?
        
        - Is there a character limit?
    
    3. Can I press the submit button with empty input boxes?

2. Have confirmation I've signed in to the website.
    
    1. Welcome in the top-left of the nav bar. (Positive visual user feedback.)
    
    2. Navbar icons change - "Sign up" and "Login" are replaced with the website's pages.

3. Easily understand what each webpage does.
    
    1. Clearly named website pages in the navbar.
    
    2. Provide clear explanations throughout the website where action is required.

4. Be able to view the website on any device.

    1. Does it display correctly on different screen sizes?

---
### **As a Returning user, I want to:**
---

5. Be able to log in to my account.
  
    1. Are my username & password recognised?

    2. Are there alerts when I enter incorrect data?

    3. Is there feedback when I've successfully signed in?

6. Be able to Create, Read, Update & Delete my data.

    1. Can I create new objects in each section of the website?

    2. Are there "Edit" & "Delete" options present for my created data?

    3. Can I see the data I've created easily?

7. Be able to access and use the website on any device.

    1. If I create my account on a computer will it work on my phone?

    2. Is my created data still present?

8. See my created league displayed on one page and share it with friends.

---
### **As a site owner, I want to:**
---

9. Ensure the user can interact with all elements to reach a logical and desired result.

    1. Manual testing of the site's features will be crucial to achieving this goal. If all user goals are met, then this goal will also be met.

10. Ensure the app and its elements display correctly on any device.

    1. Check the website on multiple devices and screen sizes.

    2. Can all elements be interacted with by mouse and touch devices?

11. Have admin privileges on the website. Ensuring I can edit/delete user data.

12. Gamify the "employee of the month" concept to encourage users to compete and be more motivated.

13. Provide a multi-use case platform for the user. 

    1. The website can be used for numerous groups - such as the office, sports teams, gaming groups, etc. - with its current core features.


---

## Grid of Opportunities:

With the above goals in mind, I have assembled the following "grid of opportunities" to showcase the prioritised features heading into the next stage of development.

| Opportunity                        | IMPORTANCE | VIABILITY |
|------------------------------------|------------|-----------|
| All website elements function correctly    | 5          | 5         |
| Sign up & Login functions work correctly on any device     | 5          | 5         |
| The user has full C.R.U.D. functionality     | 5          | 5         |
| Provide an overview page for the users League | 5          | 4        |
| Provide positive feedback to all user action | 4          | 4        |
| Provide admin functionality to the site owner         | 3          | 3         |

[Back to top ↑](#office-champion)

---

# Scope Plane 

In the above Strategy Plane section, I laid out the website's goals, developed user stories & addressed ways in which the project could meet those defined stories.

To set a clear scope for development and avoid any "feature creep", I will further elaborate on the required features for this website in this section, in doing so we will maintain an agile approach.

---

## Features Required:


The following are written concerning the above user/site-owner stories and directly reference how they can solve the stated goals.

1. A Users table within the Database to store each user's login information & a relevant table for each C.R.U.D. section the user can interact with.
    
    - Allows the user to sign up, log in and have their created data stored, ready for when they log in.

    - Will be accessible from any device.

2. Create a positive user experience by including visual, colour-coded "Alerts" (Python "Flash Messages") that: 
    
    - Notify the user of any issues with their sign-up/login efforts.
    
    - Provide the user with feedback upon carrying out any C.R.U.D. functions or when signing into the website successfully.
    
    - Provides positive feedback to the player upon completion of the game.

3. Individual named pages for each area the user can interact with.

    - Required pages (All require C.R.U.D. functionality): Leagues, Titles, Members & Notes.

    - Sign Up & Login only displayed to non-signed-in users.

4. Ensure only the correct user has CRUD functionality over their created data.

5. Ensure the main League page is sharable and viewable by non-signed-in users.

[Back to top ↑](#office-champion)

---

## Road Map

By establishing our current goals in the above section, I am now able to create a Road-Map for future updates that will improve the overall user experience of the website. 

These have been deemed non-essential for an initial "proof-of-concept" build and would simply serve to enhance the core website that is being prioritised.

---
### Future goals:
---

In a theoretical "next update", I would aim to add additional functionality to the website as I feel the core user experience is developed and functioning as intended.

**To improve the experience for the user, the following could be implemented:**

1. Add a "Make Unique" feature to force a title to only have one holder at a time. 
    - Alternatively make titles "unique" as the default setting and add a "Many Holders" option to allow a title to have more than one holder. 
    - This wasn't a pressing feature to include in an initial launch version of the website and users are currently capable of managing their settings, making titles unique or held by many as they choose.

2. Migrate the website's CSS from Materialize to Bootstrap to allow for more consistent card implementation & avoid the known issues with cards & the input form function not alerting users when left blank.

3. Allow multiple user accounts to edit the same leagues and have access to certain features allowed by that league's admin.

4. Add a feature to track title reigns, so users can see the history of each title including dates when new champions were crowned.

**To improve the experience for the site owner, the following could be implemented:**

1. Implement sponsored/ad placement on the website to generate revenue for the site owner.
    - would make thematic sense to establish a partnership/affiliation with a belt/title maker, trophy-making company or similar. 
    - Partnering with a print company could allow users to purchase related certificates.


[Back to top ↑](#office-champion)

---

# Structure Plane:


Here we will discuss the priority of necessary features required to correctly utilise this website.

---

## Feature Priority

### Base Template
---

Utilising the Jinja templating language and features of Flask, a `base` template page will be created containing the following important features, that will be displayed on all pages throughout the website:

- A minimal navigation menu with logged-in pages hidden from new users, providing access to only the `sign up` and `login` pages.
    
    - Logged-in users will have access to the `Leagues, Titles, Members & Notes` pages, along with a `log out button`.

    - It will be responsive and collapse on smaller devices into a "burger icon" menu.

    - Contain a greeting to logged-in users. Providing positive feedback and a reminder that they are indeed signed in.

- A clean footer containing a link to the website developer's GitHub & a copyright disclaimer.

- The ability to display Alerts (Flash Messages) to the user directly under the header. So that user expectations on their placement are met and maintained no matter what page they're on.

---
### Home Page
---

The first thing the user should be greeted by is an appealing `Home Page/Index` containing the following:

- A clutter-free minimal design.

- A large hero image of the website's logo.

- A row of promo cards, explaining how to use the website in a fun, provocative manner, that is culturally appropriate for the website's intended purpose - gamifying the "Employee of the Month" experience.

- A button to send new users to the "Sign Up" page

---
### Sign Up & Login Pages
---

Next, the user will be introduced to the `Sign Up` page, where they are presented with a form allowing them to create an account.

The form will do the following:

- Provide a `username text input` to let users enter their chosen `username`.

- Provide a `password text input` to let users enter their chosen `password`.

    - This will be stored in the database as hashed data for security reasons, using the `method="sha256"` meaning the admin cannot see this information, keeping the user's password hidden and secure. 

- Provide a `password confirmation input` to ensure users have entered the correct password and improve their experience by providing user assurance and further chances for alerts and feedback.

- Alert the user via "Flash Messages" if there are any issues during sign-up:
    - Username in use.
    - Passwords do not match.
    - Input is too short.
    - Field left blank.

- Alert the user positively on sign-up success & log them in.

This page will be replaced by the `Login Page` once a user has successfully signed into the website. This will include all of the above sections and features except a `password confirmation input` and its related Alerts as that isn't necessary for a returning user.

---
### Feature pages - *League, Titles, Members & Notes*
---

Once signed in the user will have access to the website's main feature pages.
These will all follow a similar theme and as such include similar functions and features, with a focus on providing the user with C.R.U.D. functionality through its layout and options:

- Section headers to instruct the user on whether they are **Adding a new element** or **Viewing their created elements**.

- Large colour-coded buttons to allow the user to access form pages to **Create a new element** or **Edit an existing element**.

- A Large Red button to open a **Delete specific element modal** with confirmation and cancel buttons for the user.

- Element-specific cards to allow the user to **View their created element** and its information.

---
### Open League Page
---

This will be the final page the user views. Each created league will feature a large button, allowing the user to open the `Open League` page. Within this page a user can:

- View their league name, relevant titles, notes and members.

- Members with a championship will be displayed at the top of the league.

- Other members will be displayed underneath.

- Notes will be displayed at the bottom.

- This will be a view-only page that users are encouraged to share with their friends.

- No edit/delete buttons will be present to prevent clutter, along with new users clicking them and being redirected to sign-up pages unnecessarily.

- Allows non-members to see the leagues they're involved in and compete to be "Champion of the Office!" - successfully gamifying the "Employee of the month" experience, while keeping user steps to a minimum. Allowing only one user in a group to create an account and be in charge of managing their groups.

---

## The interaction design (IXD)

**Buttons**

1. Will be colour-coded to match user expectations.
    
    - Green for the "Edit, Sign up or Submit" buttons. Green is seen as a positive colour and is a standard colour across the internet when submitting a form or editing data.

    - Red for "Delete" buttons. Following the same idea, Red is seen as a negative colour often associated with deleting an item or cancelling an event. 

    - Orange for the bold "Open League" buttons. This is to differentiate it from other buttons on the website and help the user distinguish it from the surrounding "Edit" & "Delete" buttons. This will open the main League page which will be the summary of the user's work, so making it unique feels important in providing a good user experience.

2. Will use "Materialize's" built-in `waves-effect waves-light` classes, to provide positive feedback to user interaction.

**Promo Cards**

1. Simple grey background with blue text. Help it stand out from the rest of the website and draw user attention.

2. Slight drop shadow on mouse hover, to show the user is focused on the card.

**Feature Cards**

1. Display the relevant user information based on a section of the website - i.e. Member displays `Name: | Role: | Title (if title holder):`

2. Dark Blue background, bold white text. Draw the user's eye and contrast the websites Amber coloured theme. Stylised to include lighter Blue strips to separate information and improve readability for users.

3. Same drop shadow as above.

**Alerts**

1. Will be colour-coded to set user expectations.
    
    - Blue will be used for successes and to provide information. It is a positive colour used to display information and matches the website's blue/orange design.

    - Red will be used to draw the user's attention. Providing a warning that there is an issue with their intended task.

2. `onClick` these elements will (as necessary):
    - Removes the alert from the screen.


**Overall this website will:**

- Be consistent in design, branding and colours used.

- Provide constant visual feedback to user actions - positive and negative.

- Allow the user to create an account and sign in/log out with ease.

- Allow the user to Create/Read/Update/Delete their created data.

- Allow the user to curate a competitive "Employee of the Month" style experience for their friend/work group.

- Be readable on all devices.

- Utilise a Relational Database Management System to store and retrieve user data.

[Back to top ↑](#office-champion)

---

# Skeleton Plane


This website will be created entirely with HTML, CSS, Javascript & Python languages.

The website will dynamically present the user's created data and elements for them to Create, Read, Edit & Delete as they see fit.

This created user data will all be housed within the [PostgreSQL](https://www.postgresql.org/) `Relational Database System`, which will be used to store the created user data in organised tables. Utilising one-to-many relationships and Foreign Keys, these tables will communicate with each other and as such we will be able to associate relevant data with the user who created it.

[SQLAlchemy](https://docs.sqlalchemy.org/en/20/) allows me to use Python as a language to populate and manage my Relational Databases.

This will then be hosted externally using [ElephantSQL](ElephantSQL.com) so that it can be accessed by [Heroku](https://dashboard.heroku.com/apps), our hosting platform of choice for this project.

---
## PostgreSQL Database

The following tables were created using SQLAlchemy and the GitHub CLI Terminal to create and read the necessary tables for this project.

 Schema |  Name  | Type  | Owner  
--------|--------|-------|--------
 public | league | table | gitpod
 public | member | table | gitpod
 public | note   | table | gitpod
 public | title  | table | gitpod
 public | user   | table | gitpod


To provide user value:

- The website will be kept clean and clutter-free, providing provocative and descriptive text that makes the user want to engage.

- Navigation links & buttons will have easy-to-understand titles and will take the user to logical destinations.

- The user will be able to Create, Read, Update & Delete objects with ease, through a simple button and form interactions.

- Forms will be labelled correctly and provide examples and icons where necessary to improve the user experience.

- Helpful Flash Message Alerts will provide positive/negative feedback where necessary.

- The Open League page will be sharable with non-signed-in users so that players can motivate each other to compete for viewable titles, gamifying the "Employee of the Month" experience as stated.

---

## Wireframes

Included below are the project's wireframes, created with [Draw io](https://www.draw.io).

The purpose of these wireframes is to demonstrate the positions of features and elements that will make up the pages of this website. 

Providing a simplified demonstration of the project's architecture and design choices.

Included below are wireframe examples of the website in two different states:

- when a user is **new** or **signed out**.
    -<details><summary>Wireframe #1 - New User/Signed Out</summary><img src="officechampion/static/assets/images/docs/wireframe1.jpg" alt="Wireframe 1 - Signed Out"></details>


- when a user is **returning** or **signed in**.
    -<details><summary>Wireframe #2 - Returning User/Signed In</summary><img src="officechampion/static/assets/images/docs/wireframe1.jpg" alt="Wireframe 2 - Signed In"></details>

---

## Database Schema

Also created was a database schema, providing a visual example of the necessary table and key pairs needed for this project and showing how they link together via `Foreign Keys`.

This was used to construct the above PostgreSQL Database.

<details><summary>Database Schema - Tables & Key pairs</summary><img src="officechampion/static/assets/images/docs/schema.jpg" alt="Database Schema Image"></details>

The "General Layout" shown at the bottom of the diagram gives an overview of the "Open League" pages functionality and how that would make use of the Foreign Key pairings to display the correct *Titles, Members & Notes* for each independent user *League*.

[Back to top ↑](#office-champion)

---

# Surface Plane

In this final UX section, I will describe how the website creates a positive experience for users through its use of hover effects, predictable navigation, descriptive alerts, clear content and overall design choices and philosophies.

---

## Design Philosophies


### Responsive Design

---

Responsive design is an important factor in the creation of any website or application.

As a developer, I am fully aware this will be viewed on several different browsers, screen sizes and devices. Manual testing will also be implemented to ensure elements display as expected. 

Materialize containers and custom CSS was utilised to ensure all images and text would fit their containers and be readable across all devices. This is to ensure a consistent user experience for both mobile and desktop.

Changes implemented between the mobile and desktop experience of this website are as follows:

- Differing rows of cards depending on screen size.

    <details><summary>Cards #1</summary><img src="officechampion/static/assets/images/docs/surface/cards1.png" alt="Cards Example Image 1"></details>
    -<details><summary>Cards #2</summary><img src="officechampion/static/assets/images/docs/surface/cards2.png" alt="Cards Example Image 2"></details>
    -<details><summary>Cards #3</summary><img src="officechampion/static/assets/images/docs/surface/cards3.png" alt="Cards Example Image 3"></details>
    -<details><summary>Cards #4</summary><img src="officechampion/static/assets/images/docs/surface/cards4.png" alt="Cards Example Image 4"></details>
    -<details><summary>Cards #5</summary><img src="officechampion/static/assets/images/docs/surface/cards5.png" alt="Cards Example Image 5"></details>
    -

- The main navigation bar collapses into a "burger menu" side navbar on smaller devices to ensure all page links are accessible to the user.
    
    <details><summary>Large Screen Navigation Bar</summary><img src="officechampion/static/assets/images/docs/surface/nav.png" alt="Large Screen Navigation Bar"></details>
    -<details><summary>Side Navigation Bar - Closed</summary><img src="officechampion/static/assets/images/docs/surface/sidenav1.png" alt="Side Navigation Bar - Closed"></details>
    -<details><summary>Side Navigation Bar - Open</summary><img src="officechampion/static/assets/images/docs/surface/sidenav2.png" alt="Side Navigation Bar - Open"></details>
    -

- A side navbar is visible on the "Open League" screen on larger screen sizes only. This allows the user to skip to a specific section as an added method of navigation through larger leagues.
    
    <details><summary>Open League Navigation Bar</summary><img src="officechampion/static/assets/images/docs/surface/league_sidenav.png" alt="Open League Navigation Bar"></details>

---
### IXD - Interaction Design
---

During the Skeleton Plane, I explained how the user experience would be improved by the interaction design of certain elements.

I have included images below to provide visual examples of each point and to serve as confirmation that these decisions have been implemented into the final design:

**Buttons**

<details><summary>Colour-coded for user expectations</summary><img src="officechampion/static/assets/images/docs/surface/btn_colour.png" alt="Colour-coded Buttons"></details>
-
<details><summary>Materialize's waves-effect provides positive feedback on interaction</summary><img src="officechampion/static/assets/images/docs/surface/btn_wave.png" alt="Wave Effect Buttons"></details>
-

**Cards**

<details><summary>Promo card design</summary><img src="officechampion/static/assets/images/docs/surface/card_promo.png" alt="Promo card design"></details>
-
<details><summary>Feature card design</summary><img src="officechampion/static/assets/images/docs/surface/card_feature.png" alt="Feature card design"></details>
-
<details><summary>Card Hover - Subtle drop shadow</summary><img src="officechampion/static/assets/images/docs/surface/card_hover.png" alt="Card Hover"></details>
-

**Alerts**

<details><summary>Blue Confirmation Alert</summary><img src="officechampion/static/assets/images/docs/surface/alert1.png" alt="Blue Confirmation Alert"></details>
-
<details><summary>Red Warning Alert</summary><img src="officechampion/static/assets/images/docs/surface/alert_signup2.png" alt="Red Warning Alert"></details>
-

The Alerts also have a Javascript `onClick` event to remove them from the DOM when a user interacts. This allows a user to close a Flash Message Alert at their convenience. A small "X" icon is present on the right-hand side of these Alerts to notify the user that they are closable.

**Defensive Design**

The delete button required a failsafe to prevent the user from accidentally clicking it and removing their data. Improving the user's experience is accomplished by providing an additional check to confirm their delete action.

On-click a modal will open containing two buttons which either:
- Confirm the Delete action and reload the page.
- Cancel the Delete action and remain on the page.

<details><summary>Delete Modal</summary><img src="officechampion/static/assets/images/docs/surface/dlt_modal.png" alt="Delete Modal"></details>
-

**Visual Separation**

Visual separation is achieved across the website through the use of Materialize `Row and Columns`. 

The website follows a traditionally ordered hierarchy. 

At the top, there is a `Sticky Header` which will maintain its position responsively across all device screen sizes. This contains a responsive navbar that shows the user relevant pages based on their login state.

Alerts display underneath this when called and are closable.

The page content is then displayed here. Generally consisting of buttons to load forms or take C.R.U.D.-related actions, or a series of viewable cards relating to the current feature page and information saved to the database by the user.

At the bottom is a simple `Footer` with a link to the developer's page and a copyright disclaimer.

This simple layout allows a user to intuitively navigate the pages with no learning curve, as it will be an experience ingrained into the muscle memory already by other websites that utilise these same standard conventions.

---

## Colour Palette

The following colour palette was utilised throughout the website.

<details><summary>Colour Palette</summary><img src="officechampion/static/assets/images/docs/surface/colours.png" alt="Colour Palette"></details>

It was adapted from Materialize's readily available colour classes and implemented mainly through inline HTML code using pre-defined classes. [Materialize Palettes](https://materializecss.com/color.html).

Orange & Blue were selected as the defining brand colours for this project.

Orange is an eye-catching colour, conveying feelings of energy and emotion. I see this as a representation of the gamified experience on offer here, the concept of motivating friends or colleagues to compete for a title or award feels summarised by this. Also, a golden-toned shade was used (amber) as gold is the colour of trophies and money - often being linked with feelings of success.

Blue alternatively is a contrasting colour to orange, ensuring they both visually complement each other and draw attention from the user. Blue is often considered a professional, safe colour which also provides a strong representation of the office setting and traditional environment of that culture.

---

## Image Choices


The website relies upon the user providing their HTML links to populate the imagery for members and titles. This is to allow users to have a personalised experience. Our database then only has to store the link as a simple `string` and it can be recalled and shown as long as its origin remains intact.

I created the website's logo using [Adobe Illustrator](https://www.adobe.com/). It was inspired by the design of Pro Wrestling & Boxing title belts and was used as a homage to these sports that provide tangible title belts and rewards to their participants. This imagery is intentionally used to convey the idea of a more tangible reward to the user. It used a pixel-styled font in its centre to show the user that this can be perceived as a "game", encouraging them to gamify their "employee of the month" or "fantasy league" experiences with Office Champion.

<details><summary>Website Logo</summary><img src="officechampion/static/assets/images/oc_logo.png" alt="Colour Palette"></details>

---

## Font / Typography

I utilised Google Fonts to acquire [Golos Text](https://fonts.google.com/specimen/Golos+Text?query=golos) which was used for the entirety of the website.

Heavier font weights were used to emphasize headers and standard font weights were used for the body text of documents and cards to ensure easy readability for the user.

Golos is a versatile closed sans-serif often used on state and social service websites and as such was created by Alexandra Korolkova and Vitaly Kuzmin for continuous on-screen reading.

I found its bold nature and easy readability to be a perfect match for Office Champion.

---

## Dependencies

Web pages are loaded "Top-Bottom" from HTML files.

With this in mind, I kept smaller CSS dependencies such as "Materialize CSS Framework", "Google Icons" & my own custom CSS in the head of the pages and larger Javascript dependencies like "Materialize JS Framework", "FontAwesome Icons" & my own custom JavaScript in the bottom of the body.

This structure should ensure that the page is loaded quickly and that the user doesn't see an unstyled page or wait for the initial elements to load. 

---

# Testing

**[--> Please refer to the separate Testing document located here <--](TESTING.md)**

**Clicking the above link will open "TESTING.MD"*

**This document contains information on the following:**
- Website Validation 
- Manual & Automated Testing of code & features 
- Device Testing
- Testing established user stories
- Confirmation of user stories & site goals
- Bug Reports

---

## Provided Test Account

The following account is pre-loaded with examples of different use cases for the Office Champion website.

Examiners are welcome to log in using the following information and be greeted by an example of an active user account, with multiple leagues, titles and members.

**TEST ACCOUNT LOGIN INFORMATION**

```
Username = Tester

Password = 12341234
```

*Alternatively feel free to make your account and populate it as you see fit. I'm confident the website will meet your expectations and provide a user-friendly experience.*

[Back to top ↑](#office-champion)

---

# Deployment


## Creating the Gitpod Workspace

The project uses the Code Institute Gitpod Template as its foundation. 

This can be accessed by doing the following:

1. Log in to GitHub 
2. Head to the [Code Institute student template](https://github.com/Code-Institute-Org/gitpod-full-template)
2. Click 'Use this Template' next to the Green Gitpod button.
3. Click the "Use this template" button.
4. In the dropdown menu select "Create a new repository".
5. You will be presented with the example screen below.
6. Enter your details & press "Create repository from template"

<details><summary>Example Screen</summary><img src="officechampion/static/assets/images/docs/github1.png" alt="GitHub Example Screen"></details>

---

## Forking the GitHub Repository

If you would like to fork this GitHub Repository - make a copy of the original on your GitHub account - for viewing or making changes do the following:

1. Log in to GitHub
2. Head to the [Office Champion GitHub Repository](https://github.com/Hadokane/CI_PP3_OFFICE_CHAMPION)
3. Select the "Fork" tab on the right-hand side of the navigation menu.
4. Choose a destination to save your newly forked repository.

<details><summary>Example Screen</summary><img src="officechampion/static/assets/images/docs/github2.png" alt="GitHub Example Screen"></details>

For further information on making a local clone of this project, I recommend reading the GitHub Docs guide on forking located [here.](https://docs.github.com/en/github-ae@latest/get-started/quickstart/fork-a-repo)

---

## Deploying with Heroku

The application was then deployed with Heroku using the following steps:

1. Create an account/Log in to [Heroku](https://dashboard.heroku.com/apps).
2. On the main page select the "New" button and chose "Create new app".
3. Enter a unique name for your project (with no spaces or capitalisation) and select your region (Europe in my case). 
4. Select 'Create App'.
5. Install Heroku into the project by entering ```npm install -g heroku``` into the terminal.
6. Enter ```heroku login -i``` into the terminal and enter your heroku credentials. Due to two-factor authentication being active in my case, I used my Heroku API key instead of my password when connecting. This can be found on your Heroku "manage account" page.
7. Enter ```heroku apps``` in the GitHub Terminal to see a list of your created apps & confirm your created app exists.s
8. Head to the Heroku dashboard "settings" tab for your created project and find the "Heroku git URL" shown there.
9. Copy that URL and paste the following into the GitHub CLI Terminal: ```git remote add heroku your_url``` (replacing your_url with the "Heroku git URL" mentioned above.)
10. Create a "requirements.txt" file by typing ``` pip3 freeze --local > requirements.txt ``` into the Gitpod Command Line Interface Terminal & commit it to GitHub.
11. Create a "Procfile" by typing ```echo web: python run.py > Procfile```. (Ensure the document is a single line & begins with a capital "P" to avoid potential errors.)
12. Use ```git push -u heroku main``` to push the main branch of the project to heroku. (Will fail if the "Procfile" or "requirements.txt" are missing from your project.)
13. Finally enter the following into the "Config Vars" section found on the Heroku Dashboards "Setting" tab. Select the "Reveal Config Vars" button and enter the following:
- ("IP", "0.0.0.0")
- ("PORT", "5000")
- ("SECRET_KEY", "whatever_you_chose_to_enter_here") (*not the actual project secret_key that was used)
14. Press "Open app" on Heroku. 
15. Breathe a sigh of relief, the app is deployed and usable!

<details><summary>Heroku Example Screen</summary><img src="officechampion/static/assets/images/docs/heroku.png" alt="Heroku Example Screen"></details>

---

## Deploying with ElephantSQL

Due to changes in Heroku, the PostgreSQL databases created during this project need to be hosted externally.

For this I've used ElephantSQL and will detail the process of deploying the databases here:

1. Navigate to [ElephantSQL](ElephantSQL.com) and click “Get a managed database today”
2. Create an account by connecting to GitHub.
3. Once signed in click the "Create New Instance" button.
4. Name your project, select your region & "Create Instance"
5. Select your project and copy the provided URL.
6. Head to the Heroku Dashboard "Settings" Tab and add the above URL to your "Config Vars"
7. Select the "More" Button next to "Open App" and select "Run Console" in Heroku.
8. Type ```Python3``` into the console and run
9. Finally enter the following:
```from officechampion import db```
```db.create_all()```
10. A new empty database has now been created.

---

## Gitpod CLI Terminal Inputs

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

To run a backend Python file, type:

`python3 app.py`

Install necessary plugins/framework for this project:

`pip3 install 'Flask-SQLAlchemy<3' psycopg2 sqlalchemy==1.4.46`

---

## PostgreSQL Inputs

**Initialise Postgresql (psql) in the terminal:**
```
set_pg

psql
```

**View a user in psql:**
```
psql -d officechampion

TABLE "user";
```

<details><summary>PSQL - Create & connect to a Database</summary><img src="officechampion/static/assets/images/docs/validation/psql_connect.png" alt="psql create database example"></details>

**Add the table information from "models.py" to the psql "officechampion" database:**
```
from officechampion import db

db.create_all()
```

<details><summary>PSQL - Confirm the Database contains the correct information </summary><img src="officechampion/static/assets/images/docs/validation/psql_confirmdb.png" alt="psql confirm database example"></details>

[Back to top ↑](#office-champion)

---

# Credits 

## Languages Used:

- HTML 5
- CSS 3
- Javascript ES2022
- Python 3

--- 
## Frameworks Libraries and Programs Used:

- [Heroku](https://heroku.com/)
  - Heroku is used for the deployment & hosting of this project.

- [ElephantSQL](ElephantSQL.com)
  - For hosting the PostgreSQL database for Heroku to access.

- [PostgreSQL](https://www.postgresql.org/)
    - Was utilised as my Relational Database Management System of choice during the project.

- [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)
    - Used as a console language to populate and manage my Relational Databases.
    - Allows use of PostgreSQL.

- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
  - Python library used with the Jinja language to create HTML template files & run python code within HTML.

- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/api/)
  - Required for Flask functionality. The templating language used within the HTML template files.

- [Materialize 1.0.0](https://materializecss.com/)
  - Front-end library utilised for its useful CSS functionality. Used throughout the website on elements such as forms, cards, nav bars and colour palette selection.

- [Google Fonts](https://fonts.google.com/)
  - Used to import the "Golos Text" font.
  - Used to import material icons.
  
- [Font Awesome](https://fontawesome.com/)
  - Used to import additional form icons.

- [Github](https://github.com/)
  - GitHub stores my project's repository.
  - Provides a method for me to submit my project data for examination purposes.

- [Gitpod](https://gitpod.io/)
  - Gitpod served as my online IDE during the project.

- [Git](https://git-scm.com/)
  - Git is used in conjunction with the above for version control.

- [Draw io](https://www.draw.io)
  - Used to create Wireframes & Database Schema for the project during development.

- [Adobe Illustrator](https://www.adobe.com/)
  - Illustrator was used to create the website's logo image.

- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
  - Chrome's Dev Tools were essential during the development of this project.
  - They allowed me to test the responsiveness across various screen sizes during creation.
  - Provided near-endless opportunities for debugging and bug identification throughout the project's dev cycle.

- [CI TEMPLATE](https://github.com/Code-Institute-Org/gitpod-full-template)
  - This repository was initially created using Code Institute's Github template.

---
## Validators Used:

- [W3C HTML Validator](https://validator.w3.org/) - Validation of HTML.
- [W3C JigSaw Validator](https://jigsaw.w3.org/css-validator/) - Validation of CSS.
- [JSHint Validator](https://jshint.com/) - Validation of Javascript.
- [Code Institute Python Linter](https://pep8ci.herokuapp.com/) - Validation of Python (Pep 8).
- [Wave Web Accessibility Evaluation Tool](https://wave.webaim.org/) - Accessibility testing.
- [A11y Color Contrast Accessibility Validator](https://color.a11y.com/Contrast/) - Contrast testing.
- [Lighthouse & Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Performance testing.

---
## Technologies Used:

1. [Markdown Guide](https://www.markdownguide.org/cheat-sheet/) - For their "Markdown Cheat Sheet" and assistive documents on writing a README.md file.

1. [Strftime](https://strftime.org/) - "strftime python Cheat Sheet."

1. [Grammarly](https://app.grammarly.com/) - For spell-checking my Text Based Adventure Module during brainstorming.

1. [Am I Responsive](https://ui.dev/amiresponsive) - For providing the mock-up image featured at the top of this document.

1. [Favicon.io](https://favicon.io/) - For providing a favicon image for the project.

1. [Youtube: Tech With Tim](https://www.youtube.com/watch?v=dam0GPOAvVI) - For his stellar course on Flask & Python. Provided additional knowledge and explanation at a helpful pace. Responsible largely for the note and sign-up functionality of the website.

1. [Youtube: Codemy](https://www.youtube.com/@Codemycom) - Additional useful series on Flask & Python. Provided a good explanation of SQLAlchemy.

1. [Flask Login Information](https://flask-login.readthedocs.io/en/latest/#flask_login.UserMixin) - Login Management & UserMixin documentation. Explained the use cases for both.

1. [StackOverflow - Longer Git Commit Article](https://stackoverflow.com/questions/74992148/how-to-write-a-commit-description-in-source-control-vscode) - Information on adding comments to Git Commits.

1. [StackOverflow - psql Table Data Article](https://stackoverflow.com/questions/26040493/how-to-show-data-in-a-table-by-using-psql-command-line-interface) - Showed terminal commands for viewing table contents.

1. [Phoenixap - Drop Database Article](https://phoenixnap.com/kb/postgresql-drop-database#:~:text=The%20first%20method%20to%20remove,execute%20the%20DROP%20DATABASE%20command) - Provided an explanation on dropping PostgreSQL databases. After updating `methods.py` I needed these changes reflected in the database, this article explained how to do that.

1. [Hackers & Slackers - SQL Data Models Article](https://hackersandslackers.com/sqlalchemy-data-models/) - Deeper look at "One-to-Many" Database Table Relationships.

1. [SQLAlchemy Error Messages](https://docs.sqlalchemy.org/en/14/errors.html#error-9h9h) - Researching error messages within bugs 5 & 6.

1. [Github - Materialize Select Form Issue](https://github.com/Dogfalo/materialize/issues/1861) - People discussing the materialize select form issue. Select form doesn't prompt the user when no input is present.

---
## Imagery Used:

1. [WikiCommons - No Image Placeholder](https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/No-Image-Placeholder.svg/1665px-No-Image-Placeholder.svg.png) - Wikipedia Creative Commons "No Image" Thumbnail. Used as a placeholder when no image is provided to "Members" or "Titles" during creation or editing.

1. [WWE.com - for Test Group Imagery](https://wwe.com/)

1. [Credit to Microsoft/Xbox Game Studio - for Halo Imagery](https://www.microsoft.com/en-gb/store/collections/halocollection)

1. [FreeSVG - Additional Royalty Free Imagery](https://freesvg.org/)

---
## Acknowledgements

With thanks to:
- My family and friends - For providing some great feedback and user-testing across multiple devices and browsers.

- Code Institute & their wider "Slack" community - For providing me with the necessary skills, knowledge and guidance to execute this project.

- Ed Bradley - For suggesting I look into "Query Filters" when I asked a project-related question on Slack. This put me on the right path to getting specific data to show on a page when called rather than all table data.

- Tech With Tim - A Youtuber with fantastic courses on Flask & Python. Served as a huge help when getting sign-up functionality working on this website.

[Back to top ↑](#office-champion)

---