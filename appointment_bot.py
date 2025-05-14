from datetime import datetime
import re

class AppointmentBot:
    def __init__(self):
        self.responses = {
            'greeting': [
                "Hello! How can I assist you today?",
                "Hi there! How may I help you?",
                "Welcome! What can I do for you?"
            ],
            'booking_start': [
                "Sure! Please provide the date for your appointment (YYYY-MM-DD).",
                "I'll help you book an appointment. What date would you like? (YYYY-MM-DD)"
            ],
            'invalid_date': [
                "Please enter a valid date in YYYY-MM-DD format.",
                "That date format isn't correct. Please use YYYY-MM-DD format."
            ],
            'invalid_time': [
                "Please enter a valid time in HH:MM format (24-hour).",
                "That time format isn't correct. Please use HH:MM in 24-hour format."
            ],
            'invalid_email': [
                "Please enter a valid email address.",
                "That doesn't look like a valid email address. Please try again."
            ],
            'goodbye': [
                "Have a great day!",
                "Goodbye! Take care!",
                "See you later!"
            ]
        }
        self.step = 0
        self.appointment_date = ""
        self.appointment_time = ""
        self.email = ""

    def get_response(self, category):
        """Get a random response from the specified category"""
        import random
        return random.choice(self.responses[category])

    def validate_date(self, date_text):
        """Validate date format (YYYY-MM-DD)"""
        try:
            datetime.strptime(date_text, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def validate_time(self, time_text):
        """Validate time format (HH:MM)"""
        try:
            datetime.strptime(time_text, '%H:%M')
            return True
        except ValueError:
            return False

    def validate_email(self, email):
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    def process_input(self, user_input):
        """Process user input and return appropriate response"""
        if user_input.lower() == 'exit':
            return self.get_response('goodbye'), True

        if self.step == 0:
            if "book" in user_input.lower():
                self.step = 1
                return self.get_response('booking_start'), False
            else:
                return self.get_response('greeting'), False

        elif self.step == 1:
            if self.validate_date(user_input):
                self.appointment_date = user_input
                self.step = 2
                return "Got it. What time would you like to book? (HH:MM, 24-hour format)", False
            else:
                return self.get_response('invalid_date'), False

        elif self.step == 2:
            if self.validate_time(user_input):
                self.appointment_time = user_input
                self.step = 3
                return "Thank you! Please provide your email address.", False
            else:
                return self.get_response('invalid_time'), False

        elif self.step == 3:
            if self.validate_email(user_input):
                self.email = user_input
                self.step = 4
                return f"Your appointment is booked for {self.appointment_date} at {self.appointment_time}. We have sent a confirmation to {self.email}. Anything else I can help you with?", False
            else:
                return self.get_response('invalid_email'), False

        elif self.step == 4:
            if user_input.lower() in ['no', 'nothing', 'exit']:
                return self.get_response('goodbye'), True
            else:
                return self.get_response('greeting'), False

def main():
    print("Appointment Booking Chatbot\nType 'exit' to quit.")
    bot = AppointmentBot()
    
    while True:
        user_input = input("You: ")
        response, should_exit = bot.process_input(user_input)
        print("Bot:", response)
        
        if should_exit:
            break

if __name__ == "__main__":
    main() 