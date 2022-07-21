POLICY_MENU = {
    "插件": ["//nz-sider/div/ul/li[1]"],
    "服务器业务流": ["//nz-sider/div/ul/li[2]"],
    "查询表管理": ["//nz-sider/div/ul/li[3]"],
    "用户管理/用户": ["//nz-sider/div/ul/li[4]", "//ul/li[4]/div[2]/ul/li[1]"],
    "用户管理/用户位置": ["//nz-sider/div/ul/li[4]", "//ul/li[4]/div[2]/ul/li[2]"],
    "用户管理/访问规则": ["//nz-sider/div/ul/li[4]", "//ul/li[4]/div[2]/ul/li[3]"],
    "用户管理/网络地址池": ["//nz-sider/div/ul/li[4]", "//ul/li[4]/div[2]/ul/li[4]"],
    "终端管理/终端": ["//nz-sider/div/ul/li[5]", "//ul/li[5]/div[2]/ul/li[1]"],
    "终端管理/终端组": ["//nz-sider/div/ul/li[5]", "//ul/li[5]/div[2]/ul/li[2]"],
    "终端管理/终端配置": ["//nz-sider/div/ul/li[5]", "//ul/li[5]/div[2]/ul/li[3]"],
    "终端管理/业务流管理": ["//nz-sider/div/ul/li[5]", "//ul/li[5]/div[2]/ul/li[4]"],
    "终端管理/查询表管理": ["//nz-sider/div/ul/li[5]", "//ul/li[5]/div[2]/ul/li[5]"],
    "资源管理/资源配置": ["//nz-sider/div/ul/li[6]", "//ul/li[6]/div[2]/ul/li[1]"],
    "系统配置/邮件中心": ["//nz-sider/div/ul/li[7]", "//ul/li[7]/div[2]/ul/li[1]"],
    "系统配置/短信中心": ["//nz-sider/div/ul/li[7]", "//ul/li[7]/div[2]/ul/li[2]"],
    "系统配置/系统信息": ["//nz-sider/div/ul/li[7]", "//ul/li[7]/div[2]/ul/li[3]"],
}
ANALYSER_MENU = {
    "首页": ["//nz-sider/div/ul/li[1]"],
    "报表/所有报表": ["//nz-sider/div/ul/li[2]", "//ul/li[2]/div[2]/ul/li[1]"],
    "报表/所有元件": ["//nz-sider/div/ul/li[2]", "//ul/li[2]/div[2]/ul/li[2]"],
    "报表/数据采集器": ["//nz-sider/div/ul/li[2]", "//ul/li[2]/div[2]/ul/li[3]"],
    "报表/视图管理": ["//nz-sider/div/ul/li[2]", "//ul/li[2]/div[2]/ul/li[4]"],
    "日志": ["//nz-sider/div/ul/li[3]"],
    "告警管理/告警策略": ["//nz-sider/div/ul/li[4]", "//ul/li[4]/div[2]/ul/li[1]"],
    "告警管理/告警模板": ["//nz-sider/div/ul/li[4]", "//ul/li[4]/div[2]/ul/li[2]"],
    "索引管理/数据索引": ["//nz-sider/div/ul/li[5]", "//ul/li[5]/div[2]/ul/li[1]"],
    "索引管理/备份与还原": ["//nz-sider/div/ul/li[5]", "//ul/li[5]/div[2]/ul/li[2]"],
}

INPUT_MENU = {
    "全局配置": ["//nz-sider/div/ul/li[1]"],
    "接口配置": ["//nz-sider/div/ul/li[2]"],
    "数据流": ["//nz-sider/div/ul/li[3]"],
    "数据输出": ["//nz-sider/div/ul/li[4]"],
    "管道配置": ["//nz-sider/div/ul/li[5]"],
    "Grok表达式": ["//nz-sider/div/ul/li[6]"],
    "查询表": ["//nz-sider/div/ul/li[7]"],
    "代理程序": ["//nz-sider/div/ul/li[8]"],
    "节点管理": ["//nz-sider/div/ul/li[9]"],
    "日志_1": ["//nz-sider/div/ul/li[10]"],
}
OPS_MENU = {
    "个人信息": ["//nz-sider/div/ul/li[1]"],
    "用户管理": ["//nz-sider/div/ul/li[2]"],
    "角色管理": ["//nz-sider/div/ul/li[3]"],
    "授权管理": ["//nz-sider/div/ul/li[4]"],
}
USER_MENU = {
    "服务管理": ["//nz-sider/div/ul/li[1]"],
    "系统状态": ["//nz-sider/div/ul/li[2]"],
    "系统设置": ["//nz-sider/div/ul/li[3]"],
}
MENU = {**POLICY_MENU, **ANALYSER_MENU, **INPUT_MENU, **OPS_MENU, **USER_MENU}

if __name__ == "__main__":
    # print(type(ANALYSER_MENU))
    print(ANALYSER_MENU["首页"][0])
    print(type(ANALYSER_MENU["首页"]))
    # print(len(ANALYSER_MENU["首页"]))
    # print(ANALYSER_MENU["索引/视图管理"][0])
    # print(ANALYSER_MENU)
    # print(MENU)
    print(MENU)
