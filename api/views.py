from api.serializers import CalcSerializer
from django.shortcuts import render

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .models import Calc
import random

# Create your views here.
@api_view(['GET'])
def HelloAPI(request):
    return Response("Hello World!")

@api_view(['GET'])
def randomAPI(request, id):
    totalCalcs = Calc.objects.all()
    randomCalcs = random.sample(list(totalCalcs), id)
    serializer = CalcSerializer(randomCalcs, many=True)
    return Response(serializer.data)
