var moveQreSection = (function() {

  /*============================
  =            URLS            =
  ============================*/

  var qreSectionMoveUrl;
  var qreSectionListUrl;
  $(document).ready(function() {
    qreSectionMoveUrl = $('#page_urls').data('qreSectionMoveUrl');
    qreSectionListUrl = $('#page_urls').data('qreSectionListUrl');
  });

  /*=================================
  =            POST FORM            =
  =================================*/

  $(document).on('click', '.qre_section_move_link',
    function(event) {
      event.preventDefault();

      var moveUrl = $(this).data('url');

      $.ajax({
          url: moveUrl,
          type: 'POST',
          data: $('#qre_section_move_form').serialize()
        })
        .done(function(data) {
          $('#qre_section_list_div').html(data);
        })
        .fail(function(e) {
          console.log("error");
          console.log(e);
        });
    });

})()
