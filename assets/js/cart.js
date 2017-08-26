 var cartModule = function() {
    var cart = {};

    cart.get_current_item_count = function(callback) {
        var item_count = 0;
        $.ajax({
            url: "/cart-item-count",
            method: "GET",
            dataType: "json",
            "beforeSend": function(xhr, settings) {
                $.ajaxSettings.beforeSend(xhr, settings);
            },
            success: function (data) {
              if (data.item_count)
                item_count = data.item_count
              callback(item_count)
            }
        })
    }
    return cart;
}

$(document).ready(function() {
    var cart = cartModule();

    cart.get_current_item_count(function(item_count) {
         $("#cart-items-badge").html(item_count);
    });

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