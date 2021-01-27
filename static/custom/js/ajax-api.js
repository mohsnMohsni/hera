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
            url: "/shop/add_comment/",
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
    listInline.append(`
                        <div class="media">
                            <img src="${response.author.avatar}" alt="avatar"
                                 style="height: 70px !important; width: 70px !important;">
                            <div class="media-body">
                            <div class="ratings">
                                <ul class="list-inline" id="list-inline">
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
            url: "/shop/like_product/",
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
        likeProduct.innerHTML = '<i class="fa fa-heart"></i>';
    } else if (status === 'False') {
        likeProduct.innerHTML = '<i class="fa fa-heart alt-color"></i>';
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
