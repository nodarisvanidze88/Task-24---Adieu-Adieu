import inflect


def main():
    x = inflect.engine()
    names = []
    while True:
        user = input("For Stop add \"S\". Name: ").strip().lower()
        if user == "s":
            break
        if user != "":
            names.append(user.title())
    print("Adieu, adieu, to " + x.join(names))


if __name__ == "__main__":
    main()
