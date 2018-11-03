function updateObject(config) {
    // A reusable component to update objects on page.

    function showOrHideLabels(formDiv){
        // Show or hide the labels from a form contained in the form div passed as an argument.
        if (config.hiddenLabels) {
            $(formDiv).find('label').each(function(index, element){
                $(element).hide();
            });
        }
    }

    $(document).one('click', config.formDisplayBtn, function(event) {
        // Get and display the update form when clicking the display button for the first time.
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
            console.log('An error occurred when trying to get the ' + config.objectClass +' update form.');
            console.log(e);
        });
    });

    $(document).on('click', config.formDisplayBtn, function(event) {
        // Toggle the create form.
        $(config.formDisplayDiv).toggle();
    });

    $(document).on('click', config.formSubmitBtn, function(event) {
        // Create new object.
        event.preventDefault();
        $.ajax({
            url: config.actionUrl,
            type: 'POST',
            data: $(config.updateForm).serialize()
        })
        .done(function(data) {
            $(config.formDisplayDiv).html(data);
            showOrHideLabels(config.formDisplayDiv);
            $(document).trigger(config.actionEvent);
        })
        .fail(function(e) {
            console.log('An error occurred when trying to update the ' + config.objectClass +'.');
            console.log(e);
        });
    });

    $(document).on(config.actionEvent, function(event) {

        $.each(config.updatedObjectData, function(index, value){
            var data = $(value.source).data(value.name);
            $(value.target).html(data);
        });

        $(config.formDisplayDiv).toggle();
    });
}
