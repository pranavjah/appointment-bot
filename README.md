# Appointment Booking Chatbot 🤖

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

A Python-based appointment booking chatbot that helps businesses automate appointment scheduling with minimal deployment complexity.

## ✨ Features

- 🤖 User-friendly conversation flow for booking appointments
- 📅 Collects essential details: date, time, and user contact information
- ✅ Simple validation of input data
- 📧 Basic appointment confirmation message
- 🔄 Easy to extend for integration with calendar APIs
- 🚀 Minimal dependencies for straightforward deployment
- 💻 Text-based interface suitable for web or messaging platforms

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/pranavjah/appointment-bot.git
cd appointment-bot
```

2. Create a virtual environment:
```bash
python -m venv chatbot-env
source chatbot-env/bin/activate  # Linux/macOS
chatbot-env\Scripts\activate     # Windows
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## 💻 Usage

Run the chatbot:
```bash
python appointment_bot.py
```

### Example Conversation

```
Appointment Booking Chatbot
Type 'exit' to quit.
You: Hi
Bot: Hello! How can I assist you today?
You: I want to book an appointment
Bot: Sure! Please provide the date for your appointment (YYYY-MM-DD).
You: 2024-03-20
Bot: Got it. What time would you like to book? (HH:MM, 24-hour format)
You: 14:30
Bot: Thank you! Please provide your email address.
You: user@example.com
Bot: Your appointment is booked for 2024-03-20 at 14:30. We have sent a confirmation to user@example.com. Anything else I can help you with?
You: No
Bot: Have a great day!
```

## 📋 Input Format

- Date: YYYY-MM-DD (e.g., 2024-03-20)
- Time: HH:MM in 24-hour format (e.g., 14:30)
- Email: Valid email address format

## 🛠️ Dependencies

- Python 3.x
- ChatterBot
- Flask (optional, for web deployment)

## 🔮 Future Improvements

- Integration with calendar APIs (Google Calendar, Calendly)
- Web interface using Flask
- Database storage for appointments
- Enhanced NLP capabilities
- Integration with messaging platforms

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Pranav Jahagirdar** - *Initial work* - [pranavjah](https://github.com/pranavjah)

## 🙏 Acknowledgments

- Thanks to all contributors who have helped shape this project
- Inspired by the need for simple appointment scheduling solutions 