from django.urls import path
from .views import DepartmentView,PersonnelListCreateView,PersonalGetUpdateDelete

urlpatterns=[
    path("department/",DepartmentView.as_view()),
    path("personnel/",PersonnelListCreateView.as_view()),
    path("personnel/<int:pk>/",PersonalGetUpdateDelete.as_view()),
]