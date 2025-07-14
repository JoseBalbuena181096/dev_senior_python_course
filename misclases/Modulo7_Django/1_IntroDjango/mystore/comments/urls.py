from .views import home_page_view, goodbye_page_view
from django.urls import path


urlpatterns = [
    path('home/', home_page_view, name='home'),
    path('goodbye/', goodbye_page_view, name='goodbye'),
]

