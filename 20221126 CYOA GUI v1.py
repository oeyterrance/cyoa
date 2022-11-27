import PySimpleGUI as sg
import numpy as np
import textwrap

#######################################################################################################################
# Beginning Stats
#######################################################################################################################
char =  {'Name' : "Bear"
        , 'Female' : "True", 'Nonbinary' : "False", 'Male' : "False"
        , 'Age' : 36
        , 'Homicide' : "True", 'Undercover' : "False", 'Forensic' : "False", 'Fraud' : "False", 'Narcotics' : "False"}

inventory = {'Pistol' : "False", 'Shotgun' : "False", 'Dagger' : "False", 'Armor' : "False", 
'Magnifing' : "False", 'Cap' : "False", 'Clover' : "False", "Key" : "False"}

stats = {'hp' : 0, 'mind' : 0, 'know' : 0, 'luck' : 0}

#######################################################################################################################
# PySimpleGUI Themes
#######################################################################################################################

# Default window colors
sg.theme('SystemDefault')

# Default font size and color
sg.set_options(font=("Times New Roman", 14))



#######################################################################################################################
# Window 1: Character Creation
#######################################################################################################################

def open_window1():
    layout = [[sg.Text("Character Background", key="new")],
              [sg.Text('')],
              [sg.Text('Name: '), sg.Input("Bear",key='-name-')],
              [sg.Text('')],
              [sg.Text('Gender: '), sg.Radio('Female', "rd_gender", default=True, key="Female"), sg.Radio('Nonbinary', "rd_gender", key="Nonbinary"), sg.Radio('Male', "rd_gender", key="Male")],
              [sg.Text('')],
              [sg.Text('Age (Years): '), sg.Input(36, key='-age-')],
              [sg.Text('')],
              [sg.Text('Specialty: '),sg.Radio('Homicide', "rd_class", default=True, key="Homicide"), sg.Radio('Undercover', "rd_class", key="Undercover"), sg.Radio('Forensic', "rd_class", key="Forensic"), sg.Radio('Fraud', "rd_class", key="Fraud"), sg.Radio('Narcotics', "rd_class", key="Narcotics")],
              [sg.Text('')],
            [sg.Button("Previous", key="back", pad=(5,0)),sg.Button("Next", key="next2", pad=(5,0))]]

    window = sg.Window("Character Creation", layout, modal=True, size=(750, 500))
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "back":
            window.close()
            main()
        if event == "next2":
            char['Name'] = values['-name-']
            char['Female'] = values['Female']
            char['Nonbinary'] = values['Nonbinary']
            char['Male'] = values['Male']
            char['Age'] = values['-age-']
            char['Homicide'] = values['Homicide']
            char['Undercover'] = values['Undercover']
            char['Forensic'] = values['Forensic']
            char['Fraud'] = values['Fraud']
            char['Narcotics'] = values['Narcotics']
            test = list(filter(values.get, values))
            window.close()
            open_window2()
            return char
        
    window.close()

#######################################################################################################################
# Window 2: Inventory
#######################################################################################################################

def open_window2():
    layout = [[sg.Text("Starting Equipment (Choose up to 5)", key="new")],
              [sg.Text('')],
              [sg.Text('Weapons and Armor:')], 
              [sg.Checkbox('Pistol: ', key='Pistol'), sg.Text('Good at close to medium range and concealable. However, low to medium damage.')], 
              [sg.Checkbox('Shotgun: ', key='Shotgun'), sg.Text('Deadly at close range. Useless at medium to long range.')],
              [sg.Checkbox('Dagger: ', key='Dagger'), sg.Text('Silent but deadly at close range. Could be thrown.')],
              [sg.Checkbox('Body Armor:', key='Armor'), sg.Text('Good at stopping some but not all bullets.')],
              [sg.Text('')],
              [sg.Text('Misc. Items')],
              [sg.Checkbox('Magnifing Glass: ', key='Magnifing'), sg.Text('All detectives use these still right?')],
              [sg.Checkbox('Cap: ', key='Cap'), sg.Text('What kind of detective would you be without your trusty cap?')],
              [sg.Checkbox('Four Leaf Clover: ', key='Clover'), sg.Text('Said to bring good luck but who knows right?')],
              [sg.Checkbox('A Key: ', key='Key'), sg.Text('A key of sorts. It might fit somewhere but you don\'t know where.')],
              [sg.Button("Previous", key="back", pad=(5,0)),sg.Button("Next", key="next3", pad=(5,0))]]
    window = sg.Window("Equipment", layout, modal=True, size=(750, 500))
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "back":
            window.close()
            open_window1()
        
        if event == "next3" and len(list(filter(values.get, values))) > 5:
            # print(len(list(filter(values.get, values))), values)
            sg.popup('I get it, you want to be prepared but I can\'t have you be OP.',      
            'You picked', len(list(filter(values.get, values))), ' items instead of just 5. Reduce it to at most 5.') 
        
        if event == "next3" and len(list(filter(values.get, values))) <= 5:
            inventory['Pistol'] = values['Pistol']
            inventory['Shotgun'] = values['Shotgun']
            inventory['Dagger'] = values['Dagger']
            inventory['Armor'] = values['Armor']
            inventory['Magnifing'] = values['Magnifing']
            inventory['Cap'] = values['Cap']
            inventory['Clover'] = values['Clover']
            inventory['Key'] = values['Key']
            window.close()
            open_window3()
        
    window.close()

