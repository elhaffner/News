import google.generativeai as genai

api_key = "AIzaSyAZ_y74Vwb453PU4VKuooxpwlhbB0uEL7o"
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)
