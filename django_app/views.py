from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from .serializers import UserSerializer, GroupSerializer
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url
from .models import Poll, Option
from .serializers import PollSerializer, OptionSerializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PollSerializer


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = OptionSerializers
