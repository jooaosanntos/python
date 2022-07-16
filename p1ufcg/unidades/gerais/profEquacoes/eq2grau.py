if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    
    delta = (b ** 2) + -4 * a * c

    if delta < 0:
        print("sem raizes reais")
    elif delta > 0:
        x1 = (-1 * b + delta ** 0.5) / (2 * a)
        x2 = (-1 * b - delta ** 0.5) / (2 * a)

        print(f"x1 = {x1:.2f}")
        print(f"x2 = {x2:.2f}")

    else:
        x = -b / 2 * a

        print(f"x = {x:.2f}")
