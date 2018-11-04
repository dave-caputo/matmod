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
      },{
        source: '#question_update_form_data',
        name: 'choiceText1',
        target: '#choice_text_1'
      },{
        source: '#question_update_form_data',
        name: 'choiceText2',
        target: '#choice_text_2'
      },{
        source: '#question_update_form_data',
        name: 'choiceText3',
        target: '#choice_text_3'
      },{
        source: '#question_update_form_data',
        name: 'choiceText4',
        target: '#choice_text_4'
      },{
        source: '#question_update_form_data',
        name: 'choiceText5',
        target: '#choice_text_5'
      }],
      formSubmitBtn: '#question_update_btn',
      actionEvent: 'questionUpdated',
      hiddenLabels: false,
  };
      console.log($('#question_update_form_data').data())
      updateObject(updateQuestionConfig);
});
