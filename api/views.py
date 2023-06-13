from django.shortcuts import render
from . models import mahasiswaModels
from . serializers import mahasiswaSerializer

# rest framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def readMahasiswa(request):
    mahasiswa = mahasiswaModels.objects.all()
    serializer = mahasiswaSerializer(mahasiswa, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detailMahasiswa(request,id):
    mahasiswa = mahasiswaModels.objects.get(pk=id) 
    serializer = mahasiswaSerializer(mahasiswa, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createMahasiswa(request):
    serializer = mahasiswaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deletemahasiswa(request, id):
    mahasiswa = mahasiswaModels.objects.get(pk=id)
    mahasiswaModels.delete()

    
    return Response('we kampret datamu iki kehapus', status=204)

