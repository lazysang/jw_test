import seldom
from modules.input.interface import Interface
from modules.other import Other
from config import TestConfig


class InterfaceTest(seldom.TestCase, Other, Interface):
    def start_class(self):
        self.open_website(url=TestConfig.url)
        self.login(username=TestConfig.test_user,
                   password=TestConfig.test_password)

    def end_class(self):
        self.logout()

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_add_interface")
    def test_add_interface_of_beats(self, dto):
        '''新增beats接口'''
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_pull_down_list_select(
            interface_type=dto["interface_type"])
        self.interface_list_click_add_interface()
        self.wait_into_page_interfase_add()
        self.interface_form_click_checkbox_global()
        self.interface_form_input_interface_name(
            interface_name=dto["interface_name"])
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()
        # 断言
        self.assertText(text=dto["interface_name"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_add_interface_of_cef_amqp")
    def test_add_interface_of_cef_amqp(self, dto):
        '''新增cef_amqp接口'''
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_pull_down_list_select(
            interface_type=dto["interface_type"])
        self.interface_list_click_add_interface()
        self.wait_into_page_interfase_add()
        self.interface_form_click_checkbox_global()
        self.interface_form_input_interface_name(
            interface_name=dto["interface_name"])
        self.interface_form_input_broker_addr(broker_addr=dto["broker_addr"])
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()
        # 断言
        self.assertText(text=dto["interface_name"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_add_interface_of_cef_kafka")
    def test_add_interface_of_cef_kafka(self, dto):
        '''新增cef_kafka接口'''
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_pull_down_list_select(
            interface_type=dto["interface_type"])
        self.interface_list_click_add_interface()
        self.wait_into_page_interfase_add()
        self.interface_form_click_checkbox_global()
        self.interface_form_input_interface_name(
            interface_name=dto["interface_name"])
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()
        # 断言
        self.assertText(text=dto["interface_name"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_add_interface_of_cef_tcp")
    def test_add_interface_of_cef_tcp(self, dto):
        '''新增cef_tcp接口'''
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_pull_down_list_select(
            interface_type=dto["interface_type"])
        self.interface_list_click_add_interface()
        self.wait_into_page_interfase_add()
        self.interface_form_click_checkbox_global()
        self.interface_form_input_interface_name(
            interface_name=dto["interface_name"])
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()
        # 断言
        self.assertText(text=dto["interface_name"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_add_interface_of_cef_udp")
    def test_add_interface_of_cef_udp(self, dto):
        '''新增cef_udp接口'''
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_pull_down_list_select(
            interface_type=dto["interface_type"])
        self.interface_list_click_add_interface()
        self.wait_into_page_interfase_add()
        self.interface_form_click_checkbox_global()
        self.interface_form_input_interface_name(
            interface_name=dto["interface_name"])
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()
        # 断言
        self.assertText(text=dto["interface_name"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_add_interface_of_netflow_udp")
    def test_add_interface_of_netflow_udp(self, dto):
        '''新增netflow_udp接口'''
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_pull_down_list_select(
            interface_type=dto["interface_type"])
        self.interface_list_click_add_interface()
        self.wait_into_page_interfase_add()
        self.interface_form_click_checkbox_global()
        self.interface_form_input_interface_name(
            interface_name=dto["interface_name"])
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()
        # 断言
        self.assertText(text=dto["interface_name"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_add_interface_of_gelf_amqp")
    def test_add_interface_of_gelf_amqp(self, dto):
        '''新增gelf_amqp接口'''
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_pull_down_list_select(
            interface_type=dto["interface_type"])
        self.interface_list_click_add_interface()
        self.wait_into_page_interfase_add()
        self.interface_form_click_checkbox_global()
        self.interface_form_input_interface_name(
            interface_name=dto["interface_name"])
        self.interface_form_input_broker_addr(broker_addr=dto["broker_addr"])
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()
        # 断言
        self.assertText(text=dto["interface_name"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_add_interface_of_gelf_http")
    def test_add_interface_of_gelf_http(self, dto):
        '''新增gelf_http接口'''
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_pull_down_list_select(
            interface_type=dto["interface_type"])
        self.interface_list_click_add_interface()
        self.wait_into_page_interfase_add()
        self.interface_form_click_checkbox_global()
        self.interface_form_input_interface_name(
            interface_name=dto["interface_name"])
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()
        # 断言
        self.assertText(text=dto["interface_name"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_add_interface_of_gelf_kafka")
    def test_add_interface_of_gelf_kafka(self, dto):
        '''新增gelf_kafka接口'''
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_pull_down_list_select(
            interface_type=dto["interface_type"])
        self.interface_list_click_add_interface()
        self.wait_into_page_interfase_add()
        self.interface_form_click_checkbox_global()
        self.interface_form_input_interface_name(
            interface_name=dto["interface_name"])
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()
        # 断言
        self.assertText(text=dto["interface_name"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_add_interface_of_gelf_kafka")
    def test_add_interface_of_gelf_kafka(self, dto):
        '''新增gelf_kafka接口'''
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_pull_down_list_select(
            interface_type=dto["interface_type"])
        self.interface_list_click_add_interface()
        self.wait_into_page_interfase_add()
        self.interface_form_click_checkbox_global()
        self.interface_form_input_interface_name(
            interface_name=dto["interface_name"])
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()
        # 断言
        self.assertText(text=dto["interface_name"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_add_interface_of_gelf_tcp")
    def test_add_interface_of_gelf_tcp(self, dto):
        '''新增gelf_tcp接口'''
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_pull_down_list_select(
            interface_type=dto["interface_type"])
        self.interface_list_click_add_interface()
        self.wait_into_page_interfase_add()
        self.interface_form_click_checkbox_global()
        self.interface_form_input_interface_name(
            interface_name=dto["interface_name"])
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()
        # 断言
        self.assertText(text=dto["interface_name"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_add_interface_of_gelf_udp")
    def test_add_interface_of_gelf_udp(self, dto):
        '''新增gelf_udp接口'''
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_pull_down_list_select(
            interface_type=dto["interface_type"])
        self.interface_list_click_add_interface()
        self.wait_into_page_interfase_add()
        self.interface_form_click_checkbox_global()
        self.interface_form_input_interface_name(
            interface_name=dto["interface_name"])
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()
        # 断言
        self.assertText(text=dto["interface_name"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_add_interface_of_rawplaintext_amqp")
    def test_add_interface_of_rawplaintext_amqp(self, dto):
        '''新增rawplaintext_amqp接口'''
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_pull_down_list_select(
            interface_type=dto["interface_type"])
        self.interface_list_click_add_interface()
        self.wait_into_page_interfase_add()
        self.interface_form_click_checkbox_global()
        self.interface_form_input_interface_name(
            interface_name=dto["interface_name"])
        self.interface_form_input_broker_addr(broker_addr=dto["broker_addr"])
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()
        # 断言
        self.assertText(text=dto["interface_name"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_add_interface_of_rawplaintext_kafka")
    def test_add_interface_of_rawplaintext_kafka(self, dto):
        '''新增rawplaintext_kafka接口'''
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_pull_down_list_select(
            interface_type=dto["interface_type"])
        self.interface_list_click_add_interface()
        self.wait_into_page_interfase_add()
        self.interface_form_click_checkbox_global()
        self.interface_form_input_interface_name(
            interface_name=dto["interface_name"])
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()
        # 断言
        self.assertText(text=dto["interface_name"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_add_interface_of_rawplaintext_tcp")
    def test_add_interface_of_rawplaintext_tcp(self, dto):
        '''新增rawplaintext_tcp接口'''
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_pull_down_list_select(
            interface_type=dto["interface_type"])
        self.interface_list_click_add_interface()
        self.wait_into_page_interfase_add()
        self.interface_form_click_checkbox_global()
        self.interface_form_input_interface_name(
            interface_name=dto["interface_name"])
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()
        # 断言
        self.assertText(text=dto["interface_name"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_add_interface_of_rawplaintext_udp")
    def test_add_interface_of_rawplaintext_udp(self, dto):
        '''新增rawplaintext_udp接口'''
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_pull_down_list_select(
            interface_type=dto["interface_type"])
        self.interface_list_click_add_interface()
        self.wait_into_page_interfase_add()
        self.interface_form_click_checkbox_global()
        self.interface_form_input_interface_name(
            interface_name=dto["interface_name"])
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()
        # 断言
        self.assertText(text=dto["interface_name"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_add_interface_of_syslog_amqp")
    def test_add_interface_of_syslog_amqp(self, dto):
        '''新增syslog_amqp接口'''
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_pull_down_list_select(
            interface_type=dto["interface_type"])
        self.interface_list_click_add_interface()
        self.wait_into_page_interfase_add()
        self.interface_form_click_checkbox_global()
        self.interface_form_input_interface_name(
            interface_name=dto["interface_name"])
        self.interface_form_input_broker_addr(broker_addr=dto["broker_addr"])
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()
        # 断言
        self.assertText(text=dto["interface_name"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_add_interface_of_syslog_kafka")
    def test_add_interface_of_syslog_kafka(self, dto):
        '''新增syslog_kafka接口'''
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_pull_down_list_select(
            interface_type=dto["interface_type"])
        self.interface_list_click_add_interface()
        self.wait_into_page_interfase_add()
        self.interface_form_click_checkbox_global()
        self.interface_form_input_interface_name(
            interface_name=dto["interface_name"])
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()
        # 断言
        self.assertText(text=dto["interface_name"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_add_interface_of_syslog_tcp")
    def test_add_interface_of_syslog_tcp(self, dto):
        '''新增syslog_tcp接口'''
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_pull_down_list_select(
            interface_type=dto["interface_type"])
        self.interface_list_click_add_interface()
        self.wait_into_page_interfase_add()
        self.interface_form_click_checkbox_global()
        self.interface_form_input_interface_name(
            interface_name=dto["interface_name"])
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()
        # 断言
        self.assertText(text=dto["interface_name"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_add_interface_of_syslog_udp")
    def test_add_interface_of_syslog_udp(self, dto):
        '''新增syslog_udp接口'''
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_pull_down_list_select(
            interface_type=dto["interface_type"])
        self.interface_list_click_add_interface()
        self.wait_into_page_interfase_add()
        self.interface_form_click_checkbox_global()
        self.interface_form_input_interface_name(
            interface_name=dto["interface_name"])
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()
        # 断言
        self.assertText(text=dto["interface_name"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_edit_interface_of_syslog_tcp")
    def test_edit_interface_of_syslog_tcp(self, dto):
        '''编辑syslog_tcp接口'''
        # 前置条件
        self.interface_function_add_interface_of_syslog_tcp(
            interface_type=dto["interface_type"], interface_name=dto["interface_name"], interface_port=dto["interface_port"])
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_operate_click_edit_interface(
            interface_name=dto["interface_name"])
        self.wait_into_page_interfase_edit()
        self.interface_form_clear_interface_name()
        self.interface_form_input_interface_name(
            interface_name=dto["interface_name_edit"])
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()
        # 断言
        self.assertText(text=dto["interface_name_edit"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name_edit"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_delete_interface_of_syslog_tcp")
    def test_delete_interface_of_syslog_tcp(self, dto):
        '''删除syslog_tcp接口'''
        # 前置条件
        self.interface_function_add_interface_of_syslog_tcp(
            interface_type=dto["interface_type"], interface_name=dto["interface_name"], interface_port=dto["interface_port"])
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_operate_click_delete_interface(
            interface_name=dto["interface_name"])
        self.alert_receive()
        self.wait_toast_delete_successfully()
        # 断言
        self.assertNotText(text=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_interface_add_static_property")
    def test_interface_add_static_property(self, dto):
        '''添加静态属性'''
        # 前置条件
        self.interface_function_add_interface_of_syslog_tcp(
            interface_type=dto["interface_type"], interface_name=dto["interface_name"], interface_port=dto["interface_port"])
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_operate_click_add_static_property(
            interface_name=dto["interface_name"])
        self.interface_static_property_form_input_field(field=dto["field"])
        self.interface_static_property_form_input_value(value=dto["value"])
        self.interface_static_property_form_click_confirm()
        self.wait_toast_add_static_proprety_successfully()
        # 断言
        self.interface_list_click_static_property(
            interface_name=dto["interface_name"])
        self.assertText(text=dto["field"])
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_interface_delete_static_property")
    def test_interface_delete_static_property(self, dto):
        '''删除静态属性'''
        # 前置条件
        self.interface_function_add_interface_of_syslog_tcp(
            interface_type=dto["interface_type"], interface_name=dto["interface_name"], interface_port=dto["interface_port"])
        self.interface_function_add_static_proprty(
            interface_name=dto["interface_name"], field=dto["field"], value=dto["value"])
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_click_static_property(
            interface_name=dto["interface_name"])
        self.interface_list_click_delete_static_property(
            interface_name=dto["interface_name"])
        self.alert_receive()
        self.wait_toast_delete_successfully()
        # 断言
        try:
            self.interface_list_click_static_property(
                interface_name=dto["interface_name"])
        except:
            self.assertTrue(True)
        else:
            self.assertTrue(False)
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_enable_port_mapping")
    def test_enable_port_mapping(self, dto):
        '''启用端口映射'''
        # 前置条件
        self.interface_function_add_interface_of_syslog_tcp(
            interface_type=dto["interface_type"], interface_name=dto["interface_name"], interface_port=dto["interface_port"])
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_operate_click_enable_port_mapping(
            interface_name=dto["interface_name"])
        self.alert_receive()
        self.wait_toast_edit_successfully()
        # 断言
        self.assertText("已启用")
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])

    @seldom.file_data(file="./test_data/auto_test/input_data/interface_data.json", key="test_disable_port_mapping")
    def test_disable_port_mapping(self, dto):
        '''禁用端口映射'''
        # 前置条件
        self.interface_function_add_interface_of_syslog_tcp(
            interface_type=dto["interface_type"], interface_name=dto["interface_name"], interface_port=dto["interface_port"])
        self.interface_function_enable_port_mapping(
            interface_name=dto["interface_name"])
        # 测试步骤
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_operate_click_disable_port_mapping(
            interface_name=dto["interface_name"])
        self.alert_receive()
        self.wait_toast_edit_successfully()
        # 断言
        self.assertText("已禁用")
        # 数据清理
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])


if __name__ == "__main__":
    from seldom import ChromeConfig
    from selenium.webdriver import ChromeOptions
    ChromeConfig.command_executor = "chromedriver.exe"
    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('--ignore-certificate-errors')
    ChromeConfig.options = options
    seldom.main(case="test_interface.InterfaceTest.test_disable_port_mapping_0",
                browser='gc', debug=True)
    # seldom.main(case="test_interface.InterfaceTest",
    #             browser='gc', debug=True)
