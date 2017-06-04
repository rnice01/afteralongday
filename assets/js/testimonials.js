$(document).ready(function(){
    var text_max = 200;
    $('#count_message').html(text_max + ' remaining');

    $('#testimonial_feedback').on('mousedown keyup', function() {
      var text_length = $('#testimonial_feedback').val().length;
      var text_remaining = text_max - text_length;
      $('#count_message').html(text_remaining + ' remaining');
    });
});