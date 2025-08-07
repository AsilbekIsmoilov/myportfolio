from django.urls import path

from portfolio.views import *

urlpatterns = [
    path('', InfoList.as_view(),name='index'),
    path('category/<slug:slug>', InfoListByCategory.as_view() ,name='category'),
    path('send-email/', send_email_view, name='send_email'),
]