import python123

token = python123.get_token("syan_cn4@163.com", "rj20130818622464585")
course_id = 11373
unit_id = 154246

data = python123.pretreatment_unit_score_data(course_id, unit_id)
print(data)
