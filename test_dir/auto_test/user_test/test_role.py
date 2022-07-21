import seldom
from modules.other import Other
from modules.user.role import Role
from modules.user.user import User
from config import TestConfig


class RoleTest(seldom.TestCase, Other, Role, User):
    def start_class(self):
        self.open_website(url=TestConfig.url)
        self.login(username=TestConfig.test_user,
                   password=TestConfig.test_password)

    def end_class(self):
        self.logout()

    @seldom.file_data(file="./test_data/auto_test/user_data/role_data.json",
                      key="test_add_role")
    def test_add_role(self, dto):
        '''成功新增角色信息'''
        # 测试步骤
        self.into_role_menu()
        self.wait_into_page_role_list()
        self.role_list_click_add()
        self.wait_into_page_role_add()
        self.role_form_input_role_name(role_name=dto["role_name"])
        self.role_form_auth_click_checkbox()
        self.role_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_role_list()
        # 断言
        self.assertText(text=dto["role_name"])
        # 数据清理
        self.role_function_delete_role(role_name=dto["role_name"])

    @seldom.file_data(file="./test_data/auto_test/user_data/role_data.json",
                      key="test_edit_role")
    def test_edit_role(self, dto):
        '''成功修改角色信息 '''
        # 前置条件
        self.role_function_add_role(role_name=dto["role_name"])
        # 测试步骤
        self.into_role_menu()
        self.wait_into_page_role_list()
        self.role_list_operate_click_edit(role_name=dto["role_name"])
        self.wait_into_page_role_edit()
        self.role_form_clear_role_name()
        self.role_form_input_role_name(role_name=dto["role_name_edit"])
        self.role_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_role_list()
        # 断言
        self.assertText(text=dto["role_name_edit"])
        # 数据清理
        self.role_function_delete_role(role_name=dto["role_name_edit"])

    @seldom.file_data(file="./test_data/auto_test/user_data/role_data.json",
                      key="test_delete_role")
    def test_delete_role(self, dto):
        '''删除角色（未绑定用户）'''
        # 前置条件
        self.role_function_add_role(role_name=dto["role_name"])
        # 测试步骤
        self.into_role_menu()
        self.wait_into_page_role_list()
        self.role_list_operate_click_delete(role_name=dto["role_name"])
        self.alert_receive()
        self.wait_toast_delete_successfully()
        self.wait_into_page_role_list()
        # 断言
        self.assertNotText(text=dto["role_name"])

    @seldom.file_data(file="./test_data/auto_test/user_data/role_data.json",
                      key="test_delete_role_bind_user")
    def test_delete_role_bind_user(self, dto):
        '''删除角色（已被用户绑定）'''
        # 前置条件
        self.role_function_add_role(role_name=dto["role_name"])
        self.user_function_add_user(user_name=dto["user_name"], password=dto["password"],
                                    name=dto["name"], mail=dto["mail"], role_name=dto["role_name"])
        # 测试步骤
        self.into_role_menu()
        self.wait_into_page_role_list()
        self.role_list_operate_click_delete(role_name=dto["role_name"])
        self.alert_receive()
        # self.wait_toast_delete_successfully()
        self.wait_toast(toast_text=dto["toast_text"])
        self.wait_into_page_role_list()
        # 断言
        self.assertText(text=dto["role_name"])
        # 数据清理
        self.user_function_delete_user(name=dto["name"])
        self.role_function_delete_role(role_name=dto["role_name"])

    @seldom.file_data(file="./test_data/auto_test/user_data/role_data.json",
                      key="test_filter_for_role_list")
    def test_filter_for_role_list(self, dto):
        '''成功过滤列表数据'''
        # 前置条件
        self.role_function_add_role(role_name=dto["role_name"])
        # 测试步骤
        self.into_role_menu()
        self.wait_into_page_role_list()
        self.filter_click_open()
        self.role_filter_input_name(role_name=dto["role_name"])
        self.filter_click_select()
        # 断言
        self.assertText(text=dto["role_name"])
        # 数据清理
        self.filter_click_reset()
        self.filter_click_close()
        self.role_function_delete_role(role_name=dto["role_name"])

    def test_fail(self):
        '''fail用例'''
        self.assertTrue(False)

    def test_error(self):
        '''error用例'''
        print(asd)

    @seldom.skip()
    def test_skip(self):
        '''skip用例'''
        pass


if __name__ == "__main__":
    from seldom import ChromeConfig
    from selenium.webdriver import ChromeOptions
    ChromeConfig.command_executor = "chromedriver.exe"
    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('--ignore-certificate-errors')
    ChromeConfig.options = options
    seldom.main(case="test_role.RoleTest.test_filter_for_role_list_0",
                browser='gc', debug=True)
    # seldom.main(case="test_role.RoleTest",
    #             browser='gc', debug=True)
