from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page_url'),
    url(r'^index/$', views.main_page, name='Ana Sayfa'),
    url(r'^iletisim/$', views.contact_detail, name='contact_detail'),

    url(r'^hakkimizda/$', views.about_us, name='Hakkımızda'),

    url(r'^hizmetlerimiz/$', views.contact_detail, name='Hizmetlerimiz'),
    url(r'^urunlerimiz/$', views.contact_detail, name='Ürünler'),
    url(r'^iletisim/$', views.contact_detail, name='Basında Prosil'),
]
