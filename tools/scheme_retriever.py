import json

def load_scheme_db(path="tools/scheme_db.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def retrieve_scheme_details(scheme_names):
    db = load_scheme_db()
    results = []

    for scheme in db:
        if scheme["name"] in scheme_names:
            results.append(scheme)

    return results
