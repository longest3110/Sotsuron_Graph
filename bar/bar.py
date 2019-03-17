import numpy as np
import matplotlib.pyplot as plt
import sqlite3

analyzed_connection = sqlite3.connect('analyzed.db')
analyzed_cursor = analyzed_connection.cursor()

quely = """
select
avg(time_master.time_ave),
avg(1.0 * respondent_master.check_perfect / respondent_master.respondent) from exercise
left join analyze_subject on analyze_subject.exercise_id = exercise.id
left join respondent_master on respondent_master.exercise_id = exercise.id
left join time_master on time_master.exercise_id = exercise.id
where respondent_master.respondent > 0
and analyze_subject.answer > 5
and analyze_subject.exercise_id != 23
and analyze_subject.exercise_id != 24
and analyze_subject.exercise_id != 29
and analyze_subject.exercise_id < 50
order by level asc, stage asc
"""

loop_data = np.array(tuple(analyzed_cursor.execute(quely)))
print(loop_data)

quely = """
select
avg(time_master.time_ave),
avg(1.0 * respondent_master.check_perfect / respondent_master.respondent) from exercise
left join analyze_subject on analyze_subject.exercise_id = exercise.id
left join respondent_master on respondent_master.exercise_id = exercise.id
left join time_master on time_master.exercise_id = exercise.id
where respondent_master.respondent > 0
and analyze_subject.answer < 6
and analyze_subject.exercise_id != 23
and analyze_subject.exercise_id != 24
and analyze_subject.exercise_id != 29
and analyze_subject.exercise_id < 50
order by level asc, stage asc
"""

no_loop_data = np.array(tuple(analyzed_cursor.execute(quely)))
print(no_loop_data)

fig = plt.figure("time")
left = np.array([0.5, 1, 2, 2.5])
label = ["", "含む", "含まない", ""]
height = np.array([0, loop_data[0][0], no_loop_data[0][0], 0])
plt.bar(left, height, tick_label=label, align="center", width=0.7)
plt.xlabel("全域サイクルを含む")
plt.ylabel("平均解答時間 [秒]")
fig.savefig('time_loop.png')


fig = plt.figure("respondent")
left = np.array([0.5, 1, 2, 2.5])
label = ["", "含む", "含まない", ""]
height = np.array([0, loop_data[0][1]*100, no_loop_data[0][1]*100, 0])
plt.bar(left, height, tick_label=label, align="center", width=0.7)
plt.xlabel("全域サイクルを含む")
plt.ylabel("平均完答率 [%]")
fig.savefig('respondent_loop.png')

analyzed_connection.commit()
analyzed_connection.close()