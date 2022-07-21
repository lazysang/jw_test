from common.utils import Utils


class InterfacePage(Utils):
    def into_interface_menu(self):
        '''进入接口配置菜单'''
        # 进入动态数据接入
        self.into_module("动态数据接入")
        # 进入接口配置
        self.into_menu("接口配置")

    def wait_into_page_interfase_list(self):
        '''等待进入所有接口列表'''
        self.wait_into_page("所有接口")

    def wait_into_page_interfase_add(self):
        '''等待进入新建接口页面'''
        self.wait_into_page("新建接口")

    def wait_into_page_interfase_edit(self):
        '''等待进入编辑接口页面'''
        self.wait_into_page("编辑接口")

    def interface_list_pull_down_list_select(self, interface_type):
        '''下拉列表选择接口类型'''
        self.click(id_="inputs")
        self.pull_down_list_select(text=interface_type)

    def interface_list_click_add_interface(self):
        '''点击【创建接口】'''
        self.click_button(button_name="创建接口")

    def interface_list_move_to_operate_button(self, interface_name):
        '''移动到更多选项'''
        button_xpath = self.select_data_button(
            text=interface_name, tr_xpath='//app-inputs-list/nz-card[3]/div[2]/div/nz-card/div[2]/div/div', text_relative_xpath='//h5', button_relative_xpath='//button[2]')
        self.move_to_element(xpath=button_xpath)

    def interface_list_click_operate_button(self, text):
        '''点击更多选项下的按钮'''
        self.click(
            xpath='//div[@class="cdk-overlay-container"]/div/div/div/ul/li/a[normalize-space(text())="{}"]/ancestor::li'.format(text))

    def interface_list_click_operate_button_by_port_mapping(self, text):
        '''点击更多选项下端口映射-这个选项特殊'''
        self.click(
            xpath='//div[@class="cdk-overlay-container"]/div/div/div/ul/li/span[normalize-space(text())="{}"]/ancestor::li'.format(text))

    def interface_list_operate_click_edit_interface(self, interface_name):
        '''列表操作点击【编辑接口】'''
        self.interface_list_move_to_operate_button(interface_name)
        self.interface_list_click_operate_button(text="编辑接口")

    def interface_list_operate_click_add_static_property(self, interface_name):
        '''列表操作点击【添加静态属性】'''
        self.interface_list_move_to_operate_button(interface_name)
        self.interface_list_click_operate_button(text="添加静态属性")

    def interface_list_operate_click_enable_port_mapping(self, interface_name):
        '''列表操作点击【启用端口映射】'''
        self.interface_list_move_to_operate_button(interface_name)
        self.sleep(0.5)
        self.interface_list_click_operate_button_by_port_mapping(text="启用端口映射")

    def interface_list_operate_click_disable_port_mapping(self, interface_name):
        '''列表操作点击【禁用端口映射】'''
        self.interface_list_move_to_operate_button(interface_name)
        self.interface_list_click_operate_button_by_port_mapping(text="禁用端口映射")

    def interface_list_operate_click_delete_interface(self, interface_name):
        '''列表操作点击【删除接口】'''
        self.interface_list_move_to_operate_button(interface_name)
        self.interface_list_click_operate_button(text="删除接口")

    def interface_list_click_static_property(self, interface_name):
        '''列表点击静态属性'''
        self.click(
            xpath='//app-input-info/div/div[1]/div/div[2]/h5[normalize-space(text())="{}"]/ancestor::app-input-info/div/div[2]/div[1]/nz-collapse[2]/nz-collapse-panel/div[1]'.format(interface_name))

    def interface_list_click_delete_static_property(self, interface_name):
        '''删除静态属性'''
        self.click(
            xpath='//app-input-info/div/div[1]/div/div[2]/h5[normalize-space(text())="{}"]/ancestor::app-input-info/div/div[2]/div[1]/nz-collapse[2]/nz-collapse-panel/div[2]/div/div/table/tr/td[4]/a/i'.format(interface_name))

    def interface_form_click_checkbox_global(self):
        '''点击【应用到全局】'''
        self.form_checkbox_click(label="应用到全局")

    def interface_form_clear_interface_name(self):
        '''清空接口名称'''
        self.form_input_clear(label="名称")

    def interface_form_input_interface_name(self, interface_name):
        '''输入接口名称'''
        self.form_input(label="名称", text=interface_name)

    def interface_form_input_broker_addr(self, broker_addr):
        '''输入Broker 地址'''
        self.form_input(label="Broker 地址", text=broker_addr)

    def interface_form_clear_port(self):
        '''清空端口'''
        self.form_input_clear(label="端口")

    def interface_form_input_port(self, interface_port):
        '''输入端口'''
        self.form_input(label="端口", text=interface_port)

    def interface_form_click_save(self):
        '''点击【保存】'''
        self.click_button(button_name="保存")

    def interface_static_property_form_input_field(self, field):
        '''输入字段'''
        self.alert_form_input(label="字段", text=field)

    def interface_static_property_form_input_value(self, value):
        '''输入值'''
        self.alert_form_input(label="值", text=value)

    def interface_static_property_form_click_confirm(self):
        '''点击【确定】'''
        self.click_button(button_name="确定")


