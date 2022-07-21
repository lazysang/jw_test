from common.utils import Utils


class IndexBase(Utils):
    def into_index_menu(self):
        '''进入索引管理/数据索引列表菜单'''
        self.into_module("动态数据分析")
        self.into_menu("索引管理/数据索引")

    def wait_into_page_index_list(self):
        '''等待进入索引列表'''
        self.wait_into_page("索引列表")

    def wait_into_page_index_add(self):
        '''等待进入新建索引页面'''
        self.wait_into_page("新建索引")

    def wait_into_page_index_edit(self):
        '''等待进入编辑索引页面'''
        self.wait_into_page("编辑索引")

    def wait_into_page_index_detail(self):
        '''等待进入索引详情页面'''
        self.wait_into_page("索引详情")

    def index_list_click_add(self):
        '''点击新建按钮'''
        self.click_button(button_name="新建")

    def index_list_operate_click_detail(self, index_name):
        '''列表操作点击【详情】'''
        self.move_to_operate_button(text=index_name)
        self.click_operate_button(text="详情")

    def index_list_operate_click_edit(self, index_name):
        '''列表操作点击【编辑】'''
        self.move_to_operate_button(text=index_name)
        self.click_operate_button(text="编辑")

    def index_list_operate_click_clone(self, index_name):
        '''列表操作点击【克隆】'''
        self.move_to_operate_button(text=index_name)
        self.click_operate_button(text="克隆")

    def index_list_operate_click_hand_over(self, index_name):
        '''列表操作点击【移交】'''
        self.move_to_operate_button(text=index_name)
        self.click_operate_button(text="移交")

    def index_list_operate_click_export(self, index_name):
        '''列表操作点击【导出】'''
        self.move_to_operate_button(text=index_name)
        self.click_operate_button(text="导出")

    def index_list_operate_click_delete(self, index_name):
        '''列表操作点击【删除】'''
        self.move_to_operate_button(text=index_name)
        self.click_operate_button(text="删除")

    def index_form_input_index_name(self, index_name):
        '''输入索引名称'''
        self.form_input(label="名称", text=index_name)

    def index_form_clear_index_name(self):
        '''清空索引名称'''
        self.form_input_clear(label="名称")

    def index_form_input_index_description(self, index_description):
        '''输入索引描述'''
        self.form_textarea(label="说明", text=index_description)

    def index_form_select_template(self, template_name):
        '''选择索引模板'''
        self.form_select_click(label="选择索引模板")
        self.pull_down_list_select(text=template_name)

    def index_form_input_index_prefix(self, index_prefix):
        '''输入索引前缀'''
        self.form_input(label="索引前缀", text=index_prefix)

    def index_form_click_save(self):
        '''点击【保存】'''
        self.click_button(button_name="保存")

    def index_detail_switch(self, text):
        '''根据文本切换tab'''
        self.click(
            xpath='//nz-tabset/nz-tabs-nav/div/div/div/div[normalize-space(text())="{}"]'.format(text))

    def index_detail_switch_to_advanced_configuration(self):
        '''切换tab到高级配置'''
        self.index_detail_switch(text="高级配置")

    def index_detail_switch_to_index_state(self):
        '''切换tab到索引状态'''
        self.index_detail_switch(text="索引状态")

    def index_detail_switch_to_index_field(self):
        '''切换tab到索引字段'''
        self.index_detail_switch(text="索引字段")

    def index_detail_switch_to_index_permission(self):
        '''切换tab到索引权限'''
        self.index_detail_switch(text="索引权限")

    def index_detail_click_add_field(self):
        '''点击添加字段-详情页面'''
        self.click_button(button_name="添加字段")

    def index_detail_field_form_input_name(self, name, index=2):
        '''输入索引字段的名称'''
        self.type(
            xpath='//app-add-fields/form/div[{index}]/div[1]/nz-form-control[1]/div/div/input'.format(index=index), text=name)

    def index_detail_field_form_input_field(self, field, index=2):
        '''输入索引字段的字段'''
        self.type(
            xpath='//app-add-fields/form/div[{index}]/div[2]/nz-form-control[1]/div/div/input'.format(index=index), text=field)

    def index_detail_field_click_confirm(self):
        '''索引字段页面点击【确定】按钮'''
        self.click_button(button_name="确定")

    def index_detail_click_return(self):
        '''索引详情页面点击【返回】'''
        self.click_button(button_name="返回")

    def index_clone_form_input_index_name(self, index_name):
        '''输入克隆名称'''
        self.alert_form_input(label="名称", text=index_name)

    def index_clone_form_input_description(self, description):
        '''输入描述'''
        self.alert_form_textarea(label="说明", text=description)

    def index_clone_form_index_index_prefix(self, index_prefix):
        '''输入索引前缀'''
        self.alert_form_input(label="索引前缀", text=index_prefix)

    def index_clone_form_click_confirm(self):
        '''点击【确定】按钮'''
        self.click_button(button_name="确定")

    def index_filter_input_name(self, index_name):
        '''输入名称'''
        self.form_input(label="名称", text=index_name)


class Index(IndexBase):
    def index_function_add_index(self, index_name, index_prefix):
        '''新增基本索引'''
        self.into_index_menu()
        self.index_list_click_add()
        self.index_form_input_index_name(index_name)
        self.index_form_input_index_prefix(index_prefix)
        self.index_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_index_list()

    def index_function_delete_index(self, index_name):
        '''删除索引'''
        self.into_index_menu()
        self.wait_into_page_index_list()
        self.index_list_operate_click_delete(index_name)
        self.alert_receive()
        self.wait_toast_delete_successfully()
