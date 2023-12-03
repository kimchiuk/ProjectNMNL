from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from .serializers import UpdateUserSerializer
from .models import User
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
@api_view(['PUT'])
def user_update(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'PUT':
        serializer = UpdateUserSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)