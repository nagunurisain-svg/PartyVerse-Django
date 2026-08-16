from django.core.management.base import BaseCommand
from game.models import Question


class Command(BaseCommand):

    help = "Add Fantasy Truth and Dare questions"

    questions = [

        # EASY - TRUTH

        ("truth", "fantasy", "easy",
         "If you could have one magical power for a day, what would it be?"),

        ("truth", "fantasy", "easy",
         "If you could fly or become invisible, which would you choose?"),

        ("truth", "fantasy", "easy",
         "If you could talk to one magical creature, which would you choose?"),

        ("truth", "fantasy", "easy",
         "If you found a magic lamp, what would your first wish be?"),

        ("truth", "fantasy", "easy",
         "If you could live in a fantasy castle, would you?"),

        ("truth", "fantasy", "easy",
         "If you could become a superhero for one day, what would your name be?"),

        ("truth", "fantasy", "easy",
         "If you could have a magical pet, what would it be?"),

        ("truth", "fantasy", "easy",
         "If you could control fire, water, air, or earth, which would you choose?"),

        ("truth", "fantasy", "easy",
         "If you could enter any fantasy movie, which one would you choose?"),

        ("truth", "fantasy", "easy",
         "If you could have a magic wand, what would you use it for first?"),


        # EASY - DARE

        ("dare", "fantasy", "easy",
         "Pretend you have magical powers and cast a spell."),

        ("dare", "fantasy", "easy",
         "Act like a superhero who just discovered their powers."),

        ("dare", "fantasy", "easy",
         "Pretend you're a dragon protecting your treasure."),

        ("dare", "fantasy", "easy",
         "Create a magical spell using three random words."),

        ("dare", "fantasy", "easy",
         "Act like a wizard for 30 seconds."),

        ("dare", "fantasy", "easy",
         "Pretend you can fly and demonstrate how you would fly."),

        ("dare", "fantasy", "easy",
         "Make your most dramatic superhero pose."),

        ("dare", "fantasy", "easy",
         "Pretend you're an alien meeting humans for the first time."),

        ("dare", "fantasy", "easy",
         "Act like a magical creature without speaking."),

        ("dare", "fantasy", "easy",
         "Pretend you just discovered a secret portal."),


        # MEDIUM - TRUTH

        ("truth", "fantasy", "medium",
         "If you could live in any fantasy universe, which one would you choose and why?"),

        ("truth", "fantasy", "medium",
         "If you could travel through time, would you visit the past or future?"),

        ("truth", "fantasy", "medium",
         "If you could become any mythical creature, what would you become?"),

        ("truth", "fantasy", "medium",
         "If you had three magical wishes, what would they be?"),

        ("truth", "fantasy", "medium",
         "If you could meet one fictional character in real life, who would it be?"),

        ("truth", "fantasy", "medium",
         "If you could create your own magical kingdom, what would it be like?"),

        ("truth", "fantasy", "medium",
         "If you could choose between being a wizard, warrior, king or queen, or explorer, which would you choose?"),

        ("truth", "fantasy", "medium",
         "If you could make one impossible thing real, what would it be?"),

        ("truth", "fantasy", "medium",
         "If you discovered a secret magical world hidden from everyone else, would you reveal it?"),

        ("truth", "fantasy", "medium",
         "If you could change one rule of reality using magic, what would you change?"),


        # MEDIUM - DARE

        ("dare", "fantasy", "medium",
         "Give yourself a dramatic speech as the ruler of a magical kingdom."),

        ("dare", "fantasy", "medium",
         "Pretend you're a wizard teaching another player their first spell."),

        ("dare", "fantasy", "medium",
         "Act out a battle against an invisible monster."),

        ("dare", "fantasy", "medium",
         "Pretend you've traveled 1,000 years into the future and explain what you see."),

        ("dare", "fantasy", "medium",
         "Invent a magical creature and explain its powers."),

        ("dare", "fantasy", "medium",
         "Pretend you're a superhero arriving to save everyone."),

        ("dare", "fantasy", "medium",
         "Act like a time traveler who accidentally arrived in the wrong year."),

        ("dare", "fantasy", "medium",
         "Pretend you're a villain explaining your master plan."),

        ("dare", "fantasy", "medium",
         "Create a fantasy superhero name for the player next to you."),

        ("dare", "fantasy", "medium",
         "Pretend you just discovered a legendary magical treasure and react dramatically."),


        # HARD - TRUTH

        ("truth", "fantasy", "hard",
         "If you could rewrite one part of reality, what would you change?"),

        ("truth", "fantasy", "hard",
         "If you could know exactly what your future looks like, would you choose to see it?"),

        ("truth", "fantasy", "hard",
         "If you could become extremely powerful but could never return to your normal life, would you accept?"),

        ("truth", "fantasy", "hard",
         "If you could save either your past or your future, which would you choose?"),

        ("truth", "fantasy", "hard",
         "If you could enter a fantasy world but never return to reality, would you go?"),

        ("truth", "fantasy", "hard",
         "If you could erase one painful memory using magic, would you?"),

        ("truth", "fantasy", "hard",
         "If you could become immortal but watch everyone you love grow old, would you accept?"),

        ("truth", "fantasy", "hard",
         "If you had unlimited magical power, what is the first thing you would change about the world?"),

        ("truth", "fantasy", "hard",
         "If you could meet your future self, what is the one question you would ask?"),

        ("truth", "fantasy", "hard",
         "If you could know one absolute truth about the universe, what would you want to know?"),


        # HARD - DARE

        ("dare", "fantasy", "hard",
         "Give a 30-second dramatic speech as the most powerful person in the universe."),

        ("dare", "fantasy", "hard",
         "Pretend you are a legendary villain explaining why you became evil."),

        ("dare", "fantasy", "hard",
         "Act out a scene where you discover that your best friend is secretly a superhero."),

        ("dare", "fantasy", "hard",
         "Pretend you're the last human alive in a fantasy world and give your final speech."),

        ("dare", "fantasy", "hard",
         "Create an imaginary superpower and demonstrate how you would use it."),

        ("dare", "fantasy", "hard",
         "Pretend you can control time and act out freezing everyone in the room."),

        ("dare", "fantasy", "hard",
         "Act out a dramatic scene where you discover you are secretly royalty."),

        ("dare", "fantasy", "hard",
         "Pretend you're fighting an invisible army and defeat it dramatically."),

        ("dare", "fantasy", "hard",
         "Create your own fantasy kingdom, including its name, ruler, and one unusual law."),

        ("dare", "fantasy", "hard",
         "Pretend you're a powerful wizard whose magic has suddenly disappeared and act out your reaction."),
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
                f"Added {added} Fantasy questions."
            )
        )

        self.stdout.write(
            f"Skipped {skipped} questions that already existed."
        )