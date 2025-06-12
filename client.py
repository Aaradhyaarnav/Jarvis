import google.generativeai as genai

genai.configure(api_key="YOUR API KEY HERE")

model = genai.GenerativeModel('gemini-2.0-flash')

def aiProcess(command):
    response = model.generate_content([
        f"You are Jarvis, a virtual assistant. Give short, simple,easy-to-understand and smart answers. No long paragraphs.",
        f"User asked: {command}"
    ],
    generation_config=genai.types.GenerationConfig(
        temperature=0.7,
        max_output_tokens=250
    ))

    return response.text

# You can delete this test code now:
# response = model.generate_content("Hello, what is coding?")
# print(response.text)
