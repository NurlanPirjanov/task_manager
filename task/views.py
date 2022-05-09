from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormView
from django.urls import reverse_lazy
from .models import *
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.messages.views import SuccessMessageMixin
class TaskMyListView(LoginRequiredMixin, ListView):
    model = TaskManager
    template_name = 'task_my.html'
class TaskMyNewListView(LoginRequiredMixin, ListView):
    model = TaskManager
    template_name = 'task_my_new.html'

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = TaskManager
    template_name = 'task_detail.html'
    def get_context_data(self, *args, **kwargs):
        context = super(TaskDetailView, self).get_context_data()
        stuff = get_object_or_404(TaskManager, id=self.kwargs['pk'])
        total_qabul = stuff.total_qabul
        context["total_likes"] = total_qabul
        return context
class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = TaskManager
    template_name = 'task_edit.html'
    form_class = AddForm
    success_url = reverse_lazy('task_list')
    success_message = "Topshiriq muafaqiyatli yangilandi"
    def form_valid(self, form):
        form.save()
        return super(TaskUpdateView, self).form_valid(form)
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class TaskDeleteView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, DeleteView):
    model = TaskManager
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')
    success_message = "Topshiriq muafaqiyatli o`chirildi"
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    model = TaskManager
    template_name = 'task_new.html'
    form_class = AddForm
    success_url = '/task_my/'
    success_message = "Topshiriq muafaqiyatli yuborildi"
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
    
class TaskCommentView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Comment
    template_name = 'comment_new.html'
    form_class = AddCommentForm
    success_message = "Muafaqiyatli yuborildi"
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.task_id = self.kwargs['pk']
        form.save()
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('task_detail', args=[self.kwargs['pk']])
def LikeView(request,pk):
    task = get_object_or_404(TaskManager, id=request.POST.get('object_id'))
    task.task_qabul.add(request.user.id)
    return HttpResponseRedirect(reverse('task_detail', args=[str(pk)]))



from rest_framework import generics
from .serializers import TaskAPIListSerializer

#API-DRF
class TaskListAPIView(generics.ListAPIView):
    queryset = TaskManager.objects.all()
    serializer_class = TaskAPIListSerializer