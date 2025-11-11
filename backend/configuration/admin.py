#########################################
"""
ADMIN UI DESING SETUP
"""
#########################################
from django.contrib import admin
from django.utils.html import mark_safe
from configuration.models import (
    Favicon,
    Logo,
    CopyRight,
    ContactInfo,
    SocialLink
)

class LogoAdmin(admin.ModelAdmin):
    list_display = ('preview_logo', 'edit_link', 'delete_link')

    def preview_logo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        return "No Image"
    preview_logo.short_description = 'Logo Preview'

    def edit_link(self, obj):
        return mark_safe(f'<a href="/admin/configuration/logo/{obj.id}/change/">Edit</a>')
    edit_link.short_description = 'Edit'

    def delete_link(self, obj):
        return mark_safe(f'<a href="/admin/configuration/logo/{obj.id}/delete/">Delete</a>')
    delete_link.short_description = 'Delete'

class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['number_1', 'number_2', 'email']

# REGISTER MODELS HERE.
admin.site.register(Favicon)
admin.site.register(Logo, LogoAdmin)
admin.site.register(CopyRight)
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(SocialLink)
