from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Exam, UserExam, Question
from django.utils import timezone

@login_required(login_url='sign-in')
def dashboard(request):
    exams = Exam.objects.all()
    user = request.user
    user_exams = UserExam.objects.filter(user=user).order_by('-date_completed', '-id')

    context = {
        'exams': exams,
        'user_exams': user_exams,
    }
    return render(request, "ExamInterface/dashboard.html", context)


@login_required(login_url='sign-in')
def exam_hall(request):
    if request.method == 'GET':
        num_questions = int(request.GET.get('num_questions', 120))
        duration = int(request.GET.get('duration', 210))

        if num_questions and duration:
            user = request.user
            exam = Exam.objects.create(
                name="Custom Exam" + str(user.id) + str(timezone.now()),
                number_of_questions=num_questions,
                time=duration
            )

            # Fetch a set of random questions to associate with the exam
            questions = Question.objects.order_by('?')[:num_questions]

            for i, question in enumerate(questions):
                question.exam = exam
                question.question_id = i + 1
                question.save()

            context = {
                'exam': exam,
                'questions': questions,
            }

            return render(request, "ExamInterface/exam-hall.html", context)

    return HttpResponseRedirect(reverse('dashboard'))

@login_required(login_url='sign-in')
def evaluate_exam(request, exam_id):
    if request.method == 'POST':
        exam = get_object_or_404(Exam, id=exam_id)
        questions = exam.question_set.all()

        score = 0
        num_correct = 0

        for question in questions:
            selected_answer = request.POST.get(f"question_{question.id}")
            question.selected_answer = selected_answer

            for key, value in question.options.items():
                if value == question.correct_answer:
                    correct_option = key
                    break
            
            if selected_answer == correct_option:
                score += 1
                num_correct +=1

            question.save()

        # Store the details of the completed exam in the database
        user_exam = UserExam()
        user_exam.user = request.user
        user_exam.exam = exam
        user_exam.score = (score/len(questions)) * 100
        user_exam.completed = True
        user_exam.date_completed = timezone.now().date()
        user_exam.save()

        context = {
            'exam': exam,
            'questions': questions,
            'score': round((score/len(questions)) * 100,2),
            'num_correct': num_correct,
        }

        return render(request, "ExamInterface/exam-board.html", context)

    return HttpResponseRedirect(reverse('dashboard'))

@login_required(login_url='sign-in')
def review_exam(request, user_exam_id):
    user_exam = get_object_or_404(UserExam, id=user_exam_id)
    questions = Question.objects.filter(exam=user_exam.exam)
    num_questions = len(questions)
    num_correct = round((user_exam.score * num_questions)/100,0)

    context = {
        'user_exam': user_exam,
        'questions': questions,
        'num_correct': num_correct,
    }

    return render(request, 'ExamInterface/review.html', context)