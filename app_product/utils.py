def filter_product(filter_value, products_list):
    """
    Check filter Value and then filter by key in filter value.
    """
    if filter_value == 'top_rated':
        products_list = sorted(products_list, key=lambda a: a.rate_avg, reverse=True)
    elif filter_value == 'lowest_price':
        products_list = products_list.order_by('shop_product__price')
    elif filter_value == 'highest_price':
        products_list = products_list.order_by('-shop_product__price')
    return products_list


def add_product_meta(dic, product):
    extra_items = ['price', 'name', 'slug', 'category', 'brand', 'quantity', 'detail', 'csrfmiddlewaretoken']
    extra_items += ('image',) if 'image' in dic.keys() else []
    [dic.pop(key) for key in extra_items]
    i = 0
    label, value = '', ''
    print(list(dic.items()))
    for k, v in dic.items():
        i += 1
        if i % 2 != 0:
            label = v
        else:
            value = v
            product.meta_field.create(label=label, value=value)
    return
