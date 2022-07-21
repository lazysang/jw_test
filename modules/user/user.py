from common.utils import Utils


class UserPage(Utils):
    def into_user_menu(self):
        '''进入角色管理'''
        # 进入平台用户管理
        self.into_module("平台用户管理")
        # 进入用户管理
        self.into_menu("用户管理")

    def wait_into_page_user_list(self):
        '''等待进入【用户管理】'''
        self.wait_into_page("用户列表")

    def wait_into_page_user_add(self):
        '''等待进入新建用户页面'''
        self.wait_into_page("新建用户")

    def wait_into_page_user_edit(self):
        '''等待进入编辑用户页面'''
        self.wait_into_page("编辑信息")

    def wait_into_page_user_account_edit(self):
        '''等待进入编辑账户页面'''
        self.wait_into_page("编辑账户信息")

    def user_list_click_add(self):
        '''点击【新增用户】按钮'''
        self.click_button(button_name="新增用户")

    def user_list_operate_click_detail(self, name):
        '''列表操作点击【查看】'''
        self.move_to_operate_button(text=name)
        self.click_operate_button(text="查看")

    def user_list_operate_click_edit(self, name):
        '''列表操作点击【编辑】'''
        self.move_to_operate_button(text=name)
        self.click_operate_button(text="编辑")

    def user_list_operate_click_edit_account(self, name):
        '''列表操作点击【编辑账户】'''
        self.move_to_operate_button(text=name)
        self.click_operate_button(text="编辑账户")

    def user_list_operate_click_disable(self, name):
        '''列表操作点击【禁用】'''
        self.move_to_operate_button(text=name)
        self.click_operate_button(text="禁用")

    def user_list_operate_click_enable(self, name):
        '''列表操作点击【启用】'''
        self.move_to_operate_button(text=name)
        self.click_operate_button(text="启用")

    def user_list_operate_click_move(self, name):
        '''列表操作点击【移动】'''
        self.move_to_operate_button(text=name)
        self.click_operate_button(text="移动")

    def user_list_operate_click_delete(self, name):
        '''列表操作点击【删除】'''
        self.move_to_operate_button(text=name)
        self.click_operate_button(text="删除")

    def user_form_input_user_name(self, user_name):
        '''输入用户名'''
        self.form_input(label="用户名", text=user_name)

    def user_form_input_password(self, password):
        '''输入密码'''
        self.form_input(label="密码", text=password)

    def user_form_input_new_password(self, new_password):
        '''输入新密码'''
        self.form_input(label="新密码", text=new_password)

    def user_form_input_confirm_password(self, confirm_password):
        '''输入确认密码'''
        self.form_input(label="确认密码", text=confirm_password)

    def user_form_input_name(self, name):
        '''输入姓名'''
        self.form_input(label="姓名", text=name)

    def uesr_form_clear_name(self):
        '''清空用姓名'''
        self.form_input_clear(label="姓名")

    def user_form_input_mail(self, mail):
        '''输入邮箱'''
        self.form_input(label="邮箱", text=mail)

    def user_form_select_role(self, role_name):
        '''选择角色'''
        # 点击角色下拉框
        self.form_select_click(label="角色")
        self.pull_down_list_select(text=role_name)

    def user_form_input_phone_number(self, phone_number):
        '''输入联系方式'''
        self.form_input(label="联系方式", text=phone_number)

    def user_form_input_remark(self, remark):
        '''输入备注'''
        self.form_input(label="备注", text=remark)

    def user_form_click_checkbox_limit(self):
        '''点击【启用登录限制】'''
        self.form_checkbox_click(label="启用登录限制")

    def user_form_click_save(self):
        '''点击【保存】'''
        self.click_button(button_name="保存")

    def user_filter_input_name(self, name):
        '''输入名称'''
        self.form_input(label="名称", text=name)


class User(UserPage):
    def user_function_add_user(self, user_name, password, name, mail, role_name):
        '''新增用户'''
        self.into_user_menu()
        self.wait_into_page_user_list()
        self.user_list_click_add()
        self.wait_into_page_user_add()
        self.user_form_input_user_name(user_name)
        self.user_form_input_password(password)
        self.user_form_input_name(name)
        self.user_form_input_mail(mail)
        self.user_form_select_role(role_name)
        self.user_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_user_list()

    def user_function_delete_user(self, name):
        '''删除用户'''
        self.into_user_menu()
        self.wait_into_page_user_list()
        self.user_list_operate_click_delete(name)
        self.alert_receive()
        self.wait_toast_delete_successfully()
