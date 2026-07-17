name = input("Tumhara naam kya hai bhai? ").strip().title()

print("\nCategories:")
print("1. joke")
print("2. analysis")
print("3. suggestion")
print("4. exit")

category = input("\nCategory select karo: ").strip().lower()

match category:
    case "joke":
        print("\n😂 Life badi aasan hoti agar bugs khud fix ho jaate!")

    case "analysis":
        age = int(input("Tumhari age kya hai? "))

        if age >= 18:
            print(f"\n{name}, tum abhi adult ho.")
        else:
            print(f"\n{name}, tum abhi student ho kyunki tumhari age 18 se kam hai.")

    case "suggestion":
        subject = input("Tumhara favourite subject kya hai? ").strip().lower()

        match subject:
            case "maths":
                print("📘 Mathematics mein analytical thinking aur problem-solving ka strong scope hai.")
            case "science":
                print("🔬 Science future technologies aur research ke liye bahut achha field hai.")
            case "computer":
                print("💻 Computer Science software development, AI aur cybersecurity jaise fields ke liye excellent choice hai.")
            case _:
                print("📚 Har subject important hota hai. Apni interest ke hisaab se seekhte raho.")

    case "exit":
        print("👋 Program band ho gaya. Dhanyavaad!")

    case _:
        print("❌ Invalid category. Kripya valid option select karein.")
