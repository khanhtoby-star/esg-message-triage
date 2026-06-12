"""
Simple rule-based baseline classifier for ESG message triage.
Used to compare against LLM classification in Q3(c).
"""

import json

# Keyword-based rules: (keywords, category, urgency)
RULES = [
    (["water leak", "running all morning"], "Facilities", "HIGH"),
    (["recycling", "contaminated", "again"], "Waste and Recycling", "MEDIUM"),
    (["accessible entrance", "blocked"], "Accessibility", "HIGH"),
]


def classify(message: str):
    message_lower = message.lower()
    for keywords, category, urgency in RULES:
        if all(kw in message_lower for kw in keywords):
            return {"category": category, "urgency": urgency}
    return {"category": "Unknown", "urgency": "LOW"}


if __name__ == "__main__":
    with open("sample_messages.json") as f:
        messages = json.load(f)

    results = []
    for item in messages:
        result = classify(item["message"])
        results.append({
            "id": item["id"],
            "message": item["message"],
            "baseline_classification": result
        })
        print(f"Message {item['id']}: {result}")

    with open("baseline_output.json", "w") as f:
        json.dump(results, f, indent=2)
