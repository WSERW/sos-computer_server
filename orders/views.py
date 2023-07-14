from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrderSerializer
import json

from .models import Order
from .telegramm import send_message


def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})


@csrf_protect
@api_view(['POST'])
def post_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        order = serializer.save()
        data = serializer.validated_data
        mailText = f'Имя:{data["name"]} \nТелефон:{data["phone"]} \nСообщение:{data["message"]}'
        try:
            send_message(f'Новая заявка c сайта №{order.id}:\n{mailText}')
            pass
        except Exception as e:
            with open("Error.txt", "w") as file:
                file.write(str(e))

        return Response({'message': 'Заявка успешно отправлена', 'order': order.id})
    else:
        return Response(serializer.errors, status=400)
