var moveQuestion = (function() {

  /*=================================
  =            POST FORM            =
  =================================*/

  $(document).on('click', '.question_move_link',
    function(event) {
      event.preventDefault();

      var moveUrl = $(this).data('url');

      console.log(moveUrl);

      $.ajax({
          url: moveUrl,
          type: 'POST',
          data: $('#question_move_form').serialize()
        })
        .done(function(data) {
          $('#question_list_div').html(data);
        })
        .fail(function(e) {
          console.log("error");
          console.log(e);
        });
    });

})()
