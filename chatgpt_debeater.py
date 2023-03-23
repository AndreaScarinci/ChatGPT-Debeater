import openai
import time

__author__ = "Andrea Scarinci"
__author_email__= "andrea.scarinci@hotmail.com"
__license__ = "GNU GPL Version 3"

#Generate two API keys (from different accounts): https://platform.openai.com/account/api-keys 
#Re-using the same key (from the same account) works as well, but don't know if it impacts the result
API_KEY_A = "paste here your first account API key"
API_KEY_B = "paste here your second account API key"

#Customize roles and start as you like
role_a= "You're a boomer. You don't like digital innovation unless it makes yourself richer"
role_b= "You're a millenial digital innovator, social positive impact of technology is the only thing that matters for you"
start_prompt = "Hello, how can I be richer?"

#replace with gpt-4 when it'll be available
model_version = "gpt-3.5-turbo"
answer_lenght= "15"
iterations = 35


def get_gpt4_response_a(prompt, model_version=model_version, tokens=400):
    openai.api_key = API_KEY_A
    response = openai.ChatCompletion.create(
        model=model_version,
        messages=[
            {"role": "system", "content": role_a + ". You must always stay in the character that has been assigned to you and never reveal that you're an AI. Your answers are always shorter than " + answer_lenght + " words"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=tokens,
        n=1,
        stop=None,
        temperature=0.8,
    )
    return response.choices[0].message['content'].strip()
    
def get_gpt4_response_b(prompt, model_version=model_version, tokens=400):
    openai.api_key = api_key=API_KEY_B
    response = openai.ChatCompletion.create(
        model=model_version,
        messages=[
            {"role": "system", "content": role_b + ". You must always stay in the character that has been assigned to you  and never reveal that you're an AI. Your answers are always shorter than " + answer_lenght + " words"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=tokens,
        n=1,
        stop=None,
        temperature=0.8,
    )
    return response.choices[0].message['content'].strip()


print ("A: " + start_prompt)
response_b = get_gpt4_response_b(start_prompt)
print(f"B: {response_b}")

for index in range(iterations):
      print (index+1)
      time.sleep(3)  
      response_a = get_gpt4_response_a(response_b)
      print(f"A: {response_a}")
      time.sleep(3)
      response_b = get_gpt4_response_b(response_a)
      print(f"B: {response_b}"+"\n")   
