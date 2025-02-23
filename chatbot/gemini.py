from google import genai
from google.genai import types

conversation_history = []

MAX_TOKENS = 100 

def count_tokens(text: str) -> int:
   
    return len(text.split())

def trim_history(history: list, max_tokens: int) -> list:

    while history and count_tokens("\n".join(history)) > max_tokens and len(history) > 1:
        history.pop(0)
    return history

def get_response(user_input: str) -> str:
    global conversation_history

    sys_instruct = (
        "You are a helpful medical diagnosis assistant. "
        "Ask clarifying questions when needed and provide diagnostic options."
    )
    
    conversation_history.append("User: " + user_input)
    
    conversation_history = trim_history(conversation_history, MAX_TOKENS)
    
    prompt = "\n".join(conversation_history)
    
    client = genai.Client(api_key="")
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt],
        config=types.GenerateContentConfig(
            system_instruction=sys_instruct,
            max_output_tokens=500,
            temperature=0.1
        )
    )
    
    assistant_reply = response.text.strip()
    conversation_history.append("Assistant: " + assistant_reply)
    
    conversation_history = trim_history(conversation_history, MAX_TOKENS)
    
    return assistant_reply


