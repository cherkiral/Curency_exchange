from django.urls import path

from .views import CurrencyView

urlpatterns = [
    path('rates/', CurrencyView.as_view()),
]
