$(document).ready(function(){
    var renameSectionConfig = {
        objectClass: 'section',
        actionUrl: $('#page_urls').data('sectionRenameUrl'),
        formDisplayBtn: '#section_rename_display',
        formDisplayDiv: '#section_rename_div',
        updateForm: '#section_rename_form',
        updatedObjectData: [
            {
                source: '#section_rename_form_data',
                name: 'sectionName',
                target: '#page_header'
            },
        ],
        formSubmitBtn: '#section_rename_btn',
        actionEvent: 'sectionRenamed',
        hiddenLabels: true,
    };
        updateObject(renameSectionConfig);
});
