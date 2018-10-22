$(document).ready(function(){
    console.log('yeps, loaded')
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
    createObject(clientConfig);

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
    createObject(qreConfig);

});
