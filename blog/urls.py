from django.urls import path
from .views import blog, blog_detail
from django.conf.urls.static import static
app_name = 'blog'

urlpatterns = [
    path('', blog, name='blog'),
    path('<int:post_id>', blog_detail, name='blog_detail'),    
]