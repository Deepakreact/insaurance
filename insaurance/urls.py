

from django.urls import path
from . import views

urlpatterns = [
    path('get_category/', views.get_Category),
    path('get_products/', views.get_Products),
    path('create_Lead/', views.create_Lead),
    path('update_lead/<str:pk>/', views.update_lead),
    path('get_leads/', views.get_Leads),
    path('get_lead/<str:pk>/', views.get_Lead),
    path('create_Request/', views.create_Request),
    path('get_user_requests/', views.get_UserGeneratedRequests),
    path('get_user_requests/<str:pk>/', views.get_UserGeneratedRequest),
    path('renew/<str:pk>/', views.update_UserGeneratedRequest),

    path('get_user_resolved_requests/', views.get_UserResolvedRequests),

    path('create_ticket/', views.create_Ticket),
    path('createlead_ticket/', views.createlead_Ticket),
    path('get_issues/<str:Id>/', views.get_Issues),
    path('getlead_issues/<str:Id>/', views.getlead_Issues),

    path('update_issues/<str:pk>/', views.update_ticket),
    path('update_lead_issues/<str:pk>/', views.updatelead_ticket),
]
