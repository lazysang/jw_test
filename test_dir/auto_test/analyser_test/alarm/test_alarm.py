import seldom
from modules.analyser.alarm.alarm import Alarm
from modules.analyser.alarm.alarm_template import AlarmTemplate
from modules.analyser.index.index import Index
from modules.other import Other
from config import TestConfig


class AlarmTest(seldom.TestCase, Other, Alarm, AlarmTemplate, Index):
    def start_class(self):
        self.open_website(url=TestConfig.url)
        self.login(username=TestConfig.test_user,
                   password=TestConfig.test_password)

    def end_class(self):
        self.logout()

    @seldom.file_data(
        file="./test_data/auto_test/analyser_data/alarm/alarm_data.json",
        key="test_add_alarm_of_type_once")
    def test_add_alarm_of_type_once(self, dto):
        '''新增告警-类型为执行一次'''
        # 前置条件
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        self.alarm_template_function_add_alarm_template(
            template_name=dto["template_name"], addressee=dto["addressee"],
            subject=dto["subject"], alarm_text=dto["alarm_text"])
        # 测试步骤
        self.into_alarm_menu()
        self.wait_into_page_alarm_list()
        self.alarm_list_click_add()
        self.wait_into_page_alarm_add()
        self.alarm_form_input_alarm_name(alarm_name=dto["alarm_name"])
        self.alarm_form_plan_select_type(plan_type=dto["plan_type"])
        self.alarm_form_plan_input_execute_time(
            execute_time=dto["execute_time"])
        self.alarm_form_click_add_execute()
        self.alarm_form_execute_alart_select_execute_type(
            execute_type=dto["execute_type"])
        self.alarm_form_execute_alart_clicl_confirm()
        self.alarm_form_execute_select_index(index_name=dto["index_name"])
        self.alarm_form_execute_input_save_field(save_field=dto["save_field"])
        self.alarm_form_select_send_inform(info_type=dto["info_type"])
        self.alarm_form_select_template(template_name=dto["template_name"])
        self.alarm_form_click_add()
        self.alarm_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_alarm_list()
        # 断言
        self.assertText(text=dto["alarm_name"])
        # 数据清理
        self.alarm_function_delete_alarm(alarm_name=dto["alarm_name"])
        self.alarm_template_function_delete_alarm_template(
            template_name=dto["template_name"])
        self.index_function_delete_index(index_name=dto["index_name"])

    @seldom.file_data(
        file="./test_data/auto_test/analyser_data/alarm/alarm_data.json",
        key="test_add_alarm_of_type_minute")
    def test_add_alarm_of_type_minute(self, dto):
        '''新增告警-类型为按分钟'''
        # 前置条件
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        self.alarm_template_function_add_alarm_template(
            template_name=dto["template_name"], addressee=dto["addressee"],
            subject=dto["subject"], alarm_text=dto["alarm_text"])
        # 测试步骤
        self.into_alarm_menu()
        self.wait_into_page_alarm_list()
        self.alarm_list_click_add()
        self.wait_into_page_alarm_add()
        self.alarm_form_input_alarm_name(alarm_name=dto["alarm_name"])
        self.alarm_form_plan_select_type(plan_type=dto["plan_type"])
        self.alarm_form_plan_input_interval(interval=dto["interval"])
        self.alarm_form_click_add_execute()
        self.alarm_form_execute_alart_select_execute_type(
            execute_type=dto["execute_type"])
        self.alarm_form_execute_alart_clicl_confirm()
        self.alarm_form_execute_select_index(index_name=dto["index_name"])
        self.alarm_form_execute_input_save_field(save_field=dto["save_field"])
        self.alarm_form_select_send_inform(info_type=dto["info_type"])
        self.alarm_form_select_template(template_name=dto["template_name"])
        self.alarm_form_click_add()
        self.alarm_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_alarm_list()
        # 断言
        self.assertText(text=dto["alarm_name"])
        # 数据清理
        self.alarm_function_delete_alarm(alarm_name=dto["alarm_name"])
        self.alarm_template_function_delete_alarm_template(
            template_name=dto["template_name"])
        self.index_function_delete_index(index_name=dto["index_name"])

    @seldom.file_data(
        file="./test_data/auto_test/analyser_data/alarm/alarm_data.json",
        key="test_add_alarm_of_type_hour")
    def test_add_alarm_of_type_hour(self, dto):
        '''新增告警-类型为按小时'''
        # 前置条件
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        self.alarm_template_function_add_alarm_template(
            template_name=dto["template_name"], addressee=dto["addressee"],
            subject=dto["subject"], alarm_text=dto["alarm_text"])
        # 测试步骤
        self.into_alarm_menu()
        self.wait_into_page_alarm_list()
        self.alarm_list_click_add()
        self.wait_into_page_alarm_add()
        self.alarm_form_input_alarm_name(alarm_name=dto["alarm_name"])
        self.alarm_form_plan_select_type(plan_type=dto["plan_type"])
        self.alarm_form_plan_input_interval(interval=dto["interval"])
        self.alarm_form_click_add_execute()
        self.alarm_form_execute_alart_select_execute_type(
            execute_type=dto["execute_type"])
        self.alarm_form_execute_alart_clicl_confirm()
        self.alarm_form_execute_select_index(index_name=dto["index_name"])
        self.alarm_form_execute_input_save_field(save_field=dto["save_field"])
        self.alarm_form_select_send_inform(info_type=dto["info_type"])
        self.alarm_form_select_template(template_name=dto["template_name"])
        self.alarm_form_click_add()
        self.alarm_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_alarm_list()
        # 断言
        self.assertText(text=dto["alarm_name"])
        # 数据清理
        self.alarm_function_delete_alarm(alarm_name=dto["alarm_name"])
        self.alarm_template_function_delete_alarm_template(
            template_name=dto["template_name"])
        self.index_function_delete_index(index_name=dto["index_name"])

    @seldom.file_data(
        file="./test_data/auto_test/analyser_data/alarm/alarm_data.json",
        key="test_add_alarm_of_type_day")
    def test_add_alarm_of_type_day(self, dto):
        '''新增告警-类型为按天'''
        # 前置条件
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        self.alarm_template_function_add_alarm_template(
            template_name=dto["template_name"], addressee=dto["addressee"],
            subject=dto["subject"], alarm_text=dto["alarm_text"])
        # 测试步骤
        self.into_alarm_menu()
        self.wait_into_page_alarm_list()
        self.alarm_list_click_add()
        self.wait_into_page_alarm_add()
        self.alarm_form_input_alarm_name(alarm_name=dto["alarm_name"])
        self.alarm_form_plan_select_type(plan_type=dto["plan_type"])
        self.alarm_form_plan_input_interval(interval=dto["interval"])
        self.alarm_form_click_add_execute()
        self.alarm_form_execute_alart_select_execute_type(
            execute_type=dto["execute_type"])
        self.alarm_form_execute_alart_clicl_confirm()
        self.alarm_form_execute_select_index(index_name=dto["index_name"])
        self.alarm_form_execute_input_save_field(save_field=dto["save_field"])
        self.alarm_form_select_send_inform(info_type=dto["info_type"])
        self.alarm_form_select_template(template_name=dto["template_name"])
        self.alarm_form_click_add()
        self.alarm_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_alarm_list()
        # 断言
        self.assertText(text=dto["alarm_name"])
        # 数据清理
        self.alarm_function_delete_alarm(alarm_name=dto["alarm_name"])
        self.alarm_template_function_delete_alarm_template(
            template_name=dto["template_name"])
        self.index_function_delete_index(index_name=dto["index_name"])

    @seldom.file_data(
        file="./test_data/auto_test/analyser_data/alarm/alarm_data.json",
        key="test_add_alarm_of_type_everyday")
    def test_add_alarm_of_type_everyday(self, dto):
        '''新增告警-类型为每天'''
        # 前置条件
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        self.alarm_template_function_add_alarm_template(
            template_name=dto["template_name"], addressee=dto["addressee"],
            subject=dto["subject"], alarm_text=dto["alarm_text"])
        # 测试步骤
        self.into_alarm_menu()
        self.wait_into_page_alarm_list()
        self.alarm_list_click_add()
        self.wait_into_page_alarm_add()
        self.alarm_form_input_alarm_name(alarm_name=dto["alarm_name"])
        self.alarm_form_plan_select_type(plan_type=dto["plan_type"])
        self.alarm_form_plan_input_interval_day(
            interval_day=dto["interval_day"])
        self.alarm_form_click_add_execute()
        self.alarm_form_execute_alart_select_execute_type(
            execute_type=dto["execute_type"])
        self.alarm_form_execute_alart_clicl_confirm()
        self.alarm_form_execute_select_index(index_name=dto["index_name"])
        self.alarm_form_execute_input_save_field(save_field=dto["save_field"])
        self.alarm_form_select_send_inform(info_type=dto["info_type"])
        self.alarm_form_select_template(template_name=dto["template_name"])
        self.alarm_form_click_add()
        self.alarm_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_alarm_list()
        # 断言
        self.assertText(text=dto["alarm_name"])
        # 数据清理
        self.alarm_function_delete_alarm(alarm_name=dto["alarm_name"])
        self.alarm_template_function_delete_alarm_template(
            template_name=dto["template_name"])
        self.index_function_delete_index(index_name=dto["index_name"])

    @seldom.file_data(
        file="./test_data/auto_test/analyser_data/alarm/alarm_data.json",
        key="test_add_alarm_of_type_weekly")
    def test_add_alarm_of_type_weekly(self, dto):
        '''新增告警-类型为每周'''
        # 前置条件
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        self.alarm_template_function_add_alarm_template(
            template_name=dto["template_name"], addressee=dto["addressee"],
            subject=dto["subject"], alarm_text=dto["alarm_text"])
        # 测试步骤
        self.into_alarm_menu()
        self.wait_into_page_alarm_list()
        self.alarm_list_click_add()
        self.wait_into_page_alarm_add()
        self.alarm_form_input_alarm_name(alarm_name=dto["alarm_name"])
        self.alarm_form_plan_select_type(plan_type=dto["plan_type"])
        self.alarm_form_plan_select_week(week=dto["week"])
        self.alarm_form_plan_input_execute_time_2(
            execute_time=dto["execute_time"])
        self.alarm_form_click_add_execute()
        self.alarm_form_execute_alart_select_execute_type(
            execute_type=dto["execute_type"])
        self.alarm_form_execute_alart_clicl_confirm()
        self.alarm_form_execute_select_index(index_name=dto["index_name"])
        self.alarm_form_execute_input_save_field(save_field=dto["save_field"])
        self.alarm_form_select_send_inform(info_type=dto["info_type"])
        self.alarm_form_select_template(template_name=dto["template_name"])
        self.alarm_form_click_add()
        self.alarm_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_alarm_list()
        # 断言
        self.assertText(text=dto["alarm_name"])
        # 数据清理
        self.alarm_function_delete_alarm(alarm_name=dto["alarm_name"])
        self.alarm_template_function_delete_alarm_template(
            template_name=dto["template_name"])
        self.index_function_delete_index(index_name=dto["index_name"])

    @seldom.file_data(
        file="./test_data/auto_test/analyser_data/alarm/alarm_data.json",
        key="test_add_alarm_of_type_monthly")
    def test_add_alarm_of_type_monthly(self, dto):
        '''新增告警-类型为每月'''
        # 前置条件
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        self.alarm_template_function_add_alarm_template(
            template_name=dto["template_name"], addressee=dto["addressee"],
            subject=dto["subject"], alarm_text=dto["alarm_text"])
        # 测试步骤
        self.into_alarm_menu()
        self.wait_into_page_alarm_list()
        self.alarm_list_click_add()
        self.wait_into_page_alarm_add()
        self.alarm_form_input_alarm_name(alarm_name=dto["alarm_name"])
        self.alarm_form_plan_select_type(plan_type=dto["plan_type"])
        self.alarm_form_plan_input_interval_month(
            interval_month=dto["interval_month"])
        self.alarm_form_plan_input_execute_time_2(
            execute_time=dto["execute_time"])
        self.alarm_form_click_add_execute()
        self.alarm_form_execute_alart_select_execute_type(
            execute_type=dto["execute_type"])
        self.alarm_form_execute_alart_clicl_confirm()
        self.alarm_form_execute_select_index(index_name=dto["index_name"])
        self.alarm_form_execute_input_save_field(save_field=dto["save_field"])
        self.alarm_form_select_send_inform(info_type=dto["info_type"])
        self.alarm_form_select_template(template_name=dto["template_name"])
        self.alarm_form_click_add()
        self.alarm_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_alarm_list()
        # 断言
        self.assertText(text=dto["alarm_name"])
        # 数据清理
        self.alarm_function_delete_alarm(alarm_name=dto["alarm_name"])
        self.alarm_template_function_delete_alarm_template(
            template_name=dto["template_name"])
        self.index_function_delete_index(index_name=dto["index_name"])

    @seldom.file_data(
        file="./test_data/auto_test/analyser_data/alarm/alarm_data.json",
        key="test_add_alarm_of_type_cron")
    def test_add_alarm_of_type_cron(self, dto):
        '''新增告警-类型为cron表达式'''
        # 前置条件
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        self.alarm_template_function_add_alarm_template(
            template_name=dto["template_name"], addressee=dto["addressee"],
            subject=dto["subject"], alarm_text=dto["alarm_text"])
        # 测试步骤
        self.into_alarm_menu()
        self.wait_into_page_alarm_list()
        self.alarm_list_click_add()
        self.wait_into_page_alarm_add()
        self.alarm_form_input_alarm_name(alarm_name=dto["alarm_name"])
        self.alarm_form_plan_select_type(plan_type=dto["plan_type"])
        self.alarm_form_plan_input_cron(cron=dto["cron"])
        self.alarm_form_click_add_execute()
        self.alarm_form_execute_alart_select_execute_type(
            execute_type=dto["execute_type"])
        self.alarm_form_execute_alart_clicl_confirm()
        self.alarm_form_execute_select_index(index_name=dto["index_name"])
        self.alarm_form_execute_input_save_field(save_field=dto["save_field"])
        self.alarm_form_select_send_inform(info_type=dto["info_type"])
        self.alarm_form_select_template(template_name=dto["template_name"])
        self.alarm_form_click_add()
        self.alarm_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_alarm_list()
        # 断言
        self.assertText(text=dto["alarm_name"])
        # 数据清理
        self.alarm_function_delete_alarm(alarm_name=dto["alarm_name"])
        self.alarm_template_function_delete_alarm_template(
            template_name=dto["template_name"])
        self.index_function_delete_index(index_name=dto["index_name"])

    @seldom.file_data(
        file="./test_data/auto_test/analyser_data/alarm/alarm_data.json",
        key="test_add_alarm_of_execute_threshold")
    def test_add_alarm_of_execute_threshold(self, dto):
        '''新增告警-计算阈值'''
        # 前置条件
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        self.alarm_template_function_add_alarm_template(
            template_name=dto["template_name"], addressee=dto["addressee"],
            subject=dto["subject"], alarm_text=dto["alarm_text"])
        # 测试步骤
        self.into_alarm_menu()
        self.wait_into_page_alarm_list()
        self.alarm_list_click_add()
        self.wait_into_page_alarm_add()
        self.alarm_form_input_alarm_name(alarm_name=dto["alarm_name"])
        self.alarm_form_plan_select_type(plan_type=dto["plan_type"])
        self.alarm_form_plan_input_cron(cron=dto["cron"])
        self.alarm_form_click_add_execute()
        self.alarm_form_execute_alart_select_execute_type(
            execute_type=dto["execute_type"])
        self.alarm_form_execute_alart_clicl_confirm()
        self.alarm_form_execute_select_index(index_name=dto["index_name"])
        self.alarm_form_execute_input_filed(filed=dto["filed"])
        self.alarm_form_execute_input_time_filed(time_filed=dto["time_filed"])
        self.alarm_form_execute_input_save_field(save_field=dto["save_field"])
        self.alarm_form_select_send_inform(info_type=dto["info_type"])
        self.alarm_form_select_template(template_name=dto["template_name"])
        self.alarm_form_click_add()
        self.alarm_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_alarm_list()
        # 断言
        self.assertText(text=dto["alarm_name"])
        # 数据清理
        self.alarm_function_delete_alarm(alarm_name=dto["alarm_name"])
        self.alarm_template_function_delete_alarm_template(
            template_name=dto["template_name"])
        self.index_function_delete_index(index_name=dto["index_name"])

    @seldom.file_data(
        file="./test_data/auto_test/analyser_data/alarm/alarm_data.json",
        key="test_add_alarm_of_add_mail")
    def test_add_alarm_of_add_mail(self, dto):
        '''新增告警-直接新建电子邮件'''
        # 前置条件
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        # 测试步骤
        self.into_alarm_menu()
        self.wait_into_page_alarm_list()
        self.alarm_list_click_add()
        self.wait_into_page_alarm_add()
        self.alarm_form_input_alarm_name(alarm_name=dto["alarm_name"])
        self.alarm_form_plan_select_type(plan_type=dto["plan_type"])
        self.alarm_form_plan_input_cron(cron=dto["cron"])
        self.alarm_form_click_add_execute()
        self.alarm_form_execute_alart_select_execute_type(
            execute_type=dto["execute_type"])
        self.alarm_form_execute_alart_clicl_confirm()
        self.alarm_form_execute_select_index(index_name=dto["index_name"])
        self.alarm_form_execute_input_filed(filed=dto["filed"])
        self.alarm_form_execute_input_time_filed(time_filed=dto["time_filed"])
        self.alarm_form_execute_input_save_field(save_field=dto["save_field"])
        self.alarm_form_select_send_inform(info_type=dto["info_type"])
        self.alarm_form_click_add()
        self.alarm_template_form_input_addressee(addressee=dto["addressee"])
        self.alarm_template_form_input_subject(subject=dto["subject"])
        self.alarm_template_form_input_alarm_text(alarm_text=dto["alarm_text"])
        self.alarm_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_alarm_list()
        # 断言
        self.assertText(text=dto["alarm_name"])
        # 数据清理
        self.alarm_function_delete_alarm(alarm_name=dto["alarm_name"])
        self.index_function_delete_index(index_name=dto["index_name"])

    @seldom.file_data(
        file="./test_data/auto_test/analyser_data/alarm/alarm_data.json",
        key="test_edit_alarm")
    def test_edit_alarm(self, dto):
        '''编辑告警'''
        # 前置条件
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        self.alarm_template_function_add_alarm_template(
            template_name=dto["template_name"], addressee=dto["addressee"],
            subject=dto["subject"], alarm_text=dto["alarm_text"])
        self.alarm_function_add_alarm(
            alarm_name=dto["alarm_name"], execute_time=dto["execute_time"],
            execute_type=dto["execute_type"], index_name=dto["index_name"],
            save_field=dto["save_field"], info_type=dto["info_type"],
            template_name=dto["template_name"])
        # 测试步骤
        self.into_alarm_menu()
        self.wait_into_page_alarm_list()
        self.alarm_list_operate_click_edit(alarm_name=dto["alarm_name"])
        self.alarm_form_clear_alarm_name()
        self.alarm_form_input_alarm_name(alarm_name=dto["alarm_name_edit"])
        self.alarm_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_alarm_list()
        # 断言
        self.assertText(text=dto["alarm_name_edit"])
        # 数据清理
        self.alarm_function_delete_alarm(alarm_name=dto["alarm_name_edit"])
        self.alarm_template_function_delete_alarm_template(
            template_name=dto["template_name"])
        self.index_function_delete_index(index_name=dto["index_name"])

    @seldom.file_data(
        file="./test_data/auto_test/analyser_data/alarm/alarm_data.json",
        key="test_delete_alarm")
    def test_delete_alarm(self, dto):
        '''删除告警'''
        # 前置条件
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        self.alarm_template_function_add_alarm_template(
            template_name=dto["template_name"], addressee=dto["addressee"],
            subject=dto["subject"], alarm_text=dto["alarm_text"])
        self.alarm_function_add_alarm(
            alarm_name=dto["alarm_name"], execute_time=dto["execute_time"],
            execute_type=dto["execute_type"], index_name=dto["index_name"],
            save_field=dto["save_field"], info_type=dto["info_type"],
            template_name=dto["template_name"])
        # 测试步骤
        self.into_alarm_menu()
        self.wait_into_page_alarm_list()
        self.alarm_list_operate_click_delete(alarm_name=dto["alarm_name"])
        self.alert_receive()
        self.wait_toast_delete_successfully()
        # 断言
        self.assertNotText(text=dto["alarm_name"])
        # 数据清理
        self.alarm_template_function_delete_alarm_template(
            template_name=dto["template_name"])
        self.index_function_delete_index(index_name=dto["index_name"])

    @seldom.file_data(
        file="./test_data/auto_test/analyser_data/alarm/alarm_data.json",
        key="test_filter_for_alarm_list")
    def test_filter_for_alarm_list(self, dto):
        '''告警列表过滤器成功筛选数据'''
        # 前置条件
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        self.alarm_template_function_add_alarm_template(
            template_name=dto["template_name"], addressee=dto["addressee"],
            subject=dto["subject"], alarm_text=dto["alarm_text"])
        self.alarm_function_add_alarm(
            alarm_name=dto["alarm_name"], execute_time=dto["execute_time"],
            execute_type=dto["execute_type"], index_name=dto["index_name"],
            save_field=dto["save_field"], info_type=dto["info_type"],
            template_name=dto["template_name"])
        # 测试步骤
        self.into_alarm_menu()
        self.wait_into_page_alarm_list()
        self.filter_click_open()
        self.alarm_filter_input_name(
            alarm_name=dto["alarm_name"])
        self.filter_click_select()
        # 断言
        self.assertText(text=dto["alarm_name"])
        # 数据清理
        self.filter_click_reset()
        self.filter_click_close()
        self.alarm_function_delete_alarm(alarm_name=dto["alarm_name"])
        self.alarm_template_function_delete_alarm_template(
            template_name=dto["template_name"])
        self.index_function_delete_index(index_name=dto["index_name"])

    @seldom.file_data(
        file="./test_data/auto_test/analyser_data/alarm/alarm_data.json",
        key="test_copy_alarm")
    def test_copy_alarm(self, dto):
        '''复制告警'''
        # 前置条件
        self.index_function_add_index(
            index_name=dto["index_name"], index_prefix=dto["index_prefix"])
        self.alarm_template_function_add_alarm_template(
            template_name=dto["template_name"], addressee=dto["addressee"],
            subject=dto["subject"], alarm_text=dto["alarm_text"])
        self.alarm_function_add_alarm(
            alarm_name=dto["alarm_name"], execute_time=dto["execute_time"],
            execute_type=dto["execute_type"], index_name=dto["index_name"],
            save_field=dto["save_field"], info_type=dto["info_type"],
            template_name=dto["template_name"])
        # 测试步骤
        self.into_alarm_menu()
        self.wait_into_page_alarm_list()
        self.alarm_list_operate_click_copy(alarm_name=dto["alarm_name"])
        self.alarm_form_clear_alarm_name()
        self.alarm_form_input_alarm_name(alarm_name=dto["alarm_name_copy"])
        self.alarm_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_alarm_list()
        # 断言
        self.assertText(text=dto["alarm_name_copy"])
        # 数据清理
        self.alarm_function_delete_alarm(alarm_name=dto["alarm_name"])
        self.alarm_function_delete_alarm(alarm_name=dto["alarm_name_copy"])
        self.alarm_template_function_delete_alarm_template(
            template_name=dto["template_name"])
        self.index_function_delete_index(index_name=dto["index_name"])


if __name__ == "__main__":
    from seldom import ChromeConfig
    from selenium.webdriver import ChromeOptions
    ChromeConfig.command_executor = "chromedriver.exe"
    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('--ignore-certificate-errors')
    ChromeConfig.options = options
    seldom.main(case="test_alarm.AlarmTest.test_copy_alarm_0",
                browser='gc', debug=True)
    # seldom.main(case="test_alarm.AlarmTest",
    #             browser='gc', debug=True)
