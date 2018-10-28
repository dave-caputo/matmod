$(document).ready(function(){
    var assessRenameConfig = {
        objectClass: 'assess',
        actionUrl: $('#page_urls').data('assessRenameUrl'),
        listUrl: $('#page_urls').data('assessListUrl'),
        formDisplayBtn: '#assess_rename_display',
        formDisplayDiv: '#assess_rename_div',
        updateForm: '#assess_rename_form',
        updatedObjectData: [
            {
                source: '#assess_rename_form_data',
                name: 'assessName',
                target: '#page_header'
            },
        ],
        formSubmitBtn: '#assess_rename_btn',
        actionEvent: 'assessRenamed',
        hiddenLabels: true,
    };
        updateObject(assessRenameConfig);
});
