from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.CustomerAddView.as_view(), name='add-customer'),
    path('update/<int:id>/', views.CustomerUpdate.as_view(), name='customer-update'),
    path('/<int:id>/', views.CustomerDeleteView.as_view(), name='data-delete'),
    path('checkin/', views.CheckInAddView.as_view(), name='checkin'),

    
]