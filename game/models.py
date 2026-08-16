from django.db import models


class Question(models.Model):

    QUESTION_TYPES = [
        ("truth", "Truth"),
        ("dare", "Dare"),
    ]

    CATEGORIES = [
        ("funny", "Funny"),
        ("fantasy", "Fantasy"),
        ("crazy", "Crazy"),
        ("friendship", "Friendship"),
        ("deep", "Deep"),
        ("horror", "Horror"),
        ("movies", "Movies"),
        ("music", "Music"),
        ("school", "School / College"),
        ("random", "Random"),
    ]

    DIFFICULTIES = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]

    question_type = models.CharField(
        max_length=10,
        choices=QUESTION_TYPES
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORIES
    )

    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTIES,
        default="easy"
    )

    text = models.TextField()

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.get_question_type_display()} - {self.text[:50]}"

    # =========================================
# ONLINE TRUTH OR DARE ROOM
# =========================================

class OnlineRoom(models.Model):

    room_code = models.CharField(
        max_length=6,
        unique=True
    )

    host_name = models.CharField(
        max_length=50
    )

    players = models.JSONField(
        default=list
    )

    selected_categories = models.JSONField(
        default=list
    )

    difficulty = models.CharField(
        max_length=10,
        default="mixed"
    )

    current_player_index = models.IntegerField(
        default=0
    )

    current_question_id = models.IntegerField(
        null=True,
        blank=True
    )

    game_started = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.room_code