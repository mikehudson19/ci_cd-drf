from django.urls import path, include
from api import views


urlpatterns = [
    path('health/', views.HealthApiView.as_view(), name='health')
]