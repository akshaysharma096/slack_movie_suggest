import ujson

from django.http import HttpResponse


def accept_json(func):
    def wrapper(request, *args, **kwargs):
        header = request.META.get('HTTP_ACCEPT', None)
        if not header or header != 'application/vnd.api+json':
            response = {
                'error': 'Request not acceptible'
            }
            return HttpResponse(ujson.dumps(response), content_type='application/vnd.api+json', status=405)
        return func(request, *args, **kwargs)

    return wrapper
