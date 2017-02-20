from api.json_render import JsonData
from popcorntime_slack.settings import RANDOM_MOVIE
from request_api.popcorn_time import popcorn_time


def get_movie(request):
    r = popcorn_time.get_request(RANDOM_MOVIE)
    if r:
        json_response = r.json()
        return JsonData(json_response, 200)
    else:
        return JsonData('Service unavailable', 503)

