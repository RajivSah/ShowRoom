
from django.contrib import admin
from .models import Publisher, Author, Book, Categories, pop_features
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
	list_display=('first_name', 'last_name', 'email')
	search_fields=('first_name','last_name')

class BookAdmin(admin.ModelAdmin):
	list_display=('title', 'publisher','publication_date')
	search_fields=('title',)
	list_filter=('publisher',)
	filter_horizontal=('authors',)
	raw_id_fields=('publisher',)
	filter_horizontal=('category',)
	filter_horizontal=('features',)

class PublisherAdmin(admin.ModelAdmin):
	list_display=('name', 'address', 'city', 'state_province', 'country', 'website')
	search_fields=('name',)
	list_filter=('country',)

class CategorieAdmin(admin.ModelAdmin):
	list_display=('cat_name',)
	search_fields=('cat_name',)

class  Popular_feature(admin.ModelAdmin):
	list_display=('feature',)
	search_fields=('feature',)


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Categories, CategorieAdmin)
admin.site.register(pop_features, Popular_feature)
