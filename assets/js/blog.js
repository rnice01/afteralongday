$(document).ready(function() {

    $('#like-button').click(function() {
        $.ajax({
            url: '/blog/like',
            method: "POST",
            dataType: "json",
            data: {
                post_id: $('#post-id').val()
            },
            "beforeSend": function(xhr, settings) {
                $.ajaxSettings.beforeSend(xhr, settings);
            },
            success: function (data) {
                if (data.message) {
                    bootbox.alert(data.message);
                } else if (data.times_liked) {
                    $('#times-liked').text(data.times_liked);
                }


            },
            error: function(data) {
               bootbox.alert("Our like button is broken :{");
            }
        });
    });

    $('#comment-button').click(function() {
        $.ajax({
            url: '/blog/comment',
            method: "POST",
            dataType: "json",
            data: {
                comment: $('#comment-field').val(),
                post_id: $('#post-id').val()
            },
            "beforeSend": function(xhr, settings) {
                $.ajaxSettings.beforeSend(xhr, settings);
            },
            success: function (data) {
                if (data.message) {
                    bootbox.alert(data.message);
                } else {
                    location.reload();
                }

            },
            error: function(data) {
               bootbox.alert("Our comment button is broken :{");
            }
        });
    });
});
