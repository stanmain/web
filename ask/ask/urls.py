"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from qa.urls import urlpatterns as qa_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(qa_urls)),
    path('login/', include(qa_urls)),
    path('signup/', include(qa_urls)),
    path('question/123/', include(qa_urls)),
    path('ask/', include(qa_urls)),
    path('popular/', include(qa_urls)),
    path('new/', include(qa_urls))
]
