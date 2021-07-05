from django.contrib import admin
from .models import Category, Appeal
from rangefilter.filter import DateTimeRangeFilter
from django.utils.html import format_html


class AppealInline(admin.TabularInline):
    model = Appeal.category.through


class AppealAdmin(admin.ModelAdmin):
    readonly_fields = ['date_of_creation']
    fields = ['id', 'email', 'title', 'history', 'category', 'status', 'date_of_creation']
    list_display = ['date_of_creation', 'number_of_likes', 'title', 'email', 'history', 'get_category', 'status', 'delete', 'publicate',]
    list_display_links = ['title']
    ordering = ['date_of_creation']
    list_filter = ['status', 'category', ('date_of_creation', DateTimeRangeFilter),]

    def get_category(self, obj):
        """method to make the display ManyToManyField in the admin panel"""
        return "\n".join([c.name for c in obj.category.all()])

    def delete(self, obj):
        """delete button in admin panel"""
        view_name = "admin:{}_{}_delete".format(obj._meta.app_label, obj._meta.model_name)
        link = 'some_link'
        html = '<input type="button" onclick="location.href=\'{}\'" value="Відхилити" />'.format(link)
        return format_html(html)

    def publicate(self, obj):
        """publicate button in admin panel"""
        view_name = "admin:{}_{}_publicate".format(obj._meta.app_label, obj._meta.model_name)
        link = 'some_link'
        html = '<input type="button" onclick="location.href=\'{}\'" value="Опублікувати" />'.format(link)
        return format_html(html)

    """Name of column in admin panel"""
    delete.short_description = ""
    publicate.short_description = ""
    get_category.short_description = "Категорії"


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    inlines = [AppealInline,]
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Appeal, AppealAdmin)
