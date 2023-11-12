from django.http import JsonResponse
from rest_framework import generics
from .serializers import *

class PerevalAddAPI(generics.CreateAPIView):
    """Класс работы с БД для первого спринта"""
    queryset = PerevalAdd.objects.all()
    serializer_class = PerevalAddSerializer

    def post(self, request):
        """
        Переопределение метода POST
        """
        pereval = PerevalAddSerializer(data=request.data)
        try:
            if pereval.is_valid(raise_exception=True):
                pereval.save()
                data = {'status': '200', 'message': 'null', 'id': f'{pereval.instance.id}'}
                return JsonResponse(data, status=200, safe=False)

        except Exception as exc:
            responseData = {'status': '400', 'message': f'Bad Request: {exc}', 'id': 'null'}
            return JsonResponse(responseData, status=400, safe=False)

