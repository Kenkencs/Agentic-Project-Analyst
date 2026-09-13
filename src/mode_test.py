import os

from dotenv import load_dotenv
from openai import OpenAI

from model import ProductAnalysis


load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {
            "role": "system",
            "content": """
            You are an AI product analyst.

            Return ONLY valid JSON.

            Use exactly this structure:

            {
                "problem": "overloaded plans",
                "severity": "very high",
                "evidence": ["string"],
                "recommendation": "string"
            }
            """,
        },
        {
            "role": "user",
            "content": (
                "Analyze the problem of students abandoning "
                "overloaded study plans."
            ),
        },
    ],
    response_format={
        "type": "json_object"
    },
)

raw_output = response.choices[0].message.content

print("RAW OUTPUT:")
print(raw_output)

analysis = ProductAnalysis.model_validate_json(raw_output)

print("\nPYDANTIC OBJECT:")
print(analysis)

print("\nFIELDS:")
print("Problem:", analysis.problem)
print("Severity:", analysis.severity)
print("Evidence:", analysis.evidence)
print("Recommendation:", analysis.recommendation)