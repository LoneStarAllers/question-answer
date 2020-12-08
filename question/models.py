from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=150, unique=True, allow_unicode=True, verbose_name='لینک یکتا')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='دسته بندی سطح بالا')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ('created',)
        db_table = 'category'

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان سوال')
    slug = models.SlugField(max_length=150, unique=True, allow_unicode=True, verbose_name='لینک یکتا')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ایجاد کننده', related_name='questions')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی', related_name='questions')
    likes = models.ManyToManyField(User, blank=True, related_name='questions_likes')
    text = models.TextField(verbose_name='متن سوال')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')

    def total_likes(self):
        return self.likes.count()

    class Meta:
        verbose_name = 'سوال'
        verbose_name_plural = 'سوال ها'
        ordering = ('created',)
        db_table = 'question'

    def __str__(self):
        return self.title

class Answer(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ایجاد کننده', related_name='answers')
    text = models.TextField(verbose_name='متن جواب')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='سوال مربوطه', related_name='answers')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')

    class Meta:
        verbose_name = 'جواب'
        verbose_name_plural = 'جواب ها'
        ordering = ('created',)
        db_table = 'answer'

    def __str__(self):
        return self.text