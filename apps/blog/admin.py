from django.contrib import admin
# Import your models here.
from blog.models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'tags', 'category', 'published')
    save_on_top = True
    actions = ['publish']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

    def publish(self, request, queryset):
        rows = queryset.update(published=True)
        if rows == 1:
            message_bit = "1 blog post was"
        else:
            message_bit = "%s blog posts were" % rows
        self.message_user(request, "%s successfully published." % message_bit)
        
admin.site.register(Post, PostAdmin)


admin.site.register(Category)