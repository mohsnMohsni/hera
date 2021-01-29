document.getElementById('search-form').addEventListener(
    "submit", (e) => {
        e.preventDefault();
    }
);

$(document.body).click(function () {
    $('#response-visual').hide("fast");
});

function getSearchValue() {
    let product_value = $('#search-product').val();
    let category_value = $('#search-category').val();
    return {product_value, category_value}
}

function searchPromise() {
    return new Promise((resolve, reject) => {
        const data = getSearchValue();
        $.ajax({
            type: 'POST',
            url: '/search/',
            data: data,
            success: function (response) {
                resolve(response);
            },
            fail: function (error) {
                reject(error);
            },
        });
    });
}

function searchResponse() {
    searchPromise()
        .then((response) => {
            console.log(response);
            searchResponseVisual(response)
        })
        .catch((error) => {
            alert(error)
        })
}

function searchResponseVisual(data) {
    $('#response-visual').show("fast");
    addProductToList(data.products);
    addCategoryToList(data.categories);
}

function addProductToList(products) {
    const productsUl = $('#products-ul');
    productsUl.html("");
    if (products.length !== 0) {
        for (const product of products) {
            productsUl.append(`
            <li> 
                <a href="/shop/product/${product.slug}">
                    ${product.name}
                </a>
                 <p class="text-muted px-2 mx-1">${product.detail.slice(0, 100)}...</p>  
            </li>
        `)
        }
    } else {
        productsUl.append(`
            <li> <p class="h-4 mt-3 text-muted text-center">Not found any product.</p> </li>
        `)
    }
}

function addCategoryToList(categories) {
    const categoriesUl = $('#categories-ul');
    categoriesUl.html("");
    if (categories.length !== 0) {
        for (const category of categories) {
            categoriesUl.append(`
            <li> 
                <a href="/shop/product/${category.slug}">
                    ${category.name}
                </a>
                 <p class="text-muted px-2 mx-1">${category.detail.slice(0, 100)}...</p>  
            </li>
        `)
        }
    } else {
        categoriesUl.append(`
            <li> <p class="h-4 mt-3 text-muted text-center">Not found any category.</p> </li>
        `)
    }
}
