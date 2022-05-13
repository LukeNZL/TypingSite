from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

rooms = [
    {'id': 1, 'name':'Lets learn Python'},
    {'id': 2, 'name': 'Deisgn with me'},
    {'id': 3, 'name': 'front end devs'},

]


def index(request):
    return HttpResponse("Typing Test")
def home(request):
    context={'rooms':rooms}
    return render(request,'polls/home.html',context)
def room(request,pk):
    room=None
    for i in rooms:
        if i['id']==int(pk):
            room = i
    context = {'room':room}
    return render(request,'polls/room.html',context)
