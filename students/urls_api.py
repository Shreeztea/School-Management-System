from rest_framework.routers import DefaultRouter
# from django.urls import path
from .api_views import StudentViewSet
# from .api_views import StudentDetailAPIView, StudentListCreateAPIView

# urlpatterns = [
#     # path('students/', StudentListCreateAPIView.as_view(), name='student-list-create-api'),
#     # path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail-api'),
# ]


router = DefaultRouter()
router.register('students', StudentViewSet, basename='student')

urlpatterns = router.urls