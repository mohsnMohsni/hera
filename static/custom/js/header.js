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

function addShopHeader(res) {
    let shopHeader = $('#header-shops');
    shopHeader.html('');
    for (let shop of res.shops) {
        shopHeader.append(`
            <a class="dropdown-item dropdown-item-header" href="/fa/shop/${shop.slug}">${shop.name}</a>
        `)
    }
}

function addCategoriesHeader(res) {
    let categoryHeader = $('#header-categories');
    categoryHeader.html('');
    for (let category of res.categories) {
        categoryHeader.append(`
            <a class="dropdown-item dropdown-item-header" href="/fa/shop/category/${category.slug}">${category.name}</a>
        `)
    }
}

function headerCategoryMenu() {
    $.ajax({
        type: 'GET',
        url: '/en/header-menu/category',
        success: function (response) {
            addCategoriesHeader(response);
        }
    })
}

function headerShopMenu() {
    $.ajax({
        type: 'GET',
        url: '/en/header-menu/shop',
        success: function (response) {
            addShopHeader(response);
        }
    })
}

headerCategoryMenu();
headerShopMenu();
