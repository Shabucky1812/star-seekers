# Star Seekers  
![Am I responsive examples for Star Seekers.](/documentation/testing/am-i-responsive.png)  

[View the Live Website here](https://star-seekers.herokuapp.com/)

Star Seekers is a fake social group that hosts late-night events for lovers of the night sky. The aim of this Star Seekers website is to allow the group to reach out to it's current members and entice new ones to join. 
Using the website, users can view details about the group, view upcoming events, ask questions about events, and book a place for them and a group of up to 4 at events.
Admins can also use the website to create new events, edit existing events, and delete events when necessary. Additionally, using the admin panel, admins can create, edit, and delete event guides, and create, edit, and delete question answers.

## Contents
- [UX](#ux)  
- [Design](#design)  
- [Features](#features)  
- [Technologies Used](#technologies-used)  
- [Deployment](#deployment)  
- [Testing](#testing)  
- [Credits](#credits) 

## UX

### User Stories:  
- US01 - Create Account
    - As a New Site User I can sign up for a new account so that I can access the sites main features.

- US02 - Positive First Impression
    - As a New Site User I can easily locate and read key information about the website so that I can quickly understand what the purpose of the site is and how to use it.

- US03 - Logging In
    - As a Site User/Admin I can log in to my account so that I can access the sites features.

- US04 - Logging Out
    - As a Site User/Admin I can log out of my account so that people using the same device as me can access their own account.

- US05 - View Events
    - As a Site User I can coherently view upcoming events so that I can see which events interest me.

- US06 - View Event Details
    - As a Site User I can click on an event so that I can view additional information about the event and access the events Q&A section and booking.

- US07 - Additional Event Info
    - As a Site User I can view important event info (such as time, date, weather, etc..) so that I can see if the event interests/suits me.

- US08 - View Event Guide
    - As a Site User I can view an event's guide so that I can see who is hosting the event.

- US09 - Book Event
    - As a Site User I can book my place at an event so that I can attend the event.

- US10 - Asking Questions
    - As a Site User I can ask the admins questions regarding a specific event so that I can receive additional info about an event.

- US11 - Booking Confirmation
    - As a Site User I can receive confirmation of my booking so that I can ensure I have correctly booked the event.

- US12 - Add Events
    - As a Site Admin I can add new events so that site users can view and book new events.

- US13 - Update Events
    - As a Site Admin I can update an event's details so that any necessary event changes can be made.

- US14 - Delete Events
    - As a Site Admin I can delete events so that cancelled or finished events are not displayed to the site users.

- US15 - Add Guides
    - As a Site Admin I can add new guides so that new guides can be linked to their events.

- US16 - Update Guides
    - As a Site Admin I can update guide details so that guide information can be changed if needed.

- US17 - Delete Guides
    - As a Site Admin I can delete guide profiles so that ex-guides can no longer be selected as event host.

- US18 - Answer User Questions
    - As a Site Admin I can respond to user questions so that the site users receive any additional info they need.

### Wireframes:  

During the planning process of this project, the following wireframes were created (using [Balsamiq](https://balsamiq.com/)) to mock out the website's front-end.

1. Home Page:  
    ![Template wireframes for home page on desktop, tablet, mobile.](/documentation/home_page.png)

2. Events Page:  
    ![Template wireframes for events page on desktop, tablet, mobile.](/documentation/events_page.png)

3. Event Detail Page:  
    ![Template wireframes for event detail page on desktop, tablet, mobile.](/documentation/event_detail_page.png)

4. Register Account Page:  
    ![Template wireframes for register account page on desktop, tablet, mobile.](/documentation/register_account_page.png)

5. Log In Page:  
    ![Template wireframes for log in page on desktop, tablet, mobile.](/documentation/log_in_page.png)

6. Log Out Page:  
    ![Template wireframes for log out page on desktop, tablet, mobile.](/documentation/log_out_page.png)

### Entity-Relationship Diagram:  

For planning the data model for Star Seekers, I created this ER diagram (using [diagrams.net](https://www.diagrams.net/)) to demonstrate how each of the custom models for the website would interact and what fields they should have.  

![Entity-Relationship Diagram for custom star seekers models.](/documentation/entity-relationship.png)

## Design

### Colour Scheme:  

Star Seekers uses the following colour palette, generated using [Coolors](https://coolors.co/):  
![Star Seekers colour palette.](/documentation/colour-palette.png)  
This palette is inspired by the shades of the night sky. The rich blue used is the main colour of the site, it's purpose is to evoke the inviting coziness of the night and it contrasts well with the strong yellow used. The subtle pink tone is used as the website's background colour because it provides more visual interest than a plain grey or white and reminds me of the pink hues in a sunrise.

### Typography:

The website uses the 2 fonts from [Google Fonts](https://fonts.google.com/) seen below:  
- Kanit:  
    ![The Kanit font used for most body text](/documentation/kanit_font.png)  
    This font is used throughout the website with a font weight of 100. I chose this font because it is simple yet effective and pleasing, and it looks nice alongside the Philosopher font.  

- Philosopher (italic):
    ![The Philosopher font used for the site's title text](/documentation/philosopher_font.png)  
    This font is used for all of Star Seekers title text as well as the logo present in the navbar. This font was selected because it is interesting in a subtle way and it looks especially 'flowy' when combined with the multiple 's' letters used in the title of 'Star Seekers'.  

## Features  

### Existing Features:  
- __F01 - Header__  
    ![The header for the Star Seekers website.](/documentation/features/header.png)  
    The first feature of the website is the header, seen above. The header is important for consistency as users expect modern websites to have one. As usual, the header contains the website logo and the internal navigation links. Additionally, to maintain responsive design, the nav links become a hamburger menu at smaller screen sizes to stop the content getting squashed. Links are present for: The home page, the events page, and the login page (if the user is already logged in then this link becomes a logout link instead). The header is valuable to the user because it lets them traverse the website in a consistent and expected way.  

- __F02 - Footer__  
    ![The footer of the Star Seekers website.](/documentation/features/footer.png)  
    This is the footer for the website. It's purpose is once again to enforce a good user experience by meeting expectations of what a modern website should look like. The footer contains the website's important copyright info, and some links to Star Seekers socials. The footer is valuable to the user because it combines with the header to make the site more inviting, and tells the user where else they can go to learn more about Star Seekers.  

- __F03 - Home Page__  
    ![The home page of the Star Seekers website.](/documentation/features/home.png)  
    The next feature is the home/landing page. As this is the very first thing a user sees upon loading the website, it is important that the home page is eye-catching without being overwhelming. To achieve this effect, the home page features a simple title, hero image, and about section. The about section contains small snippets of info about Star Seekers, what the website is all about, and what to do next if interested. The home page is valuable to the user because it gently introduces them to the site and points the in the right direction.  

- __F04 - Log In Form__  
    ![The site's login form.](/documentation/features/login.png)  
    Upon clicking the 'Sign In/Register' link, the user is brought to a log in page displaying this form. If the user already has an account then they can enter their account details here to sign in. Importantly, if the user does not yet have an account, they can use the link provided to head to the register account screen instead. This login form is valuable to the user because it lets them sign in to their account and interact more with the website's features.

- __F05 - Register Account Form__  
    ![The site's register account form.](/documentation/features/register.png)  
    Should the user click on the previous link on the login form, they will be brought to this register account form instead. This form is valuable to a new user because it lets them create an account to become part of the Star Seekers community.  

- __F06 - Log Out Form__  
    ![The site's logout confirmation form.](/documentation/features/logout.png)  
    Once the user has successfullt logged in, the 'Sign Out' link will become available in the site's header. Upon clicking that link, the user will be brought to the logout page containing this small log out confirmation. Should the user wish to log out, all they have to do is press the button and they will be redirected back to the home page. This is valauble to the user because it lets them sign out of their account and let other device users sign in to theirs instead.  

- __F07 - Upcoming Events__  
    ![Star Seeker's upcoming events list.](/documentation/features/events.png)  
    Should the user click on the 'Events' link in the header, they will be brought to this upcoming events list. This page dislays all of the upcoming events created by admins in a list format. Only events with event dates that are yet to come are shown to the user and the displayed events are ordered from closest to furthest away by event date. Each event is displayed in the form a an event 'card' which is clickable. Clicking on an event card will take the user to the event's details page. Each card displays the event's main image, title, date, and start time. Visible on the screenshot above is the add event button (near the top-right) as well as the edit event and delete event buttons (present at the bottom of each card). It is important to note that these buttons are only available to admins, a regular user will not be able to see or use them. Clicking on the add button takes the admin to the add event form, the edit button allows them to edit the relevant event, and the delete button displays a delete confirmation modal (all visible as upcoming features below). Another key detail of the upcoming events page is that it paginates automatically for every 6 events. In the image above, only 3 events are available so the pagination bar at the bottom of the screen reads: 'Page 1 of 1'. Should there be more than 6 upcoming events, this bar will allow the user to traverse between the available pages to view them. For example, if there was 16 upcoming events, the pagination bar would read: 'Page 1 of 3' and the chevron icons would be clickable to move forward and backwards through the pages. The upcoming events list is valuable to the user because it allows them to view upcoming events in a streamlined fashion, this feature is also important for site admins as most of the admin functionality is accessed from this page.  

- __F08 - Event Details__  
    ![An event's additional details.](/documentation/features/details.png)  
    Once the user has decided on an event they are interested in and clicked on it's card, they will be taken to the event's more detailed page. The first section of this page is the event details section seen above. This section features: the event image, the event title, a small event description, the event's date and start time, the meet point for attendees of the event, expected weather on the night, and a small profile about the host/guide of the event. Using all of this information, a user can decide whether they would like to book their place at the event or if they would like to look at some others instead. This section is valuable to the user because it provides all of the basic information they need to know about an event in a clean and efficient manner.  

- __F09 - Booking Form__  
    ![The form used to book a place at an Event.](/documentation/features/booking.png)  
    If a user would like to book a place at the event, they simply need to fill out this form below the details. The form is clearly marked out with the title text 'Want to come along?' and contains fields for the user's name, email address, and group size between 1 and 4. If the user is not signed in, the form will instead be replaced with a simple 'Please Sign In or Create an Account to book a place at this event' message. Once a user has filled out the form with valid data and pressed the submit button, they will be shown the following confirmation modal:  
    ![Booking confirmation modal.](/documentation/features/booking-modal.png)  
    The user can then press the 'Return to Events' button to be taken back to the upcoming events list. Also, as prompted by the modal, the user should receive a confirmation email like the one below:  
    ![Booking confirmation email.](/documentation/features/booking-email.png)  
    The booking form is valuable to the user because it lets them easily book their spot at an event and follows up with sufficient confirmation so that the user knows they have submitted the form correctly, and is certain when and where the event is.  

- __F10 - Ask a Question Form__  
    ![The form used by users to ask questions about events.](/documentation/features/question-form.png)  
    Below the details and booking section of the event details page is the questions section. Using this section, users can ask questions about the event and view questions asked by other users alongside answers to each question by the site admins. Above is the question form which lets users ask questions, it only takes two simple fields: question title, and question details. This is important so that when other users are skimming through the asked questions section, they can use the question title to decide if a question is relevant to them without having to read all of the extended details. Once again, if the user is not signed in, the form is replaced wiht a simple 'Please Sign In or Create an Account to ask questions about this event' message. The ask a question form is valuable to the uses because it increases their interactivity with the site and community and helps them decide if an event is desirable to them.  

- __F11 - Previously Asked Questions__  
    ![Previously asked questions about the event, some answered, some not.](/documentation/features/previous-questions.png)  
    The final feature present on the event details page is the previously asked questions section. When a question is successfully submitted using the question form, it will be added to this section in it's own row, marked out by the blue border. The question information appears on the left-hand side of the row and displays: the question title (underlined to stand out), the question details, and a short statement declaring who asked the question and when so that the admins know which questions should be prioritised to answer first. On the right-hand side of the row is the answer to the question. As seen for the second question above, if a question is yet to be answered, a small message appears stating so. If the admins have answered the question (seen for the first question above), then the answer appears followed by another statement showing who answered the question and when. Additionally, if there is no asked questions about an event, no blue rows appear and are instead replaced with the following message: 'No one has asked any questions about this event yet'. This section is valuable to the user because it provides them with additional information about the event that they might not have considered and it prevents admins having to answer similar questions multiple times.  

- __F12 - Add Event Form__  
    ![The admin form to add a new event.](/documentation/features/add-event.png)  
    As mentioned in F07, if an admin selects the add event button from the upcoming events page then they will be brought to this form which lets them create a new event. The form fields are: the new event title, a small description, an image related to the event, the event date, start time, meet point, expected weather on the night, and finally the event guide. All of these fields are required except for the image, if the admin submits a successful form without a new image, then a default is provided. The form's event date field uses the materalize datepicker seen below:  
    ![The datepicker brought up when submitting a value for the event date field.](/documentation/features/datepicker.png)  
    The datepicker is important because it is easy to use and ensures that the submitted date meets the format requirements for a valid date input. Also the start time field uses the default html time input to ensure the user can only submit a valid 24 hour time. The final two fields of note are the expected weather and guide fields as these are both select fields. The options for the expected weather select are: Unknown, Clear, Chilly, Rainy, Snowy, Stormy. The options for the guide select are the names of the current guides as registered in the database with the custom guide model. The add event form is valuable to the admins because it allows them to easily create a new event from the front-end.  

- __F13 - Edit Event Form__  
    ![The admin form to edit an event, pre-filled with the relevant event data.](/documentation/features/edit-event.png)  
    Also from the upcoming events page, the admins can select the edit event button on any event to be taken to the same form as before, this time however the form is pre-filled with the relevant event information. The example above shows the edit event form for the 'Urban Moonlight' event. The edit event form functions exactly the same as the add event form except any saved changes are applied to the relevant event instead of creating a new one. This feature is valuable to the admins because it means they can make small adjustments to events without having to delete and recreate them.  

- __F14 - Deleting an Event__  
    ![The modal shown when an admin attempts to delete an event.](/documentation/features/delete-event.png)  
    The final admin feature accessible from the upcoming events page is the delete event button. Should an admin attempt to delete an event by clicking the delete button that corresponds to the desired event, the above modal will be shown. This is an important defensive design feature as it prevents the admin form accidentally deleting the wrong event. The confirmation modal simply relays the correct event title to the admin and ensures that they understand the action is irreversible. This feature is valuable to the admin because it lets them remove cancelled events from the view of the site users.  

- __F15 - Admin Panel - Guides__  
    ![The Guide screen of the websites Django admin panel.](/documentation/features/admin-panel-guides.png)  
    The admins of Star Seekers can access the additional site functionality from Django's provided admin panel. This panel is reached by adding '/admin' to the sites base url (the complete url will look something like: 'https://star-seekers.herokuapp.com/admin'). From this panel, the admins can create, update, and delete event Guides using the screen shown above. Using the 'ADD GUIDE' button will take the admin to this form:  
    ![Admin Panel form used to create a new guide.](/documentation/features/add-guide-form.png)  
    This form features fields for: the guide's name, role (a select containing options for: Junior Seeker, Senior Seeker, and Guest Seeker), and a small profile image. If no image is provided then a default will be used. Additionally, the admins can click on any existing guides to be taken to a similar form with pre-filled information that they can change to edit a guide's data. Also, using 'Delete selected guides' from the action drop-down allows admins to remove ex-guides from. This part of the admin panel is valuable because it lets the admins manage their guides in every required way.  

- __F16 - Admin Panel - Answers__  
    ![The Answer screen of the websites Django admin panel](/documentation/features/admin-panel-answers.png)  
    Finally, the admins can use the same admin panel to manage answers to user questions (seen in features F10 and F11). Once again, upon clicking the 'ADD ANSWER' button, the admin will be taken to the following form:  
    ![Admin Panel form used to create a new answer.](/documentation/features/add-answer-form.png)  
    The fields on this form are: author - so the admin can select who is answering the question, question - a select field which lets the admin choose which question they are answering, and the content field - a simple text field to enter the answer. All of these fields are required. Back from the answers screen, the admin can select a previous answer to edit or use the 'Delete selected answers' action to remove unwanted answers. This part of the admin panel field is valuable to the admins because it lets them manage question answers in every required way.  

### Future Implementations:  
Whilst I do believe the existing features meet the requirements of the User Stories in a satisfactory way, there is room for expansion in the following ways:  

- Firstly, I would like for future versions of Star Seekers to not require the usage of the Django admin panel at all as it is not a custom element. To reach this target, I would like for the front-end to feature a guide page which displays all of the current guides in a similar way to the current upcoming events page. From this page, regular site users could view additional details about each guide whilst admins could use this page to access add, edit, and delete guide functionality. To remove the need of the admin panel for the answers, an 'answer question' button could be present for each unanswered question on an event details page for admins only. This button would take the admin to a new add answer form similar to the existing add event form. There could also be additional button to edit and delete existing answers somewhere in the relevant row. These implementations are not included in this version of Star Seekers because of the project scope and timeframe.

- Additionally, it would be nice for users to have more confirmation of their bookings. I would like to implement some form of 'My Bookings' page which is unique to each user and displays a list of their current bookings. This page could also be used to cancel any bookings if a user so desired. This feature is not included in this version of the site because it did not fit in the project's scope.

## Technologies Used

### Languages Used:  
- [HTML5](https://en.wikipedia.org/wiki/HTML5)  
- [CSS3](https://en.wikipedia.org/wiki/CSS)  
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)  
- [Python](https://www.python.org/)  

### Frameworks, Libraries, and Programs Used:  

- [Django](https://www.djangoproject.com/) - Used as this project's main python framework.  
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html) - Used to provide account registration and authentication.  
- [Django Testing Tools](https://docs.djangoproject.com/en/3.2/topics/testing/tools/) - Used to test the python code written for this website.  
- [dj_database_url](https://pypi.org/project/dj-database-url/) - Used to connect to postgres database.  
- [psycopg2](https://pypi.org/project/psycopg2/) - Database adapter used to connect to PostgreSQL database.  
- [Coverage](https://coverage.readthedocs.io/en/latest/) - Used to view what percentage of the python code was tested by the automated python testing.  
- [Materialize](https://materializecss.com/) - Used as this project's main CSS framework.  
- [Gunicorn](https://gunicorn.org/) - Used as the web server that allows Django to run on Heroku.  
- [Cloudinary](https://cloudinary.com/) - Used to store all images used by the website.  
- [ElephantSQL](https://www.elephantsql.com/) - Used to create this website's PostgreSQL database.
- [Google Fonts](https://fonts.google.com/) - Used to provide the fonts (Kanit and Philosopher) used by the website.  
- [Balsamiq](https://balsamiq.com/) - Used to create front-end wireframes during planning of this website.  
- [diagrams.net](https://www.diagrams.net/) - Used to create ER diagrams during planning of this website.  
- [Font Awesome](https://fontawesome.com/) - Used to provide additional icons for the website.  
- [favicon.io](https://favicon.io/favicon-generator/) - Used to create the favicon used by the website.  
- [Heroku](https://www.heroku.com/) - Used to deploy and host the website.
- [Git](https://git-scm.com/) - Used for this website's version control.
- [GitHub](https://github.com/) - Used to create this website's main repository and manage this project's kanban board.  
- [TinyPNG](https://tinypng.com/) - Used to compress the image's used in this README.  
- [Pexels](https://www.pexels.com/) - Used to provide all of the site's imagery.  
- [Am I Responsive?](https://ui.dev/amiresponsive) - used to create README website responsiveness image.

## Deployment

To clone this repository paste `git clone https://github.com/Shabucky1812/star-seekers.git` into the terminal of the editor you are using. Then follow the steps below to get everything up and running.  

### Configuring environment variables:  
- Firstly, you need to install the project dependencies listed in the requirements.txt file. To do this paste `pip install -r requirements.txt` into the terminal and hit enter.
- Next, you need to create a new file at lowest level of your workspace (the same level as README.md) called **env.py**.
- IMPORTANT: the env.py file will be used to store hidden variables such as your SECRET_KEY, to prevent any security issues you must ensure that your workspace contains a **.gitignore** file and that **env.py** is listed within it. This will ensure that your env.py file is not pushed to GitHub and made publicly available.
- Within **env.py**, import the os module by adding `import os` at the top of the file.
- Now, you need to create 4 environment variables using this code format: `os.environ['variable_name'] = 'value'`. The 4 _*variable_name*_'s should be: **DATABASE_URL**, **SECRET_KEY**, **CLOUDINARY_URL**, and finally **DEVELOPMENT**.
- As for the _*values*_, leave **DATABASE_URL** and **CLOUDINARY_URL** blank for now. Set the _*value*_ of the **DEVELOPMENT** variable to '1' and set the **SECRET_KEY** variable to any random string of characters you like, do not share this value with anyone.

### Setting up your ElephantSQL database:  
- Now, lets move on to setting up your PostgreSQL database.
- First, use this [link](https://www.elephantsql.com/) to reach the ElephantSQL website.
- Click on the **Log In** button to get signed in, if you already have an account then sign in as usaul. If not then I recommend just using GitHub to sign in by pressing the **Sign In with GitHub** button. A window may pop-up asking for verification, if so, confirm your agreement.
- You are now at the ElephantSQL dashboard, from this screen click the **Create New Instance** button.
- In the _*Name*_ field, enter a name for your database, this is usually the project name so I would suggest 'star_seekers'. In the _*Plan*_ field, select whatever plan works best for you. I used the free **Tiny Turtle** plan but if you regularly use ElephantSQL, feel free to use another.
- Ignore the _*Tags*_ field and click on the **Select Region** button to move on.
- In the _*Data center*_ field, choose any data center that is available and near you, it doesn't really matter which. Press **Review** to continue.
- Finally, on the review screen, ensure your details are correct and hit **Create instance**.
- You will now be returned to the dashboard. From here, click on your newly created instance to be taken to it's details screen.
- To connect this instance to your workspace, copy the URL from the _*URL*_ field and paste it into the value of your **DATABASE_URL** variable in **env.py**.

### Connecting to Cloudinary:  
- The last environment variable that needs configuring is the **CLOUDINARY_URL**. We will set that up now.
- Use this [link](https://cloudinary.com/) to reach the Cloudinary website. From here you need to either log in using the **Login** button or create an account if you don't yet have one using **SIGN UP FOR FREE**.
- Once authenticated, navigate to your cloudinary dashboard under _*Programmable Media > Dashboard*_.
- Copy the URL within the **API Environment variable** card and use this as the value for your **CLOUDINARY_URL** variable in **env.py**. IMPORTANT: the url you copy will include 'CLOUDINARY_URL=' at the start, this is unnecessary and should be deleted. The url you are left with as your value should start with 'cloudinary://'.

### How to make and push changes:  
- To save all of your files and make migrations paste the command `python3 manage.py migrate` into your terminal.
- Your local workspace should now be runnable. To view a local version of the website, use the command `python3 manage.py runserver` and click **Open Browser** on the pop-up that appears.
- If you wish to make any changes to the code then you can use git to save and push those changes using the following steps:
    - Save your changes to a file using _*CTRL + S*_.
    - In the terminal type `git add .` to push all changes or you can use `*git add 'file_name_here'` to be more specific.
    - Commit your changes using `git commit -m "'commit_message_here'"`.
    - Finally, push your changes to your main GitHub repository using `git push`.

### Deploy with Heroku:  
- Lastly, follow these steps to deploy the website to Heroku.  
- Use this link to log-in/sign-up to [Heroku](https://id.heroku.com/login).
- From the Heroku dashboard, select the **New** dropdown from the top-right, and then click **Create new app**.
- Enter a name into the **App name** input, select your region from the **Region** dropdown, and then click **Create app**.
- From the tabs near the top of the screen, select **Settings** and scroll down to the **Config Vars** sub-heading.
- Press **Reveal Config Vars**.
- You now need to re-create the following variables from your **env.py** file as config vars: **CLOUDINARY_URL**, **DATABASE_URL**, and **SECRET_KEY**.
- Enter these variables as keys for each config var and paste the values from your **env.py** file as the matching values.
- Now, scroll back up and select the **Deploy** tab.
- Under the **Deployment method** sub-heading, select **GitHub**.
- Search for the GitHub repo for your application and then click **Connect**.
- You can now deploy your application in two ways:
    - Select **Enable Automatic Deploys** to automatically deploy your program. This means that whenever a change is pushed, Heroku will automatically update your live app.
    - This project was manually deployed by selecting **Deploy Branch** under the **Manual Deploy** sub-heading. A manually deployed site will only update with new pushes when re-deployed next.
- Once Heroku has deployed your application, it will present you with a link to the live site.
- IMPORTANT: After your first deploy, Heroku may automatically add its Heroku Postgres add-on to your application. This add-on is not free and you will be charged if you leave it. To prevent this from happening after your first deploy:
    - Head over to your application's **Resources** tab.
    - Check under the _*Add-ons*_ subheading for the Heroku Postgres add-on.
    - If the add-on is present, delete it to avoid being charged. The website will still function because of ElephantSQL.

## Testing

Please find the testing write-up for this project in [this Testing Document](testing.md).

## Credits

### Contents  
- All of the code for this website was written by me, [Shaun Buck](https://github.com/Shabucky1812).
- All of the imagery used throughout the website was taken from [Pexels](https://www.pexels.com/).
- Inspiration for creating pagination using function based views was taken from [dontrepeatyourself.org](https://dontrepeatyourself.org/post/django-pagination-with-function-based-view/).

### Acknowledgements  
This was an incredibly rewarding and confidence-boosting project to work on. Going into planning, I had a million questions about Django and I was feeling very overwhelmed by the looming scope. Luckily however, I have been amazed at how much I have learnt taking Star Seekers from inception to completion! Despite the occassional challenge, I feel as though this project has gone smoothly and I am so proud of what I have achieved. I completely reworked how I manage my time whilst working for this website and my productivity has absolutely soared. Whilst I know the end-product isn't perfect, this project has taught me to trust myself, and completely re-invigorated my love for taking on challenges headfirst. I am truly thankful for Star Seekers.

Additionally, I would like to extend a huge thank you to my mentor Brian Macharia for all of his input to this project and his patience in me. Thank you so much!

I hope you found this README insightful, have a great day.