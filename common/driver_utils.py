from seldom.webdriver import WebDriver
from seldom.logging import log


class DriverUtilsPath():
    # 通用按钮位置
    button_name_xpath = '//button/span[normalize-space(normalize-space(text()))="{button_name}"]/parent::button'
    # 下拉选择位置
    pull_down_select_xpath = '//cdk-virtual-scroll-viewport/div[1]/nz-option-item'
    # 通用操作按钮位置
    operate_button_xpath = {"tr_xpath": '//div[@class="ant-table-content"]/table/tbody/tr',
                            "text_relative_xpath": '//td[1]//a', "button_relative_xpath": '/td/button'}
    # 通用操作选项位置
    operate_option_xpath = '/html/body/div/div/div/div/ul/lib-list-operator/li/span[normalize-space(text())="{}"]/ancestor-or-self::li'
    # 列表数据名称位置
    data_name_xpath = '//tr/td//a/span'
    # 分页控件
    pagination_xpath = '//nz-pagination'
    # 最大页码
    pagination_max_number_xpath = '//nz-pagination/li[last()-1]'
    # 当前页码
    pagination_current_number_css = 'li.ant-pagination-item-active'
    # 下一页
    pagination_next_number_css = '//nz-pagination/li[last()]'
    # 面包屑最后位置
    breadcrumb_xpath = '//lib-breadcrumb/nz-breadcrumb/nz-breadcrumb-item[last()]//a'
    # 取消警告框
    alert_cancle_xpath = '//div[@class="cdk-overlay-container"]//button[1]'
    # 确认警告框
    alert_receive_xpath = '//div[@class="cdk-overlay-container"]//button[2]'
    # toast
    toast_xpath = '//*[@id="toast-container"]/div/div'
    # 表单输入位置
    form_location_xpath = '//nz-form-label/label[normalize-space(text())="{label}"]/parent::nz-form-label/following-sibling::nz-form-control//{input_type}'
    # alert输入位置
    alert_form_location_xpath = '//nz-modal-container//nz-form-label/label[normalize-space(text())="{label}"]/parent::nz-form-label/following-sibling::nz-form-control//{input_type}'
    # 过滤器位置
    filter_xpath = '//nz-collapse-panel/div[normalize-space(text())="过滤器"]'
    # checkbox位置
    checkbox_path = '//span[normalize-space(text())="{}"]'


