$(document).ready(function() {
    $("#add-to-cart").on('click', function(e) {
        var self = this;
        bootbox.prompt({
            title: "How many orders?",
            inputType: 'number',
            callback: function (quantity) {
                if (!quantity)
                    return
                $.ajax({
                    url: "/add-to-cart",
                    method: "POST",
                    "dataType": "json",
                    data: {
                        bathbomb_id : $(self).attr("data-bathbomb-id"),
                        quantity : quantity
                    },
                    "beforeSend": function(xhr, settings) {
                        $.ajaxSettings.beforeSend(xhr, settings);
                    },
                    success: function (data) {
                       bootbox.alert("Added to cart")
                    },
                    error: function () {
                        bootbox.alert("Unable to update cart!");
                    }
                })
            }
        });
    });
});