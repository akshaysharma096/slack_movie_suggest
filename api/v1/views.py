import ujson

from api.json_render import json_for_random_movie
from api.ultra_json import UltraJsonResponse
from popcorntime_slack.settings import RANDOM_MOVIE
from request_api.popcorn_time import popcorn_time


def get_movie(request):
    r = popcorn_time.get_request(RANDOM_MOVIE)
    if r:
        json_response = json_for_random_movie(ujson.loads(r.text))
        return UltraJsonResponse(json_response)
    else:
        return UltraJsonResponse({'error': 'Service unavailable'}, status=503)
