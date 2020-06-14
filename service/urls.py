from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from service import views

urlpatterns = [
    path('elements/', views.ElementList.as_view()),
    path('elements/<int:pk>/', views.ElementDetail.as_view()),
    path('commodity/', views.CommodityList.as_view()),
    path('commodity/<int:pk>/', views.CommodityDetail.as_view()),
    path('chemical_composition/', views.Chemical_composition_List.as_view()),
    path('chemical_composition/<int:pk>/', views.Chemical_composition_Detail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)

