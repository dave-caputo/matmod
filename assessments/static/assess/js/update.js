var assessUpdateView = (function() {

  /*============================
  =            URLS            =
  ============================*/

  var assessUpdateUrl;
  $(document).ready(function() {
    assessUpdateUrl = $('#page_urls').data('assessUpdateUrl');
  });

  /*================================
  =            GET FORM            =
  ================================*/

  $(document).one('click', '#assess_update_link',
    function(event) {
      $.ajax({
          url: assessUpdateUrl,
          type: 'GET',
        })
        .done(function(data) {
          $('#assess_update_div').html(data);
        })
        .fail(function(e) {
          console.log("error");
          console.log(e);
        });
    });

  /*===================================
  =            TOGGLE FORM            =
  ===================================*/

  $(document).on('click', '#assess_update_link', function(event) {
    $('#assess_update_div').toggle();
  });

  /*=================================
  =            POST FORM            =
  =================================*/

  $(document).on('click', '#assess_update_btn', function(event) {
    event.preventDefault();
    $.ajax({
        url: assessUpdateUrl,
        type: 'POST',
        data: $('#assess_update_form').serialize()
      })
      .done(function(data) {
        $('#assess_update_div').html(data);
        $(document).trigger('assessUpdated');
      })
      .fail(function(e) {
        console.log("error");
        console.log(e);
      });
  });

  /*========================================
  =            GET UPDATED LIST            =
  ========================================*/

  $(document).on('assessUpdated', function(event) {
    var updatedQuestion = $('#assess_update_form_data').data('assess');
    $('#page_header').html(updatedQuestion);
    $('#assess_update_div').toggle();

  });


})()
