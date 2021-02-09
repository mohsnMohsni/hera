let cardPriceSpan = $('.product-price');

function priceRangeFilter() {
    let priceRange = $('#price-range');
    priceRange = priceRange.val().split(',');
    let less = +priceRange[0];
    let more = +priceRange[1];
    for (let i = 0; i < cardPriceSpan.length; i++) {
        let productCard = $(`#product-card${i + 1}`);
        if (less > parseInt(cardPriceSpan[i].innerHTML) || parseInt(cardPriceSpan[i].innerHTML) > more) {
            productCard.hide();
        } else {
            productCard.show()
        }
    }
}

function submitForm() {
    document.getElementById('filter-form').submit();
}
