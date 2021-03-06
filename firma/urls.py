"""firma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from home.views import home_view
from insaat.views import hakkimizda_view, iletisim_view
from temizlik.views import temizlik_view, bina_view
from django.conf.urls import url, include


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', home_view, name='home'),
    url(r'^temizlik-hizmetleri/', temizlik_view, name='temizlik'),
    url(r'^profesyonel-bina-yonetim-sistemleri/', bina_view, name='bina'),
    url(r'^iletisim/', iletisim_view, name='iletisim'),
    url(r'^hakkimizda/', hakkimizda_view, name='hakkimizda'),
    url(r'^post/', include('haber.urls')),
    url(r'^emlak/', include('emlak.urls')),
    url(r'^proje/', include('proje.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
