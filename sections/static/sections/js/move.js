var moveSection = (function() {

  $(document).on('click', '.section_move_link',
    function(event) {
      event.preventDefault();

      var moveUrl = $(this).data('url');
      $.ajax({
          url: moveUrl,
          type: 'POST',
          data: $('#section_move_form').serialize()
        })
        .done(function(data) {
          $('#section_table_body').html(data);
        })
        .fail(function(e) {
          console.log("error");
          console.log(e);
        });
    });

})()
