import ujson

from django.http import HttpResponse

from api.ultra_json import UltraJsonResponse


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


def load_json(func):
    def wrapper(request, *args, **kwargs):
        if request.method == "POST":
            try:
                if request.META['CONTENT_TYPE'] != 'application/json':
                    raise ValueError
                request.data = ujson.loads(request.body.decode())
            except ValueError:
                return UltraJsonResponse({'error': 'Cannot process'}, status=400)
        return func(request, *args, **kwargs)

    return wrapper
