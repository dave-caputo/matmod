// This components should be reusable by the various cards.
// It displays a create form after clicking an add button.

function setCreateComponent(config){

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
        // Event to get and display the create form.
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
            console.log("error");
            console.log(e);
        });
    });

    /*===================================
    =            TOGGLE FORM            =
    ===================================*/


    $(document).on('click', config.formDisplayBtn, function(event) {
        console.log('clicked display button');
        $(config.formDisplayDiv).toggle();
    });


    /*=================================
    =            POST FORM            =
    =================================*/


    $(document).on('click', config.formSubmitBtn, function(event) {
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
            console.log("error");
            console.log(e);
        });
    });

    $(document).on('submit', config.createForm, function(event){
        // prevent submit on hitting <enter> key
        event.preventDefault();
    });


    /*========================================
    =            GET UPDATED LIST            =
    ========================================*/

    $(document).on(config.actionEvent, function(event) {
        $.ajax({
            url: config.listUrl,
            type: 'GET',
        })
        .done(function(data) {
            $(config.listDisplayDiv).html(data);
            $(config.formDisplayDiv).toggle();
        })
        .fail(function(e) {
            console.log("error");
            console.log(e);
        });
    });
}

$(document).ready(function(){
    var config = {
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
    setCreateComponent(config);

    var config = {
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
    setCreateComponent(config);

});

