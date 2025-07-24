# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 19:06:26 2025

@author: bhara
"""

student_id=23
student_name= "bharadwaj"
student_age=23
quiz_score= 50
assignment_score=70
exam_score=80
student_attendance=75

total_score=quiz_score+assignment_score+exam_score
average_score=total_score/3

student_passed=average_score>=75

student_attendance+=1

award_eligibity=student_attendance>=90 and student_passed

print(f"student_id:{student_id}")
print(f"student_name:{student_name}")
print(f"student_age:{student_age}")
print(f"total score:{total_score}")
print(f"average score:{average_score}")
print(f"student passed:{student_passed}")
print(f"student cur attendance:{student_attendance}")
print(f"award eligibity:{award_eligibity}")