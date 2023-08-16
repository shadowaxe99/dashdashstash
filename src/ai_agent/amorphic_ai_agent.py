from ai_agent.communication_manager import CommunicationManager
from ai_agent.data_manager import DataManager
from ai_agent.decision_maker import DecisionMaker
from ai_agent.chief_of_staff import ChiefOfStaff
from ai_agent.voice_processor import VoiceProcessor
from ai_agent.user_interface import UserInterface
from ai_agent.group_text_conversations import GroupTextConversations
from ai_agent.chat_processor import ChatProcessor
from ai_agent.email_processor import EmailProcessor

class AmorphicAIAgent(CommunicationManager, DataManager, DecisionMaker, ChiefOfStaff):
    def __init__(self):
        super().__init__()

    def interact_with_user(self):
        user_input = self.get_user_input()
        if user_input.startswith('voice'):
            voice_processor = VoiceProcessor()
            voice_data = voice_processor.record_voice()
            text_data = voice_processor.convert_to_text(voice_data)
            response = self.generate_response(text_data)
            self.send_message(response)
        elif user_input.startswith('chat'):
            chat_processor = ChatProcessor()
            chat_data = chat_processor.process_chat()
            response = self.generate_response(chat_data)
            self.send_message(response)
        elif user_input.startswith('email'):
            email_processor = EmailProcessor()
            email_data = email_processor.fetch_emails()
            response = self.generate_response(email_data)
            self.send_message(response)
        else:
            user_interface = UserInterface()
            text_data = user_interface.get_user_input()
            response = self.generate_response(text_data)
            self.send_message(response)

    def generate_response(self, input_data):
        decision_maker = DecisionMaker()
        decision = decision_maker.make_decision(input_data)
        return decision
