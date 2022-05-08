from .models import HomeManager
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from accounts.models import CustomUser
from task.models import TaskManager
class HomeListView(LoginRequiredMixin, ListView):
    model = HomeManager
    template_name = 'home.html'
    def get_context_data(self, *args, **kwargs):
        context = super(HomeListView, self).get_context_data()
        user_ad = CustomUser.objects.filter(role_user=1).count()
        user_km = CustomUser.objects.filter(role_user=2).count()
        user_dk = CustomUser.objects.filter(role_user=3).count()
        user_rektor = CustomUser.objects.filter(role_user=4).count()
        total_task = TaskManager.objects.all().count()
        context["user_ad"] = user_ad
        context["user_km"] = user_km
        context["user_dk"] = user_dk
        context["user_rektor"] = user_rektor
        context["total_task"] = total_task
        return context

