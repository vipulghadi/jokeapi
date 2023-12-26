from django.shortcuts import render
from  .models import Jokes
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JokesSerializer

@api_view(["POST"])
def add_joke(request):
    
    data=request.data
    seri=JokesSerializer(data=data)
    if seri.is_valid():
        seri.save()
    else:
        error=seri.errors
        return Response(error) 
    return Response({"status":"successfull"})
    
    

@api_view(["GET"])
def get_joke(request,id):
    try:
        joke=Jokes.objects.get(pk=id)
        seri=JokesSerializer(joke)
        
        return Response(seri.data)
        
    
    except :
        joke=Jokes.objects.all().first()
        seri=JokesSerializer(joke)
      
        return Response(seri.data)