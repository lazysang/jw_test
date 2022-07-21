from .analyser import Analyser
from .other import Other
from .input import Input
from .policy import Policy


class Method(Other, Policy, Analyser, Input,):
    def init_linux_log(self, flow_name="init业务流名称", index_name="init索引名称", index_prefix="initprefix", interface_type="Syslog TCP", interface_name="init接口名称",
                       interface_port="514", stream_name="init数据流名称", stream_description="init数据流描述", output_name="init输出名称"):
        '''添加linux日志'''
        self.add_flow(flow_name)
        self.add_simple_rule_for_flow(flow_name)
        self.activate_flow(flow_name)
        self.index_function_add_index(index_name, index_prefix)
        self.interface_function_add_interface_of_syslog_tcp(
            interface_type, interface_name, interface_port)
        self.interface_function_enable_port_mapping()
        self.stream_function_add_stream(stream_name, stream_description)
        self.stream_function_add_rule_for_stream(stream_name, interface_name)
        self.stream_function_add_output_for_stream(stream_name, output_name, index_name)
        self.stream_function_run_stream(stream_name)

    def delete_init_linux_log(self, index_name="init索引名称", output_name="init输出名称", stream_name="init数据流名称", interface_name="init接口名称", flow_name="init业务流名称"):
        '''删除linux日志'''
        self.index_function_delete_index(index_name)
        self.output_function_delete_output(output_name)
        self.stream_function_delete_stream(stream_name)
        self.interface_function_delete_interface(interface_name)
        self.delete_flow(flow_name)
