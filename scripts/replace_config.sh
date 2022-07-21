# 参数替换脚本
sed -i "s/url = .*/url = \"https:\/\/${url}\"/g" config.py
sed -i "s/test_user = .*/test_user = \"${username}\"/g" config.py
sed -i "s/test_password = .*/test_password = \"${passwd}\"/g" config.py
sed -i "s/case_path = .*/case_path = \"${case_path}\"/g" config.py
sed -i "s/mail_to = .*/mail_to = \"${mail_to}\"/g" config.py