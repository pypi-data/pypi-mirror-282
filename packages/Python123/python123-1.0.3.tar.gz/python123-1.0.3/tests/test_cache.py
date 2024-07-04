import python123

token = python123.get_token("syan_cn4@163.com", "rj20130818622464585")
course_id = 11373
unit_id = 154246

# python123.cache_course_data(token, course_id)
# python123.cache_unit_problems_data(token, course_id, unit_id)
# python123.cache_unit_score_data(token, course_id, unit_id)
# python123.cache_course_data(token, course_id)
# python123.cache_unit_problems_score_data(token, course_id, unit_id)
# python123.cache_course_unit_info_data(token, course_id, unit_id)
# python123.cache_course_unit_info_list(token, course_id)

python123.cache(token, course_id, unit_id)
