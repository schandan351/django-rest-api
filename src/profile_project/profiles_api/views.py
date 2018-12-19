from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer
# Create your views here.


class HelloApiView(APIView):

    serialize_class=HelloSerializer
    def get(self,request,format=None):
        an_apiview=[
            'uses https method  as a function',
            'helloocdsnj',
            'fukcing awesome',
            'lauda ',
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})


    def post(self,request):
        serializer=HelloSerializer(data=request.data)

        if serializer.is_valid():
            name=serializer.data.get('name')
            message='hello{0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk=None):
        return Response({'method':'put'})

    def patch(self,request,pk=None):
        return Response({'method':'patch'})
    
    def delete(self,request,pk=None):
        return Response({'method':'delete'})