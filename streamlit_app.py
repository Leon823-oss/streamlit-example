
import streamlit as st
# import multiprocessing
# from multiprocessing import Process, Value, Array
# import time, os
import snap7
# import struct
import re

from streamlit_lottie import st_lottie
import json


# class S7_Client(object):
#     def __init__(self):
#         self.online = False
#         self.concount = 0
#         self.plc = snap7.client.Client()
#         self.plc.set_connection_type(1)  # 1 for PG, 2 for OP, 3 to 10 for S7 Basic

#     # def connect(self, ip, rack=0, slot=1):
#     #     try:
#     #         # mylog.logger.info("正在尝试连接 PLC %s" % (ip,))
#     #         self.plc.connect(ip, rack, slot)
#     #         if self.plc.get_connected():
#     #             # mylog.log/ger.info(ip + ' 连接成功')
#     #             self.online = True
#     #
#     #     except Exception as e:
#     #         self.plc.connect(ip, rack, slot)
#     #
#     #     finally:
#     #         if not self.plc.get_connected():
#     #             self.plc.connect(ip, rack, slot)

#     def connect(self, ip, rack=0, slot=1):
#         while not self.plc.get_connected():
#            try:
#                self.plc.connect(ip, rack, slot)
#                time.sleep(0.2)
#            except Exception as e:
#                # print("not online")
#                continue


#     def disconnect(self):
#         self.plc.disconnect()
#         # mylog.logger.info('连接断开')

#     def get_connected(self):
#         return self.plc.get_connected()

#     def get_cpu_state(self):
#         return self.plc.get_cpu_state()

#     # region Read 数据
#     def read_db_bool(self, db_num, start):
#         db_str = self.plc.read_area(0x84, db_num, start, 1)
#         db_tuple_bool = struct.unpack("?", db_str)
#         return db_tuple_bool[0]

#     def read_i_bool(self, db_num, start):
#         i_str = self.plc.read_area(0x81, db_num, start, 1)
#         i_tuple_bool = struct.unpack("?", i_str)
#         return i_tuple_bool[0]

#     def read_q_bool(self, db_num, start):
#         q_str = self.plc.read_area(0x82, db_num, start, 1)
#         q_tuple_bool = struct.unpack("?", q_str)
#         return q_tuple_bool[0]

#     def read_db_byte(self, db_num, start):
#         db_str = self.plc.read_area(0x84, db_num, start, 1)
#         db_tuple_byte = struct.unpack("B", db_str)
#         return db_tuple_byte[0]

#     def read_I_byte(self, db_num, start):
#         db_str = self.plc.read_area(0x81, db_num, start, 1)
#         db_tuple_byte = struct.unpack("B", db_str)
#         return db_tuple_byte[0]

#     def read_Q_byte(self, db_num, start):
#         db_str = self.plc.read_area(0x82, db_num, start, 1)
#         db_tuple_byte = struct.unpack("B", db_str)
#         return db_tuple_byte[0]

#     def read_db_int(self, db_num, start):
#         db_str = self.plc.read_area(0x84, db_num, start, 2)
#         db_tuple_int = struct.unpack(">h", db_str)  # 大小端
#         return db_tuple_int[0]

#     def read_db_uint(self, db_num, start):
#         db_str = self.plc.read_area(0x84, db_num, start, 2)
#         db_tuple_int = struct.unpack(">H", db_str)  # 大端
#         return db_tuple_int[0]

#     def read_db_dint(self, db_num, start):
#         db_str = self.plc.read_area(0x84, db_num, start, 4)
#         db_tuple_dint = struct.unpack(">i", db_str)  # 大端
#         return db_tuple_dint[0]

#     def read_db_udint(self, db_num, start):
#         db_str = self.plc.read_area(0x84, db_num, start, 4)
#         db_tuple_dint = struct.unpack(">I", db_str)  # 大端
#         return db_tuple_dint[0]

#     def read_db_real(self, db_num, start):
#         db_str = self.plc.read_area(0x84, db_num, start, 4)
#         db_tuple_real = struct.unpack("!f", db_str)
#         return db_tuple_real[0]

