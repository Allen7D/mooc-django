# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2021/1/20.
  Updated by Allen7D on 2021/1/20.
"""
from import_export import resources

import xadmin
from apps.course.models import Course, Lesson, Video, BannerCourse, CourseResource, CourseTag, Banner
from xadmin.layout import Fieldset, Main, Side, Row

__author__ = 'Allen7D'


### xAdmin的基础配置 ###
class GlobalSettings(object):
    site_title = '教学后台管理系统'
    site_footer = '教学在线网'
    # menu_style = 'accordion' 菜单栏出于收拢状态#


class BaseSettings(object):
    enable_themes = True  # 切换主题
    use_bootswatch = True


xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)


### Course的业务配置 ###

class LessonInline(object):
    model = Lesson
    # style = 'tab'
    extra = 0
    exclude = ['create_time', 'update_time', 'delete_time']


class CourseResourceInline(object):
    model = CourseResource
    style = 'tab'
    extra = 1
    exclude = ['create_time', 'update_time', 'delete_time']


class CourseImExResource(resources.ModelResource):
    """课程的导入&导出"""

    class Meta:
        model = Course
        # fields = ('name', 'desc',) # 导出字段(不使用则默认导出全部字段)
        # exclude = ('desc')  # 隐藏字段


# class CourseAdmin(object):
#     list_display = ['name', 'desc', 'detail', 'degree', 'learn_duration', 'student_nums']
#     search_fields = ['name', 'desc', 'detail', 'degree', 'student_nums']
#     list_filter = ['name', 'teacher__name', 'desc', 'detail', 'degree', 'learn_duration', 'student_nums']
#     list_editable = ['degree', 'desc']


class CourseAdmin(object):
    import_export_args = {'import_resource_class': CourseImExResource, 'export_resource_class': CourseImExResource}
    list_display = ['name', 'teacher', 'desc', 'show_image', 'go_to', 'detail', 'degree', 'learn_duration',
                    'student_nums']
    search_fields = ['name', 'desc', 'detail', 'degree', 'student_nums']
    list_filter = ['name', 'teacher__name', 'desc', 'detail', 'degree', 'learn_duration', 'student_nums']
    list_editable = ['degree', 'desc']  # 直接编辑
    readonly_fields = ['student_nums', 'click_nums', 'favor_nums'] + ['create_time']
    exclude = ['update_time', 'delete_time']
    ordering = ['click_nums']
    model_icon = 'fa fa-book'
    inlines = [LessonInline, CourseResourceInline]  # 显示关联的表
    style_fields = {
        # 应用ueditor
        'detail': 'ueditor'
    }

    def queryset(self):
        qs = super().queryset()
        if not self.request.user.is_superuser:
            qs = qs.filter(teacher=self.request.user.teacher)
        return qs

    def get_form_layout(self):
        # css_class='unsort no_title' 隐藏title
        self.form_layout = (
            Main(
                Fieldset('讲师信息',
                         Row('teacher', 'org'),
                         css_class='unsort no_title'
                         ),
                Fieldset('基本信息',
                         Row('name', 'image'),
                         'desc',
                         Row('learn_duration', 'degree'),
                         Row('category', 'tag'),
                         'tips', 'overview', 'notice', 'detail'
                         ),
            ),
            Side(
                Fieldset('选择信息',
                         'is_banner', 'is_classics'
                         ),
            ),
            Side(
                Fieldset('访问信息',
                         'favor_nums', 'click_nums', 'student_nums', 'create_time'
                         ),
            ),
        )
        return super(CourseAdmin, self).get_form_layout()


class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_duration', 'student_nums']
    search_fields = ['name', 'desc', 'detail', 'degree', 'student_nums']
    list_filter = ['name', 'teacher__name', 'desc', 'detail', 'degree', 'learn_duration', 'student_nums']
    list_editable = ["degree", "desc"]
    readonly_fields = ['student_nums', 'click_nums', 'favor_nums'] + ['create_time']
    exclude = ['update_time', 'delete_time']
    model_icon = 'fa fa-square'

    def queryset(self):
        qs = super().queryset()
        qs = qs.filter(is_banner=True)
        return qs


class LessonAdmin(object):
    list_display = ['course', 'name', 'create_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'create_time']
    readonly_fields = ['create_time']
    exclude = ['update_time', 'delete_time']
    model_icon = 'fa fa-list'


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'create_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'create_time']
    readonly_fields = ['create_time']
    exclude = ['update_time', 'delete_time']
    model_icon = 'fa fa-file-video-o'


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'file', 'create_time']
    search_fields = ['course', 'name', 'file']
    list_filter = ['course', 'name', 'file', 'create_time']
    readonly_fields = ['create_time']
    exclude = ['update_time', 'delete_time']
    model_icon = 'fa fa-files-o'


class CourseTagAdmin(object):
    list_display = ['course', 'tag', 'create_time']
    search_fields = ['course', 'tag']
    list_filter = ['course', 'tag', 'create_time']
    readonly_fields = ['create_time']
    exclude = ['update_time', 'delete_time']
    model_icon = 'fa fa-tag'


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index']
    readonly_fields = ['create_time']
    exclude = ['update_time', 'delete_time']
    model_icon = 'fa fa-refresh'


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(CourseTag, CourseTagAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
