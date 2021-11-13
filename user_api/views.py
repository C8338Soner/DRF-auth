from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
# Create your views here.
@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
         password = serializer.validated_data.get('password')
         serializer.validated_data['password'] = make_password(password)         
         serializer.save()        
         data = serializer.data
        else:
            data = serializer.errors
        return Response(data)