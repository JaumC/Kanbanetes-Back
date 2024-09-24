from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from backend.serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])

def profile(request):
    print('opa')
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def signup(request):
    data = request.data
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    email_confirmation = data.get('emailConfirmation')
    password = data.get('password')
    password_confirmation = data.get('passwordConfirmation')

    if email != email_confirmation:
        return Response({'error': 'E-mails não batem'}, status=status.HTTP_400_BAD_REQUEST)

    if password != password_confirmation:
        return Response({'error': 'Senhas não batem'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data={
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password
    })
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signin(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return Response({'error': 'E-mail e senha são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=email, password=password)

    if user is None:
        return Response({'error': 'E-mail ou senha incorretos'}, status=status.HTTP_400_BAD_REQUEST)

    refresh = RefreshToken.for_user(user)
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }, status=status.HTTP_200_OK)
