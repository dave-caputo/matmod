$(document).ready(function(){
    var updateClientConfig = {
        objectClass: 'client',
        actionUrl: $('#page_urls').data('clientUpdateUrl'),
        listUrl: $('#page_urls').data('clientListUrl'),
        formDisplayBtn: '#client_update_display',
        formDisplayDiv: '#client_update_div',
        updateForm: '#client_update_form',
        updatedObjectData: [
            {
                source: '#client_update_form_data',
                name: 'clientName',
                target: '#page_header'
            },
        ],
        formSubmitBtn: '#client_update_btn',
        actionEvent: 'clientUpdated',
        hiddenLabels: true,
    };
        updateObject(updateClientConfig);
});
