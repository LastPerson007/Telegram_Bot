# Telegram Bot
# Movies & Series Approval Bot 🎬

A Telegram bot designed to help group members submit requests for movies and series approvals efficiently. This bot streamlines the process of receiving, managing, and reviewing requests within a group.

---

## Features 🚀

- **Submit Requests**: Users can submit their requests using `#request` or `request` in their messages.
- **Admin Access**: Only the bot owner can view all submitted requests using a dedicated command.
- **User-Friendly Commands**:
  - `/start` – Provides information about the bot and its functionality.
  - `/requests` – Allows the bot owner to view all submitted requests.
- **Efficient Request Management**: The bot stores requests temporarily in memory for quick access.

---

## 📚 How It Works

1. **User Interaction**:
   - Users send messages with `#request` or `request` followed by their request details.
   - The bot logs the request and confirms it to the user.

2. **Admin Interaction**:
   - The bot owner uses the `/requests` command to view all submitted requests.
   - Requests include details such as the username and the request message.

---

## Setup Instructions 🛠️

### Prerequisites

- Python 3.10 or higher.
- `python-telegram-bot` library (`v20.x` or later).

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/LastPerson07/Telegram_Bot.git
   cd Telegram_Bot
````

2. **Install Dependencies**:

   ```bash
   pip install python-telegram-bot
   ```

3. **Configure the Bot**:

   * Open the `bot.py` file and update the following placeholders:

     * `BOT_TOKEN`: Replace with your bot token (obtained from @BotFather on Telegram).
     * `BOT_OWNER_ID`: Replace with your Telegram user ID (obtainable from a bot like @userinfobot).

4. **Run the Bot**:

   ```bash
   python bot.py
   ```

5. **Keep the Bot Running**:

   * Use a process manager like `screen` or `tmux`, or host it on platforms like Replit, Heroku, or Railway.

---

## Commands ✍️

### User Commands

* `/start`: Displays a welcome message and instructions on how to use the bot.
* `#request` or `request`: Users submit their requests for movies or series.

### Admin Commands

* `/requests`: Displays a list of all submitted requests. **Only accessible by the bot owner.**

---

## Example Usage 💡

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

## Logging and Debugging 📝

* The bot uses `logging` to record activity and errors.
* Logs are written to the console, making it easy to debug issues.
* Errors are gracefully handled with user-friendly messages.

---

## Customization ⚙️

Feel free to modify the following parts of the bot:

1. **Features**:

   * Add additional commands or features like editing requests or sending notifications.
2. **Storage**:

   * Currently, requests are stored in memory. You can integrate a database (e.g., SQLite or Firebase) for persistent storage.
3. **Styling**:

   * Update the bot messages to fit your group's tone and preferences.

---

## Contributing 🤝

We welcome contributions to improve this bot.
If you have ideas or find bugs, feel free to:

* Fork this repository.
* Create a pull request with your changes.
* Submit issues or feature requests.

### Repository Link:

[Telegram\_Bot by LastPerson007](https://github.com/LastPerson07/Telegram_Bot)

---

## License 📜

This project is licensed under the MIT License.
You are free to use, modify, and distribute this bot as per the terms of the license.

---

Happy Botting! 🤖🎥

```

