from django.urls import path
from .views import welcome, login_view, registration_view, logout_view, ImageCollectionPage

urlpatterns = [
    path('welcome/', welcome, name='welcome'),
    path('login/', login_view, name='login'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
]