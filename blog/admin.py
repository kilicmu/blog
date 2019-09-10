from django.contrib import admin
# Register your models here.
from .models import Article, Comments, Tags, User, Filter, Headpic
from .admin_config import ArticleAdmin, FilterAdmin, UserAdmin, HeadpicAdmin

admin.site.register(Article, ArticleAdmin)
admin.site.register(Filter, FilterAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Headpic, HeadpicAdmin)