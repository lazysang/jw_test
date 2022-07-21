import seldom
from modules.analyser.alarm.alarm_template import AlarmTemplate
from modules.other import Other
from config import TestConfig


class AlarmTemplateTest(seldom.TestCase, Other, AlarmTemplate):
    def start_class(self):
        self.open_website(url=TestConfig.url)
        self.login(username=TestConfig.test_user,
                   password=TestConfig.test_password)

    def end_class(self):
        self.logout()

    @seldom.file_data(
        file="./test_data/auto_test/analyser_data/alarm/alarm_template_data.json",
        key="test_add_alarm_template")
    def test_add_alarm_template(self, dto):
        '''新增告警模板'''
        # 测试步骤
        self.into_alarm_template_menu()
        self.wait_into_page_alarm_template_list()
        self.alarm_template_list_click_add()
        self.wait_into_page_alarm_template_add()
        self.alarm_template_form_input_template_name(
            template_name=dto["template_name"])
        self.alarm_template_form_input_addressee(addressee=dto["addressee"])
        self.alarm_template_form_input_subject(subject=dto["subject"])
        self.alarm_template_form_input_alarm_text(alarm_text=dto["alarm_text"])
        self.alarm_template_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_alarm_template_list()
        # 断言
        self.assertText(text=dto["template_name"])
        # 数据清理
        self.alarm_template_function_delete_alarm_template(
            template_name=dto["template_name"])

    @seldom.file_data(
        file="./test_data/auto_test/analyser_data/alarm/alarm_template_data.json",
        key="test_edit_alarm_template")
    def test_edit_alarm_template(self, dto):
        '''编辑告警模板'''
        # 前置条件
        self.alarm_template_function_add_alarm_template(
            template_name=dto["template_name"], addressee=dto["addressee"], subject=dto["subject"], alarm_text=dto["alarm_text"])
        # 测试步骤
        self.into_alarm_template_menu()
        self.wait_into_page_alarm_template_list()
        self.alarm_template_list_operate_click_edit(
            template_name=dto["template_name"])
        self.wait_into_page_alarm_template_edit()
        self.alarm_template_form_clear_template_name()
        self.alarm_template_form_input_template_name(
            template_name=dto["template_name_edit"])
        self.alarm_template_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_alarm_template_list()
        # 断言
        self.assertText(text=dto["template_name_edit"])
        # 数据清理
        self.alarm_template_function_delete_alarm_template(
            template_name=dto["template_name_edit"])

    @seldom.file_data(
        file="./test_data/auto_test/analyser_data/alarm/alarm_template_data.json",
        key="test_delete_alarm_template")
    def test_delete_alarm_template(self, dto):
        '''删除告警模板'''
        # 前置条件
        self.alarm_template_function_add_alarm_template(
            template_name=dto["template_name"], addressee=dto["addressee"], subject=dto["subject"], alarm_text=dto["alarm_text"])
        # 测试步骤
        self.into_alarm_template_menu()
        self.wait_into_page_alarm_template_list()
        self.alarm_template_list_operate_click_delete(
            template_name=dto["template_name"])
        self.alert_receive()
        self.wait_toast_delete_successfully()
        # 断言
        self.assertNotText(text=dto["template_name"])

    @seldom.file_data(
        file="./test_data/auto_test/analyser_data/alarm/alarm_template_data.json",
        key="test_filter_for_alarm_template_list")
    def test_filter_for_alarm_template_list(self, dto):
        '''告警模板列表过滤器成功筛选数据'''
        # 前置条件
        self.alarm_template_function_add_alarm_template(
            template_name=dto["template_name"], addressee=dto["addressee"], subject=dto["subject"], alarm_text=dto["alarm_text"])
        # 测试步骤
        self.into_alarm_template_menu()
        self.wait_into_page_alarm_template_list()
        self.filter_click_open()
        self.alarm_template_filter_input_name(
            template_name=dto["template_name"])
        self.filter_click_select()
        # 断言
        self.assertText(text=dto["template_name"])
        # 数据清理
        self.filter_click_reset()
        self.filter_click_close()
        self.alarm_template_function_delete_alarm_template(
            template_name=dto["template_name"])


if __name__ == "__main__":
    from seldom import ChromeConfig
    from selenium.webdriver import ChromeOptions
    ChromeConfig.command_executor = "chromedriver.exe"
    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('--ignore-certificate-errors')
    ChromeConfig.options = options
    # seldom.main(case="test_alarm_template.AlarmTemplateTest.test_filter_for_alarm_template_list_0",
    #             browser='gc', debug=True)
    seldom.main(case="test_alarm_template.AlarmTemplateTest",
                browser='gc', debug=True)
