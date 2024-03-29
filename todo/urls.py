from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from todo import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls))
]