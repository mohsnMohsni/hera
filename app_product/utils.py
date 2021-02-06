def filter_product(filter_value, products_list):
    """
    Check filter Value and then filter by key in filter value.
    """
    if filter_value == 'top_rated':
        products_list = sorted(
            products_list, key=lambda a: a.rate_avg, reverse=True)
    elif filter_value == 'lowest_price':
        products_list = products_list.order_by('shop_product__price')
    elif filter_value == 'highest_price':
        products_list = products_list.order_by('-shop_product__price')
    return products_list


def add_product_meta(dic, product):
    """
    Add meta field for product. Get a dic from view
    and for label and value make an extra field for product.
    """
    extra_items = ['price', 'name', 'slug', 'category',
                   'brand', 'quantity', 'detail', 'csrfmiddlewaretoken']
    extra_items += ('image',) if 'image' in dic.keys() else []
    [dic.pop(key) for key in extra_items]
    i = 0
    label, value = '', ''
    for k, v in dic.items():
        i += 1
        if i % 2 != 0:
            label = v
        else:
            value = v
            if value != '':
                product.meta_field.create(label=label, value=value)
    return


def update_product_meta(dic, product):
    """
    Update meta field for product. Get a dic from view
    and for label and value, update an extra field for product.
    """
    extra_items = ['price', 'name', 'slug', 'category',
                   'brand', 'quantity', 'detail', 'csrfmiddlewaretoken']
    extra_items += ('image',) if 'image' in dic.keys() else []
    copy_dic = dic.copy()
    [dic.pop(key) for key in extra_items]
    i = 0
    label, value = '', ''
    for k, v in dic.items():
        i += 1
        if i % 2 != 0:
            label = v
        else:
            value = v
            product_meta_field = product.first().meta_field.filter(label=label)
            if value == '' and product_meta_field.exists():
                product.delete()
            elif not product_meta_field.exists():
                copy_dic[label] = value
                add_product_meta(copy_dic, product.first())
            else:
                product_meta_field.update(value=value)
    return


def add_product_gallery(dic, gallery, product):
    """
    Get 3 parameter's and for value in dic create an gallery
    """
    for key, value in dic.items():
        gallery.objects.create(product=product, image=value)
    return
