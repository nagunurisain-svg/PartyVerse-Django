from django.core.management.base import BaseCommand
from game.models import Question


class Command(BaseCommand):

    help = "Add Music Truth and Dare questions"

    questions = [

        # =========================================
        # EASY - TRUTH
        # =========================================

        ("truth", "music", "easy",
         "What is your favorite song right now?"),

        ("truth", "music", "easy",
         "Who is your favorite singer?"),

        ("truth", "music", "easy",
         "What song do you know every word to?"),

        ("truth", "music", "easy",
         "What song always makes you happy?"),

        ("truth", "music", "easy",
         "What is the first song you remember loving?"),

        ("truth", "music", "easy",
         "What song do you listen to when you are in a great mood?"),

        ("truth", "music", "easy",
         "What is your favorite movie song?"),

        ("truth", "music", "easy",
         "Which singer would you love to see live?"),

        ("truth", "music", "easy",
         "What song would you choose as the soundtrack of your day?"),

        ("truth", "music", "easy",
         "What is one song you could listen to repeatedly without getting bored?"),


        # =========================================
        # EASY - DARE
        # =========================================

        ("dare", "music", "easy",
         "Sing the chorus of your favorite song."),

        ("dare", "music", "easy",
         "Hum a song and let everyone guess it."),

        ("dare", "music", "easy",
         "Dance to an imaginary song for 20 seconds."),

        ("dare", "music", "easy",
         "Sing a song in a completely different voice."),

        ("dare", "music", "easy",
         "Pretend you are performing on a huge concert stage."),

        ("dare", "music", "easy",
         "Make up a short song about the player next to you."),

        ("dare", "music", "easy",
         "Sing the alphabet like a famous singer."),

        ("dare", "music", "easy",
         "Create a funny beat using only your hands."),

        ("dare", "music", "easy",
         "Pretend to play an invisible guitar during a concert."),

        ("dare", "music", "easy",
         "Make up a 10-second song about PartyVerse."),


        # =========================================
        # MEDIUM - TRUTH
        # =========================================

        ("truth", "music", "medium",
         "What song describes your personality best?"),

        ("truth", "music", "medium",
         "What song reminds you of your best friend?"),

        ("truth", "music", "medium",
         "What song reminds you of a special memory?"),

        ("truth", "music", "medium",
         "Which song can instantly change your mood?"),

        ("truth", "music", "medium",
         "What song would you choose for your entrance at a big event?"),

        ("truth", "music", "medium",
         "Which artist would you choose to spend a day with?"),

        ("truth", "music", "medium",
         "What is a song you secretly enjoy even if your friends don't like it?"),

        ("truth", "music", "medium",
         "If your life had a theme song, what would it be?"),

        ("truth", "music", "medium",
         "What song would you dedicate to your closest friend?"),

        ("truth", "music", "medium",
         "Which music genre would you listen to if you could only choose one?"),


        # =========================================
        # MEDIUM - DARE
        # =========================================

        ("dare", "music", "medium",
         "Perform your favorite song like you are on a huge concert stage."),

        ("dare", "music", "medium",
         "Create a song using the names of three players."),

        ("dare", "music", "medium",
         "Pretend you are a music judge and rate another player's singing."),

        ("dare", "music", "medium",
         "Make up a rap about everyone in the room."),

        ("dare", "music", "medium",
         "Sing a romantic song in the funniest possible way."),

        ("dare", "music", "medium",
         "Pretend you are recording your first professional song."),

        ("dare", "music", "medium",
         "Create a dramatic music video scene without using any music."),

        ("dare", "music", "medium",
         "Sing a song while pretending you are extremely famous."),

        ("dare", "music", "medium",
         "Create a new music genre and demonstrate it."),

        ("dare", "music", "medium",
         "Perform an imaginary duet with another player."),


        # =========================================
        # HARD - TRUTH
        # =========================================

        ("truth", "music", "hard",
         "What song has the strongest emotional meaning for you?"),

        ("truth", "music", "hard",
         "What song reminds you of a difficult time in your life?"),

        ("truth", "music", "hard",
         "What song would you want people to remember you by?"),

        ("truth", "music", "hard",
         "If you could meet any musician from history, who would you choose?"),

        ("truth", "music", "hard",
         "If you could hear one unreleased song from any artist, whose would it be?"),

        ("truth", "music", "hard",
         "What song would you play during the most important moment of your life?"),

        ("truth", "music", "hard",
         "Which song makes you think about someone you miss?"),

        ("truth", "music", "hard",
         "If your life became a movie, what song would play during the final scene?"),

        ("truth", "music", "hard",
         "What kind of music do you think best represents who you are?"),

        ("truth", "music", "hard",
         "If you could write one song about your life, what would its main message be?"),


        # =========================================
        # HARD - DARE
        # =========================================

        ("dare", "music", "hard",
         "Perform a 30-second original song about your life."),

        ("dare", "music", "hard",
         "Create a rap about the entire group and perform it."),

        ("dare", "music", "hard",
         "Pretend you just won a major music award and give your acceptance speech."),

        ("dare", "music", "hard",
         "Create an emotional song about an imaginary story."),

        ("dare", "music", "hard",
         "Perform an imaginary concert finale with dramatic movements."),

        ("dare", "music", "hard",
         "Write and sing a four-line song about the person on your right."),

        ("dare", "music", "hard",
         "Pretend you are a music superstar explaining the story behind your biggest hit."),

        ("dare", "music", "hard",
         "Create a completely new song genre and perform a short example."),

        ("dare", "music", "hard",
         "Sing a serious song using only made-up words."),

        ("dare", "music", "hard",
         "Perform a 30-second dramatic music video scene without speaking."),

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
                f"Added {added} Music questions."
            )
        )

        self.stdout.write(
            f"Skipped {skipped} questions that already existed."
        )