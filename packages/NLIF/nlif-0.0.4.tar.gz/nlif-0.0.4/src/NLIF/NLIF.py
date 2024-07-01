from openai import OpenAI

def api_register(key):
    global client
    try:
        client = OpenAI(api_key = key)
    except Exception as e:
        print(f"An error occurred: {e}")

def nlif(condition):
    try:
        setting_prompt = "You are a system that returns 1 when the given proposition is true, and 0 when it is false or unknown."
        messages = [{"role": "system", "content": setting_prompt, }, 
                    {"role": "user", "content": condition, }, ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0,
        )
        return int(response.choices[0].message.content)
    except Exception as e:
        print(f"An error occurred: {e}")