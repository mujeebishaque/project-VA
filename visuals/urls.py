from django.urls import path
from visuals import views

urlpatterns = [
    path('/index/', views.IndexView.as_view(), name='index'),
]
