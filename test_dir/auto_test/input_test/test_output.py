import seldom
from modules.other import Other
from modules.analyser.index.index import Index
from modules.input.output import Output
from config import TestConfig


class OutputTest(seldom.TestCase, Other, Index, Output):
    def start_class(self):
        self.open_website(url=TestConfig.url)
        self.login(username=TestConfig.test_user,
                   password=TestConfig.test_password)

    def end_class(self):
        self.logout()

    @seldom.file_data(file="./test_data/auto_test/input_data/output_data.json", key="test_add_output_of_gelf")
    def test_add_output_of_gelf(self, dto):
        '''添加GELF输出'''
        # 测试步骤
        self.into_output_menu()
        self.wait_into_page_output_list()
        self.output_list_pull_down_list_select(output_type=dto["output_type"])
        self.output_list_click_add_output()
        self.wait_into_page_add_output()
        self.output_form_input_output_name(output_name=dto["output_name"])
        self.output_form_input_addr(addr=dto["addr"])
        self.output_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_output_list()
        # 断言
        self.assertText(text=dto["output_name"])
        # 数据清理
        self.output_function_delete_output(output_name=dto["output_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/output_data.json", key="test_add_output_of_console")
    def test_add_output_of_console(self, dto):
        '''添加控制台输出'''
        # 测试步骤
        self.into_output_menu()
        self.wait_into_page_output_list()
        self.output_list_pull_down_list_select(output_type=dto["output_type"])
        self.output_list_click_add_output()
        self.wait_into_page_add_output()
        self.output_form_input_output_name(output_name=dto["output_name"])
        self.output_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_output_list()
        # 断言
        self.assertText(text=dto["output_name"])
        # 数据清理
        self.output_function_delete_output(output_name=dto["output_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/output_data.json", key="test_add_output_of_engine")
    def test_add_output_of_engine(self, dto):
        '''添加引擎输出'''
        # 前置条件
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        # 测试步骤
        self.into_output_menu()
        self.wait_into_page_output_list()
        self.output_list_pull_down_list_select(output_type=dto["output_type"])
        self.output_list_click_add_output()
        self.wait_into_page_add_output()
        self.output_form_input_output_name(output_name=dto["output_name"])
        self.output_form_select_index(index_name=dto["index_name"])
        self.output_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_output_list()
        # 断言
        self.assertText(text=dto["output_name"])
        # 数据清理
        self.output_function_delete_output(output_name=dto["output_name"])
        self.index_function_delete_index(index_name=dto["index_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/output_data.json", key="test_edit_output")
    def test_edit_output(self, dto):
        '''编辑输出'''
        # 前置条件
        self.output_function_add_output_of_console(
            output_name=dto["output_name"], output_type=dto["output_type"])
        # 测试步骤
        self.into_output_menu()
        self.wait_into_page_output_list()
        self.output_list_click_edit(output_name=dto["output_name"])
        self.wait_into_page_edit_output()
        self.index_form_clear_index_name()
        self.output_form_input_output_name(output_name=dto["output_name_edit"])
        self.output_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_output_list()
        # 断言
        self.assertText(text=dto["output_name_edit"])
        # 数据清理
        self.output_function_delete_output(output_name=dto["output_name_edit"])

    @seldom.file_data(file="./test_data/auto_test/input_data/output_data.json", key="test_delete_output")
    def test_delete_output(self, dto):
        '''删除输出'''
        # 前置条件
        self.output_function_add_output_of_console(
            output_name=dto["output_name"], output_type=dto["output_type"])
        # 测试步骤
        self.into_output_menu()
        self.wait_into_page_output_list()
        self.output_list_click_delete(output_name=dto["output_name"])
        self.alert_receive()
        self.wait_toast_delete_successfully()
        # 断言
        self.assertNotText(text=dto["output_name"])


if __name__ == "__main__":
    from seldom import ChromeConfig
    from selenium.webdriver import ChromeOptions
    ChromeConfig.command_executor = "chromedriver.exe"
    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('--ignore-certificate-errors')
    ChromeConfig.options = options
    # seldom.main(case="test_output.OutputTest.test_delete_output_0",
    #             browser='gc', debug=True)
    seldom.main(case="test_output.OutputTest",
                browser='gc', debug=True)
