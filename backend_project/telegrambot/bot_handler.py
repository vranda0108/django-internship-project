import logging
import os
import sys
import django
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from django.contrib.auth.models import User
from django.utils import timezone

# Django setup
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_project.settings')
django.setup()

from telegrambot.models import UserProfile, TelegramUser

# Load .env file
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Read the Telegram token securely
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def start(update: Update, context: CallbackContext):
    chat = update.effective_chat
    user = update.effective_user

    telegram_user, created = TelegramUser.objects.update_or_create(
        telegram_id=user.id,
        defaults={
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "created_at": timezone.now(),
        }
    )

    response = f"""👋 Hello {user.first_name or 'there'}!
Here's your profile info:
🆔 Telegram ID: {user.id}
👤 Username: @{user.username if user.username else 'Not set'}
📛 First Name: {user.first_name}
🧾 Last Name: {user.last_name if user.last_name else 'Not provided'}
    """

    context.bot.send_message(chat_id=chat.id, text=response)

def main():
    if not TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN not found in environment variables.")
        return

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

def register_telegram_user(user_id, telegram_username):
    try:
        user = User.objects.get(id=user_id)
        profile, created = UserProfile.objects.get_or_create(user=user)
        profile.telegram_username = telegram_username
        profile.save()
    except User.DoesNotExist:
        pass
