from django.urls import include, path
from rest_framework import routers

from ConferenceManager.api import views

router = routers.DefaultRouter()
router.register(r'papers/getAll', views.PaperViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
    ]
