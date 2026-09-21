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