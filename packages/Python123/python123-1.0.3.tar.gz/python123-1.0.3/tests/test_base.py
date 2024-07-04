from python123 import Generator, pretreatment_unit_score_data
from tqdm import tqdm

course_id = 11373
unit_id = 154246
# 预处理
student_info_list = pretreatment_unit_score_data(course_id, unit_id)
for student_info in tqdm(student_info_list[:1]):
    generator = Generator(course_id, unit_id, student_info)
    generator.run()

