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

    // find add_event form event_date field and add datepicker class for materialize functionality
    dateField = document.getElementById('id_event_date');
    if (dateField) {
        dateField.setAttribute('class', 'datepicker');
    }

    // change start_time input field a timepicker
    timeField = document.getElementById('id_start_time');
    if (timeField) {
        timeField.setAttribute('type', 'time');
    }
});