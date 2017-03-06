from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from slack_movie_suggest.settings import FACEBOOK_WEBHOOK_TOKEN


@method_decorator(csrf_exempt, name='dispatch')
class FacebookView(View):
    def get(self, request):
        mode, token, challenge = request.GET.get('hub.mode'), request.GET.get('hub.verify_token'), request.GET.get(
            'hub.challenge')
        print(FACEBOOK_WEBHOOK_TOKEN)
        if mode != 'subscribe' or token != FACEBOOK_WEBHOOK_TOKEN:
            return HttpResponse("Forbidden", status=403)
        return HttpResponse(challenge)

    # def post(self, request):
    #     return HttpResponse("Hello")
