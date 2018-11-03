var moveQuestion = (function() {

  $(document).on('click', '.question_move_link',
    function(event) {
      event.preventDefault();

      var moveUrl = $(this).data('url');
      $.ajax({
          url: moveUrl,
          type: 'POST',
          data: $('#question_move_form').serialize()
        })
        .done(function(data) {
          $('#question_table_body').html(data);
        })
        .fail(function(e) {
          console.log("error");
          console.log(e);
        });
    });

})()
