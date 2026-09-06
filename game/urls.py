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
    "register/",
      views.register, 
      name="register"
      ),

path(
    "login/",
      views.login_view, 
      name="login"
      ),
path(
    "logout/",
      views.logout_view,
        name="logout"
        ),

        path(
    "profile/",
    views.profile,
    name="profile"
),

path(
    "ask-question/",
    views.ask_question,
    name="ask_question"
),
]