from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer,UserProfileSerializer,ProfileFeedItemSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from . import models
from .import permissions
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


# viewset api development

class HelloViewSet(viewsets.ViewSet):

    serializer_class=HelloSerializer

    def list(self,request):
        a_viewset=[
            'hello commons',
            'hello humans',
            'helllo u r cute'
        ]
        return Response({'message':'helllo','a_viewset':a_viewset})

    def create(self,request):
        serializer=HelloSerializer(data=request.data)

        if serializer.is_valid():
            name=serializer.data.get('name')
            message='hello{0}'.format(name)
            return Response({'message':message})

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})
    
    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})
    
    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})



class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class=UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)


class LoginViewSet(viewsets.ViewSet):
    '''checks user name and email and return auth token'''
    serializer_class=AuthTokenSerializer
    def create(self,request):
        '''use to obtainauthtoken apiview to validate and create token'''
        return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    '''handles updating,creating,readingprofile feed item'''
    authentication_classes=(TokenAuthentication,)
    serializer_class=ProfileFeedItemSerializer
    queryset=models.ProfileFeedItem.objects.all()
    permission_classes=(permissions.PostOwnStatus,IsAuthenticated)

    def perform_create(self,serializer):
        '''sets the user profile to the logged in user'''
        serializer.save(user_profile=self.request.user)
