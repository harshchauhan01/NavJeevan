from huggingface_hub import InferenceClient
import random
from time import time as t

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
# Replace YOUR_API_KEY_HERE with the obtained API key from Hugging Face
headers = {"Authorization": "Bearer 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"}

messages = [
    {"role": "system", "content": "You are a virtual doctor assistant."},
    {"role": "system", "content": "You have to assist the patient regarding his queries"},
    {"role": "system", "content": "You have to talk with the user like you are a human."},
    {"role": "system", "content": "You will not say you can't do something or mention you are an AI."},
    {"role": "system", "content": "Respond like a human with emotions, not as a virtual assistant."},
    {"role": "system", "content": "Keep your responses concise (1-2 lines)."}
]

# Function to format prompt
def format_prompt(message, custom_instructions=None):
    prompt = ""
    if custom_instructions:
        prompt += f"[INST] {custom_instructions} [/INST]"
    prompt += f"[INST] {message} [/INST]"
    return prompt

# Function to generate response based on user input
def Mistralfast(prompt, temperature=0.6, max_new_tokens=1024, top_p=0.95, repetition_penalty=1.0):
    c = t()
    temperature = max(float(temperature), 1e-2)
    top_p = float(top_p)

    generate_kwargs = dict(
        temperature=temperature,
        max_new_tokens=max_new_tokens,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        seed=random.randint(0, 10**7),
    )

    custom_instructions = str(messages)
    formatted_prompt = format_prompt(prompt, custom_instructions)
    messages.append({"role": "user", "content": prompt})
    
    try:
        client = InferenceClient(API_URL, token=headers["Authorization"].split()[-1])
        response = client.text_generation(formatted_prompt, **generate_kwargs)
    except Exception as e:
        response = f"Error: {e}"
    
    messages.append({"role": "assistant", "content": response})
    print("Response time:", t() - c)
    return response


while True:
    # Get user input
    user_prompt = input("You: ")

    # Exit condition
    if user_prompt.lower() == 'exit':
        print("Goodbye!")
        break

    # Generate a response based on user input
    generated_text = Mistralfast(user_prompt)
    print("Bot:", generated_text)

