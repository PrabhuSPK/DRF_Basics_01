from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('allblogs',views.allblogs,name='allblogs'),
    path('createblog',views.createblog,name='createblog'),
    path('blog/<int:pk>',views.blog,name='blog'),
    path('checkin',views.checkin,name='checkin'),
    path('updateblog/<int:pk>',views.updateblog,name='updateblog'),
    path('deleteblog/<int:pk>',views.deleteblog,name='deleteblog'),

    
    



    
]