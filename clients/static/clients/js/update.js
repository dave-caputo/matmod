var updateClient = (function() {

  /*============================
  =            URLS            =
  ============================*/

  var clientUpdateUrl;
  $(document).ready(function() {
    clientUpdateUrl = $('#page_urls').data('clientUpdateUrl');
  });

  /*================================
  =            GET FORM            =
  ================================*/

  $(document).one('click', '#client_update_link', function(event) {
    $.ajax({
        url: clientUpdateUrl,
        type: 'GET',
      })
      .done(function(data) {
        $('#client_update_div').html(data);
      })
      .fail(function(e) {
        console.log("error");
        console.log(e);
      });
  });

  /*===================================
  =            TOGGLE FORM            =
  ===================================*/

  $(document).on('click', '#client_update_link', function(event) {
    $('#client_update_div').toggle();
  });

  /*=================================
  =            POST FORM            =
  =================================*/

  $(document).on('click', '#client_update_btn', function(event) {
    event.preventDefault();
    $.ajax({
        url: clientUpdateUrl,
        type: 'POST',
        data: $('#client_update_form').serialize()
      })
      .done(function(data) {
        $('#client_update_div').html(data);
        $(document).trigger('clientUpdated');
      })
      .fail(function(e) {
        console.log("error");
        console.log(e);
      });
  });

  /*========================================
  =            GET UPDATED LIST            =
  ========================================*/

  $(document).on('clientUpdated', function(event) {
    var clientName = $('#client_update_form_data').data('clientName');
    $('#page_header').html(clientName);
    $('#client_update_div').toggle();

  });


})()
