var questionUpdateView = (function() {

  /*============================
  =            URLS            =
  ============================*/

  var questionUpdateUrl;
  $(document).ready(function() {
    questionUpdateUrl = $('#page_urls').data('questionUpdateUrl');
  });

  /*================================
  =            GET FORM            =
  ================================*/

  $(document).one('click', '#question_update_link',
    function(event) {
      $.ajax({
          url: questionUpdateUrl,
          type: 'GET',
        })
        .done(function(data) {
          $('#question_update_div').html(data);
        })
        .fail(function(e) {
          console.log("error");
          console.log(e);
        });
    });

  /*===================================
  =            TOGGLE FORM            =
  ===================================*/

  $(document).on('click', '#question_update_link', function(event) {
    $('#question_update_div').toggle();
  });

  /*=================================
  =            POST FORM            =
  =================================*/

  $(document).on('click', '#question_update_btn', function(event) {
    event.preventDefault();
    $.ajax({
        url: questionUpdateUrl,
        type: 'POST',
        data: $('#question_update_form').serialize()
      })
      .done(function(data) {
        $('#question_update_div').html(data);
        $(document).trigger('questionUpdated');
      })
      .fail(function(e) {
        console.log("error");
        console.log(e);
      });
  });

  /*========================================
  =            GET UPDATED LIST            =
  ========================================*/

  $(document).on('questionUpdated', function(event) {
    var formData = $('#question_update_form_data').data();
    var updatedQuestion = formData.question;
    var updatedWeight = formData.weight;
    $('#page_header').html(updatedQuestion);
    $('#question_weight').html(updatedWeight);
    $('#question_update_div').toggle();

  });


})()
