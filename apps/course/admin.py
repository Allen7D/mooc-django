from django.contrib import admin

from apps.course.models import Course as CourseModel, \
    Lesson as LessonModel, Video as VideoModel, \
    CourseResource as CourseResourceModel


class CourseAdmin(admin.ModelAdmin):
    pass


class LessonAdmin(admin.ModelAdmin):
    pass


class VideoAdmin(admin.ModelAdmin):
    pass


class CourseResourceAdmin(admin.ModelAdmin):
    pass


admin.site.register(CourseModel, CourseAdmin)
admin.site.register(LessonModel, LessonAdmin)
admin.site.register(VideoModel, VideoAdmin)
admin.site.register(CourseResourceModel, CourseResourceAdmin)
