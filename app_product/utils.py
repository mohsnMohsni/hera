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
