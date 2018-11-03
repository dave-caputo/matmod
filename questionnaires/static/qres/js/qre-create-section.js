$(document).ready(function(){
    var sectionCreateConfig = {
        objectClass: 'section',
        actionUrl: $('#page_urls').data('sectionCreateUrl'),
        listUrl: $('#page_urls').data('sectionListUrl'),
        formDisplayBtn: '#section_create_display',
        formDisplayDiv: '#section_create_div',
        listDisplayDiv: '#section_table_body',
        formSubmitBtn: '#section_create_btn',
        actionEvent: 'sectionCreated',
        hiddenLabels: false,
    };
    createObject(sectionCreateConfig);
});
