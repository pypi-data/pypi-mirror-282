from python123.api import get_token
from python123.cache import cache
from python123.base import Generator
from python123.pretreatment import pretreatment_unit_score_data
from tqdm import tqdm


def download_exam_test_paper(email: str, password: str, course_id: int, unit_id: int):
    """

    :param email: 用户名
    :param password: 密码
    :param course_id: 课程id
    :param unit_id: 单元id
    :return:
    """
    token = get_token(email, password)
    cache(token, course_id, unit_id)
    student_info_list = pretreatment_unit_score_data(course_id, unit_id)
    for student_info in tqdm(student_info_list):
        generator = Generator(course_id, unit_id, student_info)
        generator.run()
