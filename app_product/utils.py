from django.db.models.query import QuerySet


def make_flat_list(query_list, output):
    for i in query_list:
        if type(i) == list or type(i) == QuerySet:
            make_flat_list(i, output)
        else:
            output.append(i)
