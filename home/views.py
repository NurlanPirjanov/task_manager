from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.views.generic.base import TemplateView
from accounts.models import CustomUser
from task.models import TaskManager


class HomeListView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeListView, self).get_context_data()
        duplicates = CustomUser.objects.values('role_user__short_name').annotate(name_count=Count('role_user__short_name'))
        total_task = TaskManager.objects.all().count()
        context["duplicates"] = duplicates
        context["total_task"] = total_task
        return context
