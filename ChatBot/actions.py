import json
from pathlib import Path
from typing import Any, Text, Dict, List
from unittest.util import strclass

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase

from bargain_logic import bargainAmt


class ActionNegotiate(Action):
    def name(self) -> str:
        return "action_counter_offer"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        min_price, max_price = float(tracker.get_slot("min_price")), float(
            tracker.get_slot("max_price"))
        for each in tracker.latest_message["entities"]:
            if each["entity"] == "user_offer":
                user_offer = float(each["value"])
                counter_offer = bargainAmt(min_price, max_price, user_offer)
                dispatcher.utter_message(
                    text=f"Here is our counter-offer: {counter_offer}")
            #     return []
            # else:
            #     dispatcher.utter_message(
            #         text=f"Please enter a valid value")
        return []


# class ActionDealAcceptReject(Action):
#     def name(self) -> str:
#         return "action_reject_accept_offer"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Do magic stuff after user accepts offer
#         for each in tracker.latest_message["entities"]:
#             if each["entity"] == "accept_offer":
#                 accept_offer = each["value"]
#                 if accept_offer == "Y":
#                     dispatcher.utter_message(
#                         text=
#                         "Thank you for your business, we will now update the basket"
#                     )
#                 else:
#                     dispatcher.utter_message(
#                         text=
#                         "Ok, please provide a counter_offer to our offer above."
#                     )

#         return []
