$(document).ready(function(){
  var updateQuestionConfig = {
      objectClass: 'question',
      actionUrl: $('#page_urls').data('questionUpdateUrl'),
      formDisplayBtn: '#question_update_display',
      formDisplayDiv: '#question_update_div',
      updateForm: '#question_update_form',
      updatedObjectData: [{
        source: '#question_update_form_data',
        name: 'question',
        target: '#page_header'
      }, {
        source: '#question_update_form_data',
        name: 'weight',
        target: '#question_weight'
      }
      ],
      formSubmitBtn: '#question_update_btn',
      actionEvent: 'questionUpdated',
      hiddenLabels: true,
  };
      updateObject(updateQuestionConfig);
});
