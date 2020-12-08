from django.contrib import admin

from question.models import Question, Category, Answer

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('title',) }

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('title',)}

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass