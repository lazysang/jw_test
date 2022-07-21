from common.utils import Utils


class AlarmTemplateBase(Utils):
    def into_alarm_template_menu(self):
        '''进入告警管理/告警模板列表菜单'''
        self.into_module("动态数据分析")
        self.into_menu("告警管理/告警模板")

    def wait_into_page_alarm_template_list(self):
        '''等待进入告警模板列表'''
        self.wait_into_page("告警模板列表")

    def wait_into_page_alarm_template_add(self):
        '''等待进入添加页面'''
        self.wait_into_page("添加")

    def wait_into_page_alarm_template_edit(self):
        '''等待进入编辑页面'''
        self.wait_into_page("编辑")

    def alarm_template_list_click_add(self):
        '''点击新建按钮'''
        self.click_button(button_name="新建")

    def alarm_template_move_to_operate_by_template_name(self, template_name):
        '''移动到对应模板名的操作按钮上'''
        self.move_to_element(
            xpath='//div[@class="ant-table-content"]/table/tbody/tr//td[1]//span[normalize-space(text())="{}"]/ancestor::tr//button'.format(template_name))

    def alarm_template_list_operate_click_edit(self, template_name):
        '''列表操作点击【编辑】'''
        self.alarm_template_move_to_operate_by_template_name(template_name)
        self.click_operate_button(text="编辑")

    def alarm_template_list_operate_click_delete(self, template_name):
        '''列表操作点击【删除】'''
        self.alarm_template_move_to_operate_by_template_name(template_name)
        self.click_operate_button(text="删除")

    def alarm_template_form_input_template_name(self, template_name):
        '''输入模板名称'''
        self.form_input(label="名称", text=template_name)

    def alarm_template_form_clear_template_name(self):
        '''清空模板名称'''
        self.form_input_clear(label="名称")

    def alarm_template_form_input_addressee(self, addressee):
        '''输入收件人邮箱'''
        self.form_input(label="收件人", text=addressee)

    def alarm_template_form_input_subject(self, subject):
        '''输入主题'''
        self.form_input(label="主题", text=subject)

    def alarm_template_form_input_alarm_text(self, alarm_text):
        '''输入正文'''
        self.type(xpath='//lib-ace-editor/div[1]/textarea', text=alarm_text)

    def alarm_template_form_click_save(self):
        '''点击【保存】'''
        self.click_button(button_name="保存")

    def alarm_template_filter_input_name(self, template_name):
        '''输入名称'''
        self.form_input(label="名称", text=template_name)

    def alarm_template_filter_click_select(self):
        '''点击【查询】按钮'''
        self.click_button(button_name="查询")

    def alarm_template_filter_click_reset(self):
        '''点击【重置】按钮'''
        self.click_button(button_name="重置")


class AlarmTemplate(AlarmTemplateBase):
    def alarm_template_function_add_alarm_template(self, template_name, addressee, subject, alarm_text):
        '''新增告警模板'''
        self.into_alarm_template_menu()
        self.wait_into_page_alarm_template_list()
        self.alarm_template_list_click_add()
        self.wait_into_page_alarm_template_add()
        self.alarm_template_form_input_template_name(template_name)
        self.alarm_template_form_input_addressee(addressee)
        self.alarm_template_form_input_subject(subject)
        self.alarm_template_form_input_alarm_text(alarm_text)
        self.alarm_template_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_alarm_template_list()

    def alarm_template_function_delete_alarm_template(self, template_name):
        '''删除告警模板'''
        self.into_alarm_template_menu()
        self.wait_into_page_alarm_template_list()
        self.alarm_template_list_operate_click_delete(template_name)
        self.alert_receive()
        self.wait_toast_delete_successfully()
