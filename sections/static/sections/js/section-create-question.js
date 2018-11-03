$(document).ready(function(){
    var questionCreateConfig = {
        objectClass: 'question',
        actionUrl: $('#page_urls').data('questionCreateUrl'),
        listUrl: $('#page_urls').data('questionListUrl'),
        formDisplayBtn: '#question_create_display',
        formDisplayDiv: '#question_create_div',
        listDisplayDiv: '#question_table_body',
        formSubmitBtn: '#question_create_btn',
        actionEvent: 'questionCreated',
        hiddenLabels: false,
    };
    createObject(questionCreateConfig);
});
