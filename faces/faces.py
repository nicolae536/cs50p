def convert(strInput):
    return strInput.replace(":)", "🙂").replace(":(","🙁")

def main():
    usrInput = input()
    print(convert(usrInput))

if __name__ == "__main__":
    main()