from django.urls import path
from . import views

urlpatterns = [
     path('', views.store, name='store'),
     path('categories/<slug:category_slug>/', views.store, name='products_by_category'),
     path('categories/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
     path('search/', views.search, name='search'),
#     path('profile/', views.profile, name='profile'),
#     path('newsltter/', views.createNewsletter, name='newsletter'),
#     path('send-newsltter/', views.sendNewsletter, name='send-newsletter'),
#     path('forget-password/', views.forgetPassword, name='forget-password'),
#     path('forget-password/code/<str:ref>/', views.code, name='code'),
#     path('new-password/<str:ref>/', views.newPassword, name='new-password'),
]