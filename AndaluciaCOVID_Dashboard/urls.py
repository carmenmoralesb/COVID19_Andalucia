from . import views
from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    path('general/', views.dash_general_view, name='dash_general_view'),
    path('provinces/', views.dash_province_view, name='dash_province_view'),
    path('province/detail/<int:pk>', views.dash_province_detail_view,
         name='dash_province_detail_view'),
    path('municipio/detail/<int:pk>', views.dash_township_detail_view,
         name='dash_township_detail_view'),
    path('busqueda/', views.dash_search_view, name="dash_search_view")
]
