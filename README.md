# Star Seekers
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
    Should the user click on the 'Events' link in the header, they will be brought to this upcoming events list. This page dislays all of the upcoming events created by admins in a list format. Only events with event dates that are yet to come are shown to the user and the displayed events are ordered from closest to furthest away by event date. Each event is displayed in the form a an event 'card' which is clickable. Clicking on an event card will take the user to the event's details page. Each card displays the event's main image, title, date, and start time. Visible on the screenshot above is the add event button (near the top-right) as well as the edit event and delete event buttons (present at the bottom of each card). It is important to note that these buttons are only available to admins, a regular user will not be able to see or user them. Clicking on and add button takes the admin to the add event form, the edit button allows them to edit the relevant event, and the delete button displays a delete confirmation modal (all visible as upcoming features below). Another key detail of the upcoming events page is that it paginates automatically for every 6 events. In the image above, only 3 events are available so the pagination bar at the bottom of the screen reads: 'Page 1 of 1'. Should there be more than 6 upcoming events, this bar will allow the user to traverse between the available pages to view them. For example, if there was 16 upcoming events, the pagination bar would read: 'Page 1 of 3' and teh chevron icons woul be clickable to move forward and backwards through the pages. The upcoming events list is valuable to the user because it allows them to view upcoming events in a streamlined fashion, this feature is also important for site admins as most of the admin functionality is accessed from this page.  

- __F08 - Event Details__  
    ![An event's additional details.](/documentation/features/details.png)  
    Once the user has decided on an event they are interested in and clicked on it's card, they will be taken to the event's more detailed page. The first section of this page is the event details section seen above. This section features: the event image, the event title, a small event description, the event's date and start time, the meet point for attendees of the event, expected weather on the night, and a small profile about the host/guide of the event. Using all of this information, a user can decide whether they would like to book their place at the event or if they would like to look at some others instead. This section is valuable to the user because it provides all of the basic information they need to know about an event in a clean and efficient manner.  

- __F09 - Booking Form__  
    ![The form used to book a place at an Event.](/documentation/features/booking.png)  
    If a user would like to book a place at the event, they simply need to fill out this form below the details. The form is clearly marked out with the title text 'Want to come along?' and contains fields for the user's name, email address, and group size between 1 and 4. Once a user has filled out the form with valid data and pressed the submit button, they will be shown the following confirmation modal:  
    ![Booking confirmation modal.](/documentation/features/booking-modal.png)  
    The user can then press the 'Return to Events' button to be taken back to the upcoming events list. Also, as prompted by the modal, the user should receive a confirmation email like the one below:  
    ![Booking confirmation email.](/documentation/features/booking-email.png)  
    The booking form is valuable to the user because it lets them easily book there spot at an event and follows up with sufficient confirmation so that the user knows they have submitted the form correctly, and is certain when and where the event is.  

### Future Implementations:  


## Technologies Used

frameworks, libraries, languages, etc.

## Deployment

deployment steps

## Testing

Please find the testing write-up for this project in [this Testing Document](testing.md).

## Credits

content and acknowledgements