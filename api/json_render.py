from django.http import JsonResponse


def JsonData(data, status):
    response = {
        'attachments': [{
            
        }]
    }
    if status == 200:
        response["text"] = 'Your movie yay!'
        response["attachments"]
    else:
        response["text"] = None
    print(response)
    return JsonResponse(data=data, status=status)
