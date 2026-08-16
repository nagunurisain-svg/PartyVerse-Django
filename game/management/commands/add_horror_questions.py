from django.core.management.base import BaseCommand
from game.models import Question


class Command(BaseCommand):

    help = "Add Horror Truth and Dare questions"

    questions = [

        # =========================================
        # EASY - TRUTH
        # =========================================

        ("truth", "horror", "easy",
         "What is the scariest movie you have ever watched?"),

        ("truth", "horror", "easy",
         "Have you ever been scared while walking alone at night?"),

        ("truth", "horror", "easy",
         "What is your biggest fear?"),

        ("truth", "horror", "easy",
         "Have you ever heard a strange noise when nobody was around?"),

        ("truth", "horror", "easy",
         "What horror character scares you the most?"),

        ("truth", "horror", "easy",
         "Would you ever spend a night in a supposedly haunted house?"),

        ("truth", "horror", "easy",
         "Have you ever had a nightmare that you still remember?"),

        ("truth", "horror", "easy",
         "What place would you never want to visit alone at night?"),

        ("truth", "horror", "easy",
         "Do you believe in ghosts?"),

        ("truth", "horror", "easy",
         "What sound instantly makes you feel nervous?"),


        # =========================================
        # EASY - DARE
        # =========================================

        ("dare", "horror", "easy",
         "Tell a short scary story using your most dramatic voice."),

        ("dare", "horror", "easy",
         "Make your best scary face."),

        ("dare", "horror", "easy",
         "Pretend you just saw a ghost behind another player."),

        ("dare", "horror", "easy",
         "Walk like a zombie for 20 seconds."),

        ("dare", "horror", "easy",
         "Make a spooky sound without laughing."),

        ("dare", "horror", "easy",
         "Pretend you are a ghost trying to scare everyone."),

        ("dare", "horror", "easy",
         "Act like a frightened movie character for 20 seconds."),

        ("dare", "horror", "easy",
         "Pretend an invisible monster is chasing you."),

        ("dare", "horror", "easy",
         "Give a dramatic scream without actually hurting your voice."),

        ("dare", "horror", "easy",
         "Pretend you are exploring a haunted house for the first time."),


        # =========================================
        # MEDIUM - TRUTH
        # =========================================

        ("truth", "horror", "medium",
         "What is the creepiest experience you have ever had?"),

        ("truth", "horror", "medium",
         "Have you ever felt like someone was watching you when nobody was there?"),

        ("truth", "horror", "medium",
         "Would you spend one night alone in a place believed to be haunted?"),

        ("truth", "horror", "medium",
         "What is the scariest dream you have ever had?"),

        ("truth", "horror", "medium",
         "If you had to explore an abandoned building, what would scare you most?"),

        ("truth", "horror", "medium",
         "What fictional horror creature would you never want to meet?"),

        ("truth", "horror", "medium",
         "Have you ever been too scared to look behind you?"),

        ("truth", "horror", "medium",
         "If you could investigate one famous mystery, which would you choose?"),

        ("truth", "horror", "medium",
         "What is scarier to you: being alone in darkness or hearing strange noises?"),

        ("truth", "horror", "medium",
         "If you could know whether ghosts were real, would you want to know?"),


        # =========================================
        # MEDIUM - DARE
        # =========================================

        ("dare", "horror", "medium",
         "Tell a scary story with an unexpected ending."),

        ("dare", "horror", "medium",
         "Pretend you are trapped in a haunted house and act out your escape."),

        ("dare", "horror", "medium",
         "Act like a horror movie villain for 30 seconds."),

        ("dare", "horror", "medium",
         "Pretend you just received a mysterious message from a ghost."),

        ("dare", "horror", "medium",
         "Create a scary character and introduce yourself as that character."),

        ("dare", "horror", "medium",
         "Act out discovering mysterious footprints behind you."),

        ("dare", "horror", "medium",
         "Pretend an invisible ghost is sitting beside you and react naturally."),

        ("dare", "horror", "medium",
         "Describe an imaginary haunted house using your scariest storytelling voice."),

        ("dare", "horror", "medium",
         "Pretend you are a paranormal investigator discovering something strange."),

        ("dare", "horror", "medium",
         "Act out a scene where you hear a mysterious voice calling your name."),


        # =========================================
        # HARD - TRUTH
        # =========================================

        ("truth", "horror", "hard",
         "What is the most terrifying thought you have ever had?"),

        ("truth", "horror", "hard",
         "If you could learn the truth about one unexplained mystery, which would it be?"),

        ("truth", "horror", "hard",
         "Would you rather know when something bad will happen or never know at all?"),

        ("truth", "horror", "hard",
         "What would scare you more: being completely alone or knowing someone was nearby but invisible?"),

        ("truth", "horror", "hard",
         "If you discovered something impossible in your home, would you investigate it or leave immediately?"),

        ("truth", "horror", "hard",
         "Would you enter a place where everyone says something supernatural happened there?"),

        ("truth", "horror", "hard",
         "What is a fear you would like to overcome?"),

        ("truth", "horror", "hard",
         "If you could spend one night inside your worst nightmare, would you do it to overcome your fear?"),

        ("truth", "horror", "hard",
         "What would be your biggest fear if you were completely alone for a week?"),

        ("truth", "horror", "hard",
         "If you could ask a ghost one question and receive a truthful answer, what would you ask?"),


        # =========================================
        # HARD - DARE
        # =========================================

        ("dare", "horror", "hard",
         "Tell a 30-second horror story that gets progressively scarier."),

        ("dare", "horror", "hard",
         "Pretend you are the main character in a horror movie and act out the final scene."),

        ("dare", "horror", "hard",
         "Create a fictional haunted location and describe why nobody should visit it."),

        ("dare", "horror", "hard",
         "Pretend you just discovered that your reflection is moving differently from you."),

        ("dare", "horror", "hard",
         "Act out a scene where you realize someone invisible is standing beside you."),

        ("dare", "horror", "hard",
         "Pretend you are investigating a mysterious abandoned house and narrate everything you discover."),

        ("dare", "horror", "hard",
         "Create your own fictional horror villain and explain their mysterious origin."),

        ("dare", "horror", "hard",
         "Act out receiving a phone call from someone who supposedly disappeared years ago."),

        ("dare", "horror", "hard",
         "Tell a horror story where the final sentence completely changes the meaning of the story."),

        ("dare", "horror", "hard",
         "Pretend you are trapped in a dark room with an invisible creature and act out your escape."),

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
                f"Added {added} Horror questions."
            )
        )

        self.stdout.write(
            f"Skipped {skipped} questions that already existed."
        )