from django.shortcuts import render, get_object_or_404
#start workign with django rest
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Note
from api.serializers import NoteSerializer
# Create your views here. REST FULL API
from rest_framework import generics



@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True) #serializer multiple object
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):

    note = get_object_or_404(Note, pk=pk)

    if request.method == 'GET':
        serializer = NoteSerializer(note, many=False) #serializer one single object 
        return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    '''CREATE NOTES'''
    if request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateNote(request, pk):
    '''UPDATE NOTES'''
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'PUT':
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['DELETE'])
def deleteNote(request, pk):
    '''DELETE NOTES'''
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer 