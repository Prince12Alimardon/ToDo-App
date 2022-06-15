from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'author', 'created_at')
    list_filter = ('status', )
    search_fields = ('title', 'author__username')


admin.site.register(Todo, TodoAdmin)
