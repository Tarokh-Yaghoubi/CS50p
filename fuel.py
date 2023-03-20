while True:
    try:
        frac = input("Fraction: ")
        first, second = frac.split("/")
        ans = int(first) / int(second) * 100
        if ans > 100.0:
            pass
        
        elif ans == 100.0:
            print("F")
            break
        elif ans == 0.0:
            print("E")
            break
        else:
            print(f"{int(ans)}%")
            break
        
    except (ValueError, ZeroDivisionError):
        pass
