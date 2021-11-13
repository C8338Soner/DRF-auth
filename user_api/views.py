from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token

# Create your views here.

@api_view(['POST'])

def registration_view(request):
 if request.method == 'POST':
  serializer = RegistrationSerializer(data = request.data)
  data = {}
  if serializer.is_valid():
   account = serializer.save()
   