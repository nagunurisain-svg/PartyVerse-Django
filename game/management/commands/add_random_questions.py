from django.core.management.base import BaseCommand
from game.models import Question


class Command(BaseCommand):

    help = "Add Random Truth and Dare questions"

    questions = [

        # =========================================
        # EASY - TRUTH
        # =========================================

        ("truth", "random", "easy",
         "What is something that always makes you smile?"),

        ("truth", "random", "easy",
         "Who was your first crush?"),

        ("truth", "random", "easy",
         "What kind of compliment makes you feel special?"),

        ("truth", "random", "easy",
         "Do you believe in love at first sight?"),

        ("truth", "random", "easy",
         "What is your favorite form of affection?"),

        ("truth", "random", "easy",
         "What makes you feel comfortable around someone?"),

        ("truth", "random", "easy",
         "What is your idea of a perfect date?"),

        ("truth", "random", "easy",
         "Do you prefer hugs or holding hands?"),

        ("truth", "random", "easy",
         "What personality trait attracts you most to someone?"),

        ("truth", "random", "easy",
         "What is one small thing that can instantly improve your mood?"),


        # =========================================
        # EASY - DARE
        # =========================================

        ("dare", "random", "easy",
         "Give another player a genuine compliment."),

        ("dare", "random", "easy",
         "Describe your perfect date in 20 seconds."),

        ("dare", "random", "easy",
         "Give your best innocent romantic smile."),

        ("dare", "random", "easy",
         "Tell someone what you think their best quality is."),

        ("dare", "random", "easy",
         "Act out how you would react if your crush suddenly texted you."),

        ("dare", "random", "easy",
         "Give an imaginary romantic movie-style compliment."),

        ("dare", "random", "easy",
         "Describe your dream Valentine's Day."),

        ("dare", "random", "easy",
         "Pretend you are asking someone on your dream date."),

        ("dare", "random", "easy",
         "Tell the group one thing that makes you feel appreciated."),

        ("dare", "random", "easy",
         "Give a dramatic friendship-to-romance movie confession to an imaginary person."),


        # =========================================
        # MEDIUM - TRUTH
        # =========================================

        ("truth", "random", "medium",
         "What is something you are feeling right now that you haven't told anyone?"),

        ("truth", "random", "medium",
         "Have you ever secretly fallen for a close friend?"),

        ("truth", "random", "medium",
         "What makes you feel emotionally close to someone?"),

        ("truth", "random", "medium",
         "Have you ever liked someone who didn't know about your feelings?"),

        ("truth", "random", "medium",
         "What is your biggest green flag in a partner?"),

        ("truth", "random", "medium",
         "What is your biggest red flag in a partner?"),

        ("truth", "random", "medium",
         "Have you ever been jealous but pretended you weren't?"),

        ("truth", "random", "medium",
         "What kind of affection makes you feel most loved?"),

        ("truth", "random", "medium",
         "Have you ever wanted to message someone but stopped yourself?"),

        ("truth", "random", "medium",
         "What makes someone emotionally attractive to you?"),


        # =========================================
        # MEDIUM - DARE
        # =========================================

        ("dare", "random", "medium",
         "Give someone in the group a sincere romantic compliment."),

        ("dare", "random", "medium",
         "Pretend to confess a crush to an imaginary person."),

        ("dare", "random", "medium",
         "Describe your ideal romantic partner in 30 seconds."),

        ("dare", "random", "medium",
         "Give an imaginary date invitation using your best romantic voice."),

        ("dare", "random", "medium",
         "Tell another player what makes them attractive as a person."),

        ("dare", "random", "medium",
         "Act out how you would react if someone you liked confessed their feelings to you."),

        ("dare", "random", "medium",
         "Describe your perfect private date without mentioning expensive things."),

        ("dare", "random", "medium",
         "Give a dramatic romantic movie confession."),

        ("dare", "random", "medium",
         "Tell the group one quality you would want in a lifelong partner."),

        ("dare", "random", "medium",
         "Pretend you're on a first date and introduce yourself dramatically."),


        # =========================================
        # HARD - TRUTH
        # =========================================

        ("truth", "random", "hard",
         "What is something you are afraid to admit about your feelings?"),

        ("truth", "random", "hard",
         "Have you ever had feelings for someone you knew you shouldn't?"),

        ("truth", "random", "hard",
         "What is your biggest fear when it comes to love?"),

        ("truth", "random", "hard",
         "Have you ever hidden your feelings because you were afraid of rejection?"),

        ("truth", "random", "hard",
         "What makes you feel emotionally safe with someone?"),

        ("truth", "random", "hard",
         "Do you find emotional intimacy more important than physical attraction? Why?"),

        ("truth", "random", "hard",
         "What is something you wish someone understood about your feelings?"),

        ("truth", "random", "hard",
         "Have you ever missed someone but refused to contact them?"),

        ("truth", "random", "hard",
         "What kind of romantic moment would make you genuinely nervous?"),

        ("truth", "random", "hard",
         "What is something you would never tolerate in a relationship?"),


        # =========================================
        # HARD - DARE
        # =========================================

        ("dare", "random", "hard",
         "Give a heartfelt 30-second confession to an imaginary crush."),

        ("dare", "random", "hard",
         "Describe your ideal intimate romantic evening without being explicit."),

        ("dare", "random", "hard",
         "Tell another player one quality you think would make them a great partner."),

        ("dare", "random", "hard",
         "Pretend someone you secretly like has asked you out and act out your reaction."),

        ("dare", "random", "hard",
         "Give a dramatic speech about what love means to you."),

        ("dare", "random", "hard",
         "Describe the kind of emotional connection you want in a relationship."),

        ("dare", "random", "hard",
         "Act out a romantic movie scene where two people finally confess their feelings."),

        ("dare", "random", "hard",
         "Tell the group what makes a romantic relationship feel truly intimate to you."),

        ("dare", "random", "hard",
         "Give an imaginary partner a heartfelt message about why you appreciate them."),

        ("dare", "random", "hard",
         "Describe your dream romantic moment in 30 seconds without using the words love or kiss."),

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
                f"Added {added} Random questions."
            )
        )

        self.stdout.write(
            f"Skipped {skipped} questions that already existed."
        )