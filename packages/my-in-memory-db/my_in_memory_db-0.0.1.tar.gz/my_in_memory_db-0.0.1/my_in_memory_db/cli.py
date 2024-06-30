import argparse
from my_in_memory_db import InMemoryDatabase

db = InMemoryDatabase()

def main():
    parser = argparse.ArgumentParser(description="In-Memory Database CLI")
    parser.add_argument("command", choices=["set", "get", "delete", "info"], help="Command to execute")
    parser.add_argument("key", nargs="?", help="Key for the command")
    parser.add_argument("value", nargs="?", type=int, help="Value for the set command")

    args = parser.parse_args()

    if args.command == "set":
        if args.key is None or args.value is None:
            print("Error: 'set' command requires both key and value.")
        else:
            db.set(args.key, args.value)
            print(f"Set {args.key} to {args.value}.")
    elif args.command == "get":
        if args.key is None:
            print("Error: 'get' command requires a key.")
        else:
            print(db.get(args.key))
    elif args.command == "delete":
        if args.key is None:
            print("Error: 'delete' command requires a key.")
        else:
            db.delete(args.key)
            print(f"Deleted {args.key}.")
    elif args.command == "info":
        print(f"Version: 0001, Size: {db.size()}")

if __name__ == "__main__":
    main()

