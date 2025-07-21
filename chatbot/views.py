from django.http import JsonResponse
from .chatbot_data import get_bot_reply
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")

            # Get bot response
            response = get_bot_reply(user_message)

            return JsonResponse({
                "bot_response": response
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST requests allowed"}, status=405)
