# 💬 Python ChatBot — Rule-Based Chatbot

A simple **rule-based chatbot** written in Python for the **CodeAlpha Python Programming Internship (Task 1)**.

The chatbot replies to fixed messages like `hello`, `how are you` and `bye` using **predefined replies**. It is called *rule-based* because there is **no AI or machine learning** — the bot simply follows rules written with `if-elif`.

---

## 📌 Project Info

| | |
|---|---|
| **Task** | Task 1 — Basic Chatbot |
| **Domain** | Python Programming |
| **Organisation** | CodeAlpha |
| **Repo name** | `CodeAlpha_BasicChatbot` |
| **Language** | Python 3 |
| **Type** | Console chat (text only) |

---

## ✨ Features

| You type | Bot replies |
|---|---|
| `hello` / `hi` | Hi! Nice to meet you. |
| `how are you` / `how are you?` | I'm fine, Thanks! How are you? |
| `i am also fine` | Nice! Buddy, Always Be Happy 😊. |
| `what is your name` / `what is your name?` | I am a Python ChatBot. |
| `date and time please` | Shows the current date and time 🕒 |
| `bye` / `tata` | GoodBye! Have a nice day. *(and the chat closes)* |
| anything else | Sorry, I can't understand that. |

**Other good points:**

- 🔡 `.lower()` and `.strip()` are used, so `Hello`, `HELLO` and ` hello ` all work
- ❓ Works with and without a question mark (`how are you?`)
- 🔁 A `while True:` loop keeps the chat running until you say `bye` / `tata`
- 🛑 `break` closes the chat politely when you say bye
- 🤝 Never stays silent — every unknown message gets a polite reply
- 🕒 Uses the built-in `datetime` module, so **no extra library is needed**

---

## ▶️ How to Run

**1. Check that Python is installed:**

```bash
python --version
```

**2. Run the chatbot:**

```bash
python chatbot.py
```

> On Mac / Linux use `python3 chatbot.py`
> No installation needed — `datetime` is already part of Python.

---

## 🕹️ How to Use

1. Run the program — a welcome banner appears.
2. Type any message from the table above and press **Enter**.
3. The bot prints its reply.
4. Type **`bye`** or **`tata`** to end the chat.

---

## 🖥️ Sample Output

```
========================================
     Welcome Python ChatBot
     Type 'bye' or 'tata' to exit the chatBot
========================================

 You : hello
Bot : Hi! Nice to meet you.

 You : how are you
Bot : I'm fine, Thanks! How are you?

 You : i am also fine
Bot : Nice! Buddy, Always Be Happy 😊.

 You : what is your name?
Bot : I am a Python ChatBot.

 You : date and time please
2026-11-06 16:20:07.513484

 You : something random
Bot : Sorry, I can't understand that.

 You : bye
Bot : GoodBye! Have a nice day.
```

---

## 🧠 Python Concepts Used

| Concept | Where it is used |
|---|---|
| **Functions** | The whole chat is inside `def chatbot():`, and it is started by calling `chatbot()` |
| **`if-elif-else`** | Every rule is one `elif` — the bot checks the message from top to bottom |
| **Loops** | `while True:` keeps asking for messages again and again |
| **Input / Output** | `input()` takes the message, `print()` shows the reply |
| **Strings** | `.lower()` (makes `HELLO` = `hello`), `.strip()` (removes extra spaces), `==` for comparing text |
| **`or` operator** | `message == "bye" or message == "tata"` — either word closes the chat |
| **`break`** | Stops the `while` loop when the user says bye |
| **`import` + module** | `import datetime` → `datetime.datetime.now()` gives the real date and time |

---

## 📂 Code Structure

```
CodeAlpha_BasicChatbot/
│
├── chatbot.py     → the complete chatbot (single file)
└── README.md      → this file
```

**How the code flows:**

| Step | Line idea | Work |
|---|---|---|
| 1 | `import datetime` | Brings in the date/time tool |
| 2 | `def chatbot():` | All chat work is packed in one function |
| 3 | `print(...)` × 3 | Shows the welcome banner |
| 4 | `while True:` | Chat keeps running |
| 5 | `message = input(...).lower().strip()` | Takes input and cleans it (small letters, no extra spaces) |
| 6 | `if` / `elif` chain | Compares the message with fixed rules and prints the reply |
| 7 | `elif message == "bye" ...: break` | Ends the chat on bye / tata |
| 8 | `else:` | Polite reply for unknown messages |
| 9 | `chatbot()` | Calls the function so the program starts |

---

## 🔍 Understanding the main logic

```python
message = input("\n You : ").lower().strip()
```
One line does three jobs:
- `input()` → takes what the user typed
- `.lower()` → makes `Hello` into `hello` (so capital letters don't matter)
- `.strip()` → removes extra spaces from the start and end

```python
if message == "hello" or message == "hi":
    print("Bot : Hi! Nice to meet you.")
```
`==` compares two texts. `or` means "if either one is true". So typing `hello`
**or** `hi` gives the same reply.

```python
elif message == "how are you" or message == "how are you?":
```
Two versions are written because the user may type the question mark or not.

```python
elif message == "date and time please":
    print(datetime.datetime.now())
```
`datetime.datetime.now()` returns the **real** current date and time of the computer.

```python
elif message == "bye" or message == 'tata':
    print("Bot : GoodBye! Have a nice day.")
    break
```
`break` jumps out of the `while` loop, which ends the chat.

```python
else:
    print("Bot : Sorry, I can't understand that.")
```
If no rule matched, the bot still replies. A good chatbot **always** answers.

---

## 🚀 Future Improvements (ideas)

- Use `in` instead of `==` so a full sentence also matches:
  `if "hello" in message:` → then `hello there friend` will also work
- Format the date nicely using `strftime`:
  `datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p")` → `06-11-2026 04:20 PM`
- Add more rules: `joke`, `help`, `thanks`, `good morning`
- Remember the user's name ("My name is Rahul" → the bot remembers it)
- Save the full chat in a `chat_history.txt` file
- Convert it into a **web chatbot** using Flask

---

## 👩‍💻 Author

**Smeet Jariwala**
Python Programming Intern @ CodeAlpha
📧 smeetjariwala17@gmail.com
🔗 [LinkedIn](www.linkedin.com/in/smeet-jariwala-98b0043a5)

---

## 📜 Acknowledgement

Built as part of the **Python Programming Internship** at
[CodeAlpha](https://www.codealpha.tech) — www.codealpha.tech

⭐ If you liked this project, please give this repository a star!
