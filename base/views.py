from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
# Create your views here.

def home(request):
    rooms=Room.objects.all()
    contex={'rooms':rooms}

    return render(request,'base/home.html',contex)

def room(request,pk):
    room=Room.objects.get(id=pk)
    contex={'room':room}
    return render(request,'base/room.html',contex)

def createRoom(request):
    form=RoomForm()
    context={'form':form}
    return render(request,'base/room_form.html',context)