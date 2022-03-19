import json
from pathlib import Path
from typing import Any, Text, Dict, List
from unittest.util import strclass

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase

from bargain_logic import bargainAmt


class ActionCheckExistence(Action):
    knowledge = Path("data/pokemon_name.txt").read_text().split("\n")

    def name(self) -> Text:
        return "action_check_existence"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print(domain["slots"]["min_price"])
        for blob in tracker.latest_message['entities']:
            # print(tracker.latest_message)
            if blob['entity'] == 'pokemon_name':
                name = blob['value']
                if name in self.knowledge:
                    dispatcher.utter_message(text=f"Yes, {name} is a pokemon.")
                else:
                    dispatcher.utter_message(
                        text=
                        f"I do not recognize {name}, are you sure it is correctly spelled?"
                    )
        return []


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
                print(min_price)
                print(user_offer)
                counter_offer = bargainAmt(min_price, max_price, user_offer)
                dispatcher.utter_message(
                    text=f"Here is our counter-offer: {counter_offer}")
        return []


class ActionDealAcceptReject(Action):
    def name(self) -> str:
        return "action_reject_accept_offer"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Do magic stuff after user accepts offer
        for each in tracker.latest_message["entities"]:
            if each["entity"] == "accept_offer":
                accept_offer = each["value"]
                if accept_offer == "Y":
                    dispatcher.utter_message(
                        text=
                        "Thank you for your business, we will now update the basket"
                    )
                else:
                    dispatcher.utter_message(
                        text=
                        "Ok, please provide a counter_offer to our offer above."
                    )

        return []


class MyKnowledgeBaseAction(ActionQueryKnowledgeBase):
    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("data/pokemondb.json")
        super().__init__(knowledge_base)
