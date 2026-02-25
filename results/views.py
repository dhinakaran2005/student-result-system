from django.shortcuts import render
from .models import Student, Marks

def home(request):
    return render(request, 'home.html')


def result_view(request):
    roll = request.GET.get('roll')

    student = None
    marks = None
    grade = None
    status = None

    if roll:
        try:
            student = Student.objects.get(roll_number=roll)
            marks = Marks.objects.get(student=student)

            percentage = marks.percentage

            # Grade Logic
            if percentage >= 90:
                grade = "A+"
            elif percentage >= 75:
                grade = "A"
            elif percentage >= 60:
                grade = "B"
            elif percentage >= 50:
                grade = "C"
            else:
                grade = "D"

            # Pass / Fail
            if percentage >= 35:
                status = "PASS"
            else:
                status = "FAIL"

        except:
            student = None

    context = {
        'student': student,
        'marks': marks,
        'grade': grade,
        'status': status
    }

    return render(request, 'result.html', context)