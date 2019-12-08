from django.urls import path
from . import views

urlpatterns = [
    path('',views.first,name='first'),
    path('home/',views.index,name='home'),
    path('add/',views.add,name='add'),
    path('signup/',views.Signup.as_view(),name='signup'),
    path('new/<int:pk>',views.diaryview,name='diaryview'),
    path('edit/<int:pk>',views.updatediary,name='update'),
    path('delete/<int:pk>',views.deletediary,name='delete')
]
