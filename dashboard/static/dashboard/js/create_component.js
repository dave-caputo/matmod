function objectCreateComponent(config){
    // A reusable component to create objects on page.

    /*================================
    =            GET FORM            =
    ================================*/

    function showOrHideLabels(formDiv){
        // Show or hide the labels from a form contained in the form div passed as an argument.
        if (config.hiddenLabels) {
            $(formDiv).find('label').each(function(index, element){
                $(element).hide();
            });
        }
    }

    $(document).one('click', config.formDisplayBtn, function(event) {
        // Get and display the create form when clicking the display button for the first time.
        $.ajax({
            url: config.actionUrl,
            type: 'GET',
        })
        .done(function(data) {
            $(config.formDisplayDiv).html(data);
            showOrHideLabels(config.formDisplayDiv);
            $(config.formDisplayDiv).toggle();
        })
        .fail(function(e) {
            console.log('An error occurred when trying to get the '+ config.objectClass +' create form.');
            console.log(e);
        });
    });

    /*===================================
    =            TOGGLE FORM            =
    ===================================*/


    $(document).on('click', config.formDisplayBtn, function(event) {
        // Toggle the create form.
        $(config.formDisplayDiv).toggle();
    });


    /*=================================
    =            POST FORM            =
    =================================*/


    $(document).on('click', config.formSubmitBtn, function(event) {
        // Create new object.
        event.preventDefault();
        $.ajax({
            url: config.actionUrl,
            type: 'POST',
            data: $(config.createForm).serialize()
        })
        .done(function(data) {
            $(config.formDisplayDiv).html(data);
            showOrHideLabels(config.formDisplayDiv);
            $(document).trigger(config.actionEvent);
        })
        .fail(function(e) {
            console.log('An error occurred when trying to create a new'+ config.objectClass +'.');
            console.log(e);
        });
    });

    $(document).on('submit', config.createForm, function(event){
        // Prevent submit on hitting <enter> key
        event.preventDefault();
    });


    /*========================================
    =            GET UPDATED LIST            =
    ========================================*/

    $(document).on(config.actionEvent, function(event) {
        // Get an updated object list after object creation.
        $.ajax({
            url: config.listUrl,
            type: 'GET',
        })
        .done(function(data) {
            $(config.listDisplayDiv).html(data);
            $(config.formDisplayDiv).toggle();
        })
        .fail(function(e) {
            console.log('An error ocurred when trying to get the ' + config.objectClass + ' list.');
            console.log(e);
        });
    });
}

$(document).ready(function(){
    var clientConfig = {
        objectClass: 'client',
        actionUrl: $('#page_urls').data('clientCreateUrl'),
        listUrl: $('#page_urls').data('clientListUrl'),
        formDisplayBtn: '#client_create_display',
        formDisplayDiv: '#client_create_div',
        listDisplayDiv: '#client_list_div',
        formSubmitBtn: '#client_create_btn',
        createForm: '#client_create_form',
        actionEvent: 'clientCreated',
        hiddenLabels: true,
    };
    setCreateComponent(clientConfig);

    var qreConfig = {
        objectClass: 'questionnaire',
        actionUrl: $('#page_urls').data('qreCreateUrl'),
        listUrl: $('#page_urls').data('qreListUrl'),
        formDisplayBtn: '#qre_create_display',
        formDisplayDiv: '#qre_create_div',
        listDisplayDiv: '#qre_list_div',
        formSubmitBtn: '#qre_create_btn',
        createForm: '#qre_create_form',
        actionEvent: 'qreCreated',
        hiddenLabels: true,
    };
    setCreateComponent(qreConfig);

});

