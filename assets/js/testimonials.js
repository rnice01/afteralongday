$(document).ready(function(){
    var text_max = 200;
    $('#count_message').html(text_max + ' remaining');

    $('#testimonial_feedback').on('mousedown keyup', function() {
      var text_length = $('#testimonial_feedback').val().length;
      var text_remaining = text_max - text_length;
      $('#count_message').html(text_remaining + ' remaining');
    });

    $('#testimonial-form').submit(function(e) {
        e.preventDefault();
         $.ajax({
                url: '/testimonial/',
                method: "POST",
                dataType: "json",
                data: {
                    feedback: e.target.feedback.value
                },
                "beforeSend": function(xhr, settings) {
                    $.ajaxSettings.beforeSend(xhr, settings);
                },
                success: function (data) {
                    $('#testimonial-modal-body').html('<h3>' + data.message + '</h3>');
                },
                error: function(data) {
                   bootbox.alert("We are unable to save your feedback at this this time.")
                }
            });
    });
});