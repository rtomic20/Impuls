from django.contrib import admin
from .models import User, Work

admin.site.register(User)

class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'uploaded_at', 'approved')
    list_filter = ('approved', 'uploaded_at')
    search_fields = ('title', 'user__username')

admin.site.register(Work, WorkAdmin)