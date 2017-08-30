 var cartModule = function() {
    var cart = {};
    var self = this;

    var cartRequest = function(request) {
        if (request.data) {
            $.ajax({
                url: request.url,
                method: request.method,
                dataType: "json",
                data: request.data,
                "beforeSend": function(xhr, settings) {
                    $.ajaxSettings.beforeSend(xhr, settings);
                },
                success: function (data) {
                    if (request.successCallback)
                        request.successCallback(data);
                },
                error: function(data) {
                    if (request.errorCallback)
                        request.errorCallback(data);
                }
            });
        } else {
            $.ajax({
                url: request.url,
                method: request.method,
                dataType: "json",
                "beforeSend": function(xhr, settings) {
                    $.ajaxSettings.beforeSend(xhr, settings);
                },
                success: function (data) {
                    if (request.successCallback)
                        request.successCallback(data)
                },
                error: function(data) {
                    if (request.errorCallback)
                        request.errorCallback(data)
                }
            });
        }
    }

    cart.update_badge_count = function() {
        var request = {
            url: "/cart-item-count",
            method: "GET",
            successCallback: function(data) {
                if (data.item_count !== null)
                    $("#cart-items-badge").html(data.item_count);
            }
        };
        cartRequest(request);
    }

    cart.add_order = function(product_id, quantity) {
        var request = {
            url: "/add-to-cart",
            method: "POST",
            data: {
                bathbomb_id:  product_id,
                quantity: quantity
            },
            successCallback: function(data) {
                bootbox.alert("Added to cart");
                cart.update_badge_count();
            },
            errorCallback: function(data) {
                bootbox.alert("Unable to update cart")
            }
        };
        cartRequest(request);
    }

    cart.update_total_price = function() {
         var total_price = 0;
         $('*[id*=order-price]:visible').each(function() {
               total_price += Number($(this).attr("data-order-price"));
         });
         $("#order-total").html("$" + total_price);
    }

    cart.remove_order = function(order_id) {
        var request = {
            url: "/remove-from-cart",
            method: "POST",
            data: {
                order_id:  order_id
            },
            successCallback: function(data) {
                 $("#order-row-" + order_id).remove();
                 cart.update_badge_count();
                 cart.update_total_price();
            },
            errorCallback: function(data) {
                bootbox.alert("Unable to update cart")
            }
        };
        cartRequest(request);
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
                cart.add_order($(self).attr("data-bathbomb-id"), quantity);
            }
        });
    });

    $(document).on('click', "#cart-item-delete-btn", function() {
        var self = this;
        bootbox.confirm("Are you sure you want to remove this item?", function(confirmed) {
            if (!confirmed)
                return;
            cart.remove_order($(self).attr("data-order-id"));
        });
    });
});