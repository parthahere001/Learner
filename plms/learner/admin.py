from django.contrib import admin
# Register your models here.
from .models import Course, Csource, Student, Teacher



admin.site.site_header = "Learner Admin"
admin.site.site_title = "Learner Admin Area"
admin.site.index_title = "Welcome to the Learner Admin Area"

# class ChoiceInLine(admin.TabularInline):
#  	model = course
#  	extra = 1


class CourseAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['title']}), ('description', {
		'fields': ['description'], 'classes': ['collapse']}),('enrollkey', {'fields': ['enrollkey']}), ]
	# inlines = [ChoiceInLine]


admin.site.register(Course)

admin.site.register(Student)

admin.site.register(Teacher)
admin.site.register(Csource)





