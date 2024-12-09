from django.urls import path
from .views import ItemList, CaseList, CaseDetail, EndpointList, EndpointDetail, ThreatList, ThreatDetail

urlpatterns = [
    path('items/', ItemList.as_view(), name='item-list'),
    path('cases/', CaseList.as_view(), name='case-list'),
    path('cases/<int:pk>/', CaseDetail.as_view(), name='case-detail'),
    path('endpoints/', EndpointList.as_view(), name='endpoint-list'),
    path('endpoints/<int:pk>/', EndpointDetail.as_view(), name='endpoint-detail'),
    path('threats/', ThreatList.as_view(), name='threat-list'),
    path('threats/<int:pk>/', ThreatDetail.as_view(), name='threat-detail'),
]
