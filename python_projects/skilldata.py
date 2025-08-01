# skill_matcher.py

# Sample SkillBarter users
skill_data = {
    "ananya": {"offers": "graphic design", "wants": "python"},
    "rahul": {"offers": "video editing", "wants": "english speaking"},
    "sanjay": {"offers": "python", "wants": "web design"},
    "megha": {"offers": "english speaking", "wants": "graphic design"},
    "david": {"offers": "web design", "wants": "video editing"}
}

print("=== Welcome to SkillMatcher 🧠 (Mini SkillBarter App) ===")

user_skill = input("What skill do you want to offer? ").lower()
found_match = False

print("\n🔍 Searching for users who want your skill...\n")

for name, skills in skill_data.items():
    if skills["wants"] == user_skill:
        print(f"✅ Match found: {name.title()} wants '{user_skill}' and offers '{skills['offers']}' in return.")
        found_match = True

if not found_match:
    print("❌ No matches found for your skill right now. Try again later.")