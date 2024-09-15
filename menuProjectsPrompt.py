def twoOptionsMenu(xProject, prompt, system):
    while True:
        print(f"=== Welcome to my {xProject} Project ===")
        match input(f"Menu:\n1. {prompt}\n2. Quit Program\nSelect Menu (Number): "):
            case "1":
                system()
            case "2":
                break
            case _:
                print("Please Select Menu Number!!!\n")


def threeOptionsMenu(xProject, promptOne, promptTwo, systemOne, SystemTwo):
    print(f"\n=== Welcome to my {xProject} Project ===")
    while True:
        match input(
            f"Menu:\n1. {promptOne}\n2. {promptTwo}\n3. Quit Program\nSelect Menu (Number): "
        ):
            case "1":
                return systemOne
            case "2":
                SystemTwo()
            case "3":
                break
            case _:
                print("Please Select Menu Number!!!\n")


if __name__ == "__main__":
    twoOptionsMenu("menu", "menu", "menu")
