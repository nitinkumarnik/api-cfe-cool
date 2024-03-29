"""cfeapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from updates.views import (
				json_example_view, 
				JsonCBV, 
				JsonCBV2, 
				SerializedListView, 
				SerializedDetailView
			)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('json/JsonCBV/', JsonCBV.as_view()),
    path('json/JsonCBV2/', JsonCBV2.as_view()),
    path('json/serialize/list/', SerializedListView.as_view()),
    path('json/serialize/detail/', SerializedDetailView.as_view()),
    path('json/example/', json_example_view),
]
