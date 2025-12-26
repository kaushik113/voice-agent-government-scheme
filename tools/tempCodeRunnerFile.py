# tools/eligibility.py

def load_schemes():
    """
    Mock government schemes database
    """
    return [
        {
            "name": "वृद्धापकाळ पेन्शन योजना",
            "min_age": 60,
            "max_income": 200000,
            "category": ["SC", "ST", "OBC", "GEN"],
            "bpl_required": True,
        },
        {
            "name": "विद्यार्थी शिष्यवृत्ती योजना",
            "student_required": True,
            "max_income": 300000,
            "category": ["SC", "ST", "OBC"],
        },
    ]


def check_eligibility(memory):
    schemes = load_schemes()
    eligible = []

    age = memory.get("age")
    income = memory.get("income")
    category = memory.get("category")
    student = memory.get("student")
    bpl = memory.get("bpl")

    for s in schemes:
        if "min_age" in s and age < s["min_age"]:
            continue

        if "max_income" in s and income > s["max_income"]:
            continue

        if "category" in s and category not in s["category"]:
            continue

        if s.get("student_required") and not student:
            continue

        if s.get("bpl_required") and not bpl:
            continue

        eligible.append(s)

    return eligible

