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
                        console.log(data);
                        var cart = Cookies.get('cart')
                        var current_orders = []
                        if (cart) {
                            current_orders = JSON.parse(cart.orders)
                        }

                        var new_orders = []
                        new_orders.push(data.order_id)
                        all_orders = new_orders.concat(current_orders)
                        Cookies.set({cart : JSON.stringify(all_orders)})
                    },
                    error: function () {
                        bootbox.alert("Unable to update cart!");
                    }
                })
            }
        });
    });
});