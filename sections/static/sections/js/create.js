var createQreSection = (function() {

  /*============================
  =            URLS            =
  ============================*/

  var qreSectionCreateUrl;
  var qreSectionListUrl;
  $(document).ready(function() {
    qreSectionCreateUrl = $('#page_urls').data('qreSectionCreateUrl');
    qreSectionListUrl = $('#page_urls').data('qreSectionListUrl');
  });

  /*================================
  =            GET FORM            =
  ================================*/

  $(document).one('click', '#qre_section_create_display', function(event) {
    console.log('create display clicked!');
    $.ajax({
        url: qreSectionCreateUrl,
        type: 'GET',
      })
      .done(function(data) {
        $('#qre_section_create_div').html(data);
      })
      .fail(function(e) {
        console.log("error");
        console.log(e);
      });
  });

  /*===================================
  =            TOGGLE FORM            =
  ===================================*/

  $(document).on('click', '#qre_section_create_display', function(event) {
    $('#qre_section_create_div').toggle();
  });

  /*=================================
  =            POST FORM            =
  =================================*/

  $(document).on('click', '#qre_section_create_btn', function(event) {
    event.preventDefault();
    $.ajax({
        url: qreSectionCreateUrl,
        type: 'POST',
        data: $('#qre_section_create_form').serialize()
      })
      .done(function(data) {
        $('#qre_section_create_div').html(data);
        $(document).trigger('qreSectionCreated');
      })
      .fail(function(e) {
        console.log("error");
        console.log(e);
      });
  });

  /*========================================
  =            GET UPDATED LIST            =
  ========================================*/

  $(document).on('qreSectionCreated', function(event) {
    $.ajax({
        url: qreSectionListUrl,
        type: 'GET',
      })
      .done(function(data) {
        $('#qre_section_list_div').html(data);
        $('#qre_section_create_div').toggle();
      })
      .fail(function(e) {
        console.log("error");
        console.log(e);
      });
  });


})()
