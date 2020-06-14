from django.contrib import admin
from django.urls import path
from sites import views
from django.views.generic.base import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.submit,name="home"),
    path('submit/',views.submit,name="submit"),
    path('submit/submit/',
         RedirectView.as_view(url='http://kabilan175.pythonanywhere.com/')),
]
