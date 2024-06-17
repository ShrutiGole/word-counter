from django.contrib import admin
from django.urls import path
from word_counter import views  # Import views from the word_counter app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.counter, name='counter'),  # Map the root URL to the counter view
]