from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers



router = routers.DefaultRouter()

router.register("movies", views.MovieListCreateAPIView)

product_router = routers.NestedDefaultRouter(router, "movies", lookup="movies")



urlpatterns = [
    path("", include(router.urls)),
    path("", include(product_router.urls)),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),]
