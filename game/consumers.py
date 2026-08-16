import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from .models import OnlineRoom


class GameConsumer(AsyncWebsocketConsumer):

    # =========================================
    # CONNECT
    # =========================================

    async def connect(self):

        self.room_code = (
            self.scope["url_route"]["kwargs"]["room_code"]
        )

        self.room_group_name = (
            f"game_{self.room_code}"
        )

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()


        # =====================================
        # SEND CURRENT PLAYERS
        # =====================================

        players = await self.get_players()

        await self.send(
            text_data=json.dumps({

                "type": "players_update",

                "players": players

            })
        )


    # =========================================
    # DISCONNECT
    # =========================================

    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    # =========================================
    # RECEIVE MESSAGE
    # =========================================

    async def receive(
        self,
        text_data
    ):

        try:

            data = json.loads(
                text_data
            )

        except json.JSONDecodeError:

            return


        action = data.get(
            "action"
        )


        # =====================================
        # PLAYER JOINED
        # =====================================

        if action == "player_joined":

            await self.channel_layer.group_send(

                self.room_group_name,

                {
                    "type":
                        "players_changed"
                }

            )


        # =====================================
        # START GAME
        # =====================================

        elif action == "start":

            await self.start_game()


            await self.channel_layer.group_send(

                self.room_group_name,

                {
                    "type":
                        "game_started"
                }

            )


        # =====================================
        # DONE
        # =====================================

        elif action == "done":

            await self.channel_layer.group_send(

                self.room_group_name,

                {
                    "type":
                        "turn_completed"
                }

            )


        # =====================================
        # SKIP
        # =====================================

        elif action == "skip":

            await self.channel_layer.group_send(

                self.room_group_name,

                {
                    "type":
                        "question_skipped"
                }

            )


    # =========================================
    # PLAYERS CHANGED
    # =========================================

    async def players_changed(
        self,
        event
    ):

        players = await self.get_players()


        await self.send(

            text_data=json.dumps({

                "type":
                    "players_update",

                "players":
                    players

            })

        )


    # =========================================
    # GAME STARTED
    # =========================================

    async def game_started(
        self,
        event
    ):

        # Get the latest players
        # from the database

        players = await self.get_players()


        # Send players together
        # with the game_started event

        await self.send(

            text_data=json.dumps({

                "type":
                    "game_started",

                "players":
                    players

            })

        )


    # =========================================
    # TURN COMPLETED
    # =========================================

    async def turn_completed(
        self,
        event
    ):

        await self.send(

            text_data=json.dumps({

                "type":
                    "turn_completed"

            })

        )


    # =========================================
    # QUESTION SKIPPED
    # =========================================

    async def question_skipped(
        self,
        event
    ):

        await self.send(

            text_data=json.dumps({

                "type":
                    "question_skipped"

            })

        )


    # =========================================
    # GET PLAYERS
    # =========================================

    @database_sync_to_async
    def get_players(self):

        room = OnlineRoom.objects.filter(
            room_code=self.room_code
        ).first()


        if not room:

            return []


        return room.players


    # =========================================
    # START GAME IN DATABASE
    # =========================================

    @database_sync_to_async
    def start_game(self):

        room = OnlineRoom.objects.filter(
            room_code=self.room_code
        ).first()


        if room:

            room.game_started = True

            room.save(
                update_fields=[
                    "game_started"
                ]
            )