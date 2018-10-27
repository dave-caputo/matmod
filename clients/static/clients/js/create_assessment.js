$(document).ready(function(){
    var assessCreateConfig = {
        objectClass: 'assessment',
        actionUrl: $('#page_urls').data('assessCreateUrl'),
        listUrl: $('#page_urls').data('assessListUrl'),
        formDisplayBtn: '#assess_create_display',
        formDisplayDiv: '#assess_create_div',
        listDisplayDiv: '#assess_table_body',
        formSubmitBtn: '#assess_create_btn',
        actionEvent: 'assessCreated',
        hiddenLabels: false,
    };
    createObject(assessCreateConfig);
});
