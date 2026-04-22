import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

conversation_history = [
    {"role": "system", "content": "You are a smart AI desktop assistant like Jarvis. Answer briefly in 4–5 lines."}
]

def get_ai_response(user_input):
    try:
        conversation_history.append(
            {"role": "user", "content": user_input}
        )
        
        if len(conversation_history) > 10:
            conversation_history.pop(1)

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=conversation_history
        )

        reply = response.choices[0].message.content

        conversation_history.append(
            {"role": "assistant", "content": reply}
        )

        print("AI Reply:", reply)

        return reply

    except Exception as e:
        print("AI ERROR:", e)
        return "Sorry, I am having trouble connecting to the AI service."