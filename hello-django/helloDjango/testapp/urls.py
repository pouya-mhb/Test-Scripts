from django.urls import path
from testapp.views import app

urlpatterns = [
    path('haha/',app),
    path('login/',app),
    path('SearchResult/',app),
    path('LowFareSearch/',app),
    path('Locations/',app),
    path('Revalidate/',app),
    path('Flights/',app),
    path('PrePayments/',app)
]