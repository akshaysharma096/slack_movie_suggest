import ujson

from django.http import HttpResponse

from api.http_codes import http_codes


def view_404(request):
    response = {
        'status': 404,
        'message': http_codes[404],
    }
    return HttpResponse(ujson.dumps(response), content_type='application/json', status=404)
