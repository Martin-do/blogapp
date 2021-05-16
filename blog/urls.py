from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home"),
    
    path("post/<int:id>/", views.post_detail, name="post_detail"),
    path("create/", views.create_post, name="post_create"),
    path("post/<id>/edit/", views.post_edit, name="post_edit"),
    path("post/<int:id>/delete/", views.post_delete, name="post_delete"),
    path('accounts/profile/', views.home, name='home'),
    

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
