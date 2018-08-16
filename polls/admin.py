from django.contrib import admin
from .models import Question, Choice


# Register your models here.


# 扁平化的显示方式: TabularInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_test', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_test']
    fieldsets = [
        (None, {'fields': ['question_test']}),
        ('日期信息', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
