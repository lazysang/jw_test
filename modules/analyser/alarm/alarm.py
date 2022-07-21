from common.utils import Utils


class AlarmBase(Utils):
    def into_alarm_menu(self):
        '''进入告警管理/告警策略列表菜单'''
        self.into_module("动态数据分析")
        self.into_menu("告警管理/告警策略")

    def wait_into_page_alarm_list(self):
        '''等待进入告警策略列表'''
        self.wait_into_page("告警策略列表")

    def wait_into_page_alarm_add(self):
        '''等待进入添加页面'''
        self.wait_into_page("添加")

    def wait_into_page_alarm_edit(self):
        '''等待进入编辑页面'''
        self.wait_into_page("编辑")

    def alarm_list_click_add(self):
        '''点击新建按钮'''
        self.click_button(button_name="新建")

    def alarm_move_to_operate_by_alarm_name(self, alarm_name):
        '''移动到对应告警名的操作按钮上'''
        self.move_to_element(
            xpath='//div[@class="ant-table-content"]/table/tbody/tr//td[1]//span[normalize-space(text())="{}"]/ancestor::tr//button'.format(alarm_name))

    def alarm_list_operate_click_detail(self, alarm_name):
        '''列表操作点击【详情】'''
        self.alarm_move_to_operate_by_alarm_name(alarm_name)
        self.click_operate_button(text="详情")

    def alarm_list_operate_click_edit(self, alarm_name):
        '''列表操作点击【编辑】'''
        self.alarm_move_to_operate_by_alarm_name(alarm_name)
        self.click_operate_button(text="编辑")

    def alarm_list_operate_click_copy(self, alarm_name):
        '''列表操作点击【复制】'''
        self.alarm_move_to_operate_by_alarm_name(alarm_name)
        self.click_operate_button(text="复制")

    def alarm_list_operate_click_export(self, alarm_name):
        '''列表操作点击【导出】'''
        self.alarm_move_to_operate_by_alarm_name(alarm_name)
        self.click_operate_button(text="导出")

    def alarm_list_operate_click_delete(self, alarm_name):
        '''列表操作点击【删除】'''
        self.alarm_move_to_operate_by_alarm_name(alarm_name)
        self.click_operate_button(text="删除")

    def alarm_form_input_alarm_name(self, alarm_name):
        '''输入告警名称'''
        self.type(
            xpath='//nz-form-label/label/b[normalize-space(text())="名称"]/ancestor::nz-form-label/following-sibling::nz-form-control//input',
            text=alarm_name)

    def alarm_form_clear_alarm_name(self):
        '''清空告警名称'''
        self.clear(
            xpath='//nz-form-label/label/b[normalize-space(text())="名称"]/ancestor::nz-form-label/following-sibling::nz-form-control//input')

    def alarm_form_input_explain(self):
        '''输入说明'''
        self.form_textarea(label="说明")

    def alarm_form_plan_select_type(self, plan_type):
        '''选择计划执行类型'''
        self.form_select_click(label="类型")
        self.pull_down_list_select(text=plan_type)

    def alarm_form_plan_input_execute_time(self, execute_time):
        '''输入执行时间-执行于'''
        self.form_input(label="执行于", text=execute_time)

    def alarm_form_plan_input_execute_time_2(self, execute_time):
        '''输入执行时间-执行于-每周与每月用这个'''
        self.type(
            xpath='//nz-form-label/label[normalize-space(text())="执行于"]/parent::nz-form-label/following-sibling::nz-form-control/div/div/nz-time-picker/div/input', text=execute_time)

    def alarm_form_plan_input_interval(self, interval):
        '''输入时间间隔'''
        self.form_input(label="每隔", text=interval)

    def alarm_form_plan_input_interval_day(self, interval_day):
        '''输入时间间隔-每天'''
        self.type(
            xpath='//nz-form-label/label[normalize-space(text())="每天"]/parent::nz-form-label/following-sibling::nz-form-control/div/div/nz-time-picker/div/input', text=interval_day)

    def alarm_form_plan_select_week(self, week):
        '''选择周几'''
        self.click(
            xpath='//app-weekly//span[normalize-space(text())="{}"]'.format(week))

    def alarm_form_plan_input_interval_month(self, interval_month):
        '''输入时间间隔-每月'''
        self.form_input(label="每月", text=interval_month)

    def alarm_form_plan_input_cron(self, cron):
        '''输入cron表达式'''
        self.form_input(label="cron表达式", text=cron)

    def alarm_form_click_add_execute(self):
        '''点击【添加执行器】按钮'''
        self.click_button(button_name="添加执行器")

    def alarm_form_execute_alart_select_execute_type(self, execute_type):
        '''选择执行器类型'''
        self.click(
            xpath='//div[@class="cdk-overlay-container"]//label/span[normalize-space(text())="{}"]'.format(execute_type))

    def alarm_form_execute_alart_clicl_confirm(self):
        '''点击【确定】按钮'''
        self.click_button(button_name="确定")

    def alarm_form_execute_select_index(self, index_name):
        '''选择索引'''
        self.form_select_click(label="索引")
        self.pull_down_list_select(text=index_name)

    def alarm_form_execute_input_save_field(self, save_field):
        '''输入保存为'''
        self.form_input(label="保存为", text=save_field)

    def alarm_form_execute_input_filed(self, filed):
        '''输入字段'''
        self.form_input(label="字段", text=filed)

    def alarm_form_execute_input_time_filed(self, time_filed):
        '''输入时间字段'''
        self.form_input(label="时间字段", text=time_filed)

    def alarm_form_select_send_inform(self, info_type):
        '''选择发送通知'''
        self.click(
            xpath='//nz-form-label/label/b[normalize-space(text())="发送通知"]/ancestor::nz-form-label/following-sibling::nz-form-control[1]//nz-select')
        self.pull_down_list_select(text=info_type)

    def alarm_form_select_template(self, template_name):
        '''选择告警模板'''
        self.click(
            xpath='//nz-form-label/label/b[normalize-space(text())="发送通知"]/ancestor::nz-form-label/following-sibling::nz-form-control[2]//nz-select')
        self.pull_down_list_select(text=template_name)

    def alarm_form_click_add(self):
        '''点击发送通知的【添加】按钮'''
        self.click(
            xpath='//nz-form-item/nz-form-label/label/b[normalize-space(text())="发送通知"]/ancestor::nz-form-item//button/span[normalize-space(text())="添加"]/parent::button')

    def alarm_form_click_save(self):
        '''点击【保存】按钮'''
        self.click_button(button_name="保存")

    def alarm_filter_input_name(self, alarm_name):
        '''输入名称'''
        self.form_input(label="名称", text=alarm_name)

    def alarm_filter_click_select(self):
        '''点击【查询】按钮'''
        self.click_button(button_name="查询")

    def alarm_filter_click_reset(self):
        '''点击【重置】按钮'''
        self.click_button(button_name="重置")


class Alarm(AlarmBase):
    def alarm_function_add_alarm(self, alarm_name, execute_time,
                                 execute_type, index_name, save_field,
                                 info_type, template_name):
        '''新增告警-依赖索引与索引模板-类型为执行一次'''
        self.into_alarm_menu()
        self.wait_into_page_alarm_list()
        self.alarm_list_click_add()
        self.wait_into_page_alarm_add()
        self.alarm_form_input_alarm_name(alarm_name)
        self.alarm_form_plan_input_execute_time(
            execute_time)
        self.alarm_form_click_add_execute()
        self.alarm_form_execute_alart_select_execute_type(
            execute_type)
        self.alarm_form_execute_alart_clicl_confirm()
        self.alarm_form_execute_select_index(index_name)
        self.alarm_form_execute_input_save_field(save_field)
        self.alarm_form_select_send_inform(info_type)
        self.alarm_form_select_template(template_name)
        self.alarm_form_click_add()
        self.alarm_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_alarm_list()

    def alarm_function_delete_alarm(self, alarm_name):
        '''删除告警'''
        self.into_alarm_menu()
        self.wait_into_page_alarm_list()
        self.alarm_list_operate_click_delete(alarm_name)
        self.alert_receive()
        self.wait_toast_delete_successfully()
