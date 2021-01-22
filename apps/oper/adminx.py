import xadmin
from apps.oper.models import UserAsk, CourseComment, UserCourse, UserFavor, UserMessage


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'create_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'create_time']
    readonly_fields = ['create_time']
    exclude = ['update_time', 'delete_time']
    model_icon = 'fa fa-question-circle'


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'create_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'create_time']
    readonly_fields = ['create_time']
    exclude = ['update_time', 'delete_time']
    model_icon = 'fa fa-briefcase'

    def save_models(self):
        obj = self.new_obj
        if not obj.id:
            obj.save()
            course = obj.course
            course.student_nums += 1
            course.save()


class UserMessageAdmin(object):
    list_display = ['user', 'content', 'has_read', 'create_time']
    search_fields = ['user', 'content', 'has_read']
    list_filter = ['user', 'content', 'has_read', 'create_time']
    readonly_fields = ['create_time']
    exclude = ['update_time', 'delete_time']
    model_icon = 'fa fa-envelope'


class CourseCommentAdmin(object):
    list_display = ['user', 'course', 'content', 'create_time']
    search_fields = ['user', 'course', 'content']
    list_filter = ['user', 'course', 'content', 'create_time']
    readonly_fields = ['create_time']
    exclude = ['update_time', 'delete_time']
    model_icon = 'fa fa-pencil-square-o'


class UserFavorAdmin(object):
    list_display = ['user', 'favor_id', 'favor_type', 'create_time']
    search_fields = ['user', 'favor_id', 'favor_type']
    list_filter = ['user', 'favor_id', 'favor_type', 'create_time']
    readonly_fields = ['create_time']
    exclude = ['update_time', 'delete_time']
    model_icon = 'fa fa-heart'


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)
xadmin.site.register(UserFavor, UserFavorAdmin)
