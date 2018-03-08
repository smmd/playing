# Exercise https://codeclubprojects.org/es-ES/python/secret-messages/
import sys, os

menu_actions = {}  

# Main menu
def main_menu():
    os.system('clear')
    
    print "Welcome,\n"
    print "Please choose the menu you want to start:"
    print "1. Encrypt a message"
    print "2. Decrypt a message"
    print "\n0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)

# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return

# Menu 1 encrypt message
def menu1():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = input('Please enter the key: ')
    newMessage = ''

    message = raw_input('Please enter the message: ')

    for character in message:
		if character in alphabet:
			position = alphabet.find(character)
			newPosition = (position + key) % 26
			newCharacter = alphabet[newPosition]
			newMessage += newCharacter
		else:
			newMessage += character

    print 'Your message encrypt is: ', newMessage
    return

# Menu 2 decrypt message
def menu2():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = input('Please enter the key: ')
    newMessage = ''

    message = raw_input('Please enter the encrypt message: ')

    for character in message:
		if character in alphabet:
			position = alphabet.find(character)
			newPosition = (position - key) % 26
			newCharacter = alphabet[newPosition]
			newMessage += newCharacter
		else:
			newMessage += character

    print 'Your message encrypt is: ', newMessage
    return

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
}

# Main Program
if __name__ == "__main__":
    main_menu()