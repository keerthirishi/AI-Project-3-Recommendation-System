courses = {
    "Python Course": ["python", "programming", "coding"],
    "Machine Learning Course": ["python", "ai", "machine learning"],
    "Data Science Course": ["python", "data science", "analytics"],
    "Web Development Course": ["html", "css", "javascript"],
    "Cloud Computing Course": ["cloud", "aws", "devops"],
    "Artificial Intelligence Course": ["ai", "machine learning", "python"]
}

print("=== AI Recommendation System ===")

user_input = input("Enter interests separated by commas: ").lower()

user_interests = [x.strip() for x in user_input.split(",")]

results = []

for course, tags in courses.items():
    score = len(set(user_interests) & set(tags))

    if score > 0:
        results.append((course, score))

results.sort(key=lambda x: x[1], reverse=True)

print("\nRecommended Courses:\n")

for course, score in results:
    print(f"{course} -> Match Score: {score}")