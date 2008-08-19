from django.conf import settings
from django.contrib import admin
from raptiye.comments.models import Comments

class CommentsAdmin(admin.ModelAdmin):
	model = Comments
	date_hierarchy = "datetime"
	list_display = ("get_entry_name", "get_author_info", "get_author_web_site", "get_datetime", "published", "notification",)
	list_filter = ("published", "notification")
	list_per_page = settings.ADMIN_LIST_PER_PAGE
	ordering = ("-datetime",)
	search_fields = ("entry__title", "author__username", "content")

admin.site.register(Comments, CommentsAdmin)