#######################################################################################################################
# Window 3: Stats
#######################################################################################################################

def open_window3():
    # Counter for stats generation
    gen = 0

    layout = [[sg.Text("Character Stats Generation", key="new")],
              [sg.Text('')],
              [sg.Text('Stats:')], 
              [sg.Text('Hit Points:', key='-hp-')],
              [sg.Text('Mind:', key='-mind-')],
              [sg.Text('Knowledge:', key='-know-')],
              [sg.Text('Luck:', key='-luck-')],
              [sg.Text('')],
              [sg.Text('You can generate random stats up to 5 times.')],
              [sg.Text('You can reroll 5 more times.', key='-reroll-')],
              [sg.Button("Generate", enable_events=True, key="-Generate-", pad=(5,0))],
              [sg.Text('')],
              [sg.Text('')],
              [sg.Button("Previous", key="back", pad=(5,0)),sg.Button("Next", key="next4", pad=(5,0))]]
    window = sg.Window("Stats", layout, modal=True, size=(750, 500))
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-Generate-" and gen < 5:
            update(window)
            gen += 1
            reroll = 5 - gen
            text_elem = window['-reroll-']
            text_elem.update("You can reroll {} more times.".format(reroll))
        if event == "-Generate-" and gen >= 5:
            sg.popup('You have already generated stats 5 times.')
        if event == "next4" and gen == 0:
            sg.popup('Generate at least one set of stats.')
        if event == "back":
            window.close()
            open_window2()
        if event == "next4" and gen != 0:
            window.close()
            open_window4()
        
    window.close()

# Update function
def update(window):

    hp = np.random.randint(2,5)
    text_elem = window['-hp-']
    text_elem.update("Hit Points: {}".format(hp))
    stats['hp'] = hp
    
    mind = np.random.randint(2,5)
    text_elem = window['-mind-']
    text_elem.update("Mind: {}".format(mind))
    stats['mind'] = mind
    
    know = np.random.randint(1,3)
    text_elem = window['-know-']
    text_elem.update("Knowledge: {}".format(know))
    stats['know'] = know
    
    luck = np.random.randint(1,3)
    text_elem = window['-luck-']
    text_elem.update("Luck: {}".format(luck))
    stats['luck'] = luck

#######################################################################################################################
# Window 4: Summary
#######################################################################################################################
def open_window4():
    char_true = list(filter(char.get, char))
    inventory_true = list(filter(inventory.get, inventory))

    layout = [[sg.Text(char_true, key="new")],
              [sg.Text(inventory_true, key="new")],
              [sg.Text(stats, key="new")],
              [sg.Text('You are ' + char['Name'] + ', ex-' + char_true[3] + ' Detective for The Agnecy. In your last adventure, you were called upon by Detective Lingxin to assist in solving the haunted mansion case, a case that has been ongoing for years. Several near death experience and unfortunate circumstances left you scared. However, you both came out on top. With that behind you, you return to what\'s important: Sitting and drinking alone in your apartment.', key="new", size=(71, 8))],
              [sg.Button("Previous", key="back", pad=(5,0)),sg.Button("Finish", key="intro", pad=(5,0))]]
    window = sg.Window("Summary", layout, modal=True, size=(750, 500))
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "back":
            window.close()
            open_window3()
        if event == "intro":
            window.close()
            intro()
        
    window.close()

#######################################################################################################################
# Window 5: Introduction
#######################################################################################################################
def intro():
    layout = [[sg.Text(char_true, key="new")],
              [sg.Text(inventory_true, key="new")],
              [sg.Text(stats, key="new")],
              [sg.Text('You are ' + char['Name'] + ' a ' + char_true[3] + ' Detective for The Agnecy.', key="new")],
              [sg.Button("Next", key="next4")]]
    window = sg.Window("Introduction", layout, modal=True, size=(750, 500))
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "next4":
            window.close()
            intro()
        
    window.close()


#######################################################################################################################
# PySimpleGUI Window Engine
#######################################################################################################################
def main():

        # ------ Menu Definition ------ #
    menu_def = [['&File', ['&Open     Ctrl-O', '&Save       Ctrl-S', '&Properties', 'E&xit']],
                ['&Edit', ['&Paste', ['Special', 'Normal', ], 'Undo'], ],
                ['&Toolbar', ['---', 'Command &1', 'Command &2',
                              '---', 'Command &3', 'Command &4']],
                ['&Help', '&About...'], ]
                
    layout = [[sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
              [sg.Text('Hello traveler. Welcome back. Are you ready for adventure? You know the drill.')],
              [sg.Text('')],
              [sg.Text('First, let us create your character.')],
              [sg.Text('')],
              [sg.Text('Click "Next" when you are ready or click "Quit" if you\'re too scared.')],
              [sg.Text('')],
              [sg.Button("Quit", key="quit", pad=(5,0)),sg.Button("Next", key="next1", pad=(5,0)),]]

    window = sg.Window("Welcome! Are you ready for adventure?", layout, resizable=False, size=(750,500))
    while True:
        event, values = window.read()
        if event == "Exit" or event == "quit" or event == sg.WIN_CLOSED:
            break
        if event == 'About...':
            window.disappear()
            sg.popup('About this program', 'Version 0.1', 'Created by Florace Starfire',
                     'PySimpleGUI Version', sg.version,  grab_anywhere=True, font=("Times New Romans",12))
            window.reappear()
        if event == "next1":
            window.close()
            open_window1()
        
    window.close()

if __name__ == "__main__":
    main()