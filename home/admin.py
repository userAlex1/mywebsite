from django.contrib import admin
from .models import About, Resume, Skill, CoverLetter, Project, Contact

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("title", "file")

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "proficiency")

@admin.register(CoverLetter)
class CoverLetterAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "link")

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject")
