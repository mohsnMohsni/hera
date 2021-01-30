function getPk(n) {
    let strId = $(`#id-list${n}`);
    let arr = JSON.parse(strId.val());
    let item = arr.pop();
    deleteItem(item);
    getCartProductCount();
    if (arr.length > 0) {
        let quantity = $(`#item-quantity${n}`);
        quantity.html('');
        quantity.html(`
            <strong>Quantity</strong>
            ${arr.length}
        `);
        strId.val(JSON.stringify(arr));
    } else {
        $(`#item-container${n}`).hide();
    }

}

function deleteItem(pk) {
    $.ajax({
        type: 'POST',
        url: '/order/delete_item/',
        data: {pk},
    })
}