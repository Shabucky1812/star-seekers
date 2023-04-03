document.addEventListener('DOMContentLoaded', function() {
    
    // materialize collapsible navbar initialization
    var elems = document.querySelectorAll('.sidenav');
    M.Sidenav.init(elems);

    // materialzie datepicker initialization
    var elems = document.querySelectorAll('#id_event_date');
    M.Datepicker.init(elems);

    var elems = document.querySelectorAll('select');
    M.FormSelect.init(elems);

    // find add_event form event_date field and add datepicker class for materialzie functionality
    dateField = document.getElementById('id_event_date');
    dateField.setAttribute('class', 'datepicker');

    // change start_time input field a timepicker
    dateField = document.getElementById('id_start_time');
    dateField.setAttribute('type', 'time');
});