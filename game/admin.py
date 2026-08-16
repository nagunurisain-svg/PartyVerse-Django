from django.contrib import admin
from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    list_display = (
        "text",
        "question_type",
        "category",
        "difficulty",
        "is_active",
        "created_at",
    )

    list_filter = (
        "question_type",
        "category",
        "difficulty",
        "is_active",
    )

    search_fields = (
        "text",
    )

    ordering = (
        "-created_at",
    )