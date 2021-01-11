import json

file = './database/benchDATA.json'

def remove(benchedUser):
    with open(file, encoding="utf-8", mode="r") as f:
        db = json.load(f)

        try:
            db['benched'].remove(benchedUser)
        except:
            return False

    with open(file, encoding="utf-8", mode="w") as f:
        json.dump(db, f)

def add(benchedUser):
    with open(file, encoding="utf-8", mode="r") as f:
        db = json.load(f)

        if check(benchedUser):
            return

        db['benched'].append(benchedUser)

    with open(file, encoding="utf-8", mode="w") as f:
        json.dump(db, f)

def check(user):
    with open(file, encoding="utf-8", mode="r") as f:
        db = json.load(f)

        if user in db['benched']:
            return True
        else:
            return False

def amount():
    with open(file, encoding="utf-8", mode="r") as f:
        db = json.load(f)

        return len(db['benched'])