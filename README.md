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


### Future Implementations:  


## Technologies Used

frameworks, libraries, languages, etc.

## Deployment

deployment steps

## Testing

Please find the testing write-up for this project in [this Testing Document](testing.md).

## Credits

content and acknowledgements