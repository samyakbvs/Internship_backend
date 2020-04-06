from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from lms import views

urlpatterns = [
    path('',views.post_list.as_view(),name="home"),
    path('videos/',views.videos_post_list.as_view(),name="videos"),
    path('images/',views.images_post_list.as_view(),name="images"),
    path('docs/',views.docs_post_list.as_view(),name="docs"),
    path('<int:postId>/',views.post_detail.as_view(),name="detail"),
    # path('create/',views.CreatePost.as_view(),name="create"),
    path('<slug:postQuery>/',views.search_posts.as_view(),name="create"),

]
