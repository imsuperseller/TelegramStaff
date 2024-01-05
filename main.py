import os
import logging
from telebot import TeleBot
import openai
import core_functions
import assistant

# Configure logging
logging.basicConfig(level=logging.INFO)

# Check OpenAI version compatibility
core_functions.check_openai_version()

# Initialize OpenAI client for GPT interactions
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("No OpenAI API key found in environment variables")

# Initialize the Telegram bot
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
if not TELEGRAM_TOKEN:
    raise ValueError("No Telegram token found in environment variables")

bot = TeleBot(TELEGRAM_TOKEN, parse_mode='Markdown')

# Initialize all available tools based on the tool configurations found in the directory
tool_data = core_functions.load_tools_from_directory('tools')

# Create or load an existing assistant
assistant_id = assistant.create_assistant()


# Handler for the '/start' command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your Lead Assistant. How can I assist you today?")


# Handler for all other messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    response = assistant.ask_assistant(assistant_id, message.text)
    bot.send_message(message.chat.id, response['message']['content'])


# Start the bot and continuously check for new messages
bot.polling()
