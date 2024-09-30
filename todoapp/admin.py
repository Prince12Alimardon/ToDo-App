from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'author', 'deadline','created_at')
    list_filter = ('status', 'deadline',)
    search_fields = ('title', 'author__username')


admin.site.register(Todo, TodoAdmin)
