def validate_hello(greetings):
    print(greetings)
    if "hello" in greetings.casefold() or \
        "ciao" in greetings.casefold() or \
        "salut" in greetings.casefold() or \
        "hallo" in greetings.casefold() or \
        "hola" in greetings.casefold() or \
        "ahoj" in greetings.casefold() or \
        "czesc" in greetings.casefold():
        print("True")
        return True                      
    else :
        print("False")
        return False
    
validate_hello("hello")
validate_hello("hallo, salut")
validate_hello("salut")
validate_hello("ciao bella!")
validate_hello("hombre! Hola!")
validate_hello("Hallo, wie geht\'s dir?")
validate_hello("AHOJ")
validate_hello("czesc")
validate_hello("Ahoj")
validate_hello("meh")