import re

# ===============================
# NUMBER WORD MAPS
# ===============================

ENGLISH_NUMBERS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10
}

MARATHI_NUMBERS = {
    "एक": 1, "दोन": 2, "तीन": 3, "चार": 4, "पाच": 5,
    "सहा": 6, "सात": 7, "आठ": 8, "नऊ": 9, "दहा": 10
}

MULTIPLIERS = {
    "lakh": 100000,
    "लाख": 100000,
    "thousand": 1000,
    "हजार": 1000
}

# ===============================
# CORE NUMBER PARSER
# ===============================

def extract_number(text):
    if not text:
        return None

    text = text.lower().strip()

    # 1️⃣ Digits first (most reliable)
    nums = re.findall(r"\d+", text)
    if nums:
        return int(nums[0])

    # 2️⃣ English words
    for word, val in ENGLISH_NUMBERS.items():
        if word in text:
            base = val
            break
    else:
        base = None

    # 3️⃣ Marathi words
    if base is None:
        for word, val in MARATHI_NUMBERS.items():
            if word in text:
                base = val
                break

    if base is None:
        return None

    # 4️⃣ Multipliers (lakh / thousand)
    for mword, mult in MULTIPLIERS.items():
        if mword in text:
            return base * mult

    return base


# ===============================
# YES / NO (NUMERIC ONLY)
# ===============================

def extract_yes_no(text):
    n = extract_number(text)
    if n == 1:
        return True
    if n == 2:
        return False
    return None


# ===============================
# CATEGORY
# ===============================

def extract_category(text):
    n = extract_number(text)
    if n == 1:
        return "SC"
    if n == 2:
        return "ST"
    if n == 3:
        return "OBC"
    if n == 4:
        return "GEN"
    return None


# ===============================
# GENDER
# ===============================

def extract_gender(text):
    n = extract_number(text)
    if n == 1:
        return "MALE"
    if n == 2:
        return "FEMALE"
    return None


# ===============================
# STATE
# ===============================

def extract_state(text):
    return text.strip() if text else None
