from app import views
from django.urls import path
urlpatterns = [

path('',views.HomeView.as_view(), name="home"),
path('about/',views.AboutView.as_view(),name="about"),
path('products/',views.ProductView,name="products"),
path('contact/',views.ContactView.as_view(),name="contact"),
path('login/',views.LoginView.as_view(),name="login"),
path('register/',views.RegisterView.as_view(),name="register"),
path('cart/',views.CartView.as_view(),name="cart"),


]