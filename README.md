# Telegram Bot
# Movies & Series Approval Bot

🎬 **Movies & Series Approval Bot**  
A Telegram bot to help group members submit their requests for movies and series approvals efficiently. This bot is designed to streamline the process of receiving, managing, and reviewing requests within a group.

---

## Features
- 📩 **Submit Requests**: Users can submit their requests using the keywords `#request` or `request`.
- ✅ **Request Management**: All requests are logged and can be accessed by the bot owner.
- 🛡️ **Admin Access**: Only the bot owner can view the list of submitted requests.
- 🤝 **User-friendly Commands**:
  - `/start` – Provides information about the bot and how to use it.
  - `/requests` – Allows the bot owner to view all submitted requests.

---

## Setup Instructions

### Prerequisites
- Python 3.10 or higher
- `python-telegram-bot` library (`v20.x` or later)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/movies-series-approval-bot.git
   cd movies-series-approval-bot
````

2. **Install Dependencies**:

   ```bash
   pip install python-telegram-bot
   ```

3. **Configure the Bot**:

   * Open the script file and replace the following placeholders:

     * `BOT_TOKEN`: Add your Telegram bot token.
     * `BOT_OWNER_ID`: Add your Telegram ID.

4. **Run the Bot**:

   ```bash
   python bot.py
   ```

---

## Commands

### User Commands

* `/start`: Displays a welcome message and usage instructions.
* `#request` or `request`: Submit a request for movies or series approvals.

### Admin Commands

* `/requests`: Displays the list of all submitted requests. Only accessible by the bot owner.

---

## Bot Workflow

1. **User Submission**:

   * A user sends a message containing the keywords `#request` or `request`.
   * The bot processes the message, logs the request, and notifies the user that their request has been received.

2. **Admin Review**:

   * The bot owner uses the `/requests` command to view all submitted requests.
   * Requests are displayed with the submitter's username and request details.

---

## Example Usage

### User Interaction

* **Message**:
  `#request Approval for The Matrix movie`
* **Bot Reply**:
  `✅ Your request has been received. An admin will review it shortly.`

### Admin Interaction

* **Command**:
  `/requests`
* **Bot Reply**:

  ```
  📌 **Submitted Requests:**

  1. From: john_doe
     Request: Approval for The Matrix movie

  2. From: jane_smith
     Request: Request approval for Breaking Bad series
  ```

---

## Logging and Debugging

* Logs are written to the console for easy debugging.
* Errors are handled gracefully, with user-friendly messages displayed in case of issues.

---

## Contributions

Feel free to fork the repository and submit pull requests to improve the bot. Suggestions and feature requests are also welcome.

---

## License

This project is licensed under the MIT License.

```

