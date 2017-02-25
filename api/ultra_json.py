import ujson

from django.http import HttpResponse


def UltraJsonResponse(data, status=None):
    status_code = status if status else 200
    data = ujson.dumps(data, ensure_ascii=False, escape_forward_slashes=False, indent=4)
    return HttpResponse(data, content_type='application/json; charset=utf-8', status=status_code)
