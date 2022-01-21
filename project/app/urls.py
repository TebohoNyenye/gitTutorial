from app import views
from django.contrib.auth import views as auth_views
from django.urls import path
urlpatterns = [

path('',views.HomeView.as_view(), name="home"),
path('about/',views.AboutView.as_view(),name="about"),
path('products/',views.ProductView,name="products"),
path('contact/',views.ContactView.as_view(),name="contact"),
path('login/',views.LoginView.as_view(),name="login"),
path('register/',views.RegisterView.as_view(),name="register"),
path('cart/',views.CartView,name="cart"),
path('checkout/', views.checkout, name="checkout"),
path('update_item/', views.updateItem, name="update_item"),
path('process_order/', views.processOrder, name="process_order"),
path('change_password/', views.ChangePasswordView.as_view(), name="change_password"),
path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
path('accounts/profile/', views.ProfileView, name="profile"),



]