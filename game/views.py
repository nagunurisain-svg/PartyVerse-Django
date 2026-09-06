from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


from .models import Question, UserProfile, CustomQuestion

# =========================================
# HOME
# =========================================

def home(request):

    return render(
        request,
        "game/home.html"
    )

# =========================================
# REGISTER
# =========================================

def register(request):

    if request.method == "POST":

        name = request.POST.get(
            "name",
            ""
        ).strip()

        email = request.POST.get(
            "email",
            ""
        ).strip().lower()

        mobile_number = request.POST.get(
            "mobile_number",
            ""
        ).strip()

        password = request.POST.get(
            "password",
            ""
        )

        confirm_password = request.POST.get(
            "confirm_password",
            ""
        )


        # =====================================
        # VALIDATION
        # =====================================

        if not name or not email or not mobile_number or not password:
            return render(
                request,
                "game/register.html",
                {
                    "error": "Please fill in all fields."
                }
            )


        if password != confirm_password:
            return render(
                request,
                "game/register.html",
                {
                    "error": "Passwords do not match."
                }
            )


        if User.objects.filter(
            email=email
        ).exists():

            return render(
                request,
                "game/register.html",
                {
                    "error": "An account with this email already exists."
                }
            )


        if UserProfile.objects.filter(
            mobile_number=mobile_number
        ).exists():

            return render(
                request,
                "game/register.html",
                {
                    "error": "This mobile number is already registered."
                }
            )


        # =====================================
        # CREATE USER
        # =====================================

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name
        )


        # =====================================
        # CREATE PROFILE
        # =====================================

        UserProfile.objects.create(
            user=user,
            mobile_number=mobile_number
        )


        # =====================================
        # LOGIN USER
        # =====================================

        login(
            request,
            user
        )


        return redirect("home")


    return render(
        request,
        "game/register.html"
    )


# =========================================
# LOGIN
# =========================================

def login_view(request):

    if request.method == "POST":

        login_value = request.POST.get(
            "login",
            ""
        ).strip()

        password = request.POST.get(
            "password",
            ""
        )


        # =====================================
        # FIND USER
        # =====================================

        user = None


        # Login using email
        if "@" in login_value:

            user = User.objects.filter(
                email=login_value.lower()
            ).first()


        # Login using mobile number
        else:

            profile = UserProfile.objects.filter(
                mobile_number=login_value
            ).select_related(
                "user"
            ).first()

            if profile:
                user = profile.user


        # =====================================
        # AUTHENTICATE
        # =====================================

        if user:

            authenticated_user = authenticate(
                request,
                username=user.username,
                password=password
            )

            if authenticated_user:

                login(
                    request,
                    authenticated_user
                )

                return redirect("home")


        return render(
            request,
            "game/login.html",
            {
                "error": "Invalid email/mobile number or password."
            }
        )


    return render(
        request,
        "game/login.html"
    )


# =========================================
# LOGOUT
# =========================================

def logout_view(request):

    logout(request)

    return redirect("home")

# =========================================
# USER PROFILE
# =========================================

def profile(request):

    if not request.user.is_authenticated:
        return redirect("login")

    user_profile = request.user.profile

    return render(
        request,
        "game/profile.html",
        {
            "profile": user_profile,
        }
    )

# =========================================
# ASK YOUR OWN QUESTION
# =========================================

def ask_question(request):

    if not request.user.is_authenticated:

        return redirect("login")

    if request.method == "POST":

        question_type = request.POST.get(
            "question_type",
            ""
        ).strip()

        category = request.POST.get(
            "category",
            ""
        ).strip()

        difficulty = request.POST.get(
            "difficulty",
            ""
        ).strip()

        text = request.POST.get(
            "text",
            ""
        ).strip()


        # =================================
        # VALIDATE TYPE
        # =================================

        if question_type not in [
            "truth",
            "dare"
        ]:

            return render(
                request,
                "game/ask_question.html",
                {
                    "error": "Please select Truth or Dare."
                }
            )


        # =================================
        # VALIDATE CATEGORY
        # =================================

        valid_categories = [
            "funny",
            "fantasy",
            "crazy",
            "friendship",
            "deep",
            "horror",
            "movies",
            "music",
            "school",
            "random"
        ]

        if category not in valid_categories:

            return render(
                request,
                "game/ask_question.html",
                {
                    "error": "Please select a valid category."
                }
            )


        # =================================
        # VALIDATE DIFFICULTY
        # =================================

        if difficulty not in [
            "easy",
            "medium",
            "hard"
        ]:

            return render(
                request,
                "game/ask_question.html",
                {
                    "error": "Please select a valid difficulty."
                }
            )


        # =================================
        # VALIDATE QUESTION
        # =================================

        if not text:

            return render(
                request,
                "game/ask_question.html",
                {
                    "error": "Please enter your question."
                }
            )


        if len(text) < 5:

            return render(
                request,
                "game/ask_question.html",
                {
                    "error": "Question must contain at least 5 characters."
                }
            )


        # =================================
        # SAVE QUESTION
        # =================================

        CustomQuestion.objects.create(

            user=request.user,

            question_type=question_type,

            category=category,

            difficulty=difficulty,

            text=text

        )


        # =================================
        # RETURN TO PROFILE
        # =================================

        return redirect("profile")


    return render(
        request,
        "game/ask_question.html"
    )

