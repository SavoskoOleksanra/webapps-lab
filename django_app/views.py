from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from .serializers import UserSerializer, GroupSerializer
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url
from .models import Poll, Option, ConnectedUsers
from .serializers import PollSerializer, OptionSerializers
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django_app.tasks import send_email, long_work

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


def index(request):
    polls = [poll for poll in Poll.objects.all()]
    return render(request, 'index.html', {
        'polls': polls
    })


def room(request, poll_id):
    # Send article by id to user
    poll = Poll.objects.get(id=poll_id)
    options = [c for c in Option.objects.filter(poll_id=poll_id)]
    if poll:
        return render(request, 'room.html', {
            'poll_id': poll_id,
            'options': options,
            'poll': poll
        })
    else:
        return HttpResponse('Wrong Article id')


def users_online(request):
    if request.user.is_authenticated:
        connected_users = [user for user in ConnectedUsers.objects.all()]
        return render(request, 'online.html', {
            'connected_users': connected_users
        })


def send_email_task(request):
    email_task_id = send_email.apply_async(queue='email', args=(['savosko2017@gmail.com'],))
    return HttpResponse(f'The jobs for sending email in progress. Wait for finish. Task id {email_task_id}')


def run_long_task(request):
    ml_task_id = long_work.apply_async(queue='long_task', args=(5,))
    return HttpResponse(f'job id are:  {ml_task_id}')


def list_finished_tasks(request):
    return render(request, 'list.html')
