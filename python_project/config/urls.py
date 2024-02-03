"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from config.views import index
from auth.views import kakaologin, callback, kakaologout
from blog.views import post, post_create, post_read, post_update, post_delete 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path("auth/kakao/", kakaologin),
    path("auth/kakao/callback/", callback),
    path("auth/kakao/logout/", kakaologout),
    path("posts/", post),
    path("posts/create/", post_create),
    path("posts/read/<int:post_id>/", post_read),
    path("posts/update/<int:post_id>/", post_update),
    path("posts/delete/<int:post_id>/", post_delete),
]

urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)