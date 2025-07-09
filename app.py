from config import get_username

def main():
    print(f"Hello from the 12 Factor App, {get_username()}")

if __name__ == "__main__":
    main()