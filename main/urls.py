from django.urls import path
from .views import TeacherListView

app_name = 'myapp'

urlpatterns = [
    path('teachers/', TeacherListView.as_view(), name='teachers_list'),
]
