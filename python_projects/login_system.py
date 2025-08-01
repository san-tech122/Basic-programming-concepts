# login_system.py

users = {
    "admin": "admin123",
    "sanjay": "pythonking",
    "guest": "guestpass"
}

print("=== Welcome to Sanjay's Login System ===")

while True:
    action = input("\nDo you want to login or signup? (login/signup/exit): ").lower()

    if action == "login":
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users and users[username] == password:
            print(f"✅ Login successful! Welcome, {username}.\n")
        else:
            print("❌ Invalid username or password.")

    elif action == "signup":
        new_user = input("Choose a username: ")
        if new_user in users:
            print("⚠️ Username already taken.")
            continue

        new_pass = input("Choose a password: ")
        users[new_user] = new_pass
        print("🎉 Signup successful! You can now login.")

    elif action == "exit":
        print("👋 Exiting the system. Goodbye!")
        break

    else:
        print("❗ Please choose either 'login', 'signup', or 'exit'.")