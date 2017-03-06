import ujson

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from api.http_codes import http_codes
from api.json_render import json_for_random_movie
from api.ultra_json import UltraJsonResponse
from request_api.popcorn_time import popcorn_time
from slack_movie_suggest.settings import RANDOM_MOVIE


@csrf_exempt
@require_POST
def get_movie(request, format=None):
    r = popcorn_time.get_request(RANDOM_MOVIE)
    if r:
        json_response = json_for_random_movie(ujson.loads(r.text))
        return UltraJsonResponse(json_response)
    else:
        return UltraJsonResponse({'error': 'Service unavailable'}, status=503)


@require_GET
def root(request, format=None):
    return UltraJsonResponse({'message': http_codes[200], 'status': 200}, status=200)


