# agent/llm_normalizer.py
"""
Offline-safe LLM Normalizer
---------------------------
• Converts raw STT text → structured values
• No eligibility logic
• No scheme logic
• Deterministic + rule-based
"""

import re

# ===============================
# NUMBER WORD MAPS
# ===============================

EN_NUMBERS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
}

MR_NUMBERS = {
    "एक": 1,
    "दोन": 2,
    "तीन": 3,
    "चार": 4,
    "पाच": 5,
    "सहा": 6,
    "सात": 7,
    "आठ": 8,
    "नऊ": 9,
    "दहा": 10,
}

# ===============================
# BASIC NUMBER EXTRACTION
# ===============================

def extract_basic_number(text: str):
    if not text:
        return None

    t = text.lower().strip()

    # 1️⃣ Digits
    m = re.search(r"\b\d+\b", t)
    if m:
        return int(m.group())

    # 2️⃣ English words
    for w, v in EN_NUMBERS.items():
        if re.search(rf"\b{w}\b", t):
            return v

    # 3️⃣ Marathi words
    for w, v in MR_NUMBERS.items():
        if re.search(rf"\b{w}\b", t):
            return v

    return None


def extract_lakh_number(text: str):
    """
    Handles:
    • one lakh
    • 2 lakh
    • दोन लाख
    """
    if not text:
        return None

    t = text.lower().strip()

    if "lakh" in t or "लाख" in t:
        base = extract_basic_number(t)
        if base is not None:
            return base * 100000

    return None


# ===============================
# MAIN NORMALIZER
# ===============================

def normalize(text: str, expected: str):
    """
    expected ∈ {age, income, category, gender, yesno, state}
    """

    if not text:
        return None

    t = text.lower().strip()

    # ---------------- AGE ----------------
    if expected == "age":
        return extract_basic_number(t)

    # ---------------- INCOME ----------------
    if expected == "income":
        lakh = extract_lakh_number(t)
        if lakh is not None:
            return lakh
        return extract_basic_number(t)

    # ---------------- CATEGORY ----------------
    if expected == "category":
        if re.search(r"\b(1|one|एक|sc)\b", t):
            return "SC"
        if re.search(r"\b(2|two|दोन|st)\b", t):
            return "ST"
        if re.search(r"\b(3|three|तीन|obc)\b", t):
            return "OBC"
        if re.search(r"\b(4|four|चार|gen|general)\b", t):
            return "GEN"
        return None

    # ---------------- GENDER ----------------
    if expected == "gender":
        if re.search(r"\b(1|one|एक|male|पुरुष)\b", t):
            return "MALE"
        if re.search(r"\b(2|two|दोन|female|महिला)\b", t):
            return "FEMALE"
        return None

    # ---------------- YES / NO ----------------
    if expected == "yesno":
        if re.search(r"\b(1|one|yes|ho|होय)\b", t):
            return True
        if re.search(r"\b(2|two|no|nahi|नाही)\b", t):
            return False
        return None

    # ---------------- STATE ----------------
    if expected == "state":
        if re.search(r"\b(1|one|maharashtra)\b", t):
            return "Maharashtra"
        if re.search(r"\b(2|two|other)\b", t):
            return "Other"
        return None

    return None



#---------------------------------------------------------------------------------------------------------------------------