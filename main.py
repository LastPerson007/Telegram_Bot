import logging
import re
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)
import os  # For accessing environment variables

# Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token_here")
BOT_OWNER_ID = int(os.getenv("BOT_OWNER_ID", "0"))  # Replace with the owner's Telegram ID or set as an environment variable

# Storage for requests
requests_list = []

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles the /start command. Introduces the bot and provides details about its functionality.
    """
    await update.message.reply_text(
        "🎬 Welcome to the Movies & Series Approval Bot!\n\n"
        "This bot helps group members submit their requests for movies and series approvals to admins efficiently.\n\n"
        "📌 **Features:**\n"
        "- Submit your requests using `#request` or `request` in your message.\n"
        "- @Netflixian_Movie will review and approve your requests.\n\n"
        "💡 **Examples:**\n"
        "`#request Approval for The Matrix movie.`\n"
        "`Request approval for Breaking Bad series.`\n\n"
        "For any issues, please contact the admin. 🚀"
    )

async def process_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles messages containing `#request` or `request` keywords.
    """
    try:
        msg = update.message
        user = msg.from_user

        # Ensure the message has text
        if not msg.text:
            return

        # Check if the message contains `#request` or `request`
        if re.search(r'(?i)(#request|\brequest\b)', msg.text):
            # Extract and clean the request content
            cleaned_text = re.sub(r'(?i)(#request|\brequest\b)', '', msg.text).strip()

            # Default response if no specific content is provided
            if not cleaned_text:
                cleaned_text = "No specific details provided."

            # Save the request
            requests_list.append({
                "user_id": user.id,
                "username": user.username or user.first_name or "Anonymous User",
                "request": cleaned_text
            })

            logging.info(f"Received request from {user.username or user.first_name}: {cleaned_text}")

            # Notify the user
            await msg.reply_text(
                "✅ Your request has been received. An admin will review it shortly."
            )

    except Exception as e:
        logging.error(f"Error while processing request: {e}")
        await update.message.reply_text(
            "⚠️ Sorry, there was an error processing your request. Please try again later."
        )

async def view_requests(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Allows the bot owner to view all submitted requests.
    """
    user = update.message.from_user

    # Check if the user is the bot owner
    if user.id != BOT_OWNER_ID:
        await update.message.reply_text("❌ You are not authorized to access this information.")
        return

    # Format the requests for the owner
    if not requests_list:
        await update.message.reply_text("📂 No requests have been submitted yet.")
        return

    response = "📌 **Submitted Requests:**\n\n"
    for idx, req in enumerate(requests_list, start=1):
        response += f"{idx}. From: {req['username']}\n   Request: {req['request']}\n\n"

    # Split response if it's too long
    response_chunks = [response[i:i+4000] for i in range(0, len(response), 4000)]
    for chunk in response_chunks:
        await update.message.reply_text(chunk)

def main():
    """
    Main function to set up and run the Telegram bot.
    """
    try:
        # Build the bot application
        app = ApplicationBuilder().token(BOT_TOKEN).build()

        # Add command handler for /start
        app.add_handler(CommandHandler("start", start_command))

        # Add command handler for /requests (for bot owner only)
        app.add_handler(CommandHandler("requests", view_requests))

        # Add a message handler to process text messages
        app.add_handler(MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            process_request
        ))

        # Start the bot
        logging.info("Bot is running...")
        app.run_polling()

    except Exception as e:
        logging.critical(f"Critical error: {e}")

if __name__ == "__main__":
    main()
