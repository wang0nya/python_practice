if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
def get_average(a, b):
    avg = a/b
    return avg

marks = student_marks[query_name]
marks_sum = sum(marks)
marks_len = len(marks)

average = get_average(marks_sum, marks_len)
print("%.2f" %average)