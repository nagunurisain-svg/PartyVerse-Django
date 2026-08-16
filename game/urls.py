from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path(
        "truth-or-dare/",
        views.truth_or_dare,
        name="truth_or_dare"
    ),

    path(
        "truth-or-dare/categories/",
        views.categories,
        name="categories"
    ),

    path(
        "truth-or-dare/game/",
        views.game,
        name="game"
    ),

    path(
    "api/questions/",
    views.get_questions,
    name="get_questions"
),

    path(
    "truth-or-dare/difficulty/",
    views.difficulty,
    name="difficulty"
),

        path(
        "decision-maker/",
        views.decision_maker,
        name="decision_maker"
    ),

path(
    "online-play/",
    views.online_play,
    name="online_play"
),

path(
    "online-play/create/",
    views.create_room,
    name="create_room"
),

path(
    "online-play/join/",
    views.join_room,
    name="join_room"
),

path(
    "online-play/room/<str:room_code>/",
    views.online_lobby,
    name="online_lobby"
),
]