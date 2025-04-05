import os
import re
import json
from google import genai

def gen():
    API_KEY = os.getenv("GEMINI_KEY")
    client = genai.Client(api_key=API_KEY)


    prompt = (
        "Suggest **unique and diverse** travel destinations across India for a decentralized travel app. "
        "Each response should **include different states and regions** to ensure variety. "
        "Include both **well-known tourist attractions** and **hidden gems** that are not commonly suggested. "
        "Return the suggestions as an array of JSON objects, with the following fields: \n"
        "- **id** (string) \n"
        "- **name** (string) \n"
        "- **description** (string) \n"
        "- **location** (state or region in India) \n"
        "- **category** (e.g., Mountain, Beach, Historic Site, Wildlife, etc.) \n"
        "- **image_url** (high-quality image link from Unsplash, Pexels, or an official tourism website) \n"
        "- **rating** (number between 1.0 and 5.0) \n"
        "- **website** (official tourism website if available) \n"
        "- **price_inr** (estimated cost range in INR) \n"
        "- **distance_from_delhi_km** (approximate distance from Delhi) \n"
        "- **coordinates**: {latitude (float), longitude (float)} \n"
        "Ensure that **each response includes different states and avoids repetition**. "
        "Format the response as **valid JSON**."
    )


    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config={"temperature": 1.0} 
    )
    
    raw_text = response.text
    print("Raw Gemini response:", raw_text)
    
    # Use regex to extract the JSON content if it is enclosed in triple backticks.
    match = re.search(r"```json\s*(.*?)\s*```", raw_text, re.DOTALL)
    if match:
        json_text = match.group(1)
    else:
        json_text = raw_text.strip()

    if not json_text:
        raise ValueError("No JSON content found in Gemini response.")
    
    suggestions = json.loads(json_text)

    return suggestions

