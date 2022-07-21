from bs4 import BeautifulSoup
from seldom.logging import log


class HtmlAnalysis():
    def __init__(self, html_path):
        self.html_path = html_path

    def get_html(self):
        soup = BeautifulSoup(
            open(self.html_path, encoding='utf-8'), features='html.parser')
        return soup

    def get_tbody(self):
        ''''''
        html = self.get_html()
        tbody = html.select("tbody")
        return tbody

    def get_tbody_tr(self):
        '''返回所有tr对象'''
        html = self.get_html()
        tr = html.select("tbody tr")
        return tr

    def get_tr_id(self, index):
        '''获取id'''
        tbody_tr = self.get_tbody_tr()
        try:
            tr_id = tbody_tr[index]["id"]
        except KeyError:
            print("没有属性【id】")
            tr_id = None
        return tr_id

    def get_case_name(self, index):
        '''获取case名称'''
        tbody_tr = self.get_tbody_tr()
        try:
            text = tbody_tr[index].select("td")[1].select("div")[0].text
            case_name = text.split(" ")[0]
        except:
            case_name = "casename获取失败,id为{}".format(self.get_tr_id(index))
            log.error("casename获取失败,id为{}".format(self.get_tr_id(index)))
        if case_name in ["失败用例","错误用例","跳过用例"]:
            try:
                text = tbody_tr[index].select("td")[0].select("div")[0].text
                case_name = text
            except:
                case_name = "casename获取失败,id为{}".format(self.get_tr_id(index))
                log.error("casename获取失败,id为{}".format(self.get_tr_id(index)))
        return case_name

    def get_case_status(self, index):
        '''获取case执行状态'''
        tbody_tr = self.get_tbody_tr()
        try:
            status = tbody_tr[index].select("td")[3].select("a")[0].text
        except:
            try:
                status = tbody_tr[index].select("td")[3].text
            except:
                status = None
                log.error("未获取到执行状态信息,id为{}".format(self.get_tr_id(index)))
        return status

    def case_statistics(self):
        '''获取case执行统计,返回统计列表'''
        self.statistics_list = []
        html = self.get_html()
        pass_case = html.select(
            '#headContainer > div > div:nth-child(2) > div:nth-child(1) > div > div.row > div.col > span.h3.font-bold.mb-0')[0].text
        fail_case = html.select(
            '#headContainer > div > div:nth-child(2) > div:nth-child(2) > div > div.row > div.col > span.h3.font-bold.mb-0')[0].text
        error_case = html.select(
            '#headContainer > div > div:nth-child(3) > div:nth-child(1) > div > div.row > div.col > span.h3.font-bold.mb-0')[0].text
        skip_case = html.select(
            '#headContainer > div > div:nth-child(3) > div:nth-child(2) > div > div.row > div.col > span.h3.font-bold.mb-0')[0].text
        self.statistics_list.append(["通过用例", pass_case])
        self.statistics_list.append(["失败用例", fail_case])
        self.statistics_list.append(["错误用例", error_case])
        self.statistics_list.append(["跳过用例", skip_case])
        return self.statistics_list

    def analysis_case(self):
        '''解析case,返回case列表'''
        self.case_list = []
        for index in range(len(self.get_tbody_tr())):
            if self.get_tr_id(index=index):
                log.debug("解析数据id:{}".format(self.get_tr_id(index=index)))
                self.case_list.append([self.get_case_name(
                    index=index), self.get_case_status(index=index)])
        return self.case_list


if __name__ == "__main__":
    # html = HtmlAnalysis(html_path='./reports/2022_07_11_13_45_48_result.html')
    html = HtmlAnalysis(html_path='./reports/result.html')
    html.get_tbody_tr()
    html.get_tr_id(index=1)
    html.get_case_name(index=1)
    html.get_case_status(index=1)
    html.analysis_case()
    html.case_statistics()
    print(html.analysis_case())
