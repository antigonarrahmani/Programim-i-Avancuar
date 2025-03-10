import datetime

def greet_user():
    """Funksion për të përshëndetur përdoruesin."""
    try:
        name = input("Shkruaj emrin tënd: ").strip()
        if not name:
            raise ValueError("Emri nuk mund të jetë bosh!")
        print(f"Përshëndetje, {name}!")
    except ValueError as e:
        print(f"Gabim: {e}")

def main():
    """Funksioni kryesor që ekzekuton programin."""
    print("Hello, World!")  # Printon përshëndetjen bazë
    greet_user()  # Thërret funksionin për të marrë emrin e përdoruesit
    print("Data dhe ora aktuale:", datetime.datetime.now())  # Printon datën dhe orën

if __name__ == "__main__":
    main()