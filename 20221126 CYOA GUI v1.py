import PySimpleGUI as sg

intro = "Hello traveler. Welcome back. Are you ready for adventure? You know the drill."

#######################################################################################################################
# Beginning Stats
#######################################################################################################################
char =  {'Name' : "Bear"
        , 'Female' : "True", 'Nonbinary' : "False", 'Male' : "False"
        , 'Age' : 36
        , 'Homicide' : "True", 'Undercover' : "False", 'Forensic' : "False", 'Fraud' : "False", 'Narcotics' : "False"}

inventory = {}

sg.theme('DarkAmber')   # Add a touch of color


#######################################################################################################################
# Window 1: Character Creation
#######################################################################################################################

def open_window1():
    layout = [[sg.Text("Let's get some basic information about your character.", key="new")],
              [sg.Text('Name:'), sg.Input(key='-name-')],
              [sg.Text('Gender:'), sg.Radio('Female', "rd_gender", default=True, key="Female"), sg.Radio('Nonbinary', "rd_gender", key="Nonbinary"), sg.Radio('Male', "rd_gender", key="Male")],
              [sg.Text('Age (Years):'), sg.Input(key='-age-')],
              [sg.Text('Specialty:'),sg.Radio('Homicide', "rd_class", default=True, key="Homicide"), sg.Radio('Undercover', "rd_class", key="Undercover"), sg.Radio('Forensic', "rd_class", key="Forensic"), sg.Radio('Fraud', "rd_class", key="Fraud"), sg.Radio('Narcotics', "rd_class", key="Narcotics")],
            [sg.Button("Previous", key="back"),sg.Button("Next", key="next2")]]

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
    layout = [[sg.Text("You can't do your job without equipment. What are you carrying? Now, you can\'t pick everything, so how about you pick up to 5 items?", key="new")],
              [sg.Text('Equipment:')], 
              [sg.Checkbox('Pistol:', key='Pistol'), sg.Text('Good at close to medium range and concealable. However, low to medium damage.')], 
              [sg.Checkbox('Shotgun:', key='Shotgun'), sg.Text('Deadly at close range. Useless at medium to long range.')],
              [sg.Checkbox('Body Armor:', key='Armor'), sg.Text('Good at stopping some but not all bullets.')],
              [sg.Checkbox('Magnifing Glass', key='Magnifing'), sg.Text('All detectives use these still right?')],
              [sg.Checkbox('', key=''), sg.Text('')],
              [sg.Checkbox('', key=''), sg.Text('')],
              [sg.Checkbox('Four Leaf Clover:', key='Clover'), sg.Text('Said to bring good luck but who knows right?')],
              [sg.Checkbox('A Key:', key='Key'), sg.Text('A key of sorts. It might fit somewhere but you don\'t know where.')],
              [sg.Button("Previous", key="back"),sg.Button("Next", key="next3")]]
    window = sg.Window("Equipment", layout, modal=True, size=(750, 500))
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "back":
            window.close()
            open_window1()
        if event == "next3":
            window.close()
            open_window3()
        
    window.close()

#######################################################################################################################
# Window 3: Stats
#######################################################################################################################

def open_window3():
    layout = [[sg.Text("You got your identity and equipment. Now, are you smart or dumb? Agile or clumsy?", key="new")],
              [sg.Text('Equipment:')], 
              [sg.Checkbox('Pistol', key='Pistol'), sg.Text('Good at close to medium range and concealable. However, low to medium damage.')], 
              [sg.Checkbox('Shotgun', key='Shotgun'), sg.Text('Deadly at close range. Useless at medium to long range.')],
              [sg.Checkbox('', key=''), sg.Text('')],
              [sg.Checkbox('', key=''), sg.Text('')],
              [sg.Checkbox('', key=''), sg.Text('')],
              [sg.Checkbox('', key=''), sg.Text('')],
              [sg.Checkbox('', key=''), sg.Text('')],
              [sg.Button("Previous", key="back"),sg.Button("Next", key="next4")]]
    window = sg.Window("Stats", layout, modal=True, size=(750, 500))
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "back":
            window.close()
            open_window2()
        if event == "next4":
            window.close()
            open_window4()
        
    window.close()

#######################################################################################################################
# Window 4: Summary
#######################################################################################################################

#######################################################################################################################
# Window Engine
#######################################################################################################################
def main():
    layout = [[sg.Text(intro)],
              [sg.Text('First, let us create your character. Click "Next" when you are ready or click "Quit" if you\'re too scared.')],
              [sg.Button("Quit", key="quit"),sg.Button("Next", key="next1"),]]

    window = sg.Window("Welcome! Are you ready for adventure?", layout, resizable=False, size=(750, 500))
    while True:
        event, values = window.read()
        if event == "Exit" or event == "quit" or event == sg.WIN_CLOSED:
            break
        if event == "next1":
            window.close()
            open_window1()
        if event == "next2":
            window.close()
            open_window2()
        if event == "next3":
            window.close()
            open_window3()
        
    window.close()
if __name__ == "__main__":
    main()