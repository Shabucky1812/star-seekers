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
    
    function submitBooking(form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            let modal = document.getElementById('booking-modal');
            let instance = M.Modal.init(modal, {dismissible: false});
            instance.open();
            sendEmail(form);
        });
    };

    function sendEmail(form) {
        form.event_title.value = document.getElementById('event-title').innerText;
        form.event_start_time.value = document.getElementById('event-time').innerText;
        form.event_meet_point.value = document.getElementById('event-meet-point').innerText;
        emailjs.sendForm('booking_confirmation', 'booking_confirmation', form);
    }
});
