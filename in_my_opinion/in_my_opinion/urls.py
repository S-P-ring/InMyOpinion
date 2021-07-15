from django.contrib import admin
from django.urls import path, include


# admin.site.index_template = 'admin/my_custom.html'
# admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_opinion.urls')),
]
