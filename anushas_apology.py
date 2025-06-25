class MyCustomError(Exception):
    pass

try:
    print("Analyzing our friendship...")
    import time
    time.sleep(1.5)
    print("Status: Perfect... wait...")
    time.sleep(1.5)
    raise MyCustomError("a bug was found... and it's my fault.")

except MyCustomError as e:
    print(f"\nError: {e}")
    time.sleep(2)
    print("\nInitiating debugging sequence...")
    time.sleep(1.5)
    print("Applying patch: Unlimited apologies and one big hug.")
    time.sleep(2)
    print("\nPatch applied successfully.")
    time.sleep(1)
    print("\nI'm really sorry, Anusha ❤️") 