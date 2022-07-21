from common.utils import Utils


class IndexTemplateBase(Utils):
    def into_index_template_menu(self):
        '''进入索引管理/模板列表菜单'''
        self.into_module("动态数据分析")
        self.into_menu("索引管理/索引模板")

    def wait_into_page_index_template_list(self):
        '''等待进入模板列表'''
        self.wait_into_page("模板列表")

    def wait_into_page_index_template_add(self):
        '''等待进入新建模板页面'''
        self.wait_into_page("新建模板")

    def wait_into_page_index_template_detail(self):
        '''等待进入模板详情页面'''
        self.wait_into_page("模板详情")

    def index_template_list_click_add(self):
        '''点击新建按钮'''
        self.click_button(button_name="新建")

    def index_template_list_operate_click_detail(self, template_name):
        '''列表操作点击【详情】'''
        self.move_to_operate_button(text=template_name)
        self.click_operate_button(text="详情")

    def index_template_list_operate_click_clone(self, template_name):
        '''列表操作点击【克隆】'''
        self.move_to_operate_button(text=template_name)
        self.click_operate_button(text="克隆")

    def index_template_list_operate_click_export(self, template_name):
        '''列表操作点击【导出】'''
        self.move_to_operate_button(text=template_name)
        self.click_operate_button(text="导出")

    def index_template_list_operate_click_delete(self, template_name):
        '''列表操作点击【删除】'''
        self.move_to_operate_button(text=template_name)
        self.click_operate_button(text="删除")

    def index_template_form_input_template_name(self, template_name):
        '''输入模板名称'''
        self.form_input(label="名称", text=template_name)

    def index_template_form_clear_template_name(self):
        '''清空模板名称'''
        self.form_input_clear(label="名称")

    def index_template_form_input_name(self, name, index=3):
        '''输入索引字段的名称'''
        self.type(
            xpath='//div[{index}]/app-edit-template-field/div/div[1]/nz-form-control[1]/div/div/input'.format(index=index), text=name)

    def index_template_form_clear_name(self, index=3):
        '''清空索引字段的名称'''
        self.clear(
            xpath='//div[{index}]/app-edit-template-field/div/div[1]/nz-form-control[1]/div/div/input'.format(index=index))

    def index_template_form_input_field(self, field, index=3):
        '''输入索引字段的字段'''
        self.type(
            xpath='//div[{index}]/app-edit-template-field/div/div[2]/nz-form-control/div/div/input'.format(index=index), text=field)

    def index_template_form_clear_field(self, index=3):
        '''清空索引字段的字段'''
        self.clear(
            xpath='//div[{index}]/app-edit-template-field/div/div[2]/nz-form-control/div/div/input'.format(index=index))

    def index_template_form_click_add_field(self):
        '''点击【添加字段】'''
        self.click_button(button_name="添加字段")

    def index_template_form_click_save(self):
        '''点击【保存】'''
        self.click_button(button_name="保存")

    def index_template_detail_click_edit(self):
        '''点击【编辑】按钮-详情页面'''
        self.click_button(button_name="编辑")

    def index_template_detail_click_return(self):
        '''点击【返回】按钮-详情页面'''
        self.click_button(button_name="返回")

    def index_template_clone_form_input_template_name(self, template_name):
        '''输入克隆名称'''
        self.alert_form_input(label="名称", text=template_name)

    def index_template_clone_form_click_confirm(self):
        '''点击【确定】按钮'''
        self.click_button(button_name="确定")

    def index_template_filter_input_name(self, template_name):
        '''输入名称'''
        self.form_input(label="名称", text=template_name)

    def index_template_filter_click_select(self):
        '''点击【查询】按钮'''
        self.click_button(button_name="查询")

    def index_template_filter_click_reset(self):
        '''点击【重置】按钮'''
        self.click_button(button_name="重置")


class IndexTemplate(IndexTemplateBase):
    def index_template_function_add_template(self, template_name, name, field):
        '''新增基本模板'''
        self.into_index_template_menu()
        self.wait_into_page_index_template_list()
        self.index_template_list_click_add()
        self.wait_into_page_index_template_add()
        self.index_template_form_input_template_name(template_name)
        self.index_template_form_click_add_field()
        self.index_template_form_input_name(name)
        self.index_template_form_input_field(field)
        self.index_template_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_index_template_list()

    def index_template_function_delete_template(self, template_name):
        '''删除模板'''
        self.into_index_template_menu()
        self.wait_into_page_index_template_list()
        self.index_template_list_operate_click_delete(template_name)
        self.alert_receive()
        self.wait_toast_delete_successfully()
