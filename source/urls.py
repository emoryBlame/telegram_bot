from django.contrib import admin
from django.urls import path

from source import views


urlpatterns = [
    path('init/', views.GenaricAPIViews.as_view(), name="init"),
    path('webhooks/', views.WebhooksView.as_view(), name="webhooks"),
]
