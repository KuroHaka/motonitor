from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

class PredictorView(APIView):

  def post(self, request):
    print(request.data)
    return Response('pepe', status=status.HTTP_200_OK)
