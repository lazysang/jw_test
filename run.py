import seldom
import os
import sys
from seldom import ChromeConfig
from selenium.webdriver import ChromeOptions
from config import SMTPConfig, TestConfig
# from seldom import SMTP
from scripts.send_email import SMTP
from scripts.xlsx_report import XlsxReport
import platform

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Windows系统配置
if platform.system() == "Windows":
    # 手动指定驱动路径
    ChromeConfig.command_executor = "chromedriver.exe"
    # 浏览器无头模式
    ChromeConfig.headless = True

    options = ChromeOptions()
    # 忽略usb设备报错信息
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # 忽略证书错误信息
    options.add_argument('--ignore-certificate-errors')
    ChromeConfig.options = options

# Linux系统配置
if platform.system() == "Linux":
    # 手动指定驱动路径
    ChromeConfig.command_executor = "chromedriver"

    options = ChromeOptions()
    # 忽略usb设备报错信息
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # 忽略证书错误信息
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    ChromeConfig.options = options


if __name__ == '__main__':
    # run test file
    # seldom.main("./test_dir/test_sample.py")
    # run test dir
    # seldom.main("./test_dir/auto_test",browser='gc')
    seldom.main(TestConfig.case_path, browser='gc',
                language="zh-CN", description="自动化测试",
                title="自动化测试报告", open=False)
    xlsx_report = XlsxReport()
    xlsx_report_path = xlsx_report.create_xlsx_report()
    smtp = SMTP(user=SMTPConfig.mail_user,
                password=SMTPConfig.mail_password, host=SMTPConfig.mail_host)
    smtp.sendmail(to=SMTPConfig.mail_to, delete=True,
                  subject=SMTPConfig.mail_subject,
                  xlsx_report=xlsx_report_path)
    # smtp.sendmail(to=SMTPConfig.mail_to, delete=True,
    #               subject=SMTPConfig.mail_subject)
