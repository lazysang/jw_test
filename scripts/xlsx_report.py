from scripts.html_analysis import HtmlAnalysis
import pandas as pd
from seldom.running.config import BrowserConfig


class XlsxReport():
    def __init__(self, html_path=None, report_path=None):
        self.html_path = html_path if html_path is not None else BrowserConfig.REPORT_PATH
        self.report_path = report_path if report_path is not None else './reports/report.xlsx'

    def create_xlsx_report(self):
        '''生成xlsx报告-返回报告路径'''
        html = HtmlAnalysis(html_path=self.html_path)
        statistics_list = html.case_statistics()
        case_list = html.analysis_case()
        sheet_statistics = pd.DataFrame(
            statistics_list, columns=[u"状态", u"数量"])
        sheet_statistics
        sheet_case = pd.DataFrame(case_list, columns=[u"标题", u"执行结果"])
        with pd.ExcelWriter(self.report_path) as writer:
            sheet_statistics.style.applymap(self.sheet_statistics_color, subset=u"状态").to_excel(
                writer, sheet_name=u"测试概览", index=False)
            sheet_case.style.applymap(self.sheet_case_color, subset=u"执行结果").to_excel(
                writer, sheet_name=u"测试详情", index=False)
        return self.report_path

    def sheet_case_color(self, val):
        '''设置测试详情的颜色'''
        if val == "pass":
            color = "green"
        else:
            color = "red"
        return 'color: {}'.format(color)

    def sheet_statistics_color(self, val):
        '''设置测试概览的颜色'''
        if val == "通过用例":
            color = 'green'
        elif val == "失败用例":
            color = 'red'
        elif val == "错误用例":
            color = 'yellow'
        else:
            color = 'gray'
        return 'background-color: {}'.format(color)


if __name__ == "__main__":
    report = XlsxReport(html_path='./reports/result.html',
                        report_path='./reports/report.xlsx')
    # report = XlsxReport()
    report.create_xlsx_report()
