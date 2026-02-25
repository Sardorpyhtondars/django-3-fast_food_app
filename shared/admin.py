from django.contrib import admin

from shared.models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discount', 'created_at']
    search_fields = ['title', 'info']
    list_filter = ['status', 'created_at']

