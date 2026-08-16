from django.core.management.base import BaseCommand
from game.models import Question


class Command(BaseCommand):

    help = "Add Movies Truth and Dare questions"

    questions = [

        # =========================================
        # EASY - TRUTH
        # =========================================

        ("truth", "movies", "easy",
         "What is your favorite movie of all time?"),

        ("truth", "movies", "easy",
         "Which movie character would you want as your best friend?"),

        ("truth", "movies", "easy",
         "What movie can you watch again and again?"),

        ("truth", "movies", "easy",
         "Which movie made you laugh the most?"),

        ("truth", "movies", "easy",
         "Which movie made you cry?"),

        ("truth", "movies", "easy",
         "Who is your favorite movie actor?"),

        ("truth", "movies", "easy",
         "Who is your favorite movie actress?"),

        ("truth", "movies", "easy",
         "What is the funniest movie you have watched?"),

        ("truth", "movies", "easy",
         "Which movie would you recommend to everyone in this group?"),

        ("truth", "movies", "easy",
         "If you could watch one movie for the first time again, which would it be?"),


        # =========================================
        # EASY - DARE
        # =========================================

        ("dare", "movies", "easy",
         "Act like your favorite movie character for 20 seconds."),

        ("dare", "movies", "easy",
         "Say a famous movie-style dialogue dramatically."),

        ("dare", "movies", "easy",
         "Pretend you are accepting an award for Best Actor or Actress."),

        ("dare", "movies", "easy",
         "Act out a famous movie scene without speaking."),

        ("dare", "movies", "easy",
         "Pretend you are a movie trailer narrator."),

        ("dare", "movies", "easy",
         "Create a dramatic movie title for your life."),

        ("dare", "movies", "easy",
         "Pretend you are being interviewed after becoming a movie star."),

        ("dare", "movies", "easy",
         "Act like a movie villain for 20 seconds."),

        ("dare", "movies", "easy",
         "Pretend you are the hero arriving at the final battle."),

        ("dare", "movies", "easy",
         "Create a funny movie poster pose."),


        # =========================================
        # MEDIUM - TRUTH
        # =========================================

        ("truth", "movies", "medium",
         "Which movie character is most similar to your personality?"),

        ("truth", "movies", "medium",
         "If your life were a movie, what genre would it be?"),

        ("truth", "movies", "medium",
         "Which fictional character would you want to switch lives with?"),

        ("truth", "movies", "medium",
         "Which movie universe would you want to live in?"),

        ("truth", "movies", "medium",
         "Which movie character would you trust with your biggest secret?"),

        ("truth", "movies", "medium",
         "Which movie villain do you secretly like?"),

        ("truth", "movies", "medium",
         "If you could change the ending of one movie, which movie would it be?"),

        ("truth", "movies", "medium",
         "Which movie character would make the worst roommate?"),

        ("truth", "movies", "medium",
         "Which movie character would make the best friend?"),

        ("truth", "movies", "medium",
         "If you could be the main character in one movie, which would you choose?"),


        # =========================================
        # MEDIUM - DARE
        # =========================================

        ("dare", "movies", "medium",
         "Recreate a dramatic movie scene using only facial expressions."),

        ("dare", "movies", "medium",
         "Give a movie trailer voice-over for the person sitting next to you."),

        ("dare", "movies", "medium",
         "Pretend you are a movie director giving instructions to the group."),

        ("dare", "movies", "medium",
         "Act out a romantic movie scene with an imaginary character."),

        ("dare", "movies", "medium",
         "Pretend you are the villain explaining your master plan."),

        ("dare", "movies", "medium",
         "Create a movie title based on everyone's personalities."),

        ("dare", "movies", "medium",
         "Pretend you are auditioning for the lead role in a superhero movie."),

        ("dare", "movies", "medium",
         "Act out a dramatic movie death scene without actually falling dangerously."),

        ("dare", "movies", "medium",
         "Pretend you are a celebrity being asked ridiculous interview questions."),

        ("dare", "movies", "medium",
         "Create a 20-second trailer for a completely ridiculous movie."),


        # =========================================
        # HARD - TRUTH
        # =========================================

        ("truth", "movies", "hard",
         "If you could erase one movie from your memory and watch it again, which would you choose?"),

        ("truth", "movies", "hard",
         "Which movie character's life would you actually want to live?"),

        ("truth", "movies", "hard",
         "If you could meet one fictional character in real life, who would you choose?"),

        ("truth", "movies", "hard",
         "Which movie changed the way you think about something?"),

        ("truth", "movies", "hard",
         "If your life had a movie ending, what would you want it to be?"),

        ("truth", "movies", "hard",
         "Which movie villain do you think had the best argument?"),

        ("truth", "movies", "hard",
         "If you could rewrite one movie ending, what would you change?"),

        ("truth", "movies", "hard",
         "Which movie world would you never want to live in?"),

        ("truth", "movies", "hard",
         "If you could become famous for starring in one type of movie, what would it be?"),

        ("truth", "movies", "hard",
         "If someone made a movie about your life, who should play you?"),


        # =========================================
        # HARD - DARE
        # =========================================

        ("dare", "movies", "hard",
         "Give a dramatic 30-second monologue as the main character of a movie."),

        ("dare", "movies", "hard",
         "Create an imaginary movie and explain its entire plot in 30 seconds."),

        ("dare", "movies", "hard",
         "Pretend you are the villain and give a dramatic speech about your plan."),

        ("dare", "movies", "hard",
         "Act out the final scene of a completely imaginary action movie."),

        ("dare", "movies", "hard",
         "Pretend you just won the biggest movie award in the world and give your speech."),

        ("dare", "movies", "hard",
         "Create a superhero character and perform their introduction scene."),

        ("dare", "movies", "hard",
         "Pretend you are directing the group in the final scene of a blockbuster movie."),

        ("dare", "movies", "hard",
         "Act out a dramatic plot twist without telling anyone what it is."),

        ("dare", "movies", "hard",
         "Create a movie title, villain, hero, and ending completely on the spot."),

        ("dare", "movies", "hard",
         "Perform a 30-second silent movie scene where something goes completely wrong."),

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
                f"Added {added} Movies questions."
            )
        )

        self.stdout.write(
            f"Skipped {skipped} questions that already existed."
        )