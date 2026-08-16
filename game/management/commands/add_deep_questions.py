from django.core.management.base import BaseCommand
from game.models import Question


class Command(BaseCommand):

    help = "Add Deep Truth and Dare questions"

    questions = [

        # =========================================
        # EASY - TRUTH
        # =========================================

        ("truth", "deep", "easy",
         "What is one thing that always makes you happy?"),

        ("truth", "deep", "easy",
         "What is something you are grateful for today?"),

        ("truth", "deep", "easy",
         "What is one dream you have for your future?"),

        ("truth", "deep", "easy",
         "Who is someone you really look up to?"),

        ("truth", "deep", "easy",
         "What is one thing you would like to improve about yourself?"),

        ("truth", "deep", "easy",
         "What is your favorite memory from childhood?"),

        ("truth", "deep", "easy",
         "What makes you feel proud of yourself?"),

        ("truth", "deep", "easy",
         "What is one lesson you learned recently?"),

        ("truth", "deep", "easy",
         "What is something you could never live without?"),

        ("truth", "deep", "easy",
         "What is one place you would love to visit someday?"),


        # =========================================
        # EASY - DARE
        # =========================================

        ("dare", "deep", "easy",
         "Tell everyone one thing you genuinely like about yourself."),

        ("dare", "deep", "easy",
         "Tell another player one thing you appreciate about them."),

        ("dare", "deep", "easy",
         "Say one positive thing about your future."),

        ("dare", "deep", "easy",
         "Share one happy memory with the group."),

        ("dare", "deep", "easy",
         "Tell the group one goal you would like to achieve."),

        ("dare", "deep", "easy",
         "Say something you are proud of accomplishing."),

        ("dare", "deep", "easy",
         "Tell everyone one person who has influenced your life positively."),

        ("dare", "deep", "easy",
         "Share one piece of advice you would give your younger self."),

        ("dare", "deep", "easy",
         "Describe your happiest day in three sentences."),

        ("dare", "deep", "easy",
         "Tell the group one thing you hope happens this year."),


        # =========================================
        # MEDIUM - TRUTH
        # =========================================

        ("truth", "deep", "medium",
         "What is something you are afraid of losing?"),

        ("truth", "deep", "medium",
         "What is one mistake that taught you an important lesson?"),

        ("truth", "deep", "medium",
         "What is something you wish people understood about you?"),

        ("truth", "deep", "medium",
         "When was the last time you felt truly proud of yourself?"),

        ("truth", "deep", "medium",
         "What is one decision that changed your life?"),

        ("truth", "deep", "medium",
         "What is something you wish you had done differently?"),

        ("truth", "deep", "medium",
         "What is one goal you are serious about achieving?"),

        ("truth", "deep", "medium",
         "What kind of person do you want to become?"),

        ("truth", "deep", "medium",
         "What is something you have learned from a difficult experience?"),

        ("truth", "deep", "medium",
         "What matters more to you: success, happiness, or peace of mind? Why?"),


        # =========================================
        # MEDIUM - DARE
        # =========================================

        ("dare", "deep", "medium",
         "Tell the group about one goal you are working toward."),

        ("dare", "deep", "medium",
         "Share one lesson that life has taught you."),

        ("dare", "deep", "medium",
         "Tell another player one quality you genuinely admire in them."),

        ("dare", "deep", "medium",
         "Describe the person you want to become five years from now."),

        ("dare", "deep", "medium",
         "Share one mistake that helped you grow."),

        ("dare", "deep", "medium",
         "Tell everyone one thing you would change about the world."),

        ("dare", "deep", "medium",
         "Give the group one piece of advice you believe everyone should hear."),

        ("dare", "deep", "medium",
         "Describe your ideal future in 30 seconds."),

        ("dare", "deep", "medium",
         "Tell the group about someone who has positively influenced your life."),

        ("dare", "deep", "medium",
         "Say one thing you want to be remembered for."),


        # =========================================
        # HARD - TRUTH
        # =========================================

        ("truth", "deep", "hard",
         "What is your biggest fear about the future?"),

        ("truth", "deep", "hard",
         "What is one truth about yourself that took you a long time to accept?"),

        ("truth", "deep", "hard",
         "What is something you regret but cannot change?"),

        ("truth", "deep", "hard",
         "What is the hardest decision you have ever had to make?"),

        ("truth", "deep", "hard",
         "What is one thing you would tell your younger self if you could?"),

        ("truth", "deep", "hard",
         "What is something you are still trying to understand about yourself?"),

        ("truth", "deep", "hard",
         "What does a successful life mean to you personally?"),

        ("truth", "deep", "hard",
         "What is one thing you would sacrifice to achieve your biggest dream?"),

        ("truth", "deep", "hard",
         "What is something you wish you could change about your past?"),

        ("truth", "deep", "hard",
         "If you knew you could not fail, what would you do with your life?"),


        # =========================================
        # HARD - DARE
        # =========================================

        ("dare", "deep", "hard",
         "Give a 30-second speech about what you want your life to mean."),

        ("dare", "deep", "hard",
         "Tell the group one difficult lesson you have learned in life."),

        ("dare", "deep", "hard",
         "Describe one fear you want to overcome and why."),

        ("dare", "deep", "hard",
         "Tell another player something you genuinely respect about them."),

        ("dare", "deep", "hard",
         "Describe where you hope your life will be ten years from now."),

        ("dare", "deep", "hard",
         "Give your future self a short message."),

        ("dare", "deep", "hard",
         "Tell the group about one experience that changed the way you think."),

        ("dare", "deep", "hard",
         "Describe what you believe makes a person truly happy."),

        ("dare", "deep", "hard",
         "Share one dream you would pursue if money were not a problem."),

        ("dare", "deep", "hard",
         "Give everyone one piece of life advice that you genuinely believe."),

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
                f"Added {added} Deep questions."
            )
        )

        self.stdout.write(
            f"Skipped {skipped} questions that already existed."
        )