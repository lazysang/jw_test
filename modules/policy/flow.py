from common.utils import Utils


class FlowPage(Utils):
    flow_list_operate_option_xpath = '//lib-list-operator/li/span[normalize-space(text())="{}"]/parent::li'

    def into_flow_menu(self):
        '''进入业务流管理列表'''
        self.into_module("安全策略配置")
        self.into_menu(menu_name="服务端管理/业务流管理")

    def wait_into_page_flow_list(self):
        '''等待进入【业务流列表】'''
        self.wait_into_page(breadcrumb="所有业务流")

    def wait_into_page_edit_flow(self):
        '''等待进入【编辑业务流页面】'''
        self.wait_into_page(breadcrumb="配置业务流")

    def flow_list_click_add(self):
        '''点击【新建】'''
        self.click_button(button_name="新建")

    def flow_list_operate_click_edit(self, flow_name):
        '''列表操作点击【编辑】'''
        self.move_to_operate_button(text=flow_name)
        self.click(xpath=self.flow_list_operate_option_xpath.format("编辑"))

    def flow_list_operate_click_config(self, flow_name):
        '''列表操作点击【配置】'''
        self.move_to_operate_button(text=flow_name)
        self.click(xpath=self.flow_list_operate_option_xpath.format("配置"))

    def flow_list_operate_click_set_active(self, flow_name):
        '''列表操作点击【设置为激活】'''
        self.move_to_operate_button(text=flow_name)
        self.click(xpath=self.flow_list_operate_option_xpath.format("设置为激活"))

    def flow_list_operate_click_set_deactive(self, flow_name):
        '''列表操作点击【设置为不激活】'''
        self.move_to_operate_button(text=flow_name)
        self.click(xpath=self.flow_list_operate_option_xpath.format("设置为不激活"))

    def flow_list_operate_click_delete(self, flow_name):
        '''列表操作点击【删除】'''
        self.move_to_operate_button(text=flow_name)
        self.click(xpath=self.flow_list_operate_option_xpath.format("删除"))

    def flow_form_flow_name(self, flow_name):
        '''数据流名称'''
        self.form_input(label="名称",text=flow_name)

    def flow_form_click_save(self):
        '''点击【保存】'''
        self.click_button(button_name="保存")

    def flow_canvas_double_click(self):
        '''数据流画布双击鼠标左键'''
        self.double_click(xpath='//app-flow-config/div')

    def flow_canvas_click_start(self):
        '''点击开始'''
        self.click(xpath='//app-select-node/div/div[2]/div[7]/a')

    def flow_canvas_click_interface_log(self):
        '''点击【接口日志】'''
        self.click(xpath='//app-select-node/div/div[2]/div[7]/div/div/span')

    def flow_canvas_drag_node(self):
        '''鼠标点击节点分支拖出下一个节点选择框'''
        self.drag_and_drop_by_offset(
            xpath='//app-flow-new-config/div[1]/div/app-flow-config/div/div', x=100)

    def flow_canvas_click_end(self):
        '''点击【结束】'''
        self.click(xpath='//app-select-node/div/div[2]/div[5]/a')

    def flow_canvas_click_save_log(self):
        '''点击【保存日志】'''
        self.click(xpath='//app-select-node/div/div[2]/div[5]/div/div/span')

    def flow_canvas_click_save(self):
        '''点击【保存】'''
        self.click_button(button_name="保存")

    def flow_canvas_click_return(self):
        '''点击【返回】'''
        self.click_button(button_name="返回")


class Flow(FlowPage):
    def add_flow(self, flow_name):
        '''新增业务流'''
        self.into_flow_menu()
        self.wait_into_page_flow_list()
        self.flow_list_click_add()
        self.flow_form_flow_name(flow_name)
        self.flow_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_flow_list()

    def delete_flow(self, flow_name):
        '''删除业务流'''
        self.into_flow_menu()
        self.wait_into_page_flow_list()
        self.flow_list_operate_click_delete(flow_name)
        self.alert_receive()
        self.wait_toast_edit_successfully()

    def activate_flow(self, flow_name):
        '''激活业务流'''
        self.into_flow_menu()
        self.wait_into_page_flow_list()
        self.flow_list_operate_click_set_active(flow_name)
        self.alert_receive()
        self.wait_toast_set_successfully()

    def add_simple_rule_for_flow(self, flow_name):
        '''为业务流新增简单规则(接收日志->保存日志)'''
        self.into_flow_menu()
        self.wait_into_page_flow_list()
        self.flow_list_operate_click_config(flow_name)
        self.wait_into_page_edit_flow()
        self.flow_canvas_double_click()
        self.flow_canvas_click_start()
        self.flow_canvas_click_interface_log()
        self.flow_canvas_drag_node()

        self.flow_canvas_click_end()
        self.flow_canvas_click_save_log()
        self.flow_canvas_click_save()
        self.wait_toast_save_successfully()
        self.flow_canvas_click_return()
        self.wait_into_page_flow_list()
