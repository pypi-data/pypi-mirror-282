from python123.settings import cache_path
from python123.jsondb import JSONDatabase
from python123.settings import cache_img_path
from markdownify import markdownify as html_to_md
import os
import re
import html
from html.parser import HTMLParser
from io import StringIO
import requests
import json


class MLStripper(HTMLParser):
    """html清除"""

    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()


def strip_html_tags(h: str) -> str:
    """
    去除html标签
    :param h:  html字符串
    :return:  去除html标签后的字符串
    """
    h = html.unescape(h)
    h = re.sub(r'<script[^>]*>.*?</script>', '', h)
    h = re.sub(r'<style[^>]*>.*?</style>', '', h)
    s = MLStripper()
    s.feed(h)
    return s.get_data()


def replace_img_link(text: str) -> str:
    """
    替换图片链接
    :param text: 文本
    :return: 替换后的图片地址
    """
    if "![](/images/" in text:
        for re_url in re.findall("/images/(.*?)\\)", text):
            img_url, img_name = f"https://python123.io/images/{re_url}", re_url.split("/")[2]
            img_path = os.path.join(cache_img_path, img_name)
            if not os.path.exists(img_name):
                r = requests.get(img_url)
                with open(img_path, "wb") as f:
                    f.write(r.content)
            text = text.replace(re_url, f"{img_path}").replace("/images/", "")  # 替换图片地址
        return text
    else:
        return text


def pretreatment_unit_score_data(course_id: int, unit_id: int) -> list:
    """
    预处理单元成绩数据
    :param course_id:  课程ID
    :param unit_id:  课程单元ID
    :return: 学生信息列表
    """
    unit_score_data_path = os.path.join(cache_path, f"{course_id}_{unit_id}_unit_score_data.json")
    unit_score_data = JSONDatabase(unit_score_data_path).read()
    data_lst = []  # 保存预处理后的数据
    for user in unit_score_data["data"]["users"]:
        if len(user.get("totalCommits")) > 0:
            user_id = user.get("_id")  # 学生id
            student_id = user.get("student_id")  # 学生学号
            name = user.get("name")  # 学生姓名
            classroom = user.get("classroom")  # 学生班级
            start_at = user.get("record", {}).get("start_at", "")
            commit_at = user.get("record", {}).get("commit_at", "")
            record_score = user.get("record", {}).get("score", 0)  # 习题总分
            record_problem_ids = user.get("record", {}).get("problem_ids", [])  # 随机组卷习题列表
            record_problems = user.get("record", {}).get("problems", [])  # 习题列表
            problems_lst = []  # 作答习题列表
            if len(record_problems) > 0:
                for problems in record_problems:  # 提取题号和得分
                    score = problems.get("score", 0)  # 习题得分
                    extra_score = problems.get("extra_score", 0)  # 习题加分
                    if score is None:
                        score = 0
                    if len(record_problem_ids) > 0:  # 开启组卷查询后添加
                        if problems.get("_id") in record_problem_ids:
                            problems_lst.append({
                                "习题ID": problems.get("_id"),
                                "习题得分": score,
                                "习题加分": extra_score,
                                "作答选项": problems.get("answer", "")
                            })
                    else:  # 没开启组卷，直接添加
                        problems_lst.append({
                            "习题ID": problems.get("_id"),
                            "习题得分": score,
                            "习题加分": extra_score,
                            "作答选项": problems.get("answer", "")
                        })
            data_lst.append({
                "学生ID": user_id,
                "学生学号": student_id,
                "学生姓名": name,
                "学生班级": classroom,
                "习题总分": record_score,
                "作答习题": problems_lst,
                "开始作答时间": start_at,
                "交卷时间": commit_at,
                "单元所有习题列表": unit_score_data["data"]["problems"],
                "随机组卷习题列表": record_problem_ids
            })
    return data_lst


def pretreatment_choice_data(problem_data: dict) -> dict:
    """
    选择题数据预处理
    :param problem_data: 选择题数据
    :return:  处理后的数据
    """
    description = html_to_md(problem_data["description"]).replace("\n", "")  # 选择题习题描述
    description = replace_img_link(description)  # 替换图片链接地址
    contents = problem_data["content"]  # 习题选项
    contents_ls = []
    for content in json.loads(contents):  # 解析习题选项
        text = html_to_md(content[1]).replace("\n", "")
        text = replace_img_link(text)  # 替换图片链接地址
        contents_ls.append({"编号": content[0], "题目": text})
    return {"习题描述": description, "习题选项": contents_ls}


def pretreatment_programming_data(problem_data: dict) -> dict:
    """
    编程题数据预处理
    :param problem_data:    编程题数据
    :return:  处理后的数据
    """
    name = problem_data["name"]
    try:
        markdown_content = strip_html_tags(problem_data["content"])
    except KeyError:
        markdown_content = ""
    return {"习题名称": name, "习题简介": markdown_content}


def pretreatment_true_false_data(problem_data: dict) -> dict:
    """
    判断题数据预处理
    :param problem_data:    判断题数据
    :return:  处理后的数据
    """
    description = strip_html_tags(problem_data["description"])
    answer = problem_data["answer"]
    return {"习题描述": description, "作答选项": answer}


def pretreatment_choice_blank_data(problem_data: dict) -> dict:
    """
    选择填空题数据预处理
    :param problem_data:    选择填空题数据
    :return:  选择填空题数据
    """
    description = strip_html_tags(problem_data["description"])
    description = replace_img_link(description)  # 替换图片链接地址
    answer = problem_data["answer"]
    return {"习题描述": description, "作答选项": answer}
