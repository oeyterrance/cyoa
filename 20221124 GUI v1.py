import random
import sys
import numpy as np
import PySimpleGUI as sg

pages = {
    'intro': {'desc' : '\"Detective Bear? I don\'t have a lot of time. Do you want to take the case or not?\"', 
              'choices' : [('\"Sure, why not. Might as well do something.\"', 'intro_cont'),
                         ('\"This detective work is behind me now.\"', 'intro_end')]},

    'intro_end': {'desc': '\"Look, I gave up this gig for a reason. Call Detective Lingxin and she\'ll help you out.\" You immediately hang up.', 
        'end': 'win'},

    'intro_cont': {'desc' : 'You sigh. \"I better get paid well for this. What\'s the plan?\", \n \"Not on the phone. Meet me at the coffee shop at Broadway and Chelesa at 10 a.m. We\'ll chat then.\" \n\n Without another word she hangs up the phone. A dead detective, a call in the middle of the night, and an old, ongoing case. Also, how will she recognize me you thought. Several things occupy your mind as you lie in bed. Your mind is swimming with questions but at the same time, your body and brain are running on little sleep.', 
              'choices' : [('Do some background research on the Haunted Mansion case.', 'chapter1_res'),
                         ('Try to get some rest before the 10 a.m. meeting.', 'chapter1_sle')],
              'stats_adj' : [[-1,0,1,0],[1,0,-1,0]]},
}



#Win and lose descriptions
def win():
    # When the player wins the game
    win_phrases = ['win']
    return random.choice(win_phrases)

def hp_death():
    # When the player dies due to hp loss
    lose_phrases = ['hp death']
    return random.choice(lose_phrases)

def mind_death():
    # When the player dies due to craze
    lose_phrases = ['mind death']
    return random.choice(lose_phrases)


#### Machinery for running all games

# Beginning Stats
stats_beg =  {'stats': {'hp' : 3, 'mind' : 3, 'know' : 2, 'luck' : 0}}

# Room tracking
room_track = {'rooms': {'Hall': 0, 'Kitchen': 0, 'Dining Room': 0, 'Living Room': 0, 'Billard\'s Room': 0, 'Servant\'s Quarters': 0, 'Bedrooms': 0}}

# Checking pages to make sure the pages dictionary is good
def check_pages(pages):
    #''' make sure that every page is a win,die, or has choices coming off it.
    #'''
    allok = True
    for pageid in pages:
        page = pages[pageid]
        choices = page.get('choices',[])
        end = page.get('end',None)
        if choices and end:
            print (pageid), ": choices and end both defined"
            allok = False
        if not choices and end not in ("win"):
            print (pageid), ": no choices, but end not one of win|die"
            allok = False
    return allok

    # Move engine and choice engine
def move(choices):
    # ''' get player move from choices, returning a pageid
    # 
    # choices:  a list of page choices, where each choice is:
    # 
    # text, locationid'''

    print ("----From here, you can -----")
    
    ii = 1  # start our numbering with 1
    valid_choices = {'q': None} # 'q' is always a valid choice
    for choice in choices:
        ## name the parts of the choice, with more meaningful names
        text = choice[0]
        pageid = choice[1]
        ## we str(ii) here because the user input will be a string
        valid_choices[str(ii)] = pageid  
        print (ii, ")", text )
        ii = ii+1 
    
    ans = None
    ## get the user input, clean it up.
    while ans is None:
        ans = input("Choose from " + str(sorted(valid_choices)) + ":  " ).lower().strip()
        if ans in valid_choices:            
            if ans == 'q':
                sys.exit("Quitting game.")
            return valid_choices[ans], ans

        elif ans == 's':
            print('')
            print('Detective Bear\'s current stats:')
            print('Hit Points: ', stats_beg['stats']['hp'])
            print('Sanity: ', stats_beg['stats']['mind'])
            print('Knowledge: ', stats_beg['stats']['know'])
            print('Luck: ', stats_beg['stats']['luck'])
            print('')
            ans = None
        elif ans == 'h':
            print('')
            print('This is the help section')
            print('Enter "s" if you want to see your stats such as hp, sanity, knowledge, and/or luck.')
            print('Enter "q" if you want to quit the game.')
            print('Otherwise, please make a valid selection.')
            print('')
            ans = None

        else:
            print ("Your answer,", ans, ", isn't in the choices\n")
            ans = None # so that we can ask again

# Stats engine
def stats_up(stats_adj,i):
    stats_up = {'hp' : stats_beg['stats']['hp'] + stats_adj[i][0]
               , 'mind' : stats_beg['stats']['mind'] + stats_adj[i][1]
               , 'know' : stats_beg['stats']['know'] + stats_adj[i][2]
               , 'luck' : stats_beg['stats']['luck'] + stats_adj[i][3]
               }
               
    if int(stats_adj[i][0]) != 0 or int(stats_adj[i][1]) != 0 or int(stats_adj[i][2]) != 0 or int(stats_adj[i][3]) != 0:
        print('Your hp has been adjusted: ', int(stats_adj[i][0]), 
              '. Your mind has been adjusted: ', int(stats_adj[i][1]), 
              '. Your knowledge has been adjusted: ', int(stats_adj[i][2]),
              '. Your luck has been adjusted: ', int(stats_adj[i][3]), '.', sep = '')

    else: print('')

    stats_beg['stats'].update(stats_up)

# Game engine
def game_cli(pages,startpage):
    # '''
    # pages:  a dictionary of game pages
    # pageid: starting pageid
    # '''

    if not check_pages(pages):
        print ("there is some error in the pages data, ending game")
        return None
        
    # go to the first page
    page = pages[startpage]
    print (page['desc'] + '\n')
    
    # When it's not an instant kill and hp not below 0 and mind not below 0
    while not page.get("end",None) and int(stats_beg['stats']['hp']) > 0 and int(stats_beg['stats']['mind']) > 0:

        # move function gets fed choices and current stats in case user queries for current stats
        move_page = move(page['choices'])

        # find out where the person moved to, moving them
        pageid = move_page[0]
        # pass the ans input from the user
        input_ans = int(move_page[1]) - 1

        if 'stats_adj' in page:
            stats_up(page['stats_adj'],input_ans)
        else: print('')

        # print the description for the new position
        page = pages[pageid]
        print ("\n", page['desc'], "\n")

    if int(stats_beg['stats']['hp']) <= 0:
        print(hp_death())
    elif int(stats_beg['stats']['mind']) <= 0:
        print(mind_death())
    elif page['end'] == 'win':
        print(win())
    else:
        print ("this shouldn't happen!")
    
    print ("\n" + pages.get("OUTRO","The End.")) 


## actually start the game, with our data
if __name__ == "__main__":
    game_cli(pages,"intro")



sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
