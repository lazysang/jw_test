import seldom
from modules.other import Other
from modules.user.user import User
from modules.user.role import Role
from config import TestConfig


class UserTest(seldom.TestCase, Other, User, Role):
    def start_class(self):
        self.open_website(url=TestConfig.url)
        self.login(username=TestConfig.test_user,
                   password=TestConfig.test_password)

    def end_class(self):
        self.logout()

    @seldom.file_data(file="./test_data/auto_test/user_data/user_data.json",
                      key="test_add_user")
    def test_add_user(self, dto):
        '''成功新增用户信息'''
        # 前置条件
        self.role_function_add_role(role_name=dto["role_name"])
        # 测试步骤
        self.into_user_menu()
        self.wait_into_page_user_list()
        self.user_list_click_add()
        self.wait_into_page_user_add()
        self.user_form_input_user_name(user_name=dto["user_name"])
        self.user_form_input_password(password=dto["password"])
        self.user_form_input_name(name=dto["name"])
        self.user_form_input_mail(mail=dto["mail"])
        self.user_form_select_role(role_name=dto["role_name"])
        self.user_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_user_list()
        # 断言
        self.assertText(text=dto["name"])
        # 数据清理
        self.user_function_delete_user(name=dto["name"])
        self.role_function_delete_role(role_name=dto["role_name"])

    @seldom.file_data(file="./test_data/auto_test/user_data/user_data.json",
                      key="test_edit_user")
    def test_edit_user(self, dto):
        '''成功修改用户信息'''
        # 前置条件
        self.role_function_add_role(role_name=dto["role_name"])
        self.user_function_add_user(user_name=dto["user_name"], password=dto["password"],
                                    name=dto["name"], mail=dto["mail"], role_name=dto["role_name"])
        # 测试步骤
        self.into_user_menu()
        self.wait_into_page_user_list()
        self.user_list_operate_click_edit(name=dto["name"])
        self.wait_into_page_user_edit()
        self.uesr_form_clear_name()
        self.user_form_input_name(name=dto["name_edit"])
        self.user_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_user_list()
        # 断言
        self.assertText(text=dto["name_edit"])
        # 数据清理
        self.user_function_delete_user(name=dto["name_edit"])
        self.role_function_delete_role(role_name=dto["role_name"])

    @seldom.file_data(file="./test_data/auto_test/user_data/user_data.json",
                      key="test_edit_user_account")
    def test_edit_user_account(self, dto):
        '''成功编辑用户账户'''
        # 前置条件
        self.role_function_add_role(role_name=dto["role_name"])
        self.user_function_add_user(user_name=dto["user_name"], password=dto["password"],
                                    name=dto["name"], mail=dto["mail"], role_name=dto["role_name"])
        # 测试步骤
        self.into_user_menu()
        self.wait_into_page_user_list()
        self.user_list_operate_click_edit_account(name=dto["name"])
        self.wait_into_page_user_account_edit()
        self.user_form_input_new_password(new_password=dto["new_password"])
        self.user_form_input_confirm_password(
            confirm_password=dto["confirm_password"])
        self.user_form_click_save()
        toast = self.wait_toast_save_successfully()
        self.wait_into_page_user_list()
        # 断言
        self.assertTrue(toast)
        # 数据清理
        self.user_function_delete_user(name=dto["name"])
        self.role_function_delete_role(role_name=dto["role_name"])

    @seldom.file_data(file="./test_data/auto_test/user_data/user_data.json",
                      key="test_delete_user")
    def test_delete_user(self, dto):
        '''成功删除用户'''
        # 前置条件
        self.role_function_add_role(role_name=dto["role_name"])
        self.user_function_add_user(user_name=dto["user_name"], password=dto["password"],
                                    name=dto["name"], mail=dto["mail"], role_name=dto["role_name"])
        # 测试步骤
        self.into_user_menu()
        self.wait_into_page_user_list()
        self.user_list_operate_click_delete(name=dto["name"])
        self.alert_receive()
        self.wait_toast_delete_successfully()
        # 断言
        self.assertNotText(text=dto["name"])
        # 数据清理
        self.role_function_delete_role(role_name=dto["role_name"])

    @seldom.file_data(file="./test_data/auto_test/user_data/user_data.json",
                      key="test_filter_for_user_list")
    def test_filter_for_user_list(self, dto):
        '''成功过滤列表数据'''
        # 前置条件
        self.role_function_add_role(role_name=dto["role_name"])
        self.user_function_add_user(user_name=dto["user_name"], password=dto["password"],
                                    name=dto["name"], mail=dto["mail"], role_name=dto["role_name"])
        # 测试步骤
        self.into_user_menu()
        self.wait_into_page_user_list()
        self.filter_click_open()
        self.user_filter_input_name(name=dto["name"])
        self.filter_click_select()
        # 断言
        self.assertText(text=dto["name"])
        # 数据清理
        self.filter_click_reset()
        self.filter_click_close()
        self.user_function_delete_user(name=dto["name"])
        self.role_function_delete_role(role_name=dto["role_name"])


if __name__ == "__main__":
    from seldom import ChromeConfig
    from selenium.webdriver import ChromeOptions
    ChromeConfig.command_executor = "chromedriver.exe"
    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('--ignore-certificate-errors')
    ChromeConfig.options = options
    seldom.main(case="test_user.UserTest.test_filter_for_user_list_0",
                browser='gc', debug=True)
    # seldom.main(case="test_user.UserTest",
    #             browser='gc', debug=True)
