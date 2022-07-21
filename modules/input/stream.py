from common.utils import Utils


class StreamPage(Utils):
    stream_list_operate_option_xpath = '//div[@class="cdk-overlay-container"]/div/div/div/ul/li[normalize-space(text())="{}"]'

    def into_stream_menu(self):
        '''进入数据流菜单'''
        # 进入动态数据接入
        self.into_module("动态数据接入")
        # 进入数据流
        self.into_menu("数据流")

    def wait_into_page_stram_list(self):
        '''等待进入【数据流列表】'''
        self.wait_into_page(breadcrumb="所有数据流")

    def wait_into_page_add_stream(self):
        '''等待进入【新建数据流页面】'''
        self.wait_into_page(breadcrumb="新建数据流")

    def wait_into_page_edit_stream(self):
        '''等待进入【编辑数据流页面】'''
        self.wait_into_page(breadcrumb="编辑数据流")

    def wait_into_page_edit_stream_rule(self):
        '''等待进入【编辑数据流规则】页面'''
        self.wait_into_page(breadcrumb="编辑数据流规则")

    def wait_into_page_add_output(self):
        '''等待进入【新建输出】'''
        self.wait_into_page(breadcrumb="新建输出")

    def wait_into_page_edit_output(self):
        '''等待进入【编辑输出】'''
        self.wait_into_page(breadcrumb="编辑输出")

    def stream_list_click_add(self):
        '''点击【新建】'''
        self.click_button(button_name="新建")

    def stream_list_click_refresh(self):
        '''点击【刷新】'''
        self.click_button(button_name="刷新")

    def stream_list_operation_click_clone(self, stream_name):
        '''列表操作点击【克隆】'''
        self.move_to_operate_button(text=stream_name)
        self.click(xpath=self.stream_list_operate_option_xpath.format("克隆"))

    def stream_list_operation_click_edit_rule(self, stream_name):
        '''列表操作点击【编辑规则】'''
        self.move_to_operate_button(text=stream_name)
        self.click(xpath=self.stream_list_operate_option_xpath.format("编辑规则"))

    def stream_list_operation_click_edit(self, stream_name):
        '''列表操作点击【编辑】'''
        self.move_to_operate_button(text=stream_name)
        self.click(xpath=self.stream_list_operate_option_xpath.format("编辑"))

    def stream_list_operation_click_delete(self, stream_name):
        '''列表操作点击【删除】'''
        self.move_to_operate_button(text=stream_name)
        self.click(xpath=self.stream_list_operate_option_xpath.format("删除"))

    def stream_list_operation_click_run(self, stream_name):
        '''列表操作点击【运行】-特殊项'''
        self.move_to_operate_button(text=stream_name)
        self.click(
            xpath='//div[@class="cdk-overlay-container"]/div/div/div/ul/li/a[normalize-space(text())="运行"]/parent::li')
        # 移走鼠标，避免鼠标触摸到操作选项
        self.move_to_element(xpath=self.get_button_xpath(button_name="刷新"))

    def stream_list_operation_click_close(self, stream_name):
        '''列表操作点击【关闭】-特殊项'''
        self.move_to_operate_button(text=stream_name)
        self.click(
            xpath='//div[@class="cdk-overlay-container"]/div/div/div/ul/li/a[normalize-space(text())="关闭"]/parent::li')

    def stream_form_clear_stream_name(self):
        '''清空数据流名称'''
        self.form_input_clear(label="名称")

    def stream_form_input_stream_name(self, stream_name):
        '''输入数据流名称'''
        self.form_input(label="名称", text=stream_name)

    def stream_form_input_stream_description(self, stream_description):
        '''输入数据流描述'''
        self.form_textarea(label="说明", text=stream_description)

    def stream_form_click_checkbox(self):
        '''点击复选框'''
        self.click(xpath='//*[@id="removeMatchesFromDefault"]/span[1]/input')

    def stream_form_click_save(self):
        '''点击【保存】按钮'''
        self.click_button(button_name="保存")

    def stream_clone_form_input_stream_name(self, stream_name):
        '''输入数据流名称'''
        self.alert_form_input(label="名称", text=stream_name)

    def stream_clone_form_input_stream_description(self, stream_description):
        '''输入数据流描述'''
        self.alert_form_textarea(label="说明", text=stream_description)

    def stream_clone_form_click_confirm(self):
        '''点击【确定】按钮'''
        self.click_button(button_name="确定")

    def stream_filter_input_name(self, stream_name):
        '''输入名称'''
        self.form_input(label="名称", text=stream_name)

    def stream_rule_click_add_rule(self):
        '''点击【添加规则】'''
        self.click_button(button_name="添加规则")

    def stream_rule_form_select_condition(self, condition="匹配接口"):
        '''选择条件'''
        # 点击条件下拉框
        self.form_select_click(label="条件")
        self.pull_down_list_select(text=condition)

    def stream_rule_form_select_interface(self, interface_name):
        '''选择接口-Syslog TCP'''
        # 点击接口下拉框
        self.form_select_click(label="接口")
        self.pull_down_list_select(
            text='{}(Syslog TCP)'.format(interface_name))

    def stream_rule_form_input_field(self, field):
        '''输入字段'''
        self.alert_form_input(label="字段", text=field)

    def stream_rule_form_input_value(self, value):
        '''输入字段'''
        self.alert_form_input(label="值", text=value)

    def stream_rule_form_click_checkbox_reverse(self):
        '''点击【取反】'''
        self.form_checkbox_click(label="取反")

    def stream_rule_form_input_explain(self, rule_sxplain):
        '''输入说明'''
        self.alert_form_textarea(label="说明", text=rule_sxplain)

    def stream_rule_form_click_confirm(self):
        '''点击【确定】'''
        self.click_button(button_name="确定")

    def stream_rule_click_return(self):
        '''点击【返回】'''
        self.click_button(button_name="返回")

    def stream_rule_switch_to_output(self):
        '''切换到数据输出'''
        self.click(
            xpath='//nz-card/div[2]/nz-tabset/nz-tabs-nav/div/div/div/div[normalize-space(text())="数据输出"]')

    def stream_rule_select_output(self, mode="输出到引擎"):
        '''选择输出方式'''
        # 点击选择框
        self.click(xpath='//*[@id="inputs"]')
        # 遍历元素的方式选中【输出到引擎】
        self.pull_down_list_select(text=mode)

    def stream_rule_select_exist_output(self, output_name):
        '''选择存在的输出方式-控制台输出类型'''
        # 点击选择框
        self.click(xpath='//*[@id="allInputs"]')
        exist_output_name = '{} / 控制台输出'.format(output_name)
        self.pull_down_list_select(text=exist_output_name)

    def stream_rule_click_add_output(self):
        '''点击【添加输出】'''
        self.click_button(button_name="添加输出")

    def stream_rule_click_add_exist_output(self):
        '''点击【添加已有输出】'''
        self.click_button(button_name="添加已有输出")

    def stream_rule_output_form_clear_output_name(self):
        '''清空输出名称'''
        self.form_input_clear(label="名称")

    def stream_rule_output_form_input_output_name(self, output_name):
        '''输入输出名称'''
        self.form_input(label="名称", text=output_name)

    def stream_rule_output_form_input_addr(self, addr):
        '''输入地址'''
        self.form_input(label="地址", text=addr)

    def stream_rule_output_form_select_index(self, index_name):
        '''选择索引'''
        # 点击索引下拉框
        self.form_select_click(label="索引")
        self.pull_down_list_select(text=index_name)

    def stream_rule_output_form_click_save(self):
        '''点击【保存】'''
        self.click_button(button_name="保存")

    def stream_rule_output_list_click_edit(self, output_name):
        '''规则输出列表点击【编辑】'''
        self.click(
            xpath='//div[@class="ant-row"]//h5[normalize-space(text())="{}"]/ancestor::div[@class="ant-row"]//button/span[normalize-space(text())="编辑"]/parent::button'.format(output_name))

    def stream_rule_output_list_click_remove(self, output_name):
        '''规则输出列表点击【从数据流中移除】'''
        self.click(
            xpath='//div[@class="ant-row"]//h5[normalize-space(text())="{}"]/ancestor::div[@class="ant-row"]//button/span[normalize-space(text())="从数据流中移除"]/parent::button'.format(output_name))


