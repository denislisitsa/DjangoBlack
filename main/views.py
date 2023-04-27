from django.views.generic.list import ListView
from .models import Teacher


class TeacherListView(ListView):
    model = Teacher
    template_name = 'myapp/teacher_list.html'
    context_object_name = 'teachers'
