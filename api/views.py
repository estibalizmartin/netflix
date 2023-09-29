from django.shortcuts import render
from .models import Usuario
from rest_framework import generics
# from .serializers import CustomerSerializer

class NetflixAPI(APIView):

    def get(self, request):
        items = [
            "apple",
            "mango",
            "grapes"
        ]
        response_data = {"datas": items}
        return Response(response_data, status=status.HTTP_200_OK)

class UsuarioList(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = CustomerSerializer
