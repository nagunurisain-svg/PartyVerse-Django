from django.core.management.base import BaseCommand
from game.models import Question


class Command(BaseCommand):

    help = "Add Funny Truth and Dare questions"

    questions = [

        # =========================================
        # EASY - TRUTH
        # =========================================

        ("truth", "funny", "easy",
         "What is the funniest thing you've ever done in front of your friends?"),

        ("truth", "funny", "easy",
         "What is your funniest nickname?"),

        ("truth", "funny", "easy",
         "What is the funniest food combination you have ever tried?"),

        ("truth", "funny", "easy",
         "Have you ever laughed at the wrong moment? What happened?"),

        ("truth", "funny", "easy",
         "What is the funniest word you know?"),

        ("truth", "funny", "easy",
         "What is the funniest excuse you have ever given?"),

        ("truth", "funny", "easy",
         "What is the most embarrassing song you secretly enjoy?"),

        ("truth", "funny", "easy",
         "Have you ever talked to yourself when nobody was around?"),

        ("truth", "funny", "easy",
         "What is the funniest mistake you have made at school or college?"),

        ("truth", "funny", "easy",
         "What is the funniest photo of yourself on your phone?"),


        # =========================================
        # EASY - DARE
        # =========================================

        ("dare", "funny", "easy",
         "Talk like a robot for the next 30 seconds."),

        ("dare", "funny", "easy",
         "Make the funniest face you can."),

        ("dare", "funny", "easy",
         "Pretend to be a chicken for 20 seconds."),

        ("dare", "funny", "easy",
         "Say your name in the funniest voice possible."),

        ("dare", "funny", "easy",
         "Walk around like a penguin for 20 seconds."),

        ("dare", "funny", "easy",
         "Pretend you are a famous movie star giving an interview."),

        ("dare", "funny", "easy",
         "Sing the alphabet like an opera singer."),

        ("dare", "funny", "easy",
         "Pretend your chair is your best friend and introduce it to everyone."),

        ("dare", "funny", "easy",
         "Laugh like a cartoon character for 15 seconds."),

        ("dare", "funny", "easy",
         "Try to make everyone in the room laugh without touching anyone."),


        # =========================================
        # MEDIUM - TRUTH
        # =========================================

        ("truth", "funny", "medium",
         "What is the most ridiculous thing you have ever believed as a child?"),

        ("truth", "funny", "medium",
         "What is the strangest thing you have ever done when you thought nobody was watching?"),

        ("truth", "funny", "medium",
         "Have you ever waved back at someone who wasn't waving at you?"),

        ("truth", "funny", "medium",
         "What is the funniest misunderstanding you have ever experienced?"),

        ("truth", "funny", "medium",
         "Have you ever sent a message to the wrong person? What happened?"),

        ("truth", "funny", "medium",
         "What is the funniest lie you told to avoid getting into trouble?"),

        ("truth", "funny", "medium",
         "What is the weirdest thing you have done because you were bored?"),

        ("truth", "funny", "medium",
         "Have you ever practiced a conversation before actually having it?"),

        ("truth", "funny", "medium",
         "What is the funniest thing you have done while trying to look cool?"),

        ("truth", "funny", "medium",
         "What is your most embarrassing autocorrect mistake?"),


        # =========================================
        # MEDIUM - DARE
        # =========================================

        ("dare", "funny", "medium",
         "Pretend to be a news reporter and report something completely ridiculous."),

        ("dare", "funny", "medium",
         "Give a dramatic speech about why your favorite snack deserves an award."),

        ("dare", "funny", "medium",
         "Pretend you are a teacher who has completely forgotten what today's lesson is about."),

        ("dare", "funny", "medium",
         "Act like a celebrity being chased by imaginary fans."),

        ("dare", "funny", "medium",
         "Try to sell an ordinary object in the room like it costs one million dollars."),

        ("dare", "funny", "medium",
         "Pretend you are a motivational speaker giving advice about something completely useless."),

        ("dare", "funny", "medium",
         "Act out a dramatic breakup with your imaginary smartphone."),

        ("dare", "funny", "medium",
         "Pretend you are a chef explaining how to cook an imaginary dish."),

        ("dare", "funny", "medium",
         "Have a serious conversation with an imaginary person for 30 seconds."),

        ("dare", "funny", "medium",
         "Pretend you are a superhero whose only power is making people laugh."),


        # =========================================
        # HARD - TRUTH
        # =========================================

        ("truth", "funny", "hard",
         "What is the most embarrassing thing you have done while trying to impress someone?"),

        ("truth", "funny", "hard",
         "What is the weirdest habit you have that your friends don't know about?"),

        ("truth", "funny", "hard",
         "What is the funniest secret you've accidentally revealed?"),

        ("truth", "funny", "hard",
         "Have you ever pretended to understand something when you actually had no idea what was happening?"),

        ("truth", "funny", "hard",
         "What is the funniest reason you have ever been late somewhere?"),

        ("truth", "funny", "hard",
         "What is the most embarrassing thing you have accidentally said out loud?"),

        ("truth", "funny", "hard",
         "Have you ever laughed at yourself after making a completely unnecessary mistake?"),

        ("truth", "funny", "hard",
         "What is the strangest thing you have searched for on the internet?"),

        ("truth", "funny", "hard",
         "What is the funniest thing your friends have caught you doing?"),

        ("truth", "funny", "hard",
         "If your life became a comedy movie, what would the most embarrassing scene be?"),


        # =========================================
        # HARD - DARE
        # =========================================

        ("dare", "funny", "hard",
         "Give a completely serious five-minute-style speech about why potatoes are important, but keep it under 30 seconds."),

        ("dare", "funny", "hard",
         "Pretend you are accepting an award for the most useless talent in the world."),

        ("dare", "funny", "hard",
         "Act out an entire argument between yourself and an imaginary version of yourself."),

        ("dare", "funny", "hard",
         "Pretend you are a dramatic actor auditioning for the role of a spoon."),

        ("dare", "funny", "hard",
         "Give a romantic movie proposal to an object in the room."),

        ("dare", "funny", "hard",
         "Pretend you are an alien trying to explain how humans eat food."),

        ("dare", "funny", "hard",
         "Create and perform a completely ridiculous advertisement for your shoes."),

        ("dare", "funny", "hard",
         "Pretend you are a professional commentator describing someone simply walking across the room."),

        ("dare", "funny", "hard",
         "Act like you are trapped inside a video game and dramatically explain what is happening."),

        ("dare", "funny", "hard",
         "Create a ridiculous dance and perform it for 20 seconds."),


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
                f"Added {added} Funny questions."
            )
        )

        self.stdout.write(
            f"Skipped {skipped} questions that already existed."
        )