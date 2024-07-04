import os
from python123.cache import cache_path
from python123.jsondb import JSONDatabase
from python123.pretreatment import (
    pretreatment_choice_data,
    pretreatment_programming_data,
    pretreatment_true_false_data,
    pretreatment_choice_blank_data
)
from python123.settings import cache_code_path, download_path
from python123.F import check_and_create_folder
from datetime import datetime, timedelta
import re
import json


class Generator:
    def __init__(self, course_id: int, unit_id: int, student_info: dict):
        self.course_id, self.unit_id = course_id, unit_id
        self.student_info = student_info
        # 加载数据
        self.__load_data()
        # 定义一些属性
        self.text = ""
        self.total_score = 0  # 单元题目总分
        self.topic_score = {}  # 单元题目分值列表
        self.unit_start_at, self.unit_end_at, self.unit_total_minutes = "0", "0", "0"  # 单元开始时间 单元结束时间 单元分钟时长
        self.problems_choice_data = []  # 选择题数据
        self.problems_programming_data = []  # 编程题数据
        self.problems_true_false_data = []  # 判断题数据
        self.problems_multichoice_data = []  # 多选题数据
        self.problems_choice_blank_data = []  # 选择填空题数据
        self.problems_lst = []  # 正常题目
        self.random_rules_lst = []  # 随机组卷题目
        # 预统计
        self.__pre_statistics()

    def __load_data(self):
        course_unit_id = f"{self.course_id}_{self.unit_id}"
        # 读取课程信息
        course_data_path = os.path.join(cache_path, f"{self.course_id}_course_data.json")
        self.course_data = JSONDatabase(course_data_path).read()
        # 读取单元信息
        course_unit_info_list_path = os.path.join(cache_path, f"{self.course_id}_course_unit_info_list.json")
        self.course_unit_info_list_data = JSONDatabase(course_unit_info_list_path).read()
        # 课程单元信息数据
        course_unit_info_data_path = os.path.join(cache_path, f"{course_unit_id}_course_unit_info_data.json")
        self.course_unit_info_data = JSONDatabase(course_unit_info_data_path).read()
        # 习题数据
        unit_problems_data_path = os.path.join(cache_path, f"{course_unit_id}_unit_problems_data.json")
        self.unit_problems_data = JSONDatabase(unit_problems_data_path).read()
        # 习题得分数据
        unit_problems_score_data_path = os.path.join(cache_path, f"{course_unit_id}_unit_problems_score_data.json")
        self.unit_problems_score_data = JSONDatabase(unit_problems_score_data_path).read()

    def __pre_statistics(self):
        """预统计一些数据"""
        self.__unit_total_score()
        self.__load_problem_data()

    def __unit_total_score(self):
        # 单元总分
        course_unit_info_data = self.course_unit_info_data["data"]
        self.problems_lst = course_unit_info_data.get("problems")  # 正常题目
        self.random_rules_lst = course_unit_info_data.get("random_rules")  # 随机组卷题目
        if course_unit_info_data.get("random_problems", False):
            if course_unit_info_data.get("random_problems_count", 0):
                # 老式的随机抽题单元，所有题都是 10 分
                self.total_score = course_unit_info_data.get("random_problems_count") * 10
                for problems in self.problems_lst:
                    self.topic_score.update({problems.get("_id"): 10})
            elif len(self.random_rules_lst) > 0:  # 开启组卷
                for random_rules in self.random_rules_lst:
                    self.total_score += random_rules.get("score") * random_rules.get("count")
                    problems = random_rules.get("problems")  # 抽题组
                    for i in problems:  # 遍历抽题组
                        self.topic_score.update({i: random_rules.get("score")})  # 题目ID:分值
        else:  # 正常统计
            for problems in self.problems_lst:
                self.total_score += problems.get("score")
                self.topic_score.update({problems.get("_id"): problems.get("score")})

    def __load_problem_data(self):
        """加载预处理，单元习题数据"""
        unit_problems_data = self.unit_problems_data["data"]
        for problem_data in unit_problems_data:
            problem_id, problem_type = problem_data["_id"], problem_data["type"]  # 习题id 类型
            if problem_type == "choice":  # 选择题
                self.problems_choice_data.append({
                    "习题ID": problem_id,
                    "习题类型": problem_type,
                    "习题数据": pretreatment_choice_data(problem_data),
                    "正确答案": problem_data.get("answer")}
                )
            elif problem_type == "programming":  # 程序题
                self.problems_programming_data.append({
                    "习题ID": problem_id,
                    "习题类型": problem_type,
                    "习题数据": pretreatment_programming_data(problem_data)}
                )
            elif problem_type == "true-false":  # 判断题
                self.problems_true_false_data.append({
                    "习题ID": problem_id,
                    "习题类型": problem_type,
                    "习题数据": pretreatment_true_false_data(problem_data),
                    "正确答案": problem_data.get("answer")}
                )
            elif problem_type == 'multi-choice':  # 多选题
                self.problems_multichoice_data.append({
                    "习题ID": problem_id,
                    "习题类型": problem_type,
                    "习题数据": pretreatment_choice_data(problem_data),  # 多选题数据与选择题数据一致
                    "正确答案": problem_data.get("answer")}
                )
            elif problem_type == 'choice-blank':  # 选择填空题
                self.problems_choice_blank_data.append({
                    "习题ID": problem_id,
                    "习题类型": problem_type,
                    "习题数据": pretreatment_choice_blank_data(problem_data),  # 多选题数据与选择题数据一致
                    "正确答案": problem_data.get("answer")}
                )

    def title(self):
        """标题"""
        course_name = self.course_data["data"]["name"]
        self.text += "# " + "[" + course_name + "]{custom-style=\"一级标题\"}" + "："

    def subtitle(self):
        """副标题"""
        course_unit_info_list = self.course_unit_info_list_data["课程单元信息列表"]
        unit_name = ""
        for unit_info in course_unit_info_list:
            if self.unit_id == unit_info["单元ID"]:
                unit_name = unit_info["单元名称"]
        self.text += "[" + unit_name + "]{custom-style=\"副标题\"}" + "\n\n"

    def unit_continues(self):
        """单元持续时间"""
        course_unit_info_data = self.course_unit_info_data["data"]
        try:
            self.unit_start_at = course_unit_info_data.get("start_at")
            self.unit_end_at = course_unit_info_data.get("end_at")
            self.unit_start_at = datetime.strptime(self.unit_start_at, "%Y-%m-%dT%H:%M:%S.%fZ")
            self.unit_start_at = self.unit_start_at + timedelta(hours=8)
            self.unit_end_at = datetime.strptime(self.unit_end_at, "%Y-%m-%dT%H:%M:%S.%fZ")
            self.unit_end_at = self.unit_end_at + timedelta(hours=8)
            seconds = self.unit_end_at - self.unit_start_at
            self.unit_total_minutes = str(int(seconds.days * 24 * 60 + seconds.seconds / 60))
        except TypeError:
            self.unit_start_at, self.unit_end_at, self.unit_total_minutes = "0", "0", "0"  # 单元开始时间 单元结束时间 单元分钟时长
        self.text += f"[（单元持续时间：{self.unit_total_minutes}分钟，满分：{self.total_score}分）]" + "{custom-style='副标题二'}\n\n"

    def description(self):
        """单元描述"""
        course_unit_info_data = self.course_unit_info_data["data"]
        description = course_unit_info_data.get("description", "")
        self.text += "[" + description + ']{custom-style="单元描述"}\n\n'
        self.text += '[ ]{custom-style="空行"}\n\n'

    def answer_time(self):
        """答题时间"""
        if len(self.student_info.get("开始作答时间")) != 0:
            user_start_at = datetime.strptime(self.student_info.get("开始作答时间"), "%Y-%m-%dT%H:%M:%S.%fZ")
            user_start_at = user_start_at + timedelta(hours=8)
            user_start_at = user_start_at.strftime('%Y年%m月%d日 %H:%M')
        else:
            user_start_at = self.unit_start_at.strftime('%Y年%m月%d日 %H:%M')
        if len(self.student_info.get("交卷时间")) != 0:
            user_commit_at = datetime.strptime(self.student_info.get("交卷时间"), "%Y-%m-%dT%H:%M:%S.%fZ")
            user_commit_at = user_commit_at + timedelta(hours=8)
            user_commit_at = user_commit_at.strftime('%Y年%m月%d日 %H:%M')
        else:
            user_commit_at = self.unit_end_at.strftime('%Y年%m月%d日 %H:%M')
        if user_start_at:
            self.text += "考试时间：[" + user_start_at + ']{.underline} - '  # 开始时间
        if user_commit_at:
            self.text += "[" + user_commit_at + ']{.underline}\n\n'  # 关闭时间

    def content(self):
        problem_types, problem_types_score, problem_types_value = ['题型'], ['分值'], ['得分']
        total_score = self.student_info["习题总分"]  # 试卷总分
        # 获取习题分值
        unit_score_list = []  # 习题分值列表
        for problem_data in self.unit_problems_score_data["data"]["problems"]:
            unit_score_list.append({"_id": problem_data["_id"], "score": problem_data["score"]})
        choice_total_score = 0  # 选择题分值
        problem_total_score = 0  # 程序题分值
        true_false_total_score = 0  # 判断题分值
        multichoice_total_score = 0  # 多选题分值
        choice_blank_total_score = 0  # 选择填空题分值
        choice_total_value = 0  # 选择题得分
        problem_total_value = 0  # 程序题得分
        true_false_total_value = 0  # 判断题得分
        multichoice_total_value = 0  # 多选题得分
        choice_blank_total_value = 0  # 多选题得分

        record_problem_ids = self.student_info["随机组卷习题列表"]
        data_problems = self.student_info["单元所有习题列表"]
        # 随机组卷分值计算
        if len(record_problem_ids) > 0:
            # 选择题分值计算
            if len(self.problems_choice_data):  # 如果选择题数据不为空，进行如下操作
                for multichoice_data in self.problems_choice_data:  # 遍历单元所有选择题
                    if multichoice_data["习题ID"] in record_problem_ids:
                        for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                            if multichoice_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                                score = self.topic_score.get(multichoice_data["习题ID"])  # 获取习题分值
                                choice_total_score += score
                problem_types_score.append(str(choice_total_score))  # 添加选择题分值
            # 编程题分值计算
            if len(self.problems_programming_data):  # 如果程序题数据不为空，进行如下操作
                for programming_data in self.problems_programming_data:  # 遍历单元所有选择题
                    if programming_data["习题ID"] in record_problem_ids:
                        for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                            if programming_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                                score = self.topic_score.get(programming_data["习题ID"])  # 获取习题分值
                                problem_total_score += score
                problem_types_score.append(str(problem_total_score))  # 添加程序题分值
            # 判断题分值计算
            if len(self.problems_true_false_data):  # 如果判断题数据不为空，进行如下操作
                for true_false_data in self.problems_true_false_data:  # 遍历单元所有判断题
                    if true_false_data["习题ID"] in record_problem_ids:
                        for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                            if true_false_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                                score = self.topic_score.get(true_false_data["习题ID"])  # 获取习题分值
                                true_false_total_score += score
                problem_types_score.append(str(true_false_total_score))  # 添加判断题分值
            # 多选题分值计算
            if len(self.problems_multichoice_data):  # 如果多选题数据不为空，进行如下操作
                for multi_choice_data in self.problems_multichoice_data:  # 遍历单元所有判断题
                    if multi_choice_data["习题ID"] in record_problem_ids:
                        for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                            if multi_choice_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                                score = self.topic_score.get(multi_choice_data["习题ID"])  # 获取习题分值
                                multichoice_total_score += score
                problem_types_score.append(str(multichoice_total_score))  # 添加多选题分值
            # 选择填空题分值计算
            if len(self.problems_choice_blank_data):  # 如果选择填空题数据不为空，进行如下操作
                for multi_choice_blank_data in self.problems_choice_blank_data:  # 遍历单元所有判断题
                    if multi_choice_blank_data["习题ID"] in record_problem_ids:
                        for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                            if multi_choice_blank_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                                score = self.topic_score.get(multi_choice_blank_data["习题ID"])  # 获取习题分值
                                choice_blank_total_score += score
                problem_types_score.append(str(choice_blank_total_score))  # 添加多选题分值
        else:  # 正常组卷分值计算
            # 选择题分值计算
            if len(self.problems_choice_data):  # 如果选择题数据不为空，进行如下操作
                for multichoice_data in self.problems_choice_data:  # 遍历单元所有选择题
                    if multichoice_data["习题ID"] in data_problems:
                        for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                            if multichoice_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                                score = self.topic_score.get(multichoice_data["习题ID"])  # 获取习题分值
                                choice_total_score += score
                problem_types_score.append(str(choice_total_score))  # 添加选择题分值
            # 编程题分值计算
            if len(self.problems_programming_data):  # 如果程序题数据不为空，进行如下操作
                for programming_data in self.problems_programming_data:  # 遍历单元所有选择题
                    if programming_data["习题ID"] in data_problems:
                        for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                            if programming_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                                score = self.topic_score.get(programming_data["习题ID"])  # 获取习题分值
                                problem_total_score += score
                problem_types_score.append(str(problem_total_score))  # 添加程序题分值
            # 判断题分值计算
            if len(self.problems_true_false_data):  # 如果判断题数据不为空，进行如下操作
                for true_false_data in self.problems_true_false_data:  # 遍历单元所有判断题
                    if true_false_data["习题ID"] in data_problems:
                        for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                            if true_false_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                                score = self.topic_score.get(true_false_data["习题ID"])  # 获取习题分值
                                true_false_total_score += score
                problem_types_score.append(str(true_false_total_score))  # 添加判断题分值
            # 多选题分值计算
            if len(self.problems_multichoice_data):  # 如果多选题数据不为空，进行如下操作
                for multi_choice_data in self.problems_multichoice_data:  # 遍历单元所有判断题
                    if multi_choice_data["习题ID"] in data_problems:
                        for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                            if multi_choice_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                                score = self.topic_score.get(multi_choice_data["习题ID"])  # 获取习题分值
                                multichoice_total_score += score
                problem_types_score.append(str(multichoice_total_score))  # 添加多选题分值
            # 选择填空题分值计算
            if len(self.problems_choice_blank_data):  # 如果选择填空题数据不为空，进行如下操作
                for multi_choice_blank_data in self.problems_choice_blank_data:  # 遍历单元所有判断题
                    if multi_choice_blank_data["习题ID"] in data_problems:
                        for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                            if multi_choice_blank_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                                score = self.topic_score.get(multi_choice_blank_data["习题ID"])  # 获取习题分值
                                choice_blank_total_score += score
                problem_types_score.append(str(choice_blank_total_score))  # 添加多选题分值
        """--------------------------------选择题得分计算------------------------------"""
        if len(self.problems_choice_data):  # 如果选择题数据不为空，进行如下操作
            for multichoice_data in self.problems_choice_data:  # 遍历单元所有选择题
                for student_answer_data in self.student_info["作答习题"]:  # 遍历学生作答习题
                    if student_answer_data["习题ID"] == multichoice_data["习题ID"]:  # 如果习题id相同，进行如下操作
                        for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                            if student_answer_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                                score = self.topic_score.get(student_answer_data["习题ID"])  # 获取习题分值
                                if student_answer_data.get("习题得分") > 0:  # 如果习题得分大于0，进行如下操作
                                    choice_total_value += score  # 计算选择题总分
            problem_types.append(f'选择题')  # 添加习题类型
            problem_types_value.append(str(choice_total_value))  # 添加选择题总得分
        """--------------------------------程序题得分计算------------------------------"""
        if len(self.problems_programming_data):  # 如果程序题数据不为空，进行如下操作
            for programming_data in self.problems_programming_data:  # 遍历单元所有程序题
                for student_answer_data in self.student_info["作答习题"]:  # 遍历学生作答习题
                    if student_answer_data["习题ID"] == programming_data["习题ID"]:  # 如果习题id相同，进行如下操作
                        for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                            if student_answer_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                                # ***注意程序题计算方法不同***
                                exercise_score = self.topic_score.get(student_answer_data["习题ID"])  # 获取习题分值
                                try:
                                    score = student_answer_data.get(
                                        "习题得分") / 10 * exercise_score + student_answer_data.get("习题加分")
                                except TypeError:
                                    score = student_answer_data.get("习题得分") / 10 * exercise_score + 0
                                problem_total_value += score
            problem_types.append('程序题')  # 添加习题类型
            problem_types_value.append(str(problem_total_value))  # 添加程序题总得分
        """--------------------------------判断题得分计算------------------------------"""
        if len(self.problems_true_false_data):  # 如果判断题数据不为空，进行如下操作
            for programming_data in self.problems_true_false_data:  # 遍历单元所有选择题
                for student_answer_data in self.student_info["作答习题"]:  # 遍历学生作答习题
                    if student_answer_data["习题ID"] == programming_data["习题ID"]:  # 如果习题id相同，进行如下操作
                        for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                            if student_answer_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                                score = self.topic_score.get(student_answer_data["习题ID"])  # 获取习题分值
                                if student_answer_data.get("习题得分") > 0:  # 如果习题得分大于0，进行如下操作
                                    true_false_total_value += score  # 计算选择题总分
            problem_types.append('判断题')  # 添加习题类型
            problem_types_value.append(str(true_false_total_value))  # 添加多选题总得分
        """--------------------------------多选题得分计算------------------------------"""
        if len(self.problems_multichoice_data):  # 如果多选题数据不为空，进行如下操作
            for multichoice_data in self.problems_multichoice_data:  # 遍历单元所有选择题
                for student_answer_data in self.student_info["作答习题"]:  # 遍历学生作答习题
                    if student_answer_data["习题ID"] == multichoice_data["习题ID"]:  # 如果习题id相同，进行如下操作
                        for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                            if student_answer_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                                score = self.topic_score.get(student_answer_data["习题ID"])  # 获取习题分值
                                if student_answer_data.get("习题得分") > 0:  # 如果习题得分大于0，进行如下操作
                                    multichoice_total_value += score  # 计算选择题总分
            problem_types.append('多选题')  # 添加习题类型
            problem_types_value.append(str(multichoice_total_value))  # 添加多选题总得分
        """--------------------------------选择填空题得分计算------------------------------"""
        if len(self.problems_choice_blank_data):  # 如果多选题数据不为空，进行如下操作
            for choice_blank_data in self.problems_choice_blank_data:  # 遍历单元所有选择题
                for student_answer_data in self.student_info["作答习题"]:  # 遍历学生作答习题
                    if student_answer_data["习题ID"] == choice_blank_data["习题ID"]:  # 如果习题id相同，进行如下操作
                        for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                            if student_answer_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                                score = self.topic_score.get(student_answer_data["习题ID"])  # 获取习题分值
                                if student_answer_data.get("习题得分") > 0:  # 如果习题得分大于0，进行如下操作
                                    multichoice_total_value += score  # 计算选择题总分
            problem_types.append('选择填空题')  # 添加习题类型
            problem_types_value.append(str(multichoice_total_value))  # 添加多选题总得分
        problem_types.append('总分')
        problem_types_value.append(str(total_score))
        self.text += '| ' + ' | '.join(problem_types) + ' |\n'
        self.text += '|' + '|'.join([':---:'] * len(problem_types)) + '|\n'
        self.text += '| ' + ' | '.join(problem_types_score) + ' | ' + str(
            sum([eval(n) for n in problem_types_score[1:]])) + ' |\n'
        self.text += '| ' + ' | '.join(problem_types_value) + '|\n'
        self.text += '\n'
        self.text += '[ ]{custom-style="空行"}\n\n'  # 表格后
        """----------------------------------内容-------------------------------------"""
        option_s_n = {
            1: "A", 2: "B", 3: "C", 4: "D", 5: "E",
            6: "F", 7: "G", 8: "H", 9: "I", 10: "J",
            11: "K", 12: "L", 13: "M", 14: "N", 15: "O"
        }
        option_t_f = {"1": "√", "0": "×"}
        section = {
            1: '第一部分', 2: '第二部分', 3: '第三部分', 4: '第四部分',
            5: '第五部分', 6: '第六部分', 7: '第七部分', 8: '第八部分'
        }
        section_index = 1  # 有几部分习题
        """----------------------------------选择题内容--------------------------------"""
        choice_number = 1
        choice_text = ""
        for multichoice_data in self.problems_choice_data:  # 遍历单元所有选择题
            for student_answer_data in self.student_info["作答习题"]:  # 遍历学生作答习题
                if student_answer_data["习题ID"] == multichoice_data["习题ID"]:  # 如果习题id相同，进行如下操作
                    for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                        if student_answer_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                            score = self.topic_score.get(student_answer_data["习题ID"])  # 获取习题分值
                            try:
                                description_re = multichoice_data["习题数据"]["习题描述"]
                                description = description_re.replace(
                                    re.search("^\\d\\.?(\\d)?\\s*", description_re).group(), ""
                                )
                            except AttributeError:
                                description = multichoice_data["习题数据"]["习题描述"]

                            choice_text += f"{choice_number}." + "（" + str(score) + "分）" + description
                            choice_text += "[" + "（" + option_s_n.get(int(student_answer_data.get("作答选项"))) + "）  "
                            if student_answer_data.get("习题得分") > 0:
                                choice_text += "回答正确]" + "{custom-style=\"括号对齐\"}"
                            else:
                                choice_text += "回答错误]" + "{custom-style=\"括号对齐\"}"
                            choice_text += "[（正确答案" + option_s_n.get(
                                int(multichoice_data.get("正确答案"))) + "）]{custom-style=\"正确答案\"}" + "\n\n"
                            choice_text += '::: {custom-style="习题选项"}\n\n'
                            for options in multichoice_data.get("习题数据").get("习题选项"):
                                choice_text += option_s_n.get(options.get("编号")) + "." + options.get("题目") + "\n\n"
                            choice_text += ":::\n\n"
            choice_number += 1
        # 显示没有作答的习题
        choice_text += "\n\n --- \n\n"
        choice_number = 1
        for multichoice_data in self.problems_choice_data:  # 遍历单元所有选择题
            if multichoice_data["习题ID"] not in [student_answer_data["习题ID"] for student_answer_data in
                                                  self.student_info["作答习题"]]:  # 查询没有作答的习题
                if multichoice_data["习题ID"] in self.random_rules_lst:
                    for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                        if multichoice_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                            score = self.topic_score.get(multichoice_data["习题ID"])  # 获取习题分值
                            try:
                                description_re = multichoice_data["习题数据"]["习题描述"]
                                description = description_re.replace(
                                    re.search("^\\d\\.?(\\d)?\\s*", description_re).group(), ""
                                )
                            except AttributeError:
                                description = multichoice_data["习题数据"]["习题描述"]
                            choice_text += f"{choice_number}." + "（" + str(score) + "分）" + description
                            choice_text += "[（正确答案" + option_s_n.get(
                                int(multichoice_data.get("正确答案"))) + "）]{custom-style=\"正确答案\"}" + "\n\n"
                            choice_text += '::: {custom-style="习题选项"}\n\n'
                            for options in multichoice_data.get("习题数据").get("习题选项"):
                                choice_text += option_s_n.get(options.get("编号")) + "." + options.get("题目") + "\n\n"
                            choice_text += ":::\n\n"
            choice_number += 1
        if len(choice_text) > 10:
            self.text += "## " + "[" + section[section_index] + "、" + "选择题" + "]{custom-style=\"二级标题\"}" + "\n\n"
            section_index += 1
            self.text += choice_text
        """----------------------------------多选题内容--------------------------------"""
        multichoice_number = 1
        multichoice_text = ""
        for multichoice_data in self.problems_multichoice_data:  # 遍历单元所有选择题
            for student_answer_data in self.student_info["作答习题"]:  # 遍历学生作答习题
                if student_answer_data["习题ID"] == multichoice_data["习题ID"]:  # 如果习题id相同，进行如下操作
                    for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                        if student_answer_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                            score = self.topic_score.get(student_answer_data["习题ID"])  # 获取习题分值
                            try:
                                description_re = multichoice_data["习题数据"]["习题描述"]
                                description = description_re.replace(
                                    re.search("^\\d\\.?(\\d)?\\s*", description_re).group(), ""
                                )
                            except AttributeError:
                                description = multichoice_data["习题数据"]["习题描述"]
                            multichoice_text += f"{multichoice_number}." + "（" + str(score) + "分）" + description
                            try:
                                multichoice_text += "[" + "（" + option_s_n.get(
                                    int(student_answer_data.get("作答选项"))) + "）  "
                            except ValueError:
                                multichoice_text += "[" + "（" + ",".join([option_s_n.get(int(i)) for i in
                                                                          student_answer_data.get("作答选项").split(
                                                                              ",")]) + "）  "
                            if student_answer_data.get("习题得分") > 0:
                                multichoice_text += "回答正确]" + "{custom-style=\"括号对齐\"}\n\n"
                            else:
                                multichoice_text += "回答错误]" + "{custom-style=\"括号对齐\"}\n\n"
                            try:
                                multichoice_text += "[（正确答案" + option_s_n.get(
                                    int(multichoice_data.get("正确答案"))) + "）]{custom-style=\"正确答案\"}" + "\n\n"
                            except ValueError:
                                multichoice_text += "[（正确答案" + ",".join([option_s_n.get(int(i)) for i in
                                                                             multichoice_data.get("正确答案").split(
                                                                                 ",")]) + "）]{custom-style=\"正确答案\"}" + "\n\n"
                            multichoice_text += '::: {custom-style="习题选项"}\n\n'
                            for options in multichoice_data.get("习题数据").get("习题选项"):
                                multichoice_text += option_s_n.get(options.get("编号")) + "." + options.get(
                                    "题目") + "\n\n"
                            multichoice_text += ":::\n\n"
            multichoice_number += 1
        # 显示没有作答的习题
        multichoice_text += "\n\n --- \n\n"
        multichoice_number = 1
        for multichoice_data in self.problems_multichoice_data:  # 遍历单元所有选择题
            if multichoice_data["习题ID"] not in [student_answer_data["习题ID"] for student_answer_data in
                                                  self.student_info["作答习题"]]:  # 查询没有作答的习题
                if multichoice_data["习题ID"] in self.random_rules_lst:
                    for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                        if multichoice_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                            score = self.topic_score.get(multichoice_data["习题ID"])  # 获取习题分值
                            try:
                                description_re = multichoice_data["习题数据"]["习题描述"]
                                description = description_re.replace(
                                    re.search("^\\d\\.?(\\d)?\\s*", description_re).group(), ""
                                )
                            except AttributeError:
                                description = multichoice_data["习题数据"]["习题描述"]
                            multichoice_text += f"{multichoice_number}." + "（" + str(score) + "分）" + description
                            try:
                                multichoice_text += "[（正确答案" + option_s_n.get(
                                    int(multichoice_data.get("正确答案"))) + "）]{custom-style=\"正确答案\"}" + "\n\n"
                            except ValueError:
                                multichoice_text += "[（正确答案" + ",".join([option_s_n.get(int(i)) for i in
                                                                             multichoice_data.get("正确答案").split(
                                                                                 ",")]) + "）]{custom-style=\"正确答案\"}" + "\n\n"
                            multichoice_text += '::: {custom-style="习题选项"}\n\n'
                            for options in multichoice_data.get("习题数据").get("习题选项"):
                                multichoice_text += option_s_n.get(options.get("编号")) + "." + options.get(
                                    "题目") + "\n\n"
                            multichoice_text += ":::\n\n"
            multichoice_number += 1
        if len(multichoice_text) > 10:
            self.text += "## " + "[" + section[section_index] + "、" + "多选题" + "]{custom-style=\"二级标题\"}" + "\n\n"
            section_index += 1
            self.text += multichoice_text
        """----------------------------------选择填空题内容--------------------------------"""
        choice_blank_number = 1
        choice_blank_text = ""
        for choice_blank_data in self.problems_choice_blank_data:  # 遍历单元所有选择题
            for student_answer_data in self.student_info["作答习题"]:  # 遍历学生作答习题
                if student_answer_data["习题ID"] == choice_blank_data["习题ID"]:  # 如果习题id相同，进行如下操作
                    for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                        if student_answer_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                            score = self.topic_score.get(student_answer_data["习题ID"])  # 获取习题分值
                            try:
                                description_re = choice_blank_data["习题数据"]["习题描述"]
                                description = description_re.replace(
                                    re.search("^\\d\\.?(\\d)?\\s*", description_re).group(), "")
                            except AttributeError:
                                description = choice_blank_data["习题数据"]["习题描述"]
                            choice_blank_text += f"{choice_blank_number}." + "（" + str(score) + "分）" + description

                            if student_answer_data.get("习题得分") > 0:
                                choice_blank_text += "[回答正确]" + "{custom-style=\"括号对齐\"}\n\n"
                            else:
                                choice_blank_text += "[回答错误]" + "{custom-style=\"括号对齐\"}\n\n"
                            choice_blank_text += "作答内容\n\n"

                            choice_blank_text += "\n\n".join(
                                json.loads(choice_blank_data.get("习题数据").get("作答选项"))) + "\n\n"

                            choice_blank_text += "正确答案\n\n"
                            choice_blank_text += "\n\n".join(json.loads(choice_blank_data.get("正确答案"))) + "\n\n"
                            choice_blank_text += "\n\n"
            choice_blank_number += 1
        # 显示没有作答的习题
        choice_blank_text += "\n\n --- \n\n"
        choice_blank_number = 1
        for choice_blank_data in self.problems_choice_blank_data:  # 遍历单元所有选择题
            if choice_blank_data["习题ID"] not in [student_answer_data["习题ID"] for student_answer_data in
                                                   self.student_info["作答习题"]]:  # 查询没有作答的习题
                if choice_blank_data["习题ID"] in self.random_rules_lst:
                    for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                        if choice_blank_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                            score = self.topic_score.get(choice_blank_data["习题ID"])  # 获取习题分值
                            try:
                                description_re = choice_blank_data["习题数据"]["习题描述"]
                                description = description_re.replace(
                                    re.search("^\\d\\.?(\\d)?\\s*", description_re).group(), ""
                                )
                            except AttributeError:
                                description = choice_blank_data["习题数据"]["习题描述"]
                            choice_blank_text += f"{multichoice_number}." + "（" + str(score) + "分）" + description
                            try:
                                choice_blank_text += "[（正确答案" + option_s_n.get(
                                    int(choice_blank_data.get("正确答案"))) + "）]{custom-style=\"正确答案\"}" + "\n\n"
                            except ValueError:
                                choice_blank_text += "[（正确答案" + ",".join([option_s_n.get(int(i)) for i in
                                                                              choice_blank_data.get("正确答案").split(
                                                                                  ",")]) + "）]{custom-style=\"正确答案\"}" + "\n\n"
                            choice_blank_text += '::: {custom-style="习题选项"}\n\n'
                            for options in choice_blank_data.get("习题数据").get("习题选项"):
                                choice_blank_text += option_s_n.get(options.get("编号")) + "." + options.get(
                                    "题目") + "\n\n"
                            choice_blank_text += ":::\n\n"
            multichoice_number += 1
        if len(choice_blank_text) > 10:
            self.text += "## " + "[" + section[
                section_index] + "、" + "选择填空题" + "]{custom-style=\"二级标题\"}" + "\n\n"
            section_index += 1
            self.text += choice_blank_text
        """----------------------------------判断题内容--------------------------------"""
        true_false_number = 1
        true_false_text = ""
        for true_false_data in self.problems_true_false_data:  # 遍历单元所有选择题
            for student_answer_data in self.student_info["作答习题"]:  # 遍历学生作答习题
                if student_answer_data["习题ID"] == true_false_data["习题ID"]:  # 如果习题id相同，进行如下操作
                    for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                        if student_answer_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                            score = self.topic_score.get(student_answer_data["习题ID"])  # 获取习题分值
                            description = true_false_data["习题数据"]["习题描述"]
                            true_false_text += f"{true_false_number}." + "（" + str(score) + "分）" + description
                            true_false_text += "[" + "（" + option_t_f.get(student_answer_data.get("作答选项")) + "）  "
                            if student_answer_data.get("习题得分") > 0:
                                true_false_text += "回答正确]" + "{custom-style=\"括号对齐\"}"
                            else:
                                true_false_text += "回答错误]" + "{custom-style=\"括号对齐\"}"
                            true_false_text += "[（正确答案" + option_t_f.get(
                                true_false_data.get("正确答案")) + "）]{custom-style=\"正确答案\"}" + "\n\n"
            true_false_number += 1
        # 显示没有作答的习题
        true_false_text += "\n\n --- \n\n"
        true_false_number = 1
        for true_false_data in self.problems_true_false_data:  # 遍历单元所有选择题
            if true_false_data["习题ID"] not in [student_answer_data["习题ID"] for student_answer_data in
                                                 self.student_info["作答习题"]]:  # 查询没有作答的习题
                if true_false_data["习题ID"] in self.random_rules_lst:
                    for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                        if true_false_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                            score = self.topic_score.get(true_false_data["习题ID"])  # 获取习题分值
                            description = true_false_data["习题数据"]["习题描述"]
                            true_false_text += f"{true_false_number}." + "（" + str(score) + "分）" + description
                            true_false_text += "[（正确答案" + option_t_f.get(
                                true_false_data.get("正确答案")) + "）]{custom-style=\"正确答案\"}" + "\n\n"
            true_false_number += 1
        if len(true_false_text) > 10:
            self.text += "## " + "[" + section[section_index] + "、" + "判断题" + "]{custom-style=\"二级标题\"}" + "\n\n"
            section_index += 1
            self.text += true_false_text
        """----------------------------------程序设计题内容--------------------------------"""
        programming_number = 1
        programming_text = ""
        for programming_data in self.problems_programming_data:  # 遍历单元所有程序题
            for student_answer_data in self.student_info["作答习题"]:  # 遍历学生作答习题
                if student_answer_data["习题ID"] == programming_data["习题ID"]:  # 如果习题id相同，进行如下操作
                    for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                        if student_answer_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                            score = self.topic_score.get(student_answer_data["习题ID"])  # 获取习题分值
                            programming_id = student_answer_data["习题ID"]  # 获取习题id
                            user_id = self.student_info["学生ID"]  # 获取学生id
                            problems_code_path = os.path.join(cache_code_path,
                                                              f"{self.course_id}_{self.unit_id}_{programming_id}_{user_id}_problems_code.json")
                            problems_code = JSONDatabase(problems_code_path).read()
                            try:
                                problems_code = problems_code.get("习题代码", '')  # 获取习题代码
                                if "api/v1/files" in problems_code:
                                    problems_code_list = []
                                    for url in problems_code.split("|"):
                                        problems_code_url = f"![]({url})\n\n"
                                        problems_code_list.append(problems_code_url)
                                    problems_code = "\n".join(problems_code_list)
                            except AttributeError:  # 如果没有习题代码，就赋值为空
                                problems_code = ''
                            # ***注意程序题计算方法不同***
                            exercise_score = self.topic_score.get(student_answer_data["习题ID"])  # 获取习题分值
                            try:
                                problem_score = student_answer_data.get(
                                    "习题得分") / 10 * exercise_score + student_answer_data.get("习题加分")
                            except TypeError:
                                problem_score = student_answer_data.get("习题得分") / 10 * exercise_score + 0
                            try:
                                exercise_name_re = programming_data.get("习题数据").get("习题名称")
                                exercise_name = exercise_name_re.replace(
                                    re.search("^\\d\\.?(\\d)?\\s*", exercise_name_re).group(), ""
                                )
                            except AttributeError:
                                exercise_name = programming_data.get("习题数据").get("习题名称")
                            programming_text += f"{programming_number}." + f"（{score}分）" + exercise_name + "\n\n"
                            programming_text += '::: {custom-style="题目正文"}\n\n'
                            programming_text += programming_data.get("习题数据").get("习题简介") + "\n\n"
                            programming_text += ":::\n\n"
                            programming_text += "**作答代码：**"
                            if "![](" in problems_code:
                                programming_text += "\n \n" + problems_code + "\n" + "\n\n"
                            else:
                                programming_text += "\n```python\n" + problems_code + "\n```" + "\n\n"  # 作答代码
                            programming_text += "[得分：" + str(problem_score) + '分]{custom-style="得分"}\n\n'
                    programming_text += '[ ]{custom-style="空行"}\n\n'
                    programming_number += 1
        # 显示没有作答的习题
        programming_text += "\n\n --- \n\n"
        programming_number = 1
        for programming_data in self.problems_programming_data:  # 遍历单元所有选择题
            if programming_data["习题ID"] not in [student_answer_data["习题ID"] for student_answer_data in
                                                  self.student_info["作答习题"]]:  # 查询没有作答的习题
                if programming_data["习题ID"] in self.random_rules_lst:
                    for unit_score_list_data in unit_score_list:  # 遍历单元习题分值列表
                        if programming_data["习题ID"] == unit_score_list_data["_id"]:  # 如果习题id相同，进行如下操作
                            score = self.topic_score.get(programming_data["习题ID"])  # 获取习题分值
                            try:
                                exercise_name_re = programming_data.get("习题数据").get("习题名称")
                                exercise_name = exercise_name_re.replace(
                                    re.search("^\\d\\.?(\\d)?\\s*", exercise_name_re).group(), ""
                                )
                            except AttributeError:
                                exercise_name = programming_data.get("习题数据").get("习题名称")
                            programming_text += f"{programming_number}." + f"（{score}分）" + exercise_name + "\n\n"
                            programming_text += '::: {custom-style="题目正文"}\n\n'
                            programming_text += programming_data.get("习题数据").get("习题简介") + "\n\n"
                            programming_text += ":::\n\n"
                    programming_text += '[ ]{custom-style="空行"}\n\n'
            programming_number += 1
        if len(programming_text) > 10:
            self.text += "## " + "[" + section[
                section_index] + "、" + "程序设计题" + "]{custom-style=\"二级标题\"}" + "\n\n"
            section_index += 1
            self.text += programming_text

    def run(self):
        self.title()
        self.subtitle()
        self.unit_continues()
        self.description()
        self.answer_time()
        self.content()
        # 获取学生信息
        user_id, student_id = self.student_info["学生ID"], self.student_info["学生学号"]
        try:
            student_name, classroom = self.student_info["学生姓名"], self.student_info["学生班级"].replace(" ", "")
        except AttributeError:
            student_name, classroom = self.student_info["学生姓名"], self.student_info["学生班级"]
        root = os.path.join(download_path, f"{self.course_id}/{self.unit_id}")
        check_and_create_folder(root)
        # 创建 markdown 文件
        markdown_path = f"{root}/{student_id}-{student_name}-{classroom}.md"
        docx_path = f"{root}/{student_id}-{student_name}-{classroom}.docx"
        with open(markdown_path, "w", encoding="utf-8") as f:
            f.write(self.text)
        # 获取当前文件的路径
        current_file_path = os.path.abspath(__file__)
        # 获取当前文件所在目录的路径
        current_directory_path = os.path.dirname(current_file_path)
        reference_doc_path = f"{current_directory_path}/custom-reference.docx"
        os.system(f"pandoc {markdown_path} -s -o {docx_path} --reference-doc={reference_doc_path}")
        os.remove(f"{markdown_path}")
