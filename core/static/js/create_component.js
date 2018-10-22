function createObject(config){
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
