from common.utils import Utils


class RolePage(Utils):
    def into_role_menu(self):
        '''进入角色管理'''
        # 进入平台用户管理
        self.into_module("平台用户管理")
        # 进入角色管理
        self.into_menu("角色管理")

    def wait_into_page_role_list(self):
        '''等待进入【角色管理】'''
        self.wait_into_page("角色列表")

    def wait_into_page_role_add(self):
        '''等待进入新建角色页面'''
        self.wait_into_page("新建角色")

    def wait_into_page_role_edit(self):
        '''等待进入编辑角色页面'''
        self.wait_into_page("编辑角色")

    def role_list_click_add(self):
        '''点击【新建角色】按钮'''
        self.click_button(button_name="新建角色")

    def role_list_operate_click_edit(self, role_name):
        '''列表操作点击【编辑】'''
        self.move_to_operate_button(text=role_name)
        self.click_operate_button(text="编辑")

    def role_list_operate_click_delete(self, role_name):
        '''列表操作点击【删除】'''
        self.move_to_operate_button(text=role_name)
        self.click_operate_button(text="删除")

    def role_form_input_role_name(self, role_name):
        '''输入角色名称'''
        self.form_input(label="名称", text=role_name)

    def role_form_clear_role_name(self):
        '''清空角色名称'''
        self.form_input_clear(label="名称")

    def role_form_input_role_remark(self, role_remark):
        '''输入角色备注'''
        self.form_input(label="备注", text=role_remark)

    def role_form_auth_click_checkbox(self):
        '''勾选一个权限'''
        self.click(
            xpath='//nz-tree-node-title[@title="安全策略配置"]/preceding-sibling::nz-tree-node-checkbox')

    def role_form_click_save(self):
        '''点击【保存】'''
        self.click_button(button_name="保存")

    def role_filter_input_name(self, role_name):
        '''输入名称'''
        self.form_input(label="名称", text=role_name)


class Role(RolePage):
    def role_function_add_role(self, role_name):
        '''新增角色'''
        self.into_role_menu()
        self.wait_into_page_role_list()
        self.role_list_click_add()
        self.wait_into_page_role_add()
        self.role_form_input_role_name(role_name)
        self.role_form_auth_click_checkbox()
        self.role_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_role_list()

    def role_function_delete_role(self, role_name):
        '''删除角色'''
        self.into_role_menu()
        self.wait_into_page_role_list()
        self.role_list_operate_click_delete(role_name)
        self.alert_receive()
        self.wait_toast_delete_successfully()
