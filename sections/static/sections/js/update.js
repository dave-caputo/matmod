var sectionUpdateView = (function() {

  /*============================
  =            URLS            =
  ============================*/

  var qreSectionUpdateUrl;
  $(document).ready(function() {
    qreSectionUpdateUrl = $('#page_urls').data('qreSectionUpdateUrl');
  });

  /*================================
  =            GET FORM            =
  ================================*/

  $(document).one('click', '#update_qre_section_link',
    function(event) {

      console.log('that tickled once!')

      $.ajax({
          url: qreSectionUpdateUrl,
          type: 'GET',
        })
        .done(function(data) {
          $('#qre_section_update_div').html(data);
          console.log('success!');
        })
        .fail(function(e) {
          console.log("error");
          console.log(e);
        });
    });

  /*===================================
  =            TOGGLE FORM            =
  ===================================*/

  $(document).on('click', '#update_qre_section_link', function(event) {
    $('#qre_section_update_div').toggle();
  });

  /*=================================
  =            POST FORM            =
  =================================*/

  $(document).on('click', '#qre_section_update_btn', function(event) {
    event.preventDefault();
    $.ajax({
        url: qreSectionUpdateUrl,
        type: 'POST',
        data: $('#qre_section_update_form').serialize()
      })
      .done(function(data) {
        $('#qre_section_update_div').html(data);
        $(document).trigger('qreSectionUpdated');
      })
      .fail(function(e) {
        console.log("error");
        console.log(e);
      });
  });

  /*========================================
  =            GET UPDATED LIST            =
  ========================================*/

  $(document).on('qreSectionUpdated', function(event) {
    var updatedName = $('#qre_section_update_form_data').data('qreName');
    $('#page_header').html(updatedName);
    $('#qre_section_update_div').toggle();

  });


})()
