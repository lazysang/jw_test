import seldom
from modules.input.stream import Stream
from modules.other import Other
from modules.analyser.index.index import Index
from modules.input.interface import Interface
from modules.input.output import Output
from config import TestConfig


class StreamTest(seldom.TestCase, Other, Stream, Index, Interface, Output):
    def start_class(self):
        self.open_website(url=TestConfig.url)
        self.login(username=TestConfig.test_user,
                   password=TestConfig.test_password)

    def end_class(self):
        self.logout()

    @seldom.file_data(file="./test_data/auto_test/input_data/stream_data.json", key="test_add_stream")
    def test_add_stream(self, dto):
        '''新增数据流'''
        # 测试步骤
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        self.stream_list_click_add()
        self.wait_into_page_add_stream()
        self.stream_form_input_stream_name(stream_name=dto["stream_name"])
        self.stream_form_input_stream_description(
            stream_description=dto["stream_description"])
        self.stream_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_stram_list()
        # 断言
        self.assertText(text=dto["stream_name"])
        # 数据清理
        self.stream_function_delete_stream(stream_name=dto["stream_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/stream_data.json", key="test_edit_stream")
    def test_edit_stream(self, dto):
        '''编辑数据流'''
        # 前置条件
        self.stream_function_add_stream(
            stream_name=dto["stream_name"], stream_description=dto["stream_description"])
        # 测试步骤
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        self.stream_list_operation_click_edit(stream_name=dto["stream_name"])
        self.wait_into_page_edit_stream()
        self.stream_form_clear_stream_name()
        self.stream_form_input_stream_name(stream_name=dto["stream_name_edit"])
        self.stream_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_stram_list()
        # 断言
        self.assertText(text=dto["stream_name_edit"])
        # 数据清理
        self.stream_function_delete_stream(stream_name=dto["stream_name_edit"])

    @seldom.file_data(file="./test_data/auto_test/input_data/stream_data.json", key="test_delete_stream")
    def test_delete_stream(self, dto):
        '''删除数据流'''
        # 前置条件
        self.stream_function_add_stream(
            stream_name=dto["stream_name"], stream_description=dto["stream_description"])
        # 测试步骤
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        self.stream_list_operation_click_delete(stream_name=dto["stream_name"])
        self.alert_receive()
        self.wait_toast_delete_successfully()
        # 断言
        self.assertNotText(text=dto["stream_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/stream_data.json", key="test_clone_stream")
    def test_clone_stream(self, dto):
        '''克隆数据流'''
        # 前置条件
        self.stream_function_add_stream(
            stream_name=dto["stream_name"], stream_description=dto["stream_description"])
        # 测试步骤
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        self.stream_list_operation_click_clone(stream_name=dto["stream_name"])
        self.stream_clone_form_input_stream_name(
            stream_name=dto["stream_name_clone"])
        self.stream_clone_form_input_stream_description(
            stream_description=dto["stream_description_clone"])
        self.stream_clone_form_click_confirm()
        self.wait_toast_save_successfully()
        # 断言
        self.assertText(text=dto["stream_name_clone"])
        # 数据清理
        self.stream_function_delete_stream(stream_name=dto["stream_name"])
        self.stream_function_delete_stream(
            stream_name=dto["stream_name_clone"])

    @seldom.file_data(file="./test_data/auto_test/input_data/stream_data.json", key="test_run_stream")
    def test_run_stream(self, dto):
        '''运行数据流'''
        # 前置条件
        self.stream_function_add_stream(
            stream_name=dto["stream_name"], stream_description=dto["stream_description"])
        # 测试步骤
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        self.stream_list_operation_click_run(stream_name=dto["stream_name"])
        self.wait_toast_run_successfully()
        # 断言
        self.assertText(text="正在运行")
        # 数据清理
        self.stream_function_delete_stream(stream_name=dto["stream_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/stream_data.json", key="test_close_stream")
    def test_close_stream(self, dto):
        '''关闭数据流'''
        # 前置条件
        self.stream_function_add_stream(
            stream_name=dto["stream_name"], stream_description=dto["stream_description"])
        self.stream_function_run_stream(stream_name=dto["stream_name"])
        # 测试步骤
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        self.stream_list_operation_click_close(stream_name=dto["stream_name"])
        self.alert_receive()
        self.wait_toast_close_successfully()
        # 断言
        self.assertText(text="未运行")
        # 数据清理
        self.stream_function_delete_stream(stream_name=dto["stream_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/stream_data.json", key="test_filter_for_stream_list")
    def test_filter_for_stream_list(self, dto):
        '''数据流列表过滤器成功筛选数据'''
        # 前置条件
        self.stream_function_add_stream(
            stream_name=dto["stream_name"], stream_description=dto["stream_description"])
        # 测试步骤
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        self.filter_click_open()
        self.stream_filter_input_name(stream_name=dto["stream_name"])
        # self.index_filter_click_select()
        self.filter_click_select()
        # 断言
        self.assertText(text=dto["stream_name"])
        # 数据清理
        self.filter_click_reset()
        self.filter_click_close()
        self.stream_function_delete_stream(stream_name=dto["stream_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/stream_data.json", key="test_add_stream_rule_of_exact_match")
    def test_add_stream_rule_of_exact_match(self, dto):
        '''添加数据流规则-精确匹配'''
        # 前置条件
        self.stream_function_add_stream(
            stream_name=dto["stream_name"], stream_description=dto["stream_description"])
        # 测试步骤
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        # 测试步骤
        self.stream_list_operation_click_edit_rule(
            stream_name=dto["stream_name"])
        self.wait_into_page_edit_stream_rule()
        self.stream_rule_click_add_rule()
        self.stream_rule_form_select_condition(condition=dto["condition"])
        self.stream_rule_form_input_field(field=dto["field"])
        self.stream_rule_form_input_value(value=dto["value"])
        self.stream_rule_form_click_confirm()
        self.wait_toast_save_successfully()
        # 断言
        self.assertText(text=dto["condition"])
        # 数据清理
        self.stream_rule_click_return()
        self.stream_function_delete_stream(stream_name=dto["stream_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/stream_data.json", key="test_add_stream_rule_of_match_regular")
    def test_add_stream_rule_of_match_regular(self, dto):
        '''添加数据流规则-匹配正则表达式'''
        # 前置条件
        self.stream_function_add_stream(
            stream_name=dto["stream_name"], stream_description=dto["stream_description"])
        # 测试步骤
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        # 测试步骤
        self.stream_list_operation_click_edit_rule(
            stream_name=dto["stream_name"])
        self.wait_into_page_edit_stream_rule()
        self.stream_rule_click_add_rule()
        self.stream_rule_form_select_condition(condition=dto["condition"])
        self.stream_rule_form_input_field(field=dto["field"])
        self.stream_rule_form_input_value(value=dto["value"])
        self.stream_rule_form_click_confirm()
        self.wait_toast_save_successfully()
        # 断言
        self.assertText(text=dto["condition"])
        # 数据清理
        self.stream_rule_click_return()
        self.stream_function_delete_stream(stream_name=dto["stream_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/stream_data.json", key="test_add_stream_rule_of_greater_than")
    def test_add_stream_rule_of_greater_than(self, dto):
        '''添加数据流规则-大于'''
        # 前置条件
        self.stream_function_add_stream(
            stream_name=dto["stream_name"], stream_description=dto["stream_description"])
        # 测试步骤
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        # 测试步骤
        self.stream_list_operation_click_edit_rule(
            stream_name=dto["stream_name"])
        self.wait_into_page_edit_stream_rule()
        self.stream_rule_click_add_rule()
        self.stream_rule_form_select_condition(condition=dto["condition"])
        self.stream_rule_form_input_field(field=dto["field"])
        self.stream_rule_form_input_value(value=dto["value"])
        self.stream_rule_form_click_confirm()
        self.wait_toast_save_successfully()
        # 断言
        self.assertText(text=dto["condition"])
        # 数据清理
        self.stream_rule_click_return()
        self.stream_function_delete_stream(stream_name=dto["stream_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/stream_data.json", key="test_add_stream_rule_of_less_than")
    def test_add_stream_rule_of_less_than(self, dto):
        '''添加数据流规则-小于'''
        # 前置条件
        self.stream_function_add_stream(
            stream_name=dto["stream_name"], stream_description=dto["stream_description"])
        # 测试步骤
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        # 测试步骤
        self.stream_list_operation_click_edit_rule(
            stream_name=dto["stream_name"])
        self.wait_into_page_edit_stream_rule()
        self.stream_rule_click_add_rule()
        self.stream_rule_form_select_condition(condition=dto["condition"])
        self.stream_rule_form_input_field(field=dto["field"])
        self.stream_rule_form_input_value(value=dto["value"])
        self.stream_rule_form_click_confirm()
        self.wait_toast_save_successfully()
        # 断言
        self.assertText(text=dto["condition"])
        # 数据清理
        self.stream_rule_click_return()
        self.stream_function_delete_stream(stream_name=dto["stream_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/stream_data.json", key="test_add_stream_rule_of_exist")
    def test_add_stream_rule_of_exist(self, dto):
        '''添加数据流规则-存在'''
        # 前置条件
        self.stream_function_add_stream(
            stream_name=dto["stream_name"], stream_description=dto["stream_description"])
        # 测试步骤
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        # 测试步骤
        self.stream_list_operation_click_edit_rule(
            stream_name=dto["stream_name"])
        self.wait_into_page_edit_stream_rule()
        self.stream_rule_click_add_rule()
        self.stream_rule_form_select_condition(condition=dto["condition"])
        self.stream_rule_form_input_field(field=dto["field"])
        self.stream_rule_form_click_confirm()
        self.wait_toast_save_successfully()
        # 断言
        self.assertText(text=dto["condition"])
        # 数据清理
        self.stream_rule_click_return()
        self.stream_function_delete_stream(stream_name=dto["stream_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/stream_data.json", key="test_add_stream_rule_of_include")
    def test_add_stream_rule_of_include(self, dto):
        '''添加数据流规则-包含'''
        # 前置条件
        self.stream_function_add_stream(
            stream_name=dto["stream_name"], stream_description=dto["stream_description"])
        # 测试步骤
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        # 测试步骤
        self.stream_list_operation_click_edit_rule(
            stream_name=dto["stream_name"])
        self.wait_into_page_edit_stream_rule()
        self.stream_rule_click_add_rule()
        self.stream_rule_form_select_condition(condition=dto["condition"])
        self.stream_rule_form_input_field(field=dto["field"])
        self.stream_rule_form_input_value(value=dto["value"])
        self.stream_rule_form_click_confirm()
        self.wait_toast_save_successfully()
        # 断言
        self.assertText(text=dto["condition"])
        # 数据清理
        self.stream_rule_click_return()
        self.stream_function_delete_stream(stream_name=dto["stream_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/stream_data.json", key="test_add_stream_rule_of_never_hit")
    def test_add_stream_rule_of_never_hit(self, dto):
        '''添加数据流规则-永远命中'''
        # 前置条件
        self.stream_function_add_stream(
            stream_name=dto["stream_name"], stream_description=dto["stream_description"])
        # 测试步骤
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        # 测试步骤
        self.stream_list_operation_click_edit_rule(
            stream_name=dto["stream_name"])
        self.wait_into_page_edit_stream_rule()
        self.stream_rule_click_add_rule()
        self.stream_rule_form_select_condition(condition=dto["condition"])
        self.stream_rule_form_click_confirm()
        self.wait_toast_save_successfully()
        # 断言
        self.assertText(text=dto["condition"])
        # 数据清理
        self.stream_rule_click_return()
        self.stream_function_delete_stream(stream_name=dto["stream_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/stream_data.json", key="test_add_stream_rule_of_match_interface")
    def test_add_stream_rule_of_match_interface(self, dto):
        '''添加数据流规则-匹配接口'''
        # 前置条件
        self.interface_function_add_interface_of_syslog_tcp(
            interface_type=dto["interface_type"], interface_name=dto["interface_name"], interface_port=dto["interface_port"])
        self.stream_function_add_stream(
            stream_name=dto["stream_name"], stream_description=dto["stream_description"])
        # 测试步骤
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        self.stream_list_operation_click_edit_rule(
            stream_name=dto["stream_name"])
        self.wait_into_page_edit_stream_rule()
        self.stream_rule_click_add_rule()
        self.stream_rule_form_select_condition(condition=dto["condition"])
        self.stream_rule_form_select_interface(
            interface_name=dto["interface_name"])
        self.stream_rule_form_click_confirm()
        self.wait_toast_save_successfully()
        # 断言
        self.assertText(text=dto["condition"])
        # 数据清理
        self.stream_rule_click_return()
        self.stream_function_delete_stream(stream_name=dto["stream_name"])
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/stream_data.json", key="test_add_stream_rule_of_gelf_output")
    def test_add_stream_rule_of_gelf_output(self, dto):
        '''添加数据流规则-添加GELF输出'''
        # 前置条件
        self.stream_function_add_stream(
            stream_name=dto["stream_name"], stream_description=dto["stream_description"])
        # 测试步骤
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        self.stream_list_operation_click_edit_rule(
            stream_name=dto["stream_name"])
        self.wait_into_page_edit_stream_rule()
        self.stream_rule_switch_to_output()
        self.stream_rule_select_output(mode=dto["mode"])
        self.stream_rule_click_add_output()
        self.wait_into_page_add_output()
        self.stream_rule_output_form_input_output_name(output_name=dto["output_name"])
        self.stream_rule_output_form_input_addr(addr=dto["addr"])
        self.stream_rule_output_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_edit_stream_rule()
        # 断言
        self.assertText(text=dto["output_name"])
        # 数据清理
        self.stream_rule_click_return()
        self.stream_function_delete_stream(stream_name=dto["stream_name"])
        self.output_function_delete_output(output_name=dto["output_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/stream_data.json", key="test_add_stream_rule_of_console")
    def test_add_stream_rule_of_console(self, dto):
        '''添加数据流规则-添加控制台输出'''
        # 前置条件
        self.stream_function_add_stream(
            stream_name=dto["stream_name"], stream_description=dto["stream_description"])
        # 测试步骤
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        self.stream_list_operation_click_edit_rule(
            stream_name=dto["stream_name"])
        self.wait_into_page_edit_stream_rule()
        self.stream_rule_switch_to_output()
        self.stream_rule_select_output(mode=dto["mode"])
        self.stream_rule_click_add_output()
        self.wait_into_page_add_output()
        self.stream_rule_output_form_input_output_name(output_name=dto["output_name"])
        self.stream_rule_output_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_edit_stream_rule()
        # 断言
        self.assertText(text=dto["output_name"])
        # 数据清理
        self.stream_rule_click_return()
        self.stream_function_delete_stream(stream_name=dto["stream_name"])
        self.output_function_delete_output(output_name=dto["output_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/stream_data.json", key="test_add_stream_rule_of_engine")
    def test_add_stream_rule_of_engine(self, dto):
        '''添加数据流规则-添加引擎输出'''
        # 前置条件
        self.stream_function_add_stream(
            stream_name=dto["stream_name"], stream_description=dto["stream_description"])
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        # 测试步骤
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        self.stream_list_operation_click_edit_rule(
            stream_name=dto["stream_name"])
        self.wait_into_page_edit_stream_rule()
        self.stream_rule_switch_to_output()
        self.stream_rule_select_output(mode=dto["mode"])
        self.stream_rule_click_add_output()
        self.wait_into_page_add_output()
        self.stream_rule_output_form_input_output_name(output_name=dto["output_name"])
        self.output_form_select_index(index_name=dto["index_name"])
        self.stream_rule_output_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_edit_stream_rule()
        # 断言
        self.assertText(text=dto["output_name"])
        # 数据清理
        self.stream_rule_click_return()
        self.stream_function_delete_stream(stream_name=dto["stream_name"])
        self.output_function_delete_output(output_name=dto["output_name"])
        self.index_function_delete_index(index_name=dto["index_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/stream_data.json", key="test_add_stream_rule_of_exist_output")
    def test_add_stream_rule_of_exist_output(self, dto):
        '''编辑数据流规则-添加存在的输出'''
        self.stream_function_add_stream(
            stream_name=dto["stream_name"], stream_description=dto["stream_description"])
        self.output_function_add_output_of_console(
            output_type=dto["output_type"], output_name=dto["output_name"])
        # 测试步骤
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        self.stream_list_operation_click_edit_rule(
            stream_name=dto["stream_name"])
        self.wait_into_page_edit_stream_rule()
        self.stream_rule_switch_to_output()
        self.stream_rule_select_exist_output(output_name=dto["output_name"])
        self.stream_rule_click_add_exist_output()
        self.wait_toast_add_successfully()
        # 断言
        self.assertText(text=dto["output_name"])
        # 数据清理
        self.stream_rule_click_return()
        self.wait_into_page_stram_list()
        self.stream_function_delete_stream(stream_name=dto["stream_name"])
        self.output_function_delete_output(output_name=dto["output_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/stream_data.json", key="test_edit_stream_rule_of_engine")
    def test_edit_stream_rule_of_engine(self, dto):
        '''编辑数据流规则-引擎输出'''
        # 前置条件
        self.stream_function_add_stream(
            stream_name=dto["stream_name"], stream_description=dto["stream_description"])
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        self.stream_function_add_output_for_stream(
            stream_name=dto["stream_name"], output_name=dto["output_name"], index_name=dto["index_name"])
        # 测试步骤
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        self.stream_list_operation_click_edit_rule(
            stream_name=dto["stream_name"])
        self.wait_into_page_edit_stream_rule()
        self.stream_rule_switch_to_output()
        self.stream_rule_output_list_click_edit(output_name=dto["output_name"])
        self.wait_into_page_edit_output()
        self.stream_rule_output_form_clear_output_name()
        self.stream_rule_output_form_input_output_name(output_name=dto["output_name_edit"])
        self.stream_rule_output_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_edit_stream_rule()
        # 断言
        self.assertText(text=dto["output_name_edit"])
        # 数据清理
        self.stream_rule_click_return()
        self.wait_into_page_stram_list()
        self.stream_function_delete_stream(stream_name=dto["stream_name"])
        self.output_function_delete_output(output_name=dto["output_name_edit"])
        self.index_function_delete_index(index_name=dto["index_name"])


    @seldom.file_data(file="./test_data/auto_test/input_data/stream_data.json", key="test_remove_stream_rule_of_engine")
    def test_remove_stream_rule_of_engine(self, dto):
        '''移除数据流规则-引擎输出'''
        # 前置条件
        self.stream_function_add_stream(
            stream_name=dto["stream_name"], stream_description=dto["stream_description"])
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        self.stream_function_add_output_for_stream(
            stream_name=dto["stream_name"], output_name=dto["output_name"], index_name=dto["index_name"])
        # 测试步骤
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        self.stream_list_operation_click_edit_rule(
            stream_name=dto["stream_name"])
        self.wait_into_page_edit_stream_rule()
        self.stream_rule_switch_to_output()
        self.stream_rule_output_list_click_remove(output_name=dto["output_name"])
        self.alert_receive()
        # 断言
        self.assertNotText(text=dto["output_name"])
        # 数据清理
        self.stream_rule_click_return()
        self.wait_into_page_stram_list()
        self.stream_function_delete_stream(stream_name=dto["stream_name"])
        self.output_function_delete_output(output_name=dto["output_name"])
        self.index_function_delete_index(index_name=dto["index_name"])

if __name__ == "__main__":
    from seldom import ChromeConfig
    from selenium.webdriver import ChromeOptions
    ChromeConfig.command_executor = "chromedriver.exe"
    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('--ignore-certificate-errors')
    ChromeConfig.options = options
    seldom.main(case="test_stream.StreamTest.test_remove_stream_rule_of_engine_0",
                browser='gc', debug=True)
    # seldom.main(case="test_stream.StreamTest",
    #             browser='gc', debug=True)
