from rest_framework.routers import DefaultRouter
from django.urls import path, include
from  .views import  UserRegistrationApiView,UserLoginApiView,activate,UserLogoutView
router = DefaultRouter() # amader router
from .import views
router.register('list', views.CustomerViewset) # router er antena
urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationApiView.as_view(), name='register'),
    path('login/', UserLoginApiView.as_view(), name='login'),
    path('logout/', UserLoginApiView.as_view(), name='logout'),
    path('active/<uid64>/<token>/', views.activate, name = 'activate'),
   
]

