import seldom
from modules.analyser.index.index import Index
from modules.other import Other
from config import TestConfig


class IndexTest(seldom.TestCase, Other, Index):
    def start_class(self):
        self.open_website(url=TestConfig.url)
        self.login(username=TestConfig.test_user,
                   password=TestConfig.test_password)

    def end_class(self):
        self.logout()

    @seldom.file_data(file="./test_data/auto_test/analyser_data/index/index_data.json", key="test_add_index")
    def test_add_index(self, dto):
        '''新增索引'''
        # 测试步骤
        self.into_index_menu()
        self.wait_into_page_index_list()
        self.index_list_click_add()
        self.wait_into_page_index_add()
        self.index_form_input_index_name(index_name=dto["index_name"])
        self.index_form_input_index_description(
            index_description=dto["index_description"])
        self.index_form_input_index_prefix(index_prefix=dto["index_prefix"])
        self.index_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_index_list()
        # 断言
        self.assertText(text=dto["index_name"])
        # 数据清理
        self.index_function_delete_index(index_name=dto["index_name"])

    @seldom.file_data(file="./test_data/auto_test/analyser_data/index/index_data.json", key="test_add_index_of_template")
    def test_add_index_of_template(self, dto):
        '''新增索引-根据模板'''
        #  测试步骤
        self.into_index_menu()
        self.wait_into_page_index_list()
        self.index_list_click_add()
        self.wait_into_page_index_add()
        self.index_form_input_index_name(index_name=dto["index_name"])
        self.index_form_input_index_description(
            index_description=dto["index_description"])
        self.index_form_select_template(template_name=dto["template_name"])
        self.index_form_input_index_prefix(index_prefix=dto["index_prefix"])
        self.index_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_index_list()
        # 断言
        self.assertText(text=dto["index_name"])
        # 数据清理
        self.index_function_delete_index(index_name=dto["index_name"])

    @seldom.file_data(file="./test_data/auto_test/analyser_data/index/index_data.json", key="test_edit_index")
    def test_edit_index(self, dto):
        '''编辑索引'''
        # 前置条件
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        # 测试步骤
        self.into_index_menu()
        self.wait_into_page_index_list()
        self.index_list_operate_click_edit(index_name=dto["index_name"])
        self.wait_into_page_index_edit()
        self.index_form_clear_index_name()
        self.index_form_input_index_name(index_name=dto["index_name_edit"])
        self.index_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_index_list()

        # 断言
        self.assertText(text=dto["index_name_edit"])
        # 数据清理
        self.index_function_delete_index(index_name=dto["index_name_edit"])

    @seldom.file_data(file="./test_data/auto_test/analyser_data/index/index_data.json", key="test_delete_index")
    def test_delete_index(self, dto):
        '''删除索引'''
        # 前置条件
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        # 测试步骤
        self.into_index_menu()
        self.wait_into_page_index_list()
        self.index_list_operate_click_delete(index_name=dto["index_name"])
        self.alert_receive()
        self.wait_toast_delete_successfully()
        # 断言
        self.assertNotText(text=dto["index_name"])

    @seldom.file_data(file="./test_data/auto_test/analyser_data/index/index_data.json", key="test_add_index_field")
    def test_add_index_field(self, dto):
        '''新增索引字段'''
        # 前置条件
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        # 测试步骤
        self.into_index_menu()
        self.wait_into_page_index_list()
        self.index_list_operate_click_detail(index_name=dto["index_name"])
        self.wait_into_page_index_detail()
        self.index_detail_switch_to_index_field()
        self.index_detail_click_add_field()
        self.index_detail_field_form_input_name(name=dto["name"])
        self.index_detail_field_form_input_field(field=dto["field"])
        self.index_detail_field_click_confirm()
        self.wait_toast_save_successfully()
        # 断言
        self.assertText(text=dto["name"])
        # 数据清理
        self.index_detail_click_return()
        self.index_function_delete_index(index_name=dto["index_name"])

    @seldom.file_data(file="./test_data/auto_test/analyser_data/index/index_data.json", key="test_clone_index")
    def test_clone_index(self, dto):
        '''克隆索引'''
        # 前置条件
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        # 测试步骤
        self.into_index_menu()
        self.wait_into_page_index_list()
        self.index_list_operate_click_clone(index_name=dto["index_name"])
        self.index_clone_form_input_index_name(
            index_name=dto["index_name_clone"])
        self.index_clone_form_input_description(
            description=dto["description_clone"])
        self.index_clone_form_index_index_prefix(
            index_prefix=dto["index_prefix_clone"])
        self.index_clone_form_click_confirm()
        self.wait_toast_save_successfully()
        self.wait_into_page_index_list()
        # 断言
        self.assertText(text=dto["index_name_clone"])
        # 数据清理
        self.index_function_delete_index(index_name=dto["index_name"])
        self.index_function_delete_index(index_name=dto["index_name_clone"])

    @seldom.file_data(file="./test_data/auto_test/analyser_data/index/index_data.json", key="test_filter_for_index_list")
    def test_filter_for_index_list(self, dto):
        '''索引列表过滤器成功筛选数据'''
        # 前置条件
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        # 测试步骤
        self.into_index_menu()
        self.wait_into_page_index_list()
        self.filter_click_open()
        self.index_filter_input_name(index_name=dto["index_name"])
        self.filter_click_select()
        # 断言
        self.assertText(text=dto["index_name"])
        # 数据清理
        self.filter_click_reset()
        self.filter_click_close()
        self.index_function_delete_index(index_name=dto["index_name"])


if __name__ == "__main__":
    from seldom import ChromeConfig
    from selenium.webdriver import ChromeOptions
    ChromeConfig.command_executor = "chromedriver.exe"
    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('--ignore-certificate-errors')
    ChromeConfig.options = options
    seldom.main(case="test_index.IndexTest.test_clone_index_0",
                browser='gc', debug=True)
    # seldom.main(case="test_index.IndexTest",
    #             browser='gc', debug=True)
