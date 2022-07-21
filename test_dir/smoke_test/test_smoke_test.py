import seldom
from modules.methods import Method
from scripts.tcp_data_send import send_syslog_tcp
from config import TestConfig


class SmokeTesting(seldom.TestCase, Method):
    def start_class(self):
        self.open_website(url=TestConfig.url)
        self.login(username=TestConfig.test_user,
                   password=TestConfig.test_password)
        # self.init_linux_log()

    @seldom.file_data(file="./test_data/smoke_test/smoke_data.json", key="test_add_linux_log")
    def test_add_linux_log(self, dto):
        '''添加linux日志'''
        # self.add_flow(flow_name=dto["flow_name"])
        # self.add_simple_rule_for_flow(flow_name=dto["flow_name"])
        # self.activate_flow(flow_name=dto["flow_name"])

        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        self.interface_function_add_interface_of_syslog_tcp(
            interface_type=dto["interface_type"], interface_name=dto["interface_name"], interface_port=dto["interface_port"])
        self.interface_function_enable_port_mapping(
            interface_name=dto["interface_name"])
        self.stream_function_add_stream(
            stream_name=dto["stream_name"], stream_description=dto["stream_description"])
        self.stream_function_add_rule_for_stream(
            stream_name=dto["stream_name"], interface_name=dto["interface_name"])
        self.stream_function_add_output_for_stream(
            stream_name=dto["stream_name"], output_name=dto["output_name"], index_name=dto["index_name"])
        self.stream_function_run_stream(stream_name=dto["stream_name"])
        send_syslog_tcp(url=TestConfig.url, port=dto["interface_port"])
        self.sleep(10)
        # 断言
        self.view_log(index_name=dto["index_name"])
        self.assertElement(xpath=dto["assert_xpath"])
        # 数据清理
        self.index_function_delete_index(index_name=dto["index_name"])
        self.output_function_delete_output(output_name=dto["output_name"])
        self.stream_function_delete_stream(stream_name=dto["stream_name"])
        self.interface_function_delete_interface(
            interface_name=dto["interface_name"])
        # self.delete_flow(flow_name=dto["flow_name"])

    # @seldom.file_data(file="./test_data/smoke_test/smoke_test.json", key="test_add_resolution")
    # def test_add_resolution(self,dto):
    #     '''添加解析器'''
    #     send_syslog_tcp(url=TestConfig.url,port="514")
    #     ret = self.add_copy_resolution(interface_name=dto["interface_name"],index_name=dto["index_name"],resolution_filed=dto["resolution_filed"],resolution_title=dto["resolution_title"])
    #     # self.assertTrue(ret)
    #     send_syslog_tcp(url=TestConfig.url,port="514")
    #     self.sleep(10)
    #     self.view_log_detail(index_name=dto["index_name"])
    #     self.assertText(dto["resolution_filed"])
    #     self.delete_copy_resolution(interface_name=dto["interface_name"],resolution_title=dto["resolution_title"])

    def end_class(self):
        # self.delete_init_linux_log()
        self.logout()


if __name__ == "__main__":
    from seldom import ChromeConfig
    from selenium.webdriver import ChromeOptions
    ChromeConfig.command_executor = "chromedriver.exe"
    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('--ignore-certificate-errors')
    ChromeConfig.options = options
    seldom.main(case="test_smoke_test.SmokeTesting.test_add_linux_log_0",
                browser='gc', debug=True)
    # seldom.main(path="debug_run.py",browser='gc',debug=True)
