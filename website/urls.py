
from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from .views import HomePost, ArticleDetailView
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('single-product/', views.product, name="product"),
    path('products/', views.products, name="products"),
    path('about/', views.about, name="about"),
    path('posts/', HomePost.as_view(), name="posts"),
    path('article_detail/<int:pk>',
         ArticleDetailView.as_view(), name="detail_post"),
    path('contact/', views.contact, name="contact"),
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url("favicon.ico"))),
]
