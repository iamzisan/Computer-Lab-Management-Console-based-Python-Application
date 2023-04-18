import json

# Loads From File    
def read_to_file():
    with open('my_lab.json') as f:
        data = json.load(f)
    
    for computer in data['my_lab']:
        print(f"""
                  PC Number        : {computer['pc_number']}
                  Operating System      : {computer['OS']}
                  PC Status : {computer['Status']}
                  """)
        
def my_lab():
    with open('my_lab.json') as f:
        data = json.load(f)
        
    for computer in data['my_lab']:
        print(computer['pc_number'], f'-->', computer['OS'], f'status:')

def new_lab():
    with open('my_lab.json') as f:
        data = json.load(f)
        print(data)


def update_computer(computer):
    with open('my_lab.json', 'r+') as f:
        data = json.load(f)

        for i, comp in enumerate(data['my_lab']):
            if comp['pc_number'] == computer['pc_number']:
                data['my_lab'][i] = computer
                break

        f.seek(2)
        json.dump(data, f)

# Writes To File

"""def add_computer():
    add = input('---> ')
    with open('my_lab.json', 'r+') as f:
        data = json.load(f)
        
        data.update(add)
        f.seek(2)
        json.dump(data, f)"""

def add_computer():
    # Get input from the user
    pc_number = input('Enter PC number: ')
    OS = input('Enter OS: ')
    status = input('Enter status: ')

    # Create a dictionary to store the input
    computer = {
        'pc_number': pc_number,
        'OS': OS,
        'Status': status
    }

    # Open the json file
    with open('my_lab.json', 'r+') as f:
        data = json.load(f)

        # Update the json file with the new information
        data['my_lab'].append(computer)
        f.seek(2)
        json.dump(data, f)

def remove_computer():
    with open('my_lab.json') as f:
        data = json.load(f)
        
    search_me = input('--> ').upper()
        
    for computer in data['my_lab']:
        if computer['pc_number'] == search_me:
            del computer['OS']
            del computer['Status']
            
            
    with open('new_data.json', 'w') as f:
        json.dump(data, f, indent = 2)






# Search Inside File
def adv_search():
    with open('my_lab.json') as f:
        data = json.load(f)
    
    search_me = input('--> ').upper()
    
    for computer in data['my_lab']:
        if computer['pc_number'] == search_me:
            print(f"""
                  PC Number        : {computer['pc_number']}
                  Operating System      : {computer['OS']}
                  PC Status : {computer['Status']}
                  """)
            break
        else:
            print('NOTHING FOUND')
            break