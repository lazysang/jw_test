from common.utils import Utils


class OtherPage(Utils):
    def login_input_username(self, username):
        '''输入用户名'''
        self.type(id_="inputUsername", text=username)

    def login_input_password(self, password):
        '''输入密码'''
        self.type(id_="inputPassword", text=password)

    def login_click_login(self):
        '''点击【登录】按钮'''
        self.click(css=".space-bottom")

    def other_user_click_username(self):
        '''点击用户下拉框'''
        self.click(css="div.header-right a.dropdown-user-text")

    def other_user_pulldown_click_userinformation(self):
        '''点击用户下拉框的个人信息'''
        self.click(xpath="/html/body/div/div/div/div/ul/li[1]")

    def other_user_pulldown_click_quit(self):
        '''点击用户下拉框的退出'''
        self.click(xpath="/html/body/div/div/div/div/ul/li[3]")


class Other(OtherPage):
    def open_website(self, url):
        '''打开网页'''
        self.open(url)

    def login(self, username, password):
        """登录系统"""
        # 输入用户名
        self.login_input_username(username)
        # 输入密码
        self.login_input_password(password)
        # 点击【登录】按钮
        self.login_click_login()

    def logout(self):
        '''退出登录'''
        self.other_user_click_username()
        self.other_user_pulldown_click_quit()
