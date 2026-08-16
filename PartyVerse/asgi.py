"""
ASGI config for PartyVerse project.
"""

import os


# =========================================
# DJANGO SETTINGS
# =========================================

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "PartyVerse.settings"
)


# =========================================
# DJANGO ASGI APPLICATION
# =========================================

from django.core.asgi import get_asgi_application

django_asgi_app = get_asgi_application()


# =========================================
# STATIC FILES
# =========================================

from django.contrib.staticfiles.handlers import (
    ASGIStaticFilesHandler
)


# =========================================
# CHANNELS
# =========================================

from channels.routing import (
    ProtocolTypeRouter,
    URLRouter
)

from channels.auth import AuthMiddlewareStack

import game.routing


# =========================================
# APPLICATION
# =========================================

application = ProtocolTypeRouter({

    # =====================================
    # HTTP
    # =====================================

    "http": ASGIStaticFilesHandler(
        django_asgi_app
    ),


    # =====================================
    # WEBSOCKET
    # =====================================

    "websocket": AuthMiddlewareStack(

        URLRouter(
            game.routing.websocket_urlpatterns
        )

    ),

})