# =========================================
# TRUTH OR DARE PLAYER SETUP
# =========================================

def truth_or_dare(request):

    return render(
        request,
        "game/truth_or_dare.html"
    )


# =========================================
# CATEGORY SELECTION
# =========================================

def categories(request):

    return render(
        request,
        "game/categories.html"
    )


# =========================================
# DECISION MAKER
# =========================================

def decision_maker(request):

    return render(
        request,
        "game/decision_maker.html"
    )


# =========================================
# DIFFICULTY SELECTION
# =========================================

def difficulty(request):

    return render(
        request,
        "game/difficulty.html"
    )


# =========================================
# ACTUAL GAME
# =========================================

def game(request):

    return render(
        request,
        "game/game.html"
    )


# =========================================
# GET QUESTIONS
# =========================================

def get_questions(request):

    question_type = request.GET.get("type")

    categories = request.GET.get(
        "categories",
        request.GET.get(
            "category",
            ""
        )
    )

    difficulty = request.GET.get(
        "difficulty",
        "mixed"
    )

    # =====================================
    # CHECK QUESTION TYPE
    # =====================================

    if question_type not in [
        "truth",
        "dare"
    ]:

        return JsonResponse(
            {
                "error": "Invalid question type."
            },
            status=400
        )

    # =====================================
    # GET SELECTED CATEGORIES
    # =====================================

    selected_categories = [

        category.strip()

        for category in categories.split(",")

        if category.strip()

    ]

    # =====================================
    # BUILT-IN QUESTIONS
    # =====================================

    questions = Question.objects.filter(
        question_type=question_type,
        is_active=True
    )

    # =====================================
    # FILTER BUILT-IN BY CATEGORY
    # =====================================

    if selected_categories:

        questions = questions.filter(
            category__in=selected_categories
        )

    # =====================================
    # FILTER BUILT-IN BY DIFFICULTY
    # =====================================

    if difficulty in [
        "easy",
        "medium",
        "hard"
    ]:

        questions = questions.filter(
            difficulty=difficulty
        )

    # =====================================
    # CONVERT BUILT-IN QUESTIONS
    # =====================================

    data = [

        {
            "id": question.id,
            "category": question.category,
            "difficulty": question.difficulty,
            "text": question.text,
            "custom": False,
        }

        for question in questions
    ]

    # =====================================
    # USER CUSTOM QUESTIONS
    # =====================================

    if request.user.is_authenticated:

        custom_questions = CustomQuestion.objects.filter(
            user=request.user,
            question_type=question_type,
            is_active=True
        )

        # =================================
        # FILTER CUSTOM BY CATEGORY
        # =================================

        if selected_categories:

            custom_questions = custom_questions.filter(
                category__in=selected_categories
            )

        # =================================
        # FILTER CUSTOM BY DIFFICULTY
        # =================================

        if difficulty in [
            "easy",
            "medium",
            "hard"
        ]:

            custom_questions = custom_questions.filter(
                difficulty=difficulty
            )

        # =================================
        # ADD CUSTOM QUESTIONS
        # =================================

        data.extend(

            {
                "id": question.id,
                "category": question.category,
                "difficulty": question.difficulty,
                "text": question.text,
                "custom": True,
            }

            for question in custom_questions

        )

    # =====================================
    # RETURN JSON
    # =====================================

    return JsonResponse(
        {
            "questions": data
        }
    )


    # =====================================
    # CHECK QUESTION TYPE
    # =====================================

    if question_type not in [
        "truth",
        "dare"
    ]:

        return JsonResponse(
            {
                "error": "Invalid question type."
            },
            status=400
        )


    # =====================================
    # GET SELECTED CATEGORIES
    # =====================================

    selected_categories = [

        category.strip()

        for category in categories.split(",")

        if category.strip()

    ]


    # =====================================
    # GET ACTIVE QUESTIONS
    # =====================================

    questions = Question.objects.filter(
        question_type=question_type,
        is_active=True
    )


    # =====================================
    # FILTER BY CATEGORY
    # =====================================

    if selected_categories:

        questions = questions.filter(
            category__in=selected_categories
        )


    # =====================================
    # FILTER BY DIFFICULTY
    # =====================================

    if difficulty in [
        "easy",
        "medium",
        "hard"
    ]:

        questions = questions.filter(
            difficulty=difficulty
        )


    # =====================================
    # PREPARE DATA
    # =====================================

    data = [

        {
            "id": question.id,

            "category": question.category,

            "difficulty": question.difficulty,

            "text": question.text,

        }

        for question in questions

    ]


    # =====================================
    # RETURN JSON
    # =====================================

    return JsonResponse(
        {
            "questions": data
        }
    )


