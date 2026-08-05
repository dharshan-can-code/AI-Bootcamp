profiles = [
    {"name": "Amalya", "hours": 5, "score": 80},
    {"name": "Vedant", "hours": 8, "score": 90},
    {"name": "Haricharan", "hours": 3, "score": 60},
    {"name": "Maya", "hours": 6, "score": 75},
    {"name": "Leo", "hours": 9, "score": 95}
    {"name": "Dharshan", "hours": 1, "score": 100}
]

student = {
    "hours": int(input("Enter hours: ")),
    "score": int(input("Enter score: "))
}

closest = ""
smallest_dist = float("inf")

for profile in profiles:
    dist = abs(profile["hours"] - student["hours"]) + abs(profile["score"] - student["score"])

    if dist < smallest_dist:
        smallest_dist = dist
        closest = profile["name"]

print("Closest Match:", closest)