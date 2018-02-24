from django.contrib import admin
from django.utils.text import Truncator
from .models import Career, Path, Course, Part, UserCareer, UserPath, UserCourse, UserPart, Profil


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):

    list_display = ['title', 'resume_description', 'added_date']
    search_fields = ['title', 'description']
    list_filter = ['update_date', 'visible']
    prepopulated_fields = {'slug': ['title', ]}

    fieldsets = [
        ('General', {
            'classes': ['collapse', ],
            'fields': ['title', 'slug']
        }),
        ('Other informations', {
            'classes': ['collapse', ],
            'fields': ['avatar', 'description', 'visible']
        })
    ]

    def resume_description(self, career):
        return Truncator(career.description).chars(40, truncate='...')
    resume_description.short_description = 'Description'


@admin.register(Path)
class PathAdmin(admin.ModelAdmin):

    list_display = ['title', 'resume_description', 'added_date']
    search_fields = ['title', 'description', 'career']
    list_filter = ['update_date', 'visible']
    prepopulated_fields = {'slug': ['title', ]}

    fieldsets = [
        ('General', {
            'classes': ['collapse', ],
            'fields': ['title', 'slug', 'career']
        }),
        ('Other informations', {
            'classes': ['collapse', ],
            'fields': ['avatar', 'description', 'visible']
        })
    ]

    def resume_description(self, path):
        return Truncator(path.description).chars(40, truncate='...')
    resume_description.short_description = 'Description'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = ['title', 'resume_description', 'added_date']
    search_fields = ['title', 'description', 'path']
    list_filter = ['update_date', 'visible']
    prepopulated_fields = {'slug': ['title', ]}

    fieldsets = [
        ('General', {
            'classes': ['collapse', ],
            'fields': ['title', 'slug', 'path']
        }),
        ('Other informations', {
            'classes': ['collapse', ],
            'fields': ['avatar', 'description', 'visible']
        })
    ]

    def resume_description(self, path):
        return Truncator(path.description).chars(40, truncate='...')
    resume_description.short_description = 'Description'


admin.site.register(Part)
admin.site.register(UserCareer)
admin.site.register(UserPath)
admin.site.register(UserCourse)
admin.site.register(UserPart)
admin.site.register(Profil)
