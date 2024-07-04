# python123 平台API
import requests


def get_token(email: str, password: str) -> str:
    """获取用户token

    :param email: 用户邮箱
    :param password: 用户密码
    :return:
    """
    data = {"email": email, "pass": password}
    results = requests.put("https://www.python123.io/api/v1/session", data=data).json()
    try:
        return "Bearer " + results["data"]["token"]
    except KeyError:
        return "账号或密码错误"


def get_courses_list(token: str) -> list:
    """
    获取课程列表
    :param token: 用户 token 字符串
    :return:
    """
    url = "https://www.python123.io/api/v1/teacher/courses"
    results = requests.get(url, headers={"Authorization": token})
    results_json = results.json()
    lst = []
    for data in results_json["data"]:
        lst.append({"课程ID": data["_id"], "课程名称": data["name"]})
    return lst


def get_course_data(token: str, course_id: int) -> dict:
    """
    获取课程数据
    :param token:  用户 token 字符串
    :param course_id:  课程ID
    :return:  课程数据
    """
    url = f"https://www.python123.io/api/v1/teacher/courses/{course_id}"
    results = requests.get(url, headers={"Authorization": token})
    results_json = results.json()
    return results_json


def get_course_unit_info_list(token: str, course_id: int) -> dict:
    """
    获取课程单元信息列表
    :param token:  用户 token 字符串
    :param course_id:  课程ID
    :return:  课程单元信息列表
    """
    url = f"https://www.python123.io/api/v1/teacher/courses/{course_id}/groups"
    results = requests.get(url, headers={"Authorization": token})
    results_json = results.json()
    lst = []
    for data in results_json["data"]:
        unit_id = data["_id"]
        unit_name = data["name"]
        unit_type = data["type"]
        lst.append({"单元ID": unit_id, "单元名称": unit_name, "单元类型": unit_type})
    return {"课程单元信息列表": lst}


def get_course_unit_info_data(token: str, course_id: int, unit_id: int) -> dict:
    """
    获取课程单元信息数据
    :param token: 用户 token 字符串
    :param course_id: 课程ID
    :param unit_id: 课程单元ID
    :return: 课程单元信息数据
    """
    url = f"https://www.python123.io/api/v1/teacher/courses/{course_id}/groups/{unit_id}"
    results = requests.get(url, headers={"Authorization": token})
    results_json = results.json()
    return results_json


def get_unit_problems_data(token: str, course_id: int, unit_id: int, content: bool = True) -> dict:
    """
    获取单元习题数据
    :param token:  用户 token 字符串
    :param course_id:  课程ID
    :param unit_id:  课程单元ID
    :param content: 是否包含习题选项内容,默认为True
    :return:  单元习题数据
    """
    results = requests.get(f"https://www.python123.io/api/v1/teacher/groups/{unit_id}/problems?withContent=1",
                           headers={"Authorization": token})
    results_json = results.json()
    if results_json["code"] == 200:
        return results_json
    else:
        results = requests.get(f"https://python123.io/api/v1/teacher/groups/{course_id}/problems/{unit_id}",
                               headers={"Authorization": token})
        results_json = results.json()
        return results_json
    # if content:
    #     url = f"https://www.python123.io/api/v1/teacher/groups/{unit_id}/problems?withContent=1"
    #     results = requests.get(url, headers={"Authorization": token})
    #     results_json = results.json()
    #     return results_json
    # else:  # 如果上述url无法查询习题选项，使用如下url
    #     url = f"https://python123.io/api/v1/teacher/groups/{course_id}/problems/{unit_id}"
    #     results = requests.get(url, headers={"Authorization": token})
    #     results_json = results.json()
    #     return results_json


def get_unit_score_data(token: str, course_id: int, unit_id: int) -> dict:
    """
    获取单元成绩数据
    :param token:   用户 token 字符串
    :param course_id:  课程ID
    :param unit_id:  课程单元ID
    :return:  单元成绩数据
    """
    url = f"https://www.python123.io/api/v1/teacher/courses/{course_id}/groups/{unit_id}/simple_transcript"
    results = requests.get(url, headers={"Authorization": token})
    results_json = results.json()
    return results_json


def get_course_score_data(token: str, course_id: int) -> dict:
    """
    获取课程成绩数据
    :param token:  用户 token 字符串
    :param course_id:  课程ID
    :return:  课程成绩数据
    """
    url = f"https://www.python123.io/api/v1/teacher/courses/{course_id}/total_score_transcript"
    results = requests.get(url, headers={"Authorization": token})
    results_json = results.json()
    return results_json


def get_unit_problems_score_data(token: str, unit_id: int) -> dict:
    """
    获取单元习题评分数据
    :param token: 用户 token 字符串
    :param unit_id: 课程单元ID
    :return: 单元习题评分数据
    """
    url = f"https://www.python123.io/api/v1/teacher/groups/{unit_id}"
    results = requests.get(url, headers={"Authorization": token})
    results_json = results.json()
    return results_json


def get_problems_code(token, course_id, unit_id, problem_id, user_id):
    """
    获取习题代码
    :param token:  用户 token 字符串
    :param course_id:  课程ID
    :param unit_id:  课程单元ID
    :param problem_id:  习题ID
    :param user_id:  用户ID
    :return:
    """
    api = "https://www.python123.io/api/v1"
    url = api + f"/teacher/courses/{course_id}/groups/{unit_id}/problems/{problem_id}/users/{user_id}/code"
    results = requests.get(url, headers={"Authorization": token})
    try:
        code = results.json()["data"]["code"].replace("\r\n", "\n")  # 将\r\n替换为\n
    except KeyError:
        code_annex_img_list = []
        for attachment in results.json()["data"]["attachments"]:
            _id = attachment["_id"]
            name = attachment["name"]
            code_annex_url = f"https://python123.io/api/v1/teacher/courses/{course_id}/groups/{unit_id}/problems/{problem_id}/users/{user_id}/code/attachments/{_id}"
            code_annex_url_prefix = requests.get(code_annex_url, headers={"Authorization": token}).json()["data"]
            code_annex_img_url = f"https://python123.io/api/v1/files/{code_annex_url_prefix}/{name}"
            code_annex_img_list.append(code_annex_img_url)
        code = "|".join(code_annex_img_list)
    return {"习题代码": code}
