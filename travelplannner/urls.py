"""
URL configuration for travelplannner project.

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
from django.contrib import admin
from django.urls import path
from planner import views as p_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',p_views.signup,name='signup'),
    path('login/',p_views.login,name='login'),
    path('home/',p_views.home,name='home'),
    path('plantrip/',p_views.plantrip,name='plantrip'),
    path('add_plan/',p_views.add_plan,name='add_plan'),
    path('create_plantrip/',p_views.create_plantrip,name='create_plantrip'),
    path('tourguide/',p_views.tourguide,name='tourguide'),
    path('tourguide/<str:id>',p_views.guide_details,name='guide_details'),
    path('logout',p_views.logout,name='logout'),
    path('logout_user/',p_views.logout_user, name= 'logout_user'),


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
