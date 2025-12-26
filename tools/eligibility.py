# tools/eligibility.py

import json
import os


def load_schemes():
    """
    Load schemes from JSON file
    """
    path = os.path.join(os.path.dirname(__file__), "scheme_db.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def value_matches(rule_value, user_value):
    """
    Helper to match ALL / list / exact values
    """
    if rule_value == "ALL":
        return True

    if isinstance(rule_value, list):
        return user_value in rule_value

    return rule_value == user_value


def check_eligibility(memory):
    schemes = load_schemes()
    eligible = []

    age = memory.get("age")
    income = memory.get("income")
    category = memory.get("category")
    student = memory.get("student")
    bpl = memory.get("bpl")
    gender = memory.get("gender")
    state = memory.get("state")

    for s in schemes:

        # AGE CHECK
        if age is not None:
            if "min_age" in s and age < s["min_age"]:
                continue
            if "max_age" in s and age > s["max_age"]:
                continue

        # INCOME CHECK
        if income is not None and "max_income" in s:
            if income > s["max_income"]:
                continue

        # CATEGORY CHECK
        if "category" in s:
            if not value_matches(s["category"], category):
                continue

        # STUDENT CHECK
        if "student" in s:
            if s["student"] is True and student is not True:
                continue
            if s["student"] is False and student is True:
                continue

        # BPL CHECK
        if "bpl" in s:
            if s["bpl"] is True and bpl is not True:
                continue
            if s["bpl"] is False and bpl is True:
                continue

        # GENDER CHECK
        if "gender" in s:
            if not value_matches(s["gender"], gender):
                continue

        # STATE CHECK
        if "state" in s:
            if not value_matches(s["state"], state):
                continue

        eligible.append(s)

    return eligible
