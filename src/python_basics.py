name = "Nasir"
hours_studied = 2
topic = "Python basics"

def describe_session(name, hours, topic):
      return f"{name} studied {topic} for {hours} hours."

print(describe_session(name, hours_studied, topic))

def weekly_study_hours(days, hours_per_day):
      return days * hours_per_day

print("Weekly hours:", weekly_study_hours(5, hours_studied))

topics = ["Python", "NumPy", "Pandas"]

for item in topics:
      print("Study topic:", item)

session = {
      "topic": "Python basics",
      "hours": hours_studied,
      "completed": True,
  }

if session["completed"]:
      print("Completed topic:", session["topic"])
else:
      print("Topic not completed yet.")

scores = [72, 88, 91, 65, 84]

def average_score(values):
      return sum(values) / len(values)

average = average_score(scores)
print("Average score:", average)

if average >= 80:
      print("Status: strong")
else:
      print("Status: needs improvement")

def classify_score(score):
      if not 0 <= score <= 100:
          raise ValueError("Score must be between 0 and 100.")

      if score >= 85:
          return "High"
      elif score >= 70:
          return "Medium"
      return "Low"

for score in scores:
      print(f"Score {score}: {classify_score(score)}")