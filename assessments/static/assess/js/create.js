var createAssess = (function() {

  /*============================
  =            URLS            =
  ============================*/

  var assessCreateUrl;
  var assessListUrl;
  $(document).ready(function() {
    assessCreateUrl = $('#page_urls').data('assessCreateUrl');
    assessListUrl = $('#page_urls').data('assessListUrl');
  });

  /*================================
  =            GET FORM            =
  ================================*/

  $(document).one('click', '#assess_create_link', function(event) {
    $.ajax({
        url: assessCreateUrl,
        type: 'GET',
      })
      .done(function(data) {
        $('#assess_create_div').html(data);
      })
      .fail(function(e) {
        console.log("error");
        console.log(e);
      });
  });

  /*===================================
  =            TOGGLE FORM            =
  ===================================*/

  $(document).on('click', '#assess_create_link', function(event) {
    $('#assess_create_div').toggle();
  });

  /*=================================
  =            POST FORM            =
  =================================*/

  $(document).on('click', '#assess_create_btn', function(event) {
    event.preventDefault();
    $.ajax({
        url: assessCreateUrl,
        type: 'POST',
        data: $('#assess_create_form').serialize()
      })
      .done(function(data) {
        $('#assess_create_div').html(data);
        $(document).trigger('assessCreated');
      })
      .fail(function(e) {
        console.log("error");
        console.log(e);
      });
  });

  /*========================================
  =            GET UPDATED LIST            =
  ========================================*/

  $(document).on('assessCreated', function(event) {
    $.ajax({
        url: assessListUrl,
        type: 'GET',
      })
      .done(function(data) {
        $('#assess_list_div').html(data);
        $('#assess_create_div').toggle();
      })
      .fail(function(e) {
        console.log("error");
        console.log(e);
      });
  });


})()
