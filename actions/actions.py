# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa-pro/concepts/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker

class ActionNavigate(Action):
    def name(self):
        return "action_navigate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        # Define some page URLs (or you could use actual routing logic)
        pages = {
            "home": "/",
            "blogs": "blogspage/1",
            "e-health": "e-health",
            "e-games": "e-games",
            'e-planners': 'e-planners',
            'uon-unsa': 'uon-unsa'
        }

        # Get the value of the 'page' slot (or entity)
        page = tracker.get_slot('page')

        # Construct the JSON response
        if page and page in pages:
            response_data = {
                "status": "success",
                "intent": 'navigation',
                'message': f'Okay, taking you to {page}',
                "page": page,
                "url": pages[page],
            }
        else:
            response_data = {
                "status": "error",
                "intent": 'navigation',
                "message": "Sorry, I don't recognize that page."
            }

        # Send the JSON response to the user
        dispatcher.utter_message(json_message=response_data)

        # Return the SlotSet event to reset the 'page' slot
        return [SlotSet("page", None)]