class Stream(StreamPage):

    def stream_function_add_stream(self, stream_name, stream_description):
        '''新增数据流'''
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        self.stream_list_click_add()
        # 等待进入页面（外面页面有id=name，不然会定位到外面）
        self.wait_into_page_add_stream()
        self.stream_form_input_stream_name(stream_name)
        self.stream_form_input_stream_description(stream_description)
        # self.stream_form_click_checkbox()
        self.stream_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_stram_list()

    def stream_function_add_rule_for_stream(self, stream_name, interface_name):
        '''为数据流新增规则Syslog TCP'''
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        self.stream_list_operation_click_edit_rule(stream_name)
        self.stream_rule_click_add_rule()
        self.stream_rule_form_select_condition()
        self.stream_rule_form_select_interface(interface_name)
        self.stream_rule_form_click_confirm()
        self.wait_toast_save_successfully()
        self.stream_rule_click_return()

    def stream_function_add_output_for_stream(self, stream_name, output_name, index_name):
        '''为数据流新增输出-输出到引擎'''
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        self.stream_list_operation_click_edit_rule(stream_name)
        self.stream_rule_switch_to_output()
        self.stream_rule_select_output()
        self.stream_rule_click_add_output()
        self.stream_rule_output_form_input_output_name(output_name)
        self.stream_rule_output_form_select_index(index_name)
        self.stream_rule_output_form_click_save()
        self.wait_toast_save_successfully()
        self.stream_rule_click_return()
        self.wait_into_page_stram_list()

    def stream_function_run_stream(self, stream_name):
        '''运行数据流'''
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        self.stream_list_operation_click_run(stream_name)
        self.wait_toast_run_successfully()

    def stream_function_delete_stream(self, stream_name):
        '''删除数据流'''
        self.into_stream_menu()
        self.wait_into_page_stram_list()
        self.stream_list_operation_click_delete(stream_name)
        self.alert_receive()
        self.wait_toast_delete_successfully()
