from . import views
from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
    # api
    path('api-overview', views.apiOverview, name="api-overview"),
    path('province-list', views.provinceList, name="province-list"),
    path('district-list', views.districtList, name="province-list"),
    path('township-list', views.townshipList, name="province-list"),
    path('region-historic-detail/', views.regionHistoricDetail, name="region-historic-detail"),     
    path('township-historic-detail/<str:name>/', views.townshipHistoricDetail, name="township-historic-detail"),
    path('province-historic-detail/<str:name>/', views.provinceHistoricDetail, name="township-historic-detail"),
    path('region-acumulated-all/', views.regionAccumulatedAll, name="region-acumulated-detail"),
    path('province-acumulated-all/', views.provinceAccumulatedAll, name="province-acumulated-all")   
]