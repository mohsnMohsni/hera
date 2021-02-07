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


def update_product_meta(meta_label_obj, value):
    """
    Update meta field for product. Get a obj from add_product_meta function
    and update or create value for this object.
    """
    if value == ['']:
        return
    value_id_list = list(meta_label_obj.value.all().values_list('id', flat=True))
    for _ in value:
        if len(value_id_list):
            meta_label_obj.value.filter(id=value_id_list.pop()).update(value=_)
        else:
            meta_label_obj.value.create(value=_)
    return


def add_product_meta(dic, product):
    """
    Add meta field for product. Get a dic from view
    and for label and value make an extra field for product.
    """
    dic.pop('csrfmiddlewaretoken')
    i = 0
    label, value, meta_label, exists_status = '', '', '', ''
    for k, v in dic.items():
        i += 1
        if i % 2 != 0:
            label = v
            exists_status = product.meta_field.filter(label=label).exists()
            if not exists_status:
                meta_label = product.meta_field.create(label=label)
        else:
            value = dic.getlist(k)
            if value == [''] and exists_status:
                meta_label_obj = product.meta_field.filter(label=label)
                meta_label_obj.delete()
            elif not exists_status:
                for _ in value:
                    meta_label.value.create(value=_)
            else:
                meta_label_obj = product.meta_field.filter(label=label).first()
                update_product_meta(meta_label_obj, value)
    return


def add_product_gallery(dic, gallery, product):
    """
    Get 3 parameter's and for value in dic create an gallery
    """
    for key, value in dic.items():
        gallery.objects.create(product=product, image=value)
    return
