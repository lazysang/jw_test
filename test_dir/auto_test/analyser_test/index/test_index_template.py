import seldom
from modules.analyser.index.index_template import IndexTemplate
from modules.other import Other
from config import TestConfig


class IndexTemplateTest(seldom.TestCase, Other, IndexTemplate):
    def start_class(self):
        self.open_website(url=TestConfig.url)
        self.login(username=TestConfig.test_user,
                   password=TestConfig.test_password)

    def end_class(self):
        self.logout()

    @seldom.file_data(file="./test_data/auto_test/analyser_data/index/template_data.json", key="test_add_index_template")
    def test_add_index_template(self, dto):
        '''新增索引模板'''
        # 测试步骤
        self.into_index_template_menu()
        self.wait_into_page_index_template_list()
        self.index_template_list_click_add()
        self.wait_into_page_index_template_add()
        self.index_template_form_input_template_name(
            template_name=dto["template_name"])
        self.index_template_form_click_add_field()
        self.index_template_form_input_name(name=dto["name"])
        self.index_template_form_input_field(field=dto["field"])
        self.index_template_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_index_template_list()
        # 断言
        self.assertText(text=dto["template_name"])
        # 数据清理
        self.index_template_function_delete_template(
            template_name=dto["template_name"])

    @seldom.file_data(file="./test_data/auto_test/analyser_data/index/template_data.json", key="test_edit_index_template")
    def test_edit_index_template(self, dto):
        '''编辑索引模板'''
        # 前置条件
        self.index_template_function_add_template(
            template_name=dto["template_name"], name=dto["name"], field=dto["field"])
        # 测试步骤
        self.into_index_template_menu()
        self.wait_into_page_index_template_list()
        self.index_template_list_operate_click_detail(
            template_name=dto["template_name"])
        self.index_template_detail_click_edit()
        self.index_template_form_clear_template_name()
        self.index_template_form_input_template_name(
            template_name=dto["template_name_edit"])
        self.index_template_form_click_save()
        self.wait_toast_save_successfully()
        self.index_template_detail_click_return()
        self.wait_into_page_index_template_list()
        # 断言
        self.assertText(text=dto["template_name_edit"])
        # 数据清理
        self.index_template_function_delete_template(
            template_name=dto["template_name_edit"])

    @seldom.file_data(file="./test_data/auto_test/analyser_data/index/template_data.json", key="test_delete_index_template")
    def test_delete_index_template(self, dto):
        '''删除索引模板'''
        # 前置条件
        self.index_template_function_add_template(
            template_name=dto["template_name"], name=dto["name"], field=dto["field"])
        # 测试步骤
        self.into_index_template_menu()
        self.wait_into_page_index_template_list()
        self.index_template_list_operate_click_delete(
            template_name=dto["template_name"])
        self.alert_receive()
        self.wait_toast_delete_successfully()
        # 断言
        self.assertNotText(text=dto["template_name"])

    @seldom.file_data(file="./test_data/auto_test/analyser_data/index/template_data.json", key="test_clone_index_template")
    def test_clone_index_template(self, dto):
        '''克隆索引模板'''
        # 前置条件
        self.index_template_function_add_template(
            template_name=dto["template_name"], name=dto["name"], field=dto["field"])
        # 测试步骤
        self.into_index_template_menu()
        self.wait_into_page_index_template_list()
        self.index_template_list_operate_click_clone(
            template_name=dto["template_name"])
        self.index_template_clone_form_input_template_name(
            template_name=dto["template_name_clone"])
        self.index_template_clone_form_click_confirm()
        self.wait_toast_save_successfully()
        self.wait_into_page_index_template_list()
        # 断言
        self.assertText(text=dto["template_name_clone"])
        # 数据清理
        self.index_template_function_delete_template(
            template_name=dto["template_name"])
        self.index_template_function_delete_template(
            template_name=dto["template_name_clone"])

    @seldom.file_data(file="./test_data/auto_test/analyser_data/index/template_data.json", key="test_filter_for_index_template_list")
    def test_filter_for_index_template_list(self, dto):
        '''索引模板列表过滤器成功筛选数据'''
        # 前置条件
        self.index_template_function_add_template(
            template_name=dto["template_name"], name=dto["name"], field=dto["field"])
        # 测试步骤
        self.into_index_template_menu()
        self.wait_into_page_index_template_list()
        self.filter_click_open()
        self.index_template_filter_input_name(
            template_name=dto["template_name"])
        self.index_template_filter_click_select()
        # 断言
        self.assertText(text=dto["template_name"])
        # 数据清理
        self.index_template_filter_click_reset()
        self.filter_click_close()
        self.index_template_function_delete_template(
            template_name=dto["template_name"])


if __name__ == "__main__":
    from seldom import ChromeConfig
    from selenium.webdriver import ChromeOptions
    ChromeConfig.command_executor = "chromedriver.exe"
    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('--ignore-certificate-errors')
    ChromeConfig.options = options
    seldom.main(case="test_index_template.IndexTemplateTest.test_filter_for_index_template_list_0",
                browser='gc', debug=True)
    # seldom.main(case="test_index_template.IndexTemplateTest",
    #             browser='gc', debug=True)
