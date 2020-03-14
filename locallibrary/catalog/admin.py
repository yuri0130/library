from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(BookInstance)
admin.site.register(Language)
admin.site.register(Genre)


# needed to show associated data Tabular = Horizonal layout
# for a vertical layout use admin.StackedInline
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # typically not a good idea to display a ManyToMany field like this
    # this would make a lot of calls to the DB. the below 'display_genre'
    # is for educational purposes only
    list_display = ('title', 'author', 'display_genre')
    # allows for associated data to be shown
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    # adds filter panels to the admin
    list_filter = ('status', 'due_back')
    # you can break the admin page into sections by specifying a
    # fieldsets attribute per below
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


class BookInline(admin.TabularInline):
    model = Book
    extra = 1


# admin.ModelAdmin class allows you to customize the model view in
# the admin app
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # instead of displaying the __str__ method in the admin list view
    # we can overwrite this and add more fields as per below
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')
    # you can change the order of the detail view
    # by grouping fields in a tuple they will show up in the same row
    fields = [('first_name', 'last_name'), ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

# @admin.register(Author) is the same as doing the below:
# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book, BookAdmin)
# admin.site.register(BookInstance, BookInstanceAdmin)
