function getCartProductCount() {
    $.ajax({
        type: 'GET',
        url: '/cart/',
        success: function (response) {
            addNumberToCartIcon(response.product_count)
        }
    })
}

function addNumberToCartIcon(num) {
    $('#cart-icon').html('');
    $('#cart-icon').append(`
        <span class="badge badge-primary badge-style">
            ${num}
        </span>
    `);
}

getCartProductCount();
