from django.urls import path
from . import views
from object_detection.views import yolo_detection

urlpatterns = [
    path("", views.UploadImgView.as_view()),
    path('yolo_detection/', yolo_detection, name='yolo_detection'),
]
