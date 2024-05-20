import numpy as np

points = np.loadtxt('points.txt')
marks = np.loadtxt('marks.txt')

num_students = points.shape[0]
print(f'Liczba studentów: {num_students}')

mean_points = np.mean(points, axis=0)
print(f'Średnia liczba punktów dla każdej aktywności: {mean_points}')

total_points = np.sum(points, axis=1)
best_score = np.max(total_points)
print(f'Najlepszy student uzyskał: {best_score} punktów')

best_students = np.where(total_points == best_score)[0]
print(f'Najlepsi studenci (indeksy): {best_students}')

attendance_points = np.sum(points[:, :5], axis=1)
homework_points = np.sum(points[:, 5:], axis=1)

def get_grade(attendance, homework):
    max_index = marks.shape[0] - 1
    attendance = min(int(attendance), max_index)
    homework = min(int(homework), max_index)
    return marks[attendance, homework]

grades = np.array([get_grade(attendance_points[i], homework_points[i]) for i in range(num_students)])
print(f'Oceny studentów: {grades}')

grade_5_count = np.sum(grades == 5)
grade_5_percentage = (grade_5_count / num_students) * 100
print(f'Liczba studentów z oceną 5: {grade_5_count} ({grade_5_percentage:.2f}%)')

grade_4_or_higher_count = np.sum(grades >= 4)
grade_4_or_higher_percentage = (grade_4_or_higher_count / num_students) * 100
print(f'Liczba studentów z oceną nie mniejszą niż 4: {grade_4_or_higher_count} ({grade_4_or_higher_percentage:.2f}%)')



