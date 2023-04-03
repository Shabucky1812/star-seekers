document.addEventListener('DOMContentLoaded', function() {
    
    // materialize collapsible navbar initialization
    var elems = document.querySelectorAll('.sidenav');
    M.Sidenav.init(elems);

    // materialzie datepicker initialization
    var elems = document.querySelectorAll('#id_event_date');
    M.Datepicker.init(elems);

    // materialzie timepicker initialization
    var elems = document.querySelectorAll('#id_start_time');
    M.Timepicker.init(elems);

    var elems = document.querySelectorAll('select');
    M.FormSelect.init(elems);

    // find add_event form event_date field and add datepicker class for materialzie functionality
    dateField = document.getElementById('id_event_date')
    dateField.setAttribute('class', 'datepicker')

    // find add_event form start_time field and add timepicker class for materialzie functionality
    dateField = document.getElementById('id_start_time')
    dateField.setAttribute('class', 'timepicker')
});