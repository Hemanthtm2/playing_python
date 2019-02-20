from django.contrib import admin

from .models import Entry
# Register your models here.
@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
      fieldsets=[('Regular Expression',{'fields':['pattern','test_string']}),
                 ('Other Information',{'fields':['user','date_added']}),
                ]
      list_display=('pattern','test_string','user')
      list_filter=['user']
      search_fields=['test_string']
