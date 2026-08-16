from django.core.management.base import BaseCommand
from game.models import Question


class Command(BaseCommand):

    help = "Add School / College Truth and Dare questions"

    questions = [

        # =========================================
        # EASY - TRUTH
        # =========================================

        ("truth", "school", "easy",
         "What was your favorite subject in school or college?"),

        ("truth", "school", "easy",
         "Who was your favorite teacher?"),

        ("truth", "school", "easy",
         "What was your funniest classroom memory?"),

        ("truth", "school", "easy",
         "Have you ever fallen asleep during a class?"),

        ("truth", "school", "easy",
         "What was your favorite thing about school or college?"),

        ("truth", "school", "easy",
         "Which subject did you find the most difficult?"),

        ("truth", "school", "easy",
         "Have you ever forgotten to do your homework?"),

        ("truth", "school", "easy",
         "What was your funniest school nickname?"),

        ("truth", "school", "easy",
         "Which school or college event did you enjoy the most?"),

        ("truth", "school", "easy",
         "What is one thing you miss about your school or college days?"),


        # =========================================
        # EASY - DARE
        # =========================================

        ("dare", "school", "easy",
         "Pretend you are a strict teacher for 20 seconds."),

        ("dare", "school", "easy",
         "Give a funny classroom lecture about a completely random topic."),

        ("dare", "school", "easy",
         "Pretend you are answering a difficult exam question."),

        ("dare", "school", "easy",
         "Act like a student who forgot to study for an exam."),

        ("dare", "school", "easy",
         "Pretend to take attendance for everyone in the room."),

        ("dare", "school", "easy",
         "Give yourself a funny school report card."),

        ("dare", "school", "easy",
         "Pretend you are giving the morning school assembly speech."),

        ("dare", "school", "easy",
         "Act like a teacher who has completely lost their patience."),

        ("dare", "school", "easy",
         "Pretend you just received the highest marks in the class."),

        ("dare", "school", "easy",
         "Give a 20-second speech about why your school bag deserves an award."),


        # =========================================
        # MEDIUM - TRUTH
        # =========================================

        ("truth", "school", "medium",
         "Have you ever copied someone's homework?"),

        ("truth", "school", "medium",
         "Have you ever pretended to understand a lesson when you didn't?"),

        ("truth", "school", "medium",
         "What is the funniest excuse you have given for not completing an assignment?"),

        ("truth", "school", "medium",
         "Have you ever been caught doing something you shouldn't have been doing in class?"),

        ("truth", "school", "medium",
         "Which subject would you completely remove from the timetable?"),

        ("truth", "school", "medium",
         "Who was the funniest student in your class?"),

        ("truth", "school", "medium",
         "Have you ever been nervous before giving a presentation?"),

        ("truth", "school", "medium",
         "What is the most embarrassing thing that happened to you at school or college?"),

        ("truth", "school", "medium",
         "If you could repeat one school or college year, which would it be?"),

        ("truth", "school", "medium",
         "What is the best friendship you made at school or college?"),


        # =========================================
        # MEDIUM - DARE
        # =========================================

        ("dare", "school", "medium",
         "Pretend you are giving a presentation and suddenly forget your entire topic."),

        ("dare", "school", "medium",
         "Teach the group something completely useless like it is an important school lesson."),

        ("dare", "school", "medium",
         "Pretend you are a student trying to convince a teacher to give you extra marks."),

        ("dare", "school", "medium",
         "Give a dramatic speech about surviving exam week."),

        ("dare", "school", "medium",
         "Pretend you are the principal announcing a completely ridiculous new school rule."),

        ("dare", "school", "medium",
         "Act out a student receiving their exam results."),

        ("dare", "school", "medium",
         "Pretend you are a teacher interviewing a student for a completely ridiculous reason."),

        ("dare", "school", "medium",
         "Create a funny school rule and explain why everyone must follow it."),

        ("dare", "school", "medium",
         "Pretend you are giving a motivational speech before the biggest exam of your life."),

        ("dare", "school", "medium",
         "Act out a dramatic scene where you realize you left your assignment at home."),


        # =========================================
        # HARD - TRUTH
        # =========================================

        ("truth", "school", "hard",
         "What is one decision you made at school or college that you would change?"),

        ("truth", "school", "hard",
         "What is the biggest lesson school or college has taught you outside the classroom?"),

        ("truth", "school", "hard",
         "Have you ever felt pressured to perform well academically?"),

        ("truth", "school", "hard",
         "What is one academic failure that taught you something important?"),

        ("truth", "school", "hard",
         "What career did you dream about when you were younger?"),

        ("truth", "school", "hard",
         "What is one thing you wish teachers had taught you about real life?"),

        ("truth", "school", "hard",
         "Have you ever compared your achievements with those of your classmates?"),

        ("truth", "school", "hard",
         "What is one school or college experience that changed your personality?"),

        ("truth", "school", "hard",
         "What advice would you give your younger school or college self?"),

        ("truth", "school", "hard",
         "If you could change one thing about the education system, what would it be?"),


        # =========================================
        # HARD - DARE
        # =========================================

        ("dare", "school", "hard",
         "Give a 30-second motivational speech to students before their final exams."),

        ("dare", "school", "hard",
         "Pretend you are a teacher explaining the most important life lesson you know."),

        ("dare", "school", "hard",
         "Give a dramatic speech about your journey from your first day of school to today."),

        ("dare", "school", "hard",
         "Pretend you are the principal announcing the biggest change your school has ever seen."),

        ("dare", "school", "hard",
         "Create your dream school and explain its rules, subjects, and activities."),

        ("dare", "school", "hard",
         "Pretend you are giving a graduation speech to your entire class."),

        ("dare", "school", "hard",
         "Give advice to your younger self as if you were meeting them in your old classroom."),

        ("dare", "school", "hard",
         "Pretend you are a teacher explaining why failure can be useful."),

        ("dare", "school", "hard",
         "Create a completely new subject and give the first lesson in it."),

        ("dare", "school", "hard",
         "Give a 30-second speech about what success means to you after finishing school or college."),

    ]


    def handle(self, *args, **options):

        added = 0
        skipped = 0

        for question_type, category, difficulty, text in self.questions:

            exists = Question.objects.filter(
                question_type=question_type,
                category=category,
                difficulty=difficulty,
                text=text
            ).exists()

            if exists:
                skipped += 1
                continue

            Question.objects.create(
                question_type=question_type,
                category=category,
                difficulty=difficulty,
                text=text,
                is_active=True
            )

            added += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Added {added} School questions."
            )
        )

        self.stdout.write(
            f"Skipped {skipped} questions that already existed."
        )