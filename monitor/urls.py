
from django.urls import path
from . import views

app_name = "monitor"

urlpatterns = [
    path('', views.index, name="index"),
    path('noti/', views.notification, name='noti'),
    path('plant/<int:plant>', views.plant, name='plant'),
    path('plant/<int:plant>/loc/<int:loc>', views.loc, name='loc'),
    path('visualization/', views.visualization, name='visualization'),
    path('email/<int:plant>',views.sendMail, name='sendmail'),
]
