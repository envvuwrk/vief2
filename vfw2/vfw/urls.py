from django.contrib import admin
from django.urls.resolvers import URLPattern
from django.urls import path
from.import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('sponsors/',views.sponsors,name="sponsors"),
    path('designers/',views.designers,name="designers"),
    
    path('register/',views.register,name="register"),
    path('designer/',views.designer,name="designer"),
    path('categoryd/',views.categoryd,name="categoryd"),
    path('passport/',views.passport,name="passport"), 
    path('submit/',views.submit,name="submit"),
    
    path('model/',views.model,name="model"),
    path('measurement/',views.measurement,name="measurement"),
    path('mp/',views.mp,name="mp"),
    path('msubmit/',views.msubmit,name="msubmit"),
    
    path('exhibitor/',views.exhibitor,name="exhibitor"),
    path('excat/',views.excat,name="excat"),
    path('expayment/',views.expayment,name="expayment"),
    path('expassport/',views.expassport,name="expassport"),
    path('exsubmit/',views.exsubmit,name="exsubmit"),
   
    path('contact/',views.contact,name="contact"),
    path('gallery/',views.gallery,name="gallery"),
    path('seven/',views.seven,name="seven"),
    path('nine/',views.nine,name="nine")
]