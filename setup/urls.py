from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from siteapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.base,name='base'),
    path('cessao0',views.cessao0,name='cessao0'),
    
    path('cessao1',views.cessao1,name='cessao1'),
    path('cessao2',views.cessao2,name='cessao2'),
    path('cessao3',views.cessao3,name='cessao3'),
    path('cessao4',views.cessao4,name='cessao4'),
    path('cessao5',views.cessao5,name='cessao5'),
    path('cessao6',views.cessao6,name='cessao6'),
    path('cessao7',views.cessao7,name='cessao7'),


    path('', include('userapp.urls')),
    path('', include('siteapp.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Adicionar Isto
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adicionar Isto
