var updateView = (function() {

  /*============================
  =            URLS            =
  ============================*/

  var qreUpdateUrl;
  $(document).ready(function() {
    qreUpdateUrl = $('#page_urls').data('qreUpdateUrl');
  });

  /*================================
  =            GET FORM            =
  ================================*/

  $(document).one('click', '#update_display_qre', function(event) {
    $.ajax({
        url: qreUpdateUrl,
        type: 'GET',
      })
      .done(function(data) {
        $('#qre_update_div').html(data);
      })
      .fail(function(e) {
        console.log("error");
        console.log(e);
      });
  });

  /*===================================
  =            TOGGLE FORM            =
  ===================================*/

  $(document).on('click', '#update_display_qre', function(event) {
    $('#qre_update_div').toggle();
  });

  /*=================================
  =            POST FORM            =
  =================================*/

  $(document).on('click', '#qre_update_btn', function(event) {
    event.preventDefault();
    $.ajax({
        url: qreUpdateUrl,
        type: 'POST',
        data: $('#qre_update_form').serialize()
      })
      .done(function(data) {
        $('#qre_update_div').html(data);
        $(document).trigger('qreUpdated');
      })
      .fail(function(e) {
        console.log("error");
        console.log(e);
      });
  });

  /*========================================
  =            GET UPDATED LIST            =
  ========================================*/

  $(document).on('qreUpdated', function(event) {
    var updatedName = $('#update_form_data').data('qreName');
    $('#page_header').html(updatedName);
    $('#qre_update_div').toggle();

  });


})()