class DriverUtils(WebDriver, DriverUtilsPath):
    def click_button(self, button_name):
        '''点击按钮'''
        self.click(
            xpath=self.button_name_xpath.format(button_name=button_name))

    def get_button_xpath(self, button_name):
        '''返回按钮的xpath'''
        xpath = self.button_name_xpath.format(
            button_name=button_name)
        return xpath

    def pull_down_list_select(self, text: str = None, xpath: str = None):
        '''下拉列表选中-不传xpath时使用默认xpath'''
        # 获取下拉框所有元素，然后进行遍历
        if xpath is None:
            xpath = self.pull_down_select_xpath
        elements = self.get_elements(xpath=xpath)
        for element in elements:
            # log.debug(element)
            if text == element.get_attribute("title"):
                log.debug(element.get_attribute("title"))
                element.click()
                break
        else:
            # 构建获取到的最后一个元素，鼠标移动到元素上，加载下拉框
            move_path = '{}[{}]'.format(xpath, len(elements))
            log.debug(move_path)
            self.move_to_element(xpath=move_path)
            elements_move_later = self.get_elements(xpath=xpath)
            log.debug(len(elements_move_later))
            # 判断是否加载有新数据
            if len(elements) != len(elements_move_later):
                self.pull_down_list_select(text, xpath)

    def move_to_operate_button(self, text):
        '''移动到对应数据右侧操作按钮-通用'''
        self.move_to_element(xpath=self.list_button_by_text(text=text))

    def click_operate_button(self, text):
        '''点击操作菜单中的操作按钮-通用'''
        self.click(xpath=self.operate_option_xpath.format(text))

    def list_select_data_by_name(self, data_name):
        '''列表查找数据名称是否存在-通用'''
        elements = self.get_elements(xpath=self.data_name_xpath)
        for element in elements:
            if data_name == element.text:
                return True
        else:
            if self.has_turn_page() is True:
                if self.current_turn_page() is not self.max_turn_page():
                    next_page_number = str(int(self.current_turn_page())+1)
                    self.turn_page(next_page_number=next_page_number)
                    return self.list_select_data_by_name(data_name)
                else:
                    log.error("没有查找到数据:{}".format(data_name))
            else:
                log.error("没有查找到数据:{}".format(data_name))

    def list_button_by_text(self, text):
        '''根据文本返回按钮xpath'''
        button_xpath = self.select_data_button(text=text, tr_xpath=self.operate_button_xpath["tr_xpath"],
                                               text_relative_xpath=self.operate_button_xpath["text_relative_xpath"], button_relative_xpath=self.operate_button_xpath["button_relative_xpath"])
        return button_xpath

    def select_data_button(self, text, tr_xpath, text_relative_xpath, button_relative_xpath):
        '''根据文本内容定位按钮'''
        # 遍历当前页面
        text_xpath = tr_xpath + text_relative_xpath
        elements = self.get_elements(xpath=text_xpath)
        for element, index in zip(elements, range(len(elements))):
            # log.debug(element.text)
            if text == element.text:
                button_xpath = tr_xpath + \
                    "[{}]".format(index+1) + button_relative_xpath
                log.debug(button_xpath)
                log.debug(type(button_xpath))
                return button_xpath
        else:
            # 如果有分页，点下一页后继续查找
            if self.has_turn_page() is True:
                if self.current_turn_page() is not self.max_turn_page():
                    next_page_number = str(int(self.current_turn_page())+1)
                    self.turn_page(next_page_number=next_page_number)
                    return self.select_data_button(
                        text, tr_xpath, text_relative_xpath, button_relative_xpath)
                else:
                    log.error("no text:{}".format(text))
            else:
                log.error("no text:{}".format(text))

    def has_turn_page(self):
        '''判断是否有分页控件'''
        # try:
        #     self.get_elements(xpath=self.pagination_xpath)
        # except:
        #     log.info("no turn page")
        #     return False
        # return False
        elems = self.get_elements(xpath=self.pagination_xpath)
        if len(elems) == 0:
            log.debug("no turn page")
            return False
        else:
            return True

    def max_turn_page(self):
        '''获取最大页码'''
        max_turn_page = self.get_text(xpath=self.pagination_max_number_xpath)
        return max_turn_page

    def current_turn_page(self):
        '''获取当前页码'''
        current_turn_page = self.get_text(
            css=self.pagination_current_number_css)
        return current_turn_page

    def turn_page(self, next_page_number):
        '''翻页'''
        self.click(xpath=self.pagination_next_number_css)
        for _ in range(20):
            current_turn_page = self.get_text(
                css=self.pagination_current_number_css)
            log.debug("current_turn_page:{}".format(current_turn_page))
            log.debug("page_number:{}".format(next_page_number))
            if current_turn_page == next_page_number:
                break
            else:
                self.sleep(1)
        else:
            log.error("turn page fail")

    def wait_into_page(self, breadcrumb: str = None):
        '''等待进入页面'''
        for _ in range(20):
            try:
                current_breadcrumb = self.get_text(
                    xpath=self.breadcrumb_xpath)
            except:
                self.sleep(1)
                continue
            if current_breadcrumb == breadcrumb:
                return True
            else:
                log.debug("进入页面失败:当前页面{}不等于{}".format(
                    current_breadcrumb, breadcrumb))
                self.sleep(1)
        else:
            log.error("进入页面失败")
            return False

    def is_page(self, breadcrumb: str = None):
        '''判断页面'''
        try:
            current_breadcrumb = self.get_text(
                xpath=self.breadcrumb_xpath)
        except:
            return False
        if current_breadcrumb == breadcrumb:
            return True
        else:
            return False

    def alert_cancel(self):
        '''取消警告框'''
        self.click(xpath=self.alert_cancle_xpath)

    def alert_receive(self):
        '''确认警告框'''
        self.click(xpath=self.alert_receive_xpath)

    def wait_toast(self, toast_text=None):
        '''等待toast弹框'''
        if toast_text == None:
            return self.has_toast()
        if toast_text is not None:
            return self.is_toast_text(toast_text)

    def has_toast(self):
        '''判断是否出现toast'''
        # try:
        #     self.get_element(xpath=self.toast_xpath)
        # except:
        #     log.error("没有出现toast")
        #     return False
        # return True
        elems = self.get_elements(xpath=self.toast_xpath)
        if len(elems) == 0:
            log.error("没有出现toast")
            return False
        else:
            return True

    def is_toast_text(self, toast_text):
        '''判断toast文字'''
        try:
            current_toast_text = self.get_text(
                xpath=self.toast_xpath)
        except:
            log.error("没有获取到toast文字")
            return False
        if toast_text == current_toast_text:
            log.debug("toast文字正确")
            return True
        else:
            log.error("tosat文字错误toast_text:{}不等于current_toast_text:{}".format(
                toast_text, current_toast_text))
            return False

    def form_location_for_label(self, label, input_type):
        '''表单根据lable定位元素'''
        return self.form_location_xpath.format(label=label, input_type=input_type)

    def form_input(self, label, text):
        '''表单input输入'''
        self.type(xpath=self.form_location_for_label(
            label=label, input_type="input"), text=text)

    def form_input_clear(self, label):
        '''表单input清除输入'''
        self.clear(xpath=self.form_location_for_label(
            label=label, input_type="input"))

    def form_textarea(self, label, text):
        '''表单textarea输入'''
        self.type(xpath=self.form_location_for_label(
            label=label, input_type="textarea"), text=text)

    def form_select_click(self, label):
        '''表单select选择'''
        self.click(xpath=self.form_location_for_label(
            label=label, input_type="nz-select"))

    def form_checkbox_click(self, label):
        '''表单checkbox点击'''
        self.click(xpath=self.checkbox_path.format(label))

    def alert_form_location_for_label(self, label, input_type):
        '''表单根据lable定位元素'''
        return self.alert_form_location_xpath.format(label=label, input_type=input_type)

    def alert_form_input(self, label, text):
        '''alert input输入'''
        self.type(xpath=self.alert_form_location_for_label(
            label=label, input_type="input"), text=text)

    def alert_form_input_clear(self, label):
        '''alert input清除输入'''
        self.clear(xpath=self.alert_form_location_for_label(
            label=label, input_type="input"))

    def alert_form_textarea(self, label, text):
        '''alert textarea输入'''
        self.type(xpath=self.alert_form_location_for_label(
            label=label, input_type="textarea"), text=text)

    def alert_form_select_click(self, label):
        '''alert select选择'''
        self.click(xpath=self.alert_form_location_for_label(
            label=label, input_type="nz-select"))

    def wait_toast_save_successfully(self):
        '''等待toast【保存成功】'''
        return self.wait_toast("保存成功")

    def wait_toast_delete_successfully(self):
        '''等待toast【删除成功】'''
        self.wait_toast("删除成功")

    def wait_toast_edit_successfully(self):
        '''等待toast【修改成功】'''
        self.wait_toast("修改成功")

    def wait_toast_run_successfully(self):
        '''等待toast【运行成功】'''
        self.wait_toast(toast_text="运行成功")

    def wait_toast_close_successfully(self):
        '''等待toast【关闭成功】'''
        self.wait_toast(toast_text="关闭成功")

    def wait_toast_set_successfully(self):
        '''等待toast【设置成功】'''
        self.wait_toast(toast_text="设置成功")

    def wait_toast_add_static_proprety_successfully(self):
        '''等待toast【属性添加成功】'''
        self.wait_toast(toast_text="属性添加成功")

    def wait_toast_add_successfully(self):
        '''等待toast【添加成功】'''
        self.wait_toast(toast_text="添加成功")

    def filter_click_open(self):
        '''展开过滤器'''
        self.click(xpath=self.filter_xpath)

    def filter_click_close(self):
        '''收起过滤器'''
        self.filter_click_open()

    def filter_click_select(self):
        '''点击【查询】按钮'''
        self.click_button(button_name="查询")

    def filter_click_reset(self):
        '''点击【重置】按钮'''
        self.click_button(button_name="重置")
