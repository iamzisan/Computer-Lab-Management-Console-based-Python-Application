import essential

def main_menu():
    print("""\n
    Choose From Below
    --------------------------      
    1. Display All Computers
    2. Add Computer
    3. Update Computers
    4. Search Computer
    5. Remove Computer
    6. Exit
    """)
main_menu()
    
def selectInput():
    choice_x = input('Enter: ')
    
    if choice_x == '1':
        essential.read_to_file()
        main_menu()
        selectInput()
        
    elif choice_x == '2':
        essential.add_computer()
        print('\nSUCCESSFULLY Added\n-------------------')
        main_menu()
        selectInput()

    elif choice_x == '3':
        essential.update_computer()
        print('Update')
        
        
    
        
        
    elif choice_x == '4':
        essential.adv_search()
        main_menu()
        selectInput()

    elif choice_x == '5':
        essential.my_lab()
        essential.remove_computer()
        print('\nSUCCESSFULLY REMOVED\n-------------------')
        main_menu()
        selectInput()

        
    elif choice_x == '6':

        exit()
        
    else:
        print('INVALID')
        main_menu()
        selectInput()
        
selectInput()