 var cartModule = function() {
    var cart = {};

    cart.update_badge_count = function() {
        $.ajax({
            url: "/cart-item-count",
            method: "GET",
            dataType: "json",
            "beforeSend": function(xhr, settings) {
                $.ajaxSettings.beforeSend(xhr, settings);
            },
            success: function (data) {
              if (data.item_count !== null)
                $("#cart-items-badge").html(data.item_count)
            }
        })
    }
    return cart;
}

$(document).ready(function() {
    var cart = cartModule();

    cart.update_badge_count();

    $(document).on('click', "#add-to-cart", function(e) {
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
                       bootbox.alert("Added to cart");
                       cart.update_badge_count();

                    },
                    error: function () {
                        bootbox.alert("Unable to update cart!");
                    }
                })
            }
        });
    });

    $(document).on('click', "#cart-item-delete-btn", function() {
        var self = this;
        bootbox.confirm("Are you sure you want to remove this item?", function(confirmed) {
            if (!confirmed)
                return;
            $.ajax({
                url: "/remove-from-cart",
                method: "POST",
                "dataType": "json",
                data: {
                    order_id : $(self).attr("data-order-id")
                },
                "beforeSend": function(xhr, settings) {
                    $.ajaxSettings.beforeSend(xhr, settings);
                },
                success: function(data) {
                    $("#order-row-" + $(self).attr("data-order-id")).remove();
                    cart.update_badge_count();
                }
            })
        });
    });
});