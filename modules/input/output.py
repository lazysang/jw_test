from common.utils import Utils


class OutputPage(Utils):
    def into_output_menu(self):
        '''进入数据输出菜单'''
        self.into_module("动态数据接入")
        self.into_menu("数据输出")

    def wait_into_page_output_list(self):
        '''等待进入【输出列表】'''
        self.wait_into_page(breadcrumb="所有输出")

    def wait_into_page_add_output(self):
        '''等待进入【新建输出】'''
        self.wait_into_page(breadcrumb="新建输出")

    def wait_into_page_edit_output(self):
        '''等待进入【编辑输出】'''
        self.wait_into_page(breadcrumb="编辑输出")

    def output_list_pull_down_list_select(self, output_type):
        '''下拉列表选择输出类型'''
        self.click(id_="inputs")
        self.pull_down_list_select(text=output_type)

    def output_list_click_add_output(self):
        '''点击【添加输出】'''
        self.click_button(button_name="添加输出")

    def output_form_clear_output_name(self):
        '''清空输出名称'''
        self.form_input_clear(label="名称")

    def output_form_input_output_name(self, output_name):
        '''输入输出名称'''
        self.form_input(label="名称", text=output_name)

    def output_form_input_addr(self, addr):
        '''输入地址'''
        self.form_input(label="地址", text=addr)

    def output_form_select_index(self, index_name):
        '''选择索引'''
        # 点击索引下拉框
        self.form_select_click(label="索引")
        self.pull_down_list_select(text=index_name)

    def output_form_click_save(self):
        '''点击【保存】'''
        self.click_button(button_name="保存")

    def output_click_list_button(self, output_name, button_name):
        """点击数据输出列表操作"""
        button_xpath = self.select_data_button(
            text=output_name, tr_xpath='//app-output-list-detail/nz-card[2]/div[2]/div/div', text_relative_xpath='//h5', button_relative_xpath='//button/span[normalize-space(text())="{}"]/parent::button'.format(button_name))
        # 点击【编辑】
        self.click(xpath=button_xpath)

    def output_list_click_edit(self, output_name):
        """列表点击【编辑】按钮"""
        self.output_click_list_button(output_name, button_name="编辑")

    def output_list_click_delete(self, output_name):
        """列表点击【删除】按钮"""
        self.output_click_list_button(output_name, button_name="删除")


class Output(OutputPage):
    def output_function_add_output_of_console(self, output_type, output_name):
        '''添加输出-输出到控制台'''
        self.into_output_menu()
        self.wait_into_page_output_list()
        self.output_list_pull_down_list_select(output_type)
        self.output_list_click_add_output()
        self.wait_into_page_add_output()
        self.output_form_input_output_name(output_name)
        self.output_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_output_list()

    def output_function_add_output_of_engine(self, output_type, output_name, index_name):
        '''添加输出-输出到引擎,需要前置条件索引存在'''
        self.into_output_menu()
        self.wait_into_page_output_list()
        self.output_list_pull_down_list_select(output_type)
        self.output_list_click_add_output()
        self.wait_into_page_add_output()
        self.output_form_input_output_name(output_name)
        self.output_form_select_index(index_name)
        self.output_form_click_save()
        self.wait_toast_save_successfully()
        self.wait_into_page_output_list()

    def output_function_delete_output(self, output_name):
        '''删除数据输出'''
        self.into_output_menu()
        self.wait_into_page_output_list()
        self.output_list_click_delete(output_name)
        self.alert_receive()
        self.wait_toast_delete_successfully()
