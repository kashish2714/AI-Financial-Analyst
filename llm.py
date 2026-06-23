import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)


def generate_ai_insight(stock_data, prediction, confidence):
    prompt = f"""
    Stock: {stock_data['ticker']}
    Price: {stock_data['price']}
    Prediction: {prediction}
    Confidence: {confidence}%

    Give a short financial analyst report explaining why this prediction happened.
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
