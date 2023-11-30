from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import BlogSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
#throttling
from rest_framework.throttling import UserRateThrottle
from rest_framework.decorators import throttle_classes

# Create your views here.
# def index(request):
#     blogs=Blog.objects.all()
#     data={
#         "data": list(blogs.values())
#     }
#     print(data['data'][0]['id'])
#     print(data['data'][1]['title'])
    
#     return JsonResponse(data)

# def blog(request,pk):
#     blog=Blog.objects.get(pk=pk)
#     data={
#         "title_prabhu": blog.title,
#         "desc": blog.desc,
#         "date": blog.date,
#         "is_published": blog.is_published,
#     }
#     return JsonResponse(data)

##Views for API(Start)
#homepage
@api_view(['GET'])   
def index(request):
    return Response("Cod3d B! Pr3bhu")

#all blogs
@api_view(['GET'])   
def allblogs(request):
    all_blogs = Blog.objects.all()
    serializer=BlogSerializer(all_blogs,many=True)
    return Response(serializer.data)

#create blog
@api_view(['POST'])
def createblog(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
#single blog
@api_view(['GET'])   
def blog(request, pk):
    blog = get_object_or_404(Blog,pk=pk)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)

#update blog
@api_view(['PUT'])
def updateblog(request, pk):
    blog = get_object_or_404(Blog,pk=pk)
    serializer = BlogSerializer(instance=blog,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
#delete blog
@api_view(['DELETE'])
def deleteblog(request, pk):
    blog = get_object_or_404(Blog,pk=pk)
    blog.delete()
    return Response("Blog deleted successfully")

##Views for API(End)

#throttling(allows user can run only 1 times per day)
class OncePerDayUserThrottle(UserRateThrottle):
    rate = '1/day'

@api_view(['GET'])
@throttle_classes([OncePerDayUserThrottle])
def checkin(request):
    return Response({"message": "Hello for today! See you tomorrow!"})