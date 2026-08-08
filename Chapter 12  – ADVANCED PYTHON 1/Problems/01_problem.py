for name in ("1.txt", "2.txt", "3.txt"):
    try:
        with open(name, "r") as f:
            print(f.read())
    except Exception as e:
        print(f"Error: {e}")
        

print("Thank You!")