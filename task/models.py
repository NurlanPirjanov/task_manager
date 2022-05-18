from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField
from accounts.models import CustomUser
from accounts.models import RoleUser


# def user_directory_path(instance, filename):
#     return 'post'
class TaskManager(models.Model):
    role_user = models.ForeignKey(RoleUser, on_delete=models.CASCADE, verbose_name="Topshiriq kimlar uchun?")
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Kim tomanidan Topshiriq berilishi'
    )
    title = models.CharField(max_length=150, verbose_name='Sarlavha')
    body = RichTextField(verbose_name='Topshiriq haqida to`liq ma`lumot')
    file = models.FileField(upload_to='files/', null=True)
    ot_date = models.DateTimeField(auto_now_add=True, verbose_name="Berilgan vaqti")
    do_date = models.DateTimeField(verbose_name='Tugatish vaqti')
    task_qabul = models.ManyToManyField(
        get_user_model(),
        related_name='task_qabul',
        )
    active = models.BooleanField(default=True, verbose_name='Faolligi')
    def total_qabul(self):
        return self.task_qabul.all()
    def __str__(self):
        return f'{self.title}'
    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])
    class Meta:
        verbose_name = 'Topshiriq '
        verbose_name_plural = 'Topshiriqlar '

class Comment(models.Model):
    task = models.ForeignKey(TaskManager, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=200, verbose_name='Izoh')
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='files/', verbose_name='Fayl biriktirish', blank=True, null=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Avtor'
    )

    def __str__(self):
        return self.comment
    class Meta:
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'