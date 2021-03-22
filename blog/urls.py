from django.urls import path
from .views import blog_detail, create_blog, edit_blog, delete_blog

urlpatterns = [
    path('blog_detail/<int:blog_id>/', blog_detail),
    path('create_blog/', create_blog),
    path('edit/<int:pk>/', edit_blog),
    path('delete_blog/<int:pk>/', delete_blog),
]