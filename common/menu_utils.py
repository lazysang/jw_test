from seldom.webdriver import WebDriver
from seldom.logging import log
from .menu_dict import MENU


class MemuUtilsPath():
    # 模块标题
    title_css = '.server-title'
    # 模块-安全策略配置
    module_configserver_css = '.configserver'
    # 模块-动态数据分析
    module_server_css = '.server'
    # 模块-动态数据接入
    module_interfaceserver_css = '.interfaceserver'
    # 模块-平台用户管理
    module_authserver_css = '.authserver'
    # 模块-系统运维控制
    module_console_css = '.console'
    # 返回主页按钮
    return_home_xpath = "/html/body/app-root/app-main/nz-layout/nz-header/div/div[2]/a[2]"
    # 主页logo
    home_logo_xpath = '//nz-tabset/nz-tabs-nav/div[2]/img'
    # 选中的菜单
    menu_select_css = '.ant-menu-item-selected>a>span'
    # 菜单位置
    menu_path_xpath = '//nz-sider//span[normalize-space(text())="{}"]/ancestor-or-self::li[1]'


class MemuUtils(WebDriver, MemuUtilsPath):
    def is_module(self, module_name: str = None):
        '''判断模块'''
        try:
            current_module_name = self.get_text(
                css=self.title_css)
        except:
            log.debug("模块不匹配")
            return False
        if current_module_name == module_name:
            return True
        else:
            return False

    def wait_into_module(self, module_name):
        '''等待进入模块'''
        try:
            current_module_name = self.get_text(
                css=self.title_css)
        except:
            log.error("进入模块失败")
            return False
        if current_module_name == module_name:
            return True
        else:
            log.error("进入模块失败")
            return False

    def into_module(self, module_name: str = None):
        '''进入模块
        模块：
            安全策略配置
            动态数据分析
            动态数据接入
            平台用户管理
            系统运维控制
        '''
        if self.is_module(module_name) is True:
            return None
        if self.is_home() is False:
            self.back_home()
        if module_name == "安全策略配置":
            self.click(css=self.module_configserver_css)
            self.wait_into_module(module_name=module_name)
            return None
        if module_name == "动态数据分析":
            self.click(css=self.module_server_css)
            self.wait_into_module(module_name=module_name)
            return None
        if module_name == "动态数据接入":
            self.click(css=self.module_interfaceserver_css)
            self.wait_into_module(module_name=module_name)
            return None
        if module_name == "平台用户管理":
            self.click(css=self.module_authserver_css)
            self.wait_into_module(module_name=module_name)
            return None
        if module_name == "系统运维控制":
            self.click(css=self.module_console_css)
            self.wait_into_module(module_name=module_name)
            return None
        log.error("module_name error:{}".format(module_name))

    def is_home(self):
        '''判断是否在主页'''

        home_title = self.get_title
        if home_title == "统一管理平台":
            return True
        else:
            return False

    def back_home(self):
        '''返回主页'''
        self.click(
            xpath=self.return_home_xpath)
        self.wait_into_home()

    def wait_into_home(self):
        '''等待进入主页'''
        # try:
        #     self.get_element(xpath=self.home_logo_xpath)
        # except:
        #     log.error("进入主页失败")
        #     return False
        # return True
        elems = self.get_elements(xpath=self.home_logo_xpath)
        if len(elems) == 0:
            log.error("进入主页失败")
            return False
        else:
            return True

    def is_menu(self, menu_name: str = None):
        '''判断当前菜单'''
        try:
            current_menu_name = self.get_text(
                css=self.menu_select_css)
        except:
            log.debug("菜单不匹配")
            return False
        if current_menu_name == menu_name:
            return True
        else:
            return False

    # def wait_into_menu(self, breadcrumb: str = None):
    #     '''等待进入菜单'''
    #     try:
    #         current_breadcrumb = self.get_text(
    #             xpath='//lib-breadcrumb/nz-breadcrumb/nz-breadcrumb-item[1]//a')
    #     except:
    #         log.error("进入菜单失败")
    #         return False
    #     if current_breadcrumb == breadcrumb:
    #         return True
    #     else:
    #         log.error("进入菜单失败")
    #         return False

    # def into_menu(self, menu_name):
    #     '''进入菜单'''
    #     try:
    #         menu_xpath_list = MENU[menu_name]
    #     except:
    #         log.error("输入菜单不再字典中：{}".format(menu_name))
    #         return None
    #     if len(menu_xpath_list) == 1:
    #         if self.is_menu(menu_name) is True:
    #             return None
    #         else:
    #             self.click(xpath=menu_xpath_list[0])
    #             self.sleep(1)
    #             return None
    #     if len(menu_xpath_list) == 2:
    #         last_menu = menu_name.split('/')[-1]
    #         if self.is_menu(last_menu) is True:
    #             return None
    #         else:
    #             for index in range(len(menu_xpath_list)):
    #                 self.click(xpath=menu_xpath_list[index])
    #             self.sleep(1)
    #             return None

    def into_menu(self, menu_name):
        '''进入菜单
        菜单：
            "日志"
            "告警管理/告警策略"
        '''
        menu_list = menu_name.split("/")
        if len(menu_list) == 1:
            if self.is_menu(menu_name) is True:
                return None
            else:
                self.click(
                    xpath=self.menu_path_xpath.format(menu_list[0]))
                self.sleep(1)
                return None
        if len(menu_list) == 2:
            if self.is_menu(menu_list[-1]) is True:
                return None
            else:
                for index in range(len(menu_list)):
                    self.click(
                        xpath=self.menu_path_xpath.format(menu_list[index]))
                self.sleep(1)
                return None
