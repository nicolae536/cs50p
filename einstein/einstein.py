def einstein(m):
    return m * 300000000**2


def main():
    usrInput = int(input("m:"))
    print(f"E:{einstein(usrInput)}")

if __name__ == "__main__":
    main()