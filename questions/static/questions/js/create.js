var createView = (function() {

  /*============================
  =            URLS            =
  ============================*/

  var questionCreateUrl;
  var questionListUrl;
  $(document).ready(function() {
    questionCreateUrl = $('#page_urls').data('questionCreateUrl');
    questionListUrl = $('#page_urls').data('questionListUrl');
  });

  /*================================
  =            GET FORM            =
  ================================*/

  $(document).one('click', '#create_question_link', function(event) {
    event.preventDefault();

    console.log('tickled!');

    $.ajax({
        url: questionCreateUrl,
        type: 'GET',
      })
      .done(function(data) {
        $('#question_create_div').html(data);
      })
      .fail(function(e) {
        console.log("error");
        console.log(e);
      });
  });

  /*===================================
  =            TOGGLE FORM            =
  ===================================*/

  $(document).on('click', '#create_question_link', function(event) {
    $('#question_create_div').toggle();
  });

  /*=================================
  =            POST FORM            =
  =================================*/

  $(document).on('click', '#question_create_btn', function(event) {
    event.preventDefault();
    $.ajax({
        url: questionCreateUrl,
        type: 'POST',
        data: $('#question_create_form').serialize()
      })
      .done(function(data) {
        $('#question_create_div').html(data);
        $(document).trigger('questionCreated');
      })
      .fail(function(e) {
        console.log("error");
        console.log(e);
      });
  });

  /*========================================
  =            GET UPDATED LIST            =
  ========================================*/

  $(document).on('questionCreated', function(event) {
    $.ajax({
        url: questionListUrl,
        type: 'GET',
      })
      .done(function(data) {
        $('#question_list_div').html(data);
      })
      .fail(function(e) {
        console.log("error");
        console.log(e);
      });
  });

})()
