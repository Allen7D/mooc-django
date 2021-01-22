import xadmin
from apps.org.models import Teacher, Org, City
from xadmin.layout import Fieldset, Main, Side, Row


class OrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'favor_nums']  # 列表显示的字段
    search_fields = ['name', 'desc', 'click_nums', 'favor_nums']  #
    list_filter = ['name', 'desc', 'click_nums', 'favor_nums']  # 过滤器
    readonly_fields = ['course_nums', 'student_nums', 'click_nums', 'favor_nums'] + ['create_time']  # 只读字段(无法修改)
    exclude = ['update_time', 'delete_time']  # 隐藏字段(不显示)
    model_icon = 'fa fa-building'  # Menu的icon

    def get_form_layout(self):
        self.form_layout = (
            Main(
                Fieldset('基本信息',
                         Row('name', 'image'),
                         'desc',
                         Row('tag', 'category'),
                         Row('city', 'address'),
                         ),
            ),
            Side(
                Fieldset('选择信息',
                         'is_auth', 'is_gold'
                         ),
            ),
            Side(
                Fieldset('访问信息',
                         'course_nums', 'student_nums', 'favor_nums', 'click_nums', 'create_time'
                         ),
            ),
        )
        return super(OrgAdmin, self).get_form_layout()


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company']
    search_fields = ['name', 'work_years', 'work_company']
    list_filter = ['org', 'name', 'work_years', 'work_company']
    readonly_fields = ['click_nums', 'favor_nums'] + ['create_time']
    exclude = ['update_time', 'delete_time']
    model_icon = 'fa fa-street-view'

    def get_form_layout(self):
        # form_layout 适用于预览、新建、更新 3种界面
        self.form_layout = (
            Main(
                Fieldset('所属信息',
                         Row('user', 'org'),
                         css_class='unsort no_title'
                         ),
                Fieldset('基本信息',
                         Row('name', 'image'),
                         Row('age', 'work_years'),
                         Row('work_company', 'work_position'),
                         'feature',
                         ),
            ),
            Side(
                Fieldset('访问信息',
                         'favor_nums', 'click_nums', 'create_time'
                         ),
            ),
        )
        return super(TeacherAdmin, self).get_form_layout()


class CityAdmin(object):
    list_display = ['id', 'name', 'desc']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc']
    list_editable = ['name', 'desc']
    model_icon = 'fa fa-map'


# register的顺序就是Menu里顺序
xadmin.site.register(Org, OrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(City, CityAdmin)
