from common.utils import Utils


class QueryPage(Utils):
    def into_incident_menu(self):
        '''进入日志菜单'''
        # 进入动态数据分析
        self.into_module("动态数据分析")
        # 进入日志菜单
        self.into_menu("日志")

    def wait_into_page_incident_list(self):
        '''等待进入【日志页面】'''
        self.wait_into_page("查询")

    def query_list_click_index_select(self):
        '''点击选择索引下拉框'''
        self.click(xpath='//*[@id="selectIndex"]')

    def query_list_select_index(self, index_name):
        '''选中索引'''
        self.pull_down_list_select(text=index_name)

    def query_list_click_plus_sign(self):
        '''点击加号展开第一条数据'''
        self.click(xpath='//mat-table/mat-row[1]/mat-cell[1]')


class Query(QueryPage):
    def view_log(self, index_name):
        '''查看日志'''
        self.into_incident_menu()
        self.wait_into_page_incident_list()
        self.query_list_click_index_select()
        self.query_list_select_index(index_name)

    def view_log_detail(self, index_name):
        '''查看日志详情'''
        self.into_incident_menu()
        self.wait_into_page_incident_list()
        self.query_list_click_index_select()
        self.query_list_select_index(index_name)
        self.query_list_click_plus_sign()
