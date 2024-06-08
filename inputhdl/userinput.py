
def showError(title,message):
    print("\n###############")
    print(f"\n|> {title}")
    print(f"\n|> {message}")
    print("\n###############\n")

def getString(msg):
    return input(msg)

def getInt(msg):
    v = input(msg)
    try:
        v = int(v)
    except ValueError:
        showError(
            'Invalid Input!',
            'Please Enter Numbers only (no spaces)'
            )
        return getInt(msg)
    else: 
        return v
