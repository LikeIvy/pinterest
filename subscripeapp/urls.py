from django.urls import path

from subscripeapp.views import SubscriptionView


app_name = 'subscripeapp'


urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
]