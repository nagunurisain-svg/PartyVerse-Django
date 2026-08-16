from django.core.management.base import BaseCommand
from game.models import Question


class Command(BaseCommand):

    help = "Add Crazy Truth and Dare questions"

    questions = [

        # =========================================
        # EASY - TRUTH
        # =========================================

        ("truth", "crazy", "easy",
         "What is the craziest food combination you would actually try?"),

        ("truth", "crazy", "easy",
         "What is the weirdest thing you have ever done because you were bored?"),

        ("truth", "crazy", "easy",
         "If you had to wear one ridiculous outfit for a whole day, what would it be?"),

        ("truth", "crazy", "easy",
         "What is the strangest thing you have ever said by accident?"),

        ("truth", "crazy", "easy",
         "If you could replace your voice with any sound, what would you choose?"),

        ("truth", "crazy", "easy",
         "What is the weirdest nickname you would give yourself?"),

        ("truth", "crazy", "easy",
         "If your pet could talk, what embarrassing thing would it tell everyone about you?"),

        ("truth", "crazy", "easy",
         "What is the craziest hairstyle you would try once?"),

        ("truth", "crazy", "easy",
         "If you could turn into an animal for one hour, which animal would you choose?"),

        ("truth", "crazy", "easy",
         "What completely useless superpower would you love to have?"),


        # =========================================
        # EASY - DARE
        # =========================================

        ("dare", "crazy", "easy",
         "Walk like a penguin for 20 seconds."),

        ("dare", "crazy", "easy",
         "Talk in a robot voice for the next 30 seconds."),

        ("dare", "crazy", "easy",
         "Pretend you are a chicken until your next turn."),

        ("dare", "crazy", "easy",
         "Make the strangest face you can."),

        ("dare", "crazy", "easy",
         "Dance without music for 20 seconds."),

        ("dare", "crazy", "easy",
         "Pretend the floor is lava for 15 seconds."),

        ("dare", "crazy", "easy",
         "Act like a confused alien who just landed on Earth."),

        ("dare", "crazy", "easy",
         "Pretend your hand is a phone and have a serious conversation with it."),

        ("dare", "crazy", "easy",
         "Walk backwards while introducing yourself dramatically."),

        ("dare", "crazy", "easy",
         "Make up a completely ridiculous superhero name and pose."),


        # =========================================
        # MEDIUM - TRUTH
        # =========================================

        ("truth", "crazy", "medium",
         "What is the craziest thing you would do if you knew nobody would judge you?"),

        ("truth", "crazy", "medium",
         "If you could switch lives with anyone for one day, who would you choose?"),

        ("truth", "crazy", "medium",
         "What is the weirdest dream you can remember?"),

        ("truth", "crazy", "medium",
         "If you had to survive one week using only three random objects, what would you choose?"),

        ("truth", "crazy", "medium",
         "What is the strangest rule you would create if you became the ruler of the world?"),

        ("truth", "crazy", "medium",
         "If you could make one completely impossible thing happen tomorrow, what would it be?"),

        ("truth", "crazy", "medium",
         "What is the craziest excuse you could invent for being late?"),

        ("truth", "crazy", "medium",
         "If your thoughts were displayed above your head for one day, would you survive?"),

        ("truth", "crazy", "medium",
         "If you had to live inside one cartoon world, which would you choose?"),

        ("truth", "crazy", "medium",
         "What is the most ridiculous challenge you think you could actually complete?"),


        # =========================================
        # MEDIUM - DARE
        # =========================================

        ("dare", "crazy", "medium",
         "Pretend you are a news reporter covering the most ridiculous event imaginable."),

        ("dare", "crazy", "medium",
         "Invent a completely useless product and advertise it dramatically."),

        ("dare", "crazy", "medium",
         "Pretend you are a famous singer performing your biggest hit."),

        ("dare", "crazy", "medium",
         "Act like a monkey trying to use a smartphone."),

        ("dare", "crazy", "medium",
         "Pretend you are a chef preparing an invisible five-star meal."),

        ("dare", "crazy", "medium",
         "Have a dramatic argument with an imaginary villain."),

        ("dare", "crazy", "medium",
         "Pretend you are a superhero whose only power is controlling spoons."),

        ("dare", "crazy", "medium",
         "Create a ridiculous dance move and teach it to another player."),

        ("dare", "crazy", "medium",
         "Pretend you are an alien trying to order food at a restaurant."),

        ("dare", "crazy", "medium",
         "Give a motivational speech about something completely useless."),


        # =========================================
        # HARD - TRUTH
        # =========================================

        ("truth", "crazy", "hard",
         "If you could completely restart your life with one unusual rule, what would the rule be?"),

        ("truth", "crazy", "hard",
         "If everyone could hear your thoughts for one hour, what would you do?"),

        ("truth", "crazy", "hard",
         "If you could make one completely impossible dream come true, what would you choose?"),

        ("truth", "crazy", "hard",
         "If you had to spend a year living in a completely bizarre place, where would you choose?"),

        ("truth", "crazy", "hard",
         "If you could remove one normal rule from society, which one would you remove?"),

        ("truth", "crazy", "hard",
         "If you could turn any ordinary object into something extremely powerful, what would you choose?"),

        ("truth", "crazy", "hard",
         "If your life had one completely ridiculous plot twist, what would you want it to be?"),

        ("truth", "crazy", "hard",
         "If you could become famous for something completely ridiculous, what would it be?"),

        ("truth", "crazy", "hard",
         "If you had to choose between being extremely lucky or extremely unpredictable, which would you choose?"),

        ("truth", "crazy", "hard",
         "If you could create one bizarre law that everyone had to follow for a day, what would it be?"),


        # =========================================
        # HARD - DARE
        # =========================================

        ("dare", "crazy", "hard",
         "Pretend you are the president of a completely ridiculous country and give your first speech."),

        ("dare", "crazy", "hard",
         "Create a completely ridiculous invention and explain how it works."),

        ("dare", "crazy", "hard",
         "Pretend you are being interviewed after saving the world using a completely useless object."),

        ("dare", "crazy", "hard",
         "Act out a dramatic scene where your imaginary pet becomes your boss."),

        ("dare", "crazy", "hard",
         "Pretend you are a time traveler who accidentally changed the world by making one tiny mistake."),

        ("dare", "crazy", "hard",
         "Give a serious courtroom defense for why you should be allowed to own a pet dinosaur."),

        ("dare", "crazy", "hard",
         "Pretend you are a world-famous celebrity who has forgotten why you are famous."),

        ("dare", "crazy", "hard",
         "Create a ridiculous new sport and explain its rules to everyone."),

        ("dare", "crazy", "hard",
         "Act out a battle against an invisible army using only dramatic sound effects."),

        ("dare", "crazy", "hard",
         "Give a 30-second speech explaining why humans should communicate only through dance."),

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
                f"Added {added} Crazy questions."
            )
        )

        self.stdout.write(
            f"Skipped {skipped} questions that already existed."
        )