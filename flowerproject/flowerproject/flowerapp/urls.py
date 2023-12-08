from .import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='index'),











    # path('',views.home,name='home.html'),
    # path('result/',views.result,name='result.html'),
    # path('result/',views.result,name='result.html'),
    # path('result/',views.result,name='result.html'),
    # path('result/',views.result,name='result.html'),
    # path('about/',views.about,name='about.html'),
    # path('contact/',views.contact,name='contact'),
    # path('details/', views.details, name='details'),
    # path('thanks/', views.thanks, name='thanks.html'),
]
