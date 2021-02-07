document.getElementById('add-to-cart').addEventListener(
    "click", function (e) {
        e.preventDefault();
    });

function setValNull() {
    $("#review").val('');
}

function getCommentValue() {
    const productId = $('#product-slug').val();
    const userId = $('#user-id').val();
    const review = $('#review').val();
    const starrr = $('.starrr')[0];
    const star = starrr.getElementsByClassName('fa-star').length;
    return JSON.stringify({product: productId, user: userId, text: review, rate: star});
}

function sendCommentPromise() {
    return new Promise((resolve, reject) => {
        let data = getCommentValue()
        $.ajax({
            type: "POST",
            url: "/en/shop/api/add_comment/",
            data: data,
            success: function (response) {
                resolve(response);
            },
            fail: function (err) {
                reject(err);
            },
        });
    });
}

function makeStarforRate(rate) {
    let ulList = '';
    for (let i = 0; i < +rate; i++) {
        ulList += '<li class="list-inline-item"><i class="fa fa-star"></i></li>'
    }
    for (let i = 5; i > +rate; i--) {
        ulList += '<li class="list-inline-item"><i class="fa fa-star-o"></i></li>'
    }
    return ulList
}

function addComment(response) {
    let listInline = $('#list-inline');
    $('#no-comments').hide();
    listInline.append(`
                        <div class="media">
                            <img src="${response.author.avatar}" alt="avatar"
                                 style="height: 70px !important; width: 70px !important;" class="mx-3">
                            <div class="media-body">
                            <div class="ratings">
                                <ul class="list-inline my-1" dir="ltr">
                                    ${makeStarforRate(response.rate)}
                                </ul>
                            </div>
                            <div class="name">
                                <h5 style="text-transform: capitalize"> ${response.author.full_name} </h5>
                            </div>
                            <div class="date">
                                <p> ${response.create_at} </p>
                            </div>
                            <div class="review-comment">
                                <p> ${response.text} </p>
                            </div>
                        </div>
                    </div>
            `)
}

function sendCommentResponse() {
    sendCommentPromise()
        .then((response) => {
            addComment(response);
            setValNull();
        }).catch((error) => {
        alert(error)
    })
}

function getLikeValue() {
    const productId = $('#product-slug').val();
    const userId = $('#user-id').val();
    return JSON.stringify({product: productId, user: userId});
}

function sendLikePromise() {
    return new Promise((resolve, reject) => {
        let data = getLikeValue()
        $.ajax({
            type: "POST",
            url: "/en/shop/api/like_product/",
            data: data,
            success: function (response) {
                resolve(response);
            },
            fail: function (err) {
                reject(err);
            },
        });
    });
}

function setLikeValue(status) {
    let likeProduct = document.getElementById('like-product');
    likeProduct.innerHTML = "";
    if (status === 'True') {
        likeProduct.innerHTML = '<i class="fa fa-bookmark"></i>';
    } else if (status === 'False') {
        likeProduct.innerHTML = '<i class="fa fa-bookmark-o alt-color"></i>';
    }
}

function sendLikeResponse() {
    sendLikePromise()
        .then((response) => {
            setLikeValue(response);
        }).catch((error) => {
        alert(error)
    })
}

function addCartMeta(id) {
    let label = $('#select-label').text();
    let value = $('#select-choice').val();
    $.ajax({
        type: 'POST',
        url: '/en/order/cart_meta/',
        data: {id: id, label: label, value: value},
        fail: function (err) {
            console.log(err);
        }
    })
}

function addToCartAjax() {
    let id = $('#shopProduct-id').val();
    addCartMeta(id);
    $.ajax({
        type: 'POST',
        url: '/en/cart/',
        data: {id},
        success: function (response) {
            getCartProductCount();
        },
    })
}

setValNull();