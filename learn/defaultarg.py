

def ask_ok(prompt, retries = 4, reminder="Please try again"):
    while True:
        reply = input(prompt)
        if reply in {"y", "ye", "yes"}:
            return True
        if reply in {"n", "no"}:
            return False
        retries -= 1
        if (retries < 0):
            raise ValueError("invalid user response")
        print(reminder)
        
            