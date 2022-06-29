from __future__ import unicode_literals
from django.urls import path

from .views import FarmListCreateView, \
    FarmRetrieveUpdateDestroyView, OwnerListCreateView, \
    OwnerRetrieveUpdateDestroyView

from .views.farm import FarmSearchView

urlpatterns = [
     path('farms', FarmListCreateView.as_view(),
         name="farms-list-create"),
     path('farms/<int:pk>', FarmRetrieveUpdateDestroyView.as_view(),
         name="farms-retrieve-update-destroy"),
    path('farms/search/', FarmSearchView.as_view(),
        name='farms-search-view'),


     path('owners', OwnerListCreateView.as_view(),
         name="owners-list-create"),
     path('owners/<int:pk>',
         OwnerRetrieveUpdateDestroyView.as_view(),
         name="owners-retrieve-update-destroy"),

]
