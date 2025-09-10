from typing import Literal

INTENT_MAP = {
    "price": "sales",
    "цена": "sales",
    "доставка": "sales",
    "faq": "support",
    "вопрос": "support",
    "помощь": "support",
    "post": "pr",
    "пост": "pr",
    "слоган": "pr",
}

def classify_intent(text: str) -> Literal["sales", "support", "pr", "unknown"]:
    text_lower = text.lower()
    for key, role in INTENT_MAP.items():
        if key in text_lower:
            return role
    return "unknown"
