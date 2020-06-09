# import pdftotree
import subprocess
import pyocr
import importlib
import sys, os
import time
from scrapy.selector import Selector
import requests

importlib.reload(sys)
time1 = time.time()


def pdf_to_html(pdf_path):
    """
    将pdf转HTML，成功与不成功的
    :param pdf_path: pdf的本地路径
    :return:如果该文件是扫描版，返回扫描版，如果转换失败返回False,如果成功返回转化成HTML的地址
    """
    try:
        pdf_file = pdf_path
        html_output = pdf_file.split(".")[0] + ".html"
        html_output_path = html_output.split("/")[-1]
        cmd = 'pdftotree' + " " + "-o" + " " + html_output + " " + pdf_file
        b = (cmd.split())
        for i in b:
            if "cannot build tree structure" in i:
                raise Exception("该文件是PDF扫描版")
            if "tabula.errors.JavaNotFoundError" in i:
                raise Exception(
                    "tabula.errors.JavaNotFoundError: `java` command is not found from this Python process. "
                    "Please ensure Java is installed and PATH is set for `java`")
            html_output_path = html_output_path + html_output_path
            domain_url = "/Users/gongsi/PycharmProjects/sticker/formal/AIQT_DATA/citic_report/citic_report/down_pdf/"
            file_path = os.path.join(os.path.dirname(__file__), )
            print(">>>>file", file_path)
            if os.path.exists(domain_url + html_output_path):
                return html_output_path
            return False
    except Exception as e:
        print('出现错误了', e)
        if "PDF扫描版" in e:
            return "PDF扫描版"
        return False

def run_command(command):
    """
    执行cmd命令
    :param command: cmd字符串
    :return: 包含执行命令结果的一个迭代器
    """
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

pdf_to_html('test.pdf')

