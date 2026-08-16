from django.core.management.base import BaseCommand
from game.models import Question


class Command(BaseCommand):

    help = "Add Friendship Truth and Dare questions"

    questions = [

        # =========================================
        # EASY - TRUTH
        # =========================================

        ("truth", "friendship", "easy",
         "Who is the funniest person in your friend group?"),

        ("truth", "friendship", "easy",
         "Who was your first best friend?"),

        ("truth", "friendship", "easy",
         "What is your favorite memory with your friends?"),

        ("truth", "friendship", "easy",
         "Which friend makes you laugh the most?"),

        ("truth", "friendship", "easy",
         "Who in this group would you call first when you need help?"),

        ("truth", "friendship", "easy",
         "What is your favorite thing about your best friend?"),

        ("truth", "friendship", "easy",
         "Which friend knows you the best?"),

        ("truth", "friendship", "easy",
         "Who is most likely to make everyone laugh?"),

        ("truth", "friendship", "easy",
         "What is the funniest memory you have with your friends?"),

        ("truth", "friendship", "easy",
         "Which friend would you choose for a long road trip?"),


        # =========================================
        # EASY - DARE
        # =========================================

        ("dare", "friendship", "easy",
         "Give a genuine compliment to the player on your left."),

        ("dare", "friendship", "easy",
         "Tell your best friend one thing you appreciate about them."),

        ("dare", "friendship", "easy",
         "Give someone in the group a funny nickname."),

        ("dare", "friendship", "easy",
         "High-five every player."),

        ("dare", "friendship", "easy",
         "Tell the person next to you your favorite memory with them."),

        ("dare", "friendship", "easy",
         "Take a group selfie with everyone making a funny face."),

        ("dare", "friendship", "easy",
         "Say something nice about every player."),

        ("dare", "friendship", "easy",
         "Choose a friend and imitate their laugh."),

        ("dare", "friendship", "easy",
         "Tell another player why they are a good friend."),

        ("dare", "friendship", "easy",
         "Create a friendship team name for everyone in the group."),


        # =========================================
        # MEDIUM - TRUTH
        # =========================================

        ("truth", "friendship", "medium",
         "Which friend would you trust with your biggest secret?"),

        ("truth", "friendship", "medium",
         "Have you ever been jealous of one of your friends?"),

        ("truth", "friendship", "medium",
         "What is something you wish your friends understood about you?"),

        ("truth", "friendship", "medium",
         "Have you ever hidden something from your best friend?"),

        ("truth", "friendship", "medium",
         "Which friend would survive longest with you on a deserted island?"),

        ("truth", "friendship", "medium",
         "Who in your friend group would you trust to make an important decision for you?"),

        ("truth", "friendship", "medium",
         "What is the most memorable adventure you have had with friends?"),

        ("truth", "friendship", "medium",
         "Have you ever apologized to a friend even when you thought you were right?"),

        ("truth", "friendship", "medium",
         "What quality do you value most in a friend?"),

        ("truth", "friendship", "medium",
         "Which friend would you choose as your partner in a competition?"),


        # =========================================
        # MEDIUM - DARE
        # =========================================

        ("dare", "friendship", "medium",
         "Tell another player three things you genuinely like about them."),

        ("dare", "friendship", "medium",
         "Let the group choose a funny nickname for you for the next round."),

        ("dare", "friendship", "medium",
         "Imitate your closest friend for 30 seconds."),

        ("dare", "friendship", "medium",
         "Tell a funny story involving another player."),

        ("dare", "friendship", "medium",
         "Choose two players and describe why they would make a great team."),

        ("dare", "friendship", "medium",
         "Give a dramatic friendship speech to the whole group."),

        ("dare", "friendship", "medium",
         "Pretend you are introducing your best friend on a television show."),

        ("dare", "friendship", "medium",
         "Create a secret handshake with another player."),

        ("dare", "friendship", "medium",
         "Choose someone and recreate a funny memory with them."),

        ("dare", "friendship", "medium",
         "Describe every player using one funny but friendly word."),


        # =========================================
        # HARD - TRUTH
        # =========================================

        ("truth", "friendship", "hard",
         "Have you ever felt like a friend was drifting away from you?"),

        ("truth", "friendship", "hard",
         "What is the hardest thing about maintaining a friendship?"),

        ("truth", "friendship", "hard",
         "Have you ever regretted ending a friendship?"),

        ("truth", "friendship", "hard",
         "What is one thing you would never forgive a close friend for?"),

        ("truth", "friendship", "hard",
         "Have you ever stayed friends with someone even though the friendship was difficult?"),

        ("truth", "friendship", "hard",
         "What is something you have learned from a friendship that ended?"),

        ("truth", "friendship", "hard",
         "Would you rather have one extremely close friend or many casual friends?"),

        ("truth", "friendship", "hard",
         "What is the most important quality a lifelong friend should have?"),

        ("truth", "friendship", "hard",
         "Have you ever been afraid of losing a close friend?"),

        ("truth", "friendship", "hard",
         "What is one thing you would do to save an important friendship?"),


        # =========================================
        # HARD - DARE
        # =========================================

        ("dare", "friendship", "hard",
         "Give a heartfelt 30-second speech about what friendship means to you."),

        ("dare", "friendship", "hard",
         "Tell one player something you genuinely appreciate about your friendship with them."),

        ("dare", "friendship", "hard",
         "Choose a friend and describe one moment when they helped you."),

        ("dare", "friendship", "hard",
         "Give the entire group a motivational speech about staying good friends."),

        ("dare", "friendship", "hard",
         "Choose two players and explain why you think they would make lifelong friends."),

        ("dare", "friendship", "hard",
         "Tell someone in the group one positive thing they may not realize about themselves."),

        ("dare", "friendship", "hard",
         "Recreate the moment you first met one of your friends."),

        ("dare", "friendship", "hard",
         "Invent a friendship award and give it to another player."),

        ("dare", "friendship", "hard",
         "Describe your ideal friendship using only five words."),

        ("dare", "friendship", "hard",
         "Choose one player and give them a sincere friendship promise."),
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
                f"Added {added} Friendship questions."
            )
        )

        self.stdout.write(
            f"Skipped {skipped} questions that already existed."
        )