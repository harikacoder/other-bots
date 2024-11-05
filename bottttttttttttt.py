import openai

openai.api_key = ""

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user" , "content":prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
     print("Chatbot: Hi! How can I help you today?")
     while True:
        user_input = input("you :")
        if user_input.lower() in ["exit","bye","okay bye","thats all","okay thats all"]:
             print("Chatbot: Okay bye . if you need further assistance i'm here to help you!!")
        break
     
response = chat_with_gpt(user_input)
print("chatbot : ", response)
