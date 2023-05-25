from django.contrib import admin

admin.site.site_title = "Manage employees"
admin.site.site_header = "Manage employees"


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "date_hired", "email", "position")
    list_display_links = ("id", "full_name")
    search_fields = ("full_name", "position", "email")
    save_on_top = True