class Interface(InterfacePage):
    def interface_function_add_interface_of_syslog_tcp(self, interface_type, interface_name, interface_port):
        '''新增syslog_tcp接口'''
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_pull_down_list_select(interface_type)
        self.interface_list_click_add_interface()
        self.wait_into_page_interfase_add()
        self.interface_form_click_checkbox_global()
        self.interface_form_input_interface_name(interface_name)
        self.interface_form_clear_port()
        self.interface_form_input_port(interface_port)
        self.interface_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_interfase_list()

    def interface_function_delete_interface(self, interface_name):
        '''删除接口'''
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_operate_click_delete_interface(interface_name)
        self.alert_receive()
        self.wait_toast_delete_successfully()

    def interface_function_enable_port_mapping(self, interface_name):
        '''启用单接口端口映射'''
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_operate_click_enable_port_mapping(interface_name)
        self.alert_receive()
        self.wait_toast_edit_successfully()

    def interface_function_disable_port_mapping(self, interface_name):
        '''启用单接口端口映射'''
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_operate_click_disable_port_mapping(interface_name)
        self.alert_receive()
        self.wait_toast_edit_successfully()

    def interface_function_add_static_proprty(self, interface_name, field, value):
        '''添加静态属性'''
        self.into_interface_menu()
        self.wait_into_page_interfase_list()
        self.interface_list_operate_click_add_static_property(
            interface_name)
        self.interface_static_property_form_input_field(field)
        self.interface_static_property_form_input_value(value)
        self.interface_static_property_form_click_confirm()
        self.wait_toast_add_static_proprety_successfully()
    # def add_copy_resolution(self, interface_name, index_name, resolution_filed, resolution_title):
    #     '''新增复制解析器'''
    #     # 进入动态数据接入
    #     self.into_module("动态数据接入")
    #     # 进入接口配置
    #     self.into_menu("接口配置")
    #     # 根据接口名获取按钮
    #     button_xpath = self.select_data_button(
    #         text=interface_name, tr_xpath="//app-inputs-list/nz-card[3]/div[2]/div/nz-card[2]/div[2]/div/div", text_relative_xpath="//h5", button_relative_xpath="//button[1]")
    #     # 点击【管理解析器】
    #     self.click(xpath=button_xpath)
    #     # 点击索引下拉框index_name
    #     self.click(id_="input")
    #     # 下拉列表选择索引
    #     self.pull_down_list_select(
    #         text=index_name, xpath='/html/body/div[1]/div/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item')
    #     # 点击【加载】
    #     self.click(xpath='//nz-tabset/div/div/div[1]/button')
    #     # 点击对应字段的【创建解析器】
    #     button_xpath = self.select_data_button(
    #         text="message", tr_xpath="//nz-card/div[2]/nz-card[1]/div[2]/div/div/div/div[2]/div[2]/div", text_relative_xpath="//b", button_relative_xpath="//app-message-field/div[2]/div/a[last()]")
    #     self.click(xpath=button_xpath)
    #     # 点击【复制】
    #     self.click(xpath="/html/body/div/div/div/div/ul/li[1]")
    #     # 表单
    #     self.type(text=resolution_filed,
    #               xpath="//nz-card/div[2]/form/nz-form-item[4]/nz-form-control/div/div/input")
    #     self.type(
    #         text=resolution_title, xpath="//nz-card/div[2]/form/nz-form-item[6]/nz-form-control/div/div/input")
    #     # 点击【保存】
    #     self.click(xpath="//nz-card/div[1]/div/div[2]/button[1]")
    #     self.wait_toast(toast_text="保存成功")
    #     # 点击【返回】
    #     self.click(xpath="//nz-card/div[1]/div/div[2]/button[3]")
    #     self.wait_into_page(breadcrumb="所有接口")
    #     return True

    # def delete_copy_resolution(self, interface_name, resolution_title):
    #     '''删除复制解析器'''
    #     # 进入动态数据接入
    #     self.into_module("动态数据接入")
    #     # 进入接口配置
    #     self.into_menu("接口配置")
    #     # 根据接口名获取按钮
    #     button_xpath = self.select_data_button(
    #         text=interface_name, tr_xpath="//app-inputs-list/nz-card[3]/div[2]/div/nz-card[2]/div[2]/div/div", text_relative_xpath="//h5", button_relative_xpath="//button[1]")
    #     # 点击【管理解析器】
    #     self.click(xpath=button_xpath)
    #     # 点击【删除】
    #     button_xpath = self.select_data_button(
    #         text=resolution_title, tr_xpath="//nz-card/div[2]/nz-card[2]/div[2]/div/div/div", text_relative_xpath="//b", button_relative_xpath="//button[2]")
    #     self.click(xpath=button_xpath)
    #     # 确认删除
    #     self.receive_alert()
    #     self.wait_toast(toast_text="删除成功")
    #     # 点击【返回】
    #     self.click(xpath="//nz-card/div[1]/div/div[2]/button[3]")
    #     self.wait_into_page(breadcrumb="所有接口")
