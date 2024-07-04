# 学生答题数据缓存
from python123 import api
from python123.jsondb import JSONDatabase
from python123.settings import cache_path, cache_code_path
from loguru import logger
import os
from python123.pretreatment import pretreatment_unit_score_data
from tqdm import tqdm


def cache_course_data(token: str, course_id: int) -> None:
    """

    :param token: 用户token
    :param course_id: 课程id
    :return:
    """
    json_db_path = os.path.join(cache_path, f"{course_id}_course_data.json")
    json_db = JSONDatabase(json_db_path)
    course_data = api.get_course_data(token, course_id)
    json_db.write(course_data)
    logger.info(f"download {course_id} course data")


def cache_unit_problems_data(token: str, course_id: int, unit_id: int) -> None:
    """
    下载单元习题数据
    :param token:  用户 token 字符串
    :param course_id:  课程ID
    :param unit_id: 课程单元ID
    :return:  None
    """
    json_db_path = os.path.join(cache_path, f"{course_id}_{unit_id}_unit_problems_data.json")
    json_db = JSONDatabase(json_db_path)
    try:
        unit_problems_data = api.get_unit_problems_data(token, course_id, unit_id)
        content = unit_problems_data["data"][0]["content"]
    except KeyError:
        unit_problems_data = api.get_unit_problems_data(token, course_id, unit_id, content=False)
    json_db.write(unit_problems_data)
    logger.info(f"download {course_id} {unit_id} unit_problems_data")


def cache_unit_score_data(token: str, course_id: int, unit_id: int) -> None:
    """
    下载单元成绩数据
    :param token:  用户 token 字符串
    :param course_id:   课程ID
    :param unit_id: 课程单元ID
    :return:
    """
    json_db_path = os.path.join(cache_path, f"{course_id}_{unit_id}_unit_score_data.json")
    json_db = JSONDatabase(json_db_path)
    unit_score_data = api.get_unit_score_data(token, course_id, unit_id)
    json_db.write(unit_score_data)
    logger.info(f"download {course_id} {unit_id} unit_score_data")


def cache_course_score_data(token: str, course_id: int) -> None:
    """
    下载课程成绩数据
    :param token:  用户 token 字符串
    :param course_id:   课程ID
    :return: None
    """
    json_db_path = os.path.join(cache_path, f"{course_id}_course_score_data.json")
    json_db = JSONDatabase(json_db_path)
    course_score_data = api.get_course_score_data(token, course_id)
    json_db.write(course_score_data)
    logger.info(f"download {course_id} course_score_data")


def cache_unit_problems_score_data(token: str, course_id: int, unit_id: int) -> None:
    """
    下载单元习题评分数据
    :param token:  用户 token 字符串
    :param course_id:   课程ID
    :param unit_id: 课程单元ID
    :return:  None
    """
    json_db_path = os.path.join(cache_path, f"{course_id}_{unit_id}_unit_problems_score_data.json")
    json_db = JSONDatabase(json_db_path)
    unit_problems_score_data = api.get_unit_problems_score_data(token, unit_id)
    json_db.write(unit_problems_score_data)
    logger.info(f"download {course_id} {unit_id} unit_problems_score_data")


def cache_course_unit_info_data(token: str, course_id: int, unit_id: int) -> None:
    """
    下载课程单元信息数据
    :param token:  用户 token 字符串
    :param course_id:  课程ID
    :param unit_id:  课程单元ID
    :return:  None
    """
    json_db_path = os.path.join(cache_path, f"{course_id}_{unit_id}_course_unit_info_data.json")
    json_db = JSONDatabase(json_db_path)
    course_unit_info_data = api.get_course_unit_info_data(token, course_id, unit_id)
    json_db.write(course_unit_info_data)
    logger.info(f"download {course_id} {unit_id} course_unit_info_data")


def cache_course_unit_info_list(token: str, course_id: int) -> None:
    """
    下载课程单元信息列表数据
    :param token:  用户 token 字符串
    :param course_id:  课程ID
    :return:  None
    """
    json_db_path = os.path.join(cache_path, f"{course_id}_course_unit_info_list.json")
    json_db = JSONDatabase(json_db_path)
    course_unit_info_list = api.get_course_unit_info_list(token, course_id)
    json_db.write(course_unit_info_list)
    logger.info(f"download {course_id} course_unit_info_list")


def cache_download_code_list(token: str, course_id, unit_id, student_info: dict) -> list:
    """
    保存习题代码

    :param token:   用户 token 字符串
    :param course_id:  课程ID
    :param unit_id:  课程单元ID
    :param student_info:  学生信息
    :return:  None
    """
    unit_problems_data_path = os.path.join(cache_path, f"{course_id}_{unit_id}_unit_problems_data.json")
    unit_problems_data = JSONDatabase(unit_problems_data_path).read()["data"]
    problems_programming_data = []
    for problem_data in unit_problems_data:
        problem_id, problem_type = problem_data["_id"], problem_data["type"]  # 习题id 类型
        if problem_type == "programming":
            problems_programming_data.append({"习题ID": problem_id})
    download_code_list = []
    for programming_data in problems_programming_data:  # 遍历单元所有选择题
        for student_answer_data in student_info["作答习题"]:  # 遍历学生作答习题
            if student_answer_data["习题ID"] == programming_data["习题ID"]:  # 如果习题id相同，进行如下操作
                download_code_list.append({
                    "token": token,
                    "course_id": course_id,
                    "unit_id": unit_id,
                    "problem_id": student_answer_data["习题ID"],
                    "user_id": student_info["学生ID"]
                })
    return download_code_list


def cache_problems_code(parameters: dict) -> None:
    """
    下载习题代码
    :param parameters:
    :return:  None
    """
    token = parameters["token"]
    course_id, unit_id = parameters["course_id"], parameters["unit_id"]
    problem_id = parameters["problem_id"]
    user_id = parameters["user_id"]
    problems_code_path = os.path.join(cache_code_path,
                                      f"{course_id}_{unit_id}_{problem_id}_{user_id}_problems_code.json")
    problems_code = JSONDatabase(problems_code_path)
    problems_code.write(api.get_problems_code(token, course_id, unit_id, problem_id, user_id))
    logger.info(f"course:{course_id} unit:{unit_id} problem:{problem_id} user:{user_id}")


def cache(token: str, course_id: int, unit_id: int):
    """缓存主函数

    :param token:
    :param course_id:
    :param unit_id:
    :return:
    """
    # 下载数据
    cache_course_data(token, course_id)
    cache_unit_problems_data(token, course_id, unit_id)
    cache_unit_score_data(token, course_id, unit_id)
    cache_course_data(token, course_id)
    cache_unit_problems_score_data(token, course_id, unit_id)
    cache_course_unit_info_data(token, course_id, unit_id)
    cache_course_unit_info_list(token, course_id)
    # 预处理
    student_info_list = pretreatment_unit_score_data(course_id, unit_id)
    # 根据学生信息，预下载作答代码
    download_code_list_all = []
    for student_info in tqdm(student_info_list):  # 测试
        download_code_list = cache_download_code_list(token, course_id, unit_id, student_info)
        for download_code_data in download_code_list:
            download_code_list_all.append(download_code_data)
    for download_code_data in tqdm(download_code_list_all):
        cache_problems_code(download_code_data)
