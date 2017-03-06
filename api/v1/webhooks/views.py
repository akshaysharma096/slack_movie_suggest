from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .actions import send_typing
from api.decorators import load_json
from api.ultra_json import UltraJsonResponse
from slack_movie_suggest.settings import FACEBOOK_WEBHOOK_TOKEN


@method_decorator([csrf_exempt, load_json], name='dispatch')
class FacebookView(View):
    http_method_names = ['get', 'post']

    def get(self, request):
        mode, token, challenge = request.GET.get('hub.mode'), request.GET.get('hub.verify_token'), request.GET.get(
            'hub.challenge')
        print(FACEBOOK_WEBHOOK_TOKEN)
        if mode != 'subscribe' or token != FACEBOOK_WEBHOOK_TOKEN:
            return HttpResponse("Forbidden", status=403)
        return HttpResponse(challenge)

    def post(self, request, *args, **kwargs):
        print(request.data)
        user_id = request.data['sender']['id']
        send_typing(user_id)
        return UltraJsonResponse({'success': True}, status=200)
