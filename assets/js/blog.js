$(document).ready(function() {
    var request = function(url, data, successCallback, errorCallback) {
        $.ajax({
            url: url,
            method: "POST",
            dataType: "json",
            data: data,
            "beforeSend": function(xhr, settings) {
                $.ajaxSettings.beforeSend(xhr, settings);
            },
            success: function (data) {
                successCallback(data);
            },
            error: function(data) {
               errorCallback(data);
            }
        });
    }

    $('#like-button').click(function() {
        var data = { post_id: $('#post-id').val() };
        var url = "/blog/like";
        var success = function(data) {
             if (data.message) {
                    bootbox.alert(data.message);
                } else if (data.times_liked) {
                    $('#times-liked').text(data.times_liked);
                }
        }
        request(url, data, success, function(data) {
            bootbox.alert("Our like button is broken :{");
        });
    });

    $('#comment-button').click(function() {
        var data =  {
            comment: $('#comment-field').val(),
            post_id: $('#post-id').val()
        };
        var success = function(data) {
            if (data.message) {
                bootbox.alert(data.message);
                } else {
                location.reload();
            }
        }

        request('/blog/comment', data, success, function(data) {
            bootbox.alert("Our comment button is broken :{");
        });
    });

    $('.delete-comment').click(function() {
        var self = this;
        bootbox.confirm("Are you sure you want to delete this comment?", function(result) {
            if (result == false)
                return;
            var selected_id = $(self).attr("data-comment-id");
            var data = { comment_id: selected_id }
            var success = function(data) {
                if (data.comment_id && selected_id == data.comment_id)
                    $('#comment-card-' + data.comment_id).remove();
            };

            request('/blog/comment/delete', data, success, function(data) {
                bootbox.alert("Could not delete comment");
            });
        });
    });
});
