document.addEventListener('DOMContentLoaded', function() {
    
    // materialize collapsible navbar initialization
    var elems = document.querySelectorAll('.sidenav');
    M.Sidenav.init(elems);

    // materialize datepicker initialization
    var elems = document.querySelectorAll('#id_event_date');
    M.Datepicker.init(elems);

    // materialize select initialization
    var elems = document.querySelectorAll('select');
    M.FormSelect.init(elems);

    // materialize modal initialization
    var elems = document.querySelectorAll('.modal');
    M.Modal.init(elems);

    // find add_event form event_date field and add datepicker class for materialize functionality
    dateField = document.getElementById('id_event_date');
    if (dateField) {
        dateField.setAttribute('class', 'datepicker');
    };

    // change start_time input field a timepicker
    timeField = document.getElementById('id_start_time');
    if (timeField) {
        timeField.setAttribute('type', 'time');
    };

    // catch booking submit and run submission function
    let bookingForm = document.getElementById('booking-form');
    if (bookingForm) {
        submitBooking(bookingForm);
    };

    // check for unanswered questions and provide default text, the answerBlocks variable
    // must be iterated through in this way as it is a NodeList not an array and cannot be handled as such.
    let answerBlocks = document.getElementsByClassName('answer');
    if (answerBlocks.length !== 0) {
        // for every question on the page, if the question has not been answered, provide the default text instead.
        for (let i = 0; i < answerBlocks.length; i++) {
            // if the answer block div has no children then it does not have an answer paragraph and therefore is unanswered.
            if (answerBlocks[i].children.length == 0) {
                answerBlocks[i].innerHTML = `<p>Sorry! This question has not been answered yet, check back again later.</p>`
            }
        }
    }
    
    /**
     * Receives the booking form from the page and adds submit as en event listener.
     * On submit, locates the confirmation modal and triggers it to appear. Finally,
     * the function then calls the sendEmail function with the form data.
     * 
     * @param {object} form - the booking form from the event details page
     */
    function submitBooking(form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            let modal = document.getElementById('booking-modal');
            let instance = M.Modal.init(modal, {dismissible: false});
            instance.open();
            sendEmail(form);
        });
    };

    /**
     * Receives the submitted form and uses it's data to send a confirmation email
     * to the user using emailJS. Also uses additional event info from the details
     * section of the page to further customise the email.
     * 
     * @param {object} form - the submitted booking form
     */
    function sendEmail(form) {
        form.event_title.value = document.getElementById('event-title').innerText;
        form.event_start_time.value = document.getElementById('event-time').innerText;
        form.event_meet_point.value = document.getElementById('event-meet-point').innerText;
        emailjs.sendForm('booking_confirmation', 'booking_confirmation', form);
    }
});
