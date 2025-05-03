from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('home/', views.home_page, name='home'),  
    path('gallery/', views.gallery, name='gallery'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('virtual/', views.empty_view, name='virtual'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('auction/', views.auction, name='auction'),
    path('checkout/', views.checkout, name='checkout'),
    path('about/', views.about, name='about'),
    path('logout/', views.logout_view, name='logout'),
    path('update-cart/', views.update_cart, name='update_cart'),  
]