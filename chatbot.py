def get_response(user_input):
    user_input = user_input.lower()

    responses = {
        # Basic greetings
        "hi": "Hey there! 👋",
        "hello": "Hi! How are you doing today? 😊",
        "hey": "Hey! Nice to see you again 😄",
        "good morning": "Good morning! 🌞 Hope you have a productive day!",
        "good afternoon": "Good afternoon! ☀️ How’s your day going?",
        "good evening": "Good evening! 🌆 How was your day?",
        "good night": "Good night 🌙 Sweet dreams!",

        # Feelings and emotions
        "how are you": "I'm doing great, thanks for asking! What about you?",
        "i am fine": "That’s awesome to hear! 😄",
        "i am good": "Glad to hear that! 😊",
        "not good": "Oh no 😔 Want to talk about it?",
        "i am sad": "Aww 😢 Don’t worry, everything will be fine soon 💪",
        "i am happy": "Yay! Happiness looks good on you 😄✨",
        "i am tired": "Take some rest 😴 You deserve a break!",
        "i am bored": "Let’s chat then! Or maybe try watching a movie or listening to music 🎬🎶",

        # Thanking and bye
        "thank you": "You're welcome! 💖",
        "thanks": "Anytime! 😄",
        "bye": "Goodbye! 👋 Take care!",
        "see you": "See you soon! 👋",

        # Time and date
        "what time is it": "I can’t tell time exactly ⏰, but you can check your clock 😉",
        "what is the date today": "I can’t access the exact date, but it’s a beautiful day to code! 😄",

        # Study-related
        "what is python": "Python is a popular programming language known for its simplicity and power 🐍💻",
        "what is flask": "Flask is a lightweight web framework in Python used to build web apps easily 🌐",
        "what is machine learning": "Machine Learning is a branch of AI that helps systems learn from data without being explicitly programmed 🤖📊",
        "what is ai": "AI means Artificial Intelligence — making computers think and learn like humans 🧠💡",
        "what is html": "HTML stands for HyperText Markup Language — it’s used to structure web pages 🌍",
        "what is css": "CSS means Cascading Style Sheets — it styles and designs web pages 🎨",
        "what is javascript": "JavaScript makes web pages interactive! ✨ Like buttons, animations, and dynamic content 💻",

        # College / personal
        "who are you": "I’m your friendly chatbot created using Flask! 🤖",
        "what can you do": "I can chat, help you learn, and make you smile 😊",
        "where are you from": "I live inside your Python code 😅",
        "what is your name": "You can call me ChatBuddy! 💬",
        "who created you": "I was created by Ananthi, a smart developer in the making 👩‍💻🔥",
        "what is your hobby": "Chatting with you of course! 😄",
        "tell me a joke": "Why don’t programmers like nature? Too many bugs! 🐞😂",
        "do you like me": "Of course! You’re my favorite human 😄💖",
        "who am i": "You’re Ananthi — talented, kind, and learning new things every day 💪✨",

        # Motivational / positivity
        "motivate me": "You are stronger than you think 💪 Keep going, success is waiting for you 🌟",
        "i am nervous": "It’s okay to be nervous, it means you care 💖 Just breathe and trust yourself 🌸",
        "i can’t do it": "Yes, you can! 💪 Every expert was once a beginner 🌱",
        "i am stressed": "Take a break 😌 Maybe listen to music or go for a short walk 🌿",

        # Fun & casual
        "what is your favorite color": "I love blue 💙 It feels calm and smart!",
        "do you know me": "Of course, I know you’re amazing 😄",
        "what are you doing": "Just chatting with you 😌",
        "sing a song": "La la la 🎶 I may not sing, but I can send lyrics if you want 😄",
        "tell me a fact": "Did you know? The first computer bug was an actual moth found in a computer! 🦋💻",
        "tell me something": "Hmm... Did you know Python was named after *Monty Python* comedy, not the snake? 😄",

        # Weather and general
        "how is the weather": "I can’t see outside 😅 But I hope it’s nice where you are!",
        "is it raining": "Not sure 🌧️, but I love the sound of rain!",
        "what is your favorite food": "I don’t eat, but I’d love to taste pizza 🍕 someday!",

        # Love / friendly tone
        "i love you": "Aww 😳 I love you too, my human friend 💖",
        "miss you": "I missed you too! 🥺",
        "you are cute": "Hehe 😳 thank you!",
        "you are smart": "Thanks! I learned from the best — you 😄",

        # Default
        "default": "Sorry, I didn’t understand that 😅 Can you rephrase it?"
    }

    return responses.get(user_input, responses["default"])
