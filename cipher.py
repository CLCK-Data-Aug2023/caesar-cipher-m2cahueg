# Defining the Encryption Key.
Encryption_Key = {"a":"f","b":"g","c":"h","d":"i","e":"j","f":"k","g":"l","h":"m","i":"n","j":"o","k":"p","l":"q","m":"r","n":"s","o":"t","p":"u","q":"v","r":"w","s":"x","t":"y","u":"z","v":"a","w":"b","x":"c","y":"d","z":"e"}

#Collecting user input, making it lowercase, and storing it as a list.
Unencrypted_Text_List = list(input("Please enter a sentence: ").lower())

#Setting Encrypted Text to ""
Encrypted_Text = ""

#Building a loop to build the encrypted text output. 
#Using the try except block allows the code to easily encrypt values that are defined in the Encryption Key. 
#Additionally, it easily passes unencrypted text that is not defined in the Encryption Key (i.e, Spaces, Special Characters, and Numbers) into the encrypted text. 
for i in range(len(Unencrypted_Text_List)):
    try:
        Character = Unencrypted_Text_List[i]
        Encrypted_Text += Encryption_Key[Character]
    except:
        Encrypted_Text += Character
#Printing the encrypted text.    
print("The encrypted sentence is:", Encrypted_Text)



