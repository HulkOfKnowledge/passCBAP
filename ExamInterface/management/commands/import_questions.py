import json
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction
from ExamInterface.models import Exam, Question


class Command(BaseCommand):
    help = 'Populates the Exam and Question models from questions.json'

    def handle(self, *args, **options):
        try:
            with open(r'C:\Users\Vendease\Documents\HulkOfKnowledge\projects\passCBAP\ExamInterface\questions.json', 'r') as f:
                questions_data = json.load(f)

            with transaction.atomic():
                for question_data in questions_data:
                    exam_name = 'All Questions'  # Provide the name of the exam
                    number_of_questions = len(questions_data)  # Total number of questions in the exam
                    time =  210 # Time limit for the exam in minutes

                    exam, _ = Exam.objects.get_or_create(name=exam_name, number_of_questions=number_of_questions, time=time)

                    Question.objects.create(
                        exam=exam,
                        question_id=question_data['id'],
                        question=question_data['question'],
                        options=question_data['options'],
                        correct_answer=question_data['correct_answer'],
                        explanation=question_data['explanation']
                    )

            self.stdout.write(self.style.SUCCESS('Questions have been successfully populated.'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('questions.json file not found. Please make sure the file exists.'))


# To run the script, use the following command:
# python manage.py import_questions