#     def read_db_char(self, db_num, start):
#         db_str = self.plc.read_area(0x84, db_num, start, 1)
#         db_tuple_char = struct.unpack("c", db_str)
#         return db_tuple_char[0]

#     def read_db_string(self, db_num, start, length):
#         db_str = self.plc.read_area(0x84, db_num, start, length + 2)
#         db_tuple_str = struct.unpack(str(length + 2) + 's', db_str)
#         return str(db_tuple_str[0][2:], encoding='gbk')

#     def read_M_int(self, db_num, start):
#         db_str = self.plc.read_area(0x83, db_num, start, 2)
#         db_tuple_int = struct.unpack(">h", db_str)
#         return db_tuple_int[0]

#     def read_M_bool(self, db_num, start):
#         i_str = self.plc.read_area(0x83, db_num, start, 1)
#         i_tuple_bool = struct.unpack("?", i_str)
#         return i_tuple_bool[0]

#     def read_M_byte(self, db_num, start):
#         db_str = self.plc.read_area(0x83, db_num, start, 1)
#         db_tuple_byte = struct.unpack("B", db_str)
#         return db_tuple_byte[0]

#     def read_db(self, db_num, start, size):
#         # db_buf = self.plc.db_read(db_num, start, size)
#         # db_tuple_read = struct.unpack("B", db_buf)
#         return self.plc.db_read(db_num, start, size)

#     def read_plc_datetime(self, db_num, start):
#         YEAR = self.read_db_uint(db_num, start)
#         MONTH = self.read_db_byte(db_num, start + 2)
#         DAY = self.read_db_byte(db_num, start + 3)
#         WEEKDAY = self.read_db_byte(db_num, start + 4)
#         HOUR = self.read_db_byte(db_num, start + 5)
#         MINUTE = self.read_db_byte(db_num, start + 6)
#         SECOND = self.read_db_byte(db_num, start + 7)
#         NANOSECOND = self.read_db_udint(db_num, start + 8)
#         strdatetime = "%04d" % YEAR + '-' + "%02d" % MONTH + "-" + "%02d" % DAY + " " + "%02d" % HOUR + ':' + \
#                       "%02d" % MINUTE + ':' + "%02d" % SECOND + ':' + "%04d" % NANOSECOND
#         return strdatetime

#     # endregion
#     # region Write 数据
#     def write_db_bool(self, db_num, start, data):
#         _data = struct.pack("!?", data)
#         self.plc.write_area(0x84, db_num, start, _data)

#     def write_db_byte(self, db_num, start, data):
#         _data = struct.pack("B", data)
#         self.plc.write_area(0x84, db_num, start, _data)

#     def write_db_int(self, db_num, start, data):
#         _data = struct.pack(">h", data)
#         self.plc.write_area(0x84, db_num, start, _data)

#     def write_db_uint(self, db_num, start, data):
#         _data = struct.pack(">H", data)
#         self.plc.write_area(0x84, db_num, start, _data)

#     def write_db_dint(self, db_num, start, data):
#         _data = struct.pack(">i", data)
#         self.plc.write_area(0x84, db_num, start, _data)

#     def write_db_dint(self, db_num, start, data):
#         _data = struct.pack(">I", data)
#         self.plc.write_area(0x84, db_num, start, _data)

#     def write_db_float(self, db_num, start, data):
#         _data = struct.pack("!f", data)
#         self.plc.write_area(0x84, db_num, start, _data)

#     def write_db_string(self, db_num, start, data):
#         _data = struct.pack(str(len(data) + 2) + 's', data.encode('utf-8'))  #
#         self.plc.write_area(0x84, db_num, start, _data)

#     def write_db_char(self, db_num, start, data):
#         _data = struct.pack("c", data.encode('utf-8'))
#         self.plc.write_area(0x84, db_num, start, _data)

#     def write_M_int(self, db_num, start, data):
#         _data = struct.pack(">h", data)
#         self.plc.write_area(0x83, db_num, start, _data)

#     def write_M_bool(self, db_num, start, data):
#         _data = struct.pack("!?", data)
#         self.plc.write_area(0x83, db_num, start, _data)

#     def write_M_byte(self, db_num, start, data):
#         _data = struct.pack("B", data)
#         self.plc.write_area(0x83, db_num, start, _data)

#     def write_Q_byte(self, db_num, start, data):
#         _data = struct.pack("B", data)
#         self.plc.write_area(0x82, db_num, start, _data)
    # endregion


# car1 = S7_Client()
# car2 = S7_Client()
# car3 = S7_Client()
# ip1 = '10.10.41.31'
# ip2 = '10.10.41.32'
# ip3 = '10.10.41.33'

def processing_1():
    while 1:
        time.sleep(3)


def processing_2():
    while 1:
        print("processing 2")
        time.sleep(3)


def check_ip(ipAddr):
    pattern = "^([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])$"
    result = re.fullmatch(pattern, ipAddr)
    if result:
        return True
    else:
        return False


def main():

    st.set_page_config(
        page_title="Sweet APP",
        page_icon=":cake:",
        layout="wide",
        initial_sidebar_state="auto",
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# This is a header. This is an *extremely* cool app!"
        }
    )

    def sd_submitbtn_callback():
        st.write(st.session_state.sd_devices_choose)

    st.caption("APP")
    # st.title("APP")

    st.markdown('''
    <hr/>
    ''', unsafe_allow_html=True)

    c1, c2, c3 = st.sidebar.columns([0.5, 1, 0.5])
    with c1:
        with open("83685-hubit.json", "r", errors='ignore') as f:
            data1 = json.load(f)
            st_lottie(data1, key="1")
    with c2:
        st.sidebar.empty()
        st.title("app factory")
    with c3:
        st.sidebar.empty()

    st.sidebar.markdown('''
    <hr/>
    ''', unsafe_allow_html=True)

    devices_list = ["", "货物提升机", "小车", "换层提升机", '安全门', '充电机']
    devices = st.sidebar.selectbox("选择设备", devices_list, key='sd_devices_choose')
    # st.sidebar.write("你选择的设备是 ", devices)
    if devices != "":
        with st.sidebar.form("form_devices"):
            st.write("请输入设备信息")
            device_num = st.number_input("设备数量", min_value=1, max_value=100, step=1)
            ip_temp = st.text_input("设备IP地址")
            col1, col2 = st.columns(2)
            with col1:
                btn_conn = st.form_submit_button("点击连接")
                if btn_conn:
                    if check_ip(ip_temp):
                        pass
                    else:
                        st.error("输入格式不正确！")

            with col2:
                btn_disconn = st.form_submit_button("断开连接")
                if btn_disconn:
                    pass

    else:
        pass

    if devices == '小车' and check_ip(ip_temp):
        st.write("当前设备*************", devices)

        temp_c = int(device_num)
        info_col = st.columns(temp_c)

        # row_count = temp_c // 8
        # row_count_mod = temp_c % 8
        #
        # print(row_count)
        # print(row_count_mod)

        for r in range(temp_c):
            with info_col[r]:
                with st.expander("点击查看状态", expanded=True):
                    st.success("连接成功")

        st.markdown('''
        <hr/>
        ''', unsafe_allow_html=True)

        st.write("设备控制按钮*", devices)
        col = st.columns(8)
        with col[0]:
            st.empty()
        with col[1]:
            btn = st.button("全部初始化")
            if btn:
                print("1")
        with col[2]:
            st.button("全部在线预约")
        with col[3]:
            st.button("全部离线预约")
        with col[4]:
            st.button("全部紧急停止")
        with col[5]:
            st.button("全部故障复位")
        with col[6]:
            st.empty()
        with col[7]:
            st.empty()
    # rad = st.sidebar.radio("Select function", ('Signal mode', 'All mode'))
    # if rad == 'Signal mode':
    #     pass
    # else:
    #     pass


    # slider_input = st.slider('My slider', 0, 10, key='my_slider', on_change=form_callback)
    # checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    # st.text_input("当前巷道", value=val, on_change=form_callback, key='my_input')
    #
    # if st.checkbox("view"):
    #     st.button("开始")


if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=processing_1, args=())
#     p2 = multiprocessing.Process(target=processing_2, args=())
#     p1.start()
#     p2.start()
    #
    main()
