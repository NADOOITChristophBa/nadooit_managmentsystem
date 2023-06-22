from bot_management.plattforms.whatsapp.utils import get_message_for_request
from bot_management.plattforms.whatsapp.utils import register_bot_route
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@register_bot_route("3cfa80bb-f3c1-49ff-bf1d-2f51f5f22138")
@csrf_exempt
def handle_message(request, *args, token=None, **kwargs):
    print(request)
    print("AND HERE")
    # HTTPS 200 OK response required
    # If get request, return challenge
    if request.method == "GET":
        return HttpResponse(request.GET.get("hub.challenge"))

    # If post request, handle message
    elif request.method == "POST":
        message = get_message_for_request(request)
        print(message)

    return HttpResponse(status=200)
