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

    cart.updateBadgeCount = function() {
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

    cart.addOrder = function(product_id, quantity) {
        var request = {
            url: "/add-to-cart",
            method: "POST",
            data: {
                bathbomb_id:  product_id,
                quantity: quantity
            },
            successCallback: function(data) {
                cart.updateBadgeCount();
            },
            errorCallback: function(data) {
                bootbox.alert("Unable to update cart")
            }
        };
        cartRequest(request);
    }

    cart.updateTotalPrice = function() {
         var total_price = 0;
         $('.order-subtotal').each(function() {
               total_price += Number($(this).text());
         });
         $("#order-total").text(total_price);
    }

    cart.removeOrder = function(order_id) {
        var request = {
            url: "/remove-from-cart",
            method: "POST",
            data: {
                order_id:  order_id
            },
            successCallback: function(data) {
                 $("#order-row-" + order_id).remove();
                 cart.updateBadgeCount();
                 cart.updateTotalPrice();
            },
            errorCallback: function(data) {
                bootbox.alert("Unable to update cart")
            }
        };
        cartRequest(request);
    }

    cart.updateOrder = function(orderId, quantity) {
        var request = {
            url: "/update-order",
            method: "POST",
            data: {
                order_id:  orderId,
                quantity: quantity
            },
            successCallback: function(data) {
                var subtotal = Number(data.quantity) * Number(data.price)
                var subtotalSpan = $('#order-row-' + orderId).find('.order-subtotal');
                subtotalSpan.text(subtotal);
                cart.updateTotalPrice();
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

    cart.updateBadgeCount();

    $(document).on('click', "#add-to-cart", function(e) {
        var self = this;
        bootbox.prompt({
            title: "Enter quantity",
            inputType: 'number',
            callback: function (quantity) {
                if (!quantity)
                    return
                cart.addOrder($(self).attr("data-bathbomb-id"), quantity);
            }
        });
    });

    $(document).on('click', '#cart-item-update-btn', function() {
        var orderId = $(this).attr('data-order-id');
        var quantityRow = $('#order-' + orderId + '-quantity');
        if (Number(quantityRow.val()) <= 0) {
            bootbox.alert("Quantity must be 1 or greater");
            return;
        }
        cart.updateOrder(orderId, quantityRow.val());
    });

    $(document).on('click', "#cart-item-delete-btn", function() {
        var self = this;
        bootbox.confirm("Are you sure you want to remove this item?", function(confirmed) {
            if (!confirmed)
                return;
            cart.removeOrder($(self).attr("data-order-id"));
        });
    });
    
    $(document).on('click', '#login-signup-prompt', function() {
        bootbox.alert('Please <a href="/accounts/login">Login</a> or <a href="/accounts/register">Sign up</a> to start shopping!');
    });
});