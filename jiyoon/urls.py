from django.contrib import admin
from django.urls import path,include
import YOON.views
import YOON.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', YOON.views.home, name="home"),
    path('blog/',include(YOON.urls)),
]
