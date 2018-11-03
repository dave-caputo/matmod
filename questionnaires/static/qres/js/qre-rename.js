$(document).ready(function(){
    var renameQreConfig = {
        objectClass: 'questionnaire',
        actionUrl: $('#page_urls').data('qreRenameUrl'),
        formDisplayBtn: '#qre_rename_display',
        formDisplayDiv: '#qre_rename_div',
        updateForm: '#qre_rename_form',
        updatedObjectData: [
            {
                source: '#qre_rename_form_data',
                name: 'qreName',
                target: '#page_header'
            },
        ],
        formSubmitBtn: '#qre_rename_btn',
        actionEvent: 'qreRenamed',
        hiddenLabels: true,
    };
        updateObject(renameQreConfig);
});
