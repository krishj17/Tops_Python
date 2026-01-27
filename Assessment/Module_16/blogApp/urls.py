from django.urls import path
from blogApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_page),
    path('dashboard', dashboard_page, name="dashboard"),
    path('blogs', blogs_page, name="blogs"),
    path('blog/<slug:slug>', blog_page, name="blog"),
    path('register', register_page, name="register"),
    path('login', login_page, name="login"),

    path('posts', get_posts, name="get-posts"),
    path('post/add', add_post, name="add-post"),
    path('post/update', update_post, name="update-post"),
    path('post/delete', delete_post, name="delete-post"),

    path('post/like', like_post, name="like-post"),
    path('post/comment', post_comment, name="post-comment"),

    path("user/register", register_user, name="register-user"),
    path("user/login", login_user, name="login-user"),
    path("user/logout", logout_user, name="logout-user"),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)