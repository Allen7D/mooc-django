from django.contrib import admin

from apps.oper.models import UserAsk as UserAskModel, \
    UserCourse as UserCourseModel, CourseComment as CourseCommentModel, \
    UserFavor as UserFavorModel, UserMessage as UserMessageModel


class UserAskAdmin(admin.ModelAdmin):
    pass


class UserCourseAdmin(admin.ModelAdmin):
    pass


class CourseCommentAdmin(admin.ModelAdmin):
    pass


class UserFavorAdmin(admin.ModelAdmin):
    pass


class UserMessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserAskModel, UserAskAdmin)
admin.site.register(UserCourseModel, UserCourseAdmin)
admin.site.register(CourseCommentModel, CourseCommentAdmin)
admin.site.register(UserFavorModel, UserFavorAdmin)
admin.site.register(UserMessageModel, UserMessageAdmin)
