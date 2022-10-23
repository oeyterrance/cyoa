#!/usr/bin/env python

## the special line above this is called the "shebang".  On unix/linux/mac
## if the first line starts with '#!' this tells the operating system
## which program to use to run the file.  Windows tends to depend on the 
## file entension.  

## by convention, python interprets the first string in the file as 
## a module level DOCSTRING, describing the contents of the file, and what it
## does

## by convention, imports come after the module level docstring
import random
import sys
import numpy as np

print('Ring, ring, ring. Ring, ring, ring.', '\n'
, 'Fuck you thought. You glance at the clock on your nightstand.', '\n'
, 'The faded green light on your clock flickers 2:34 a.m. Who the hell is calling you this early you thought.', '\n'
, '\n'
, '\"This better be important.\" you said in a groggy voice.', '\n'
, '\"Is this Detective Bear?\" asked the faint voice.', '\n'
, '\"Who\'s asking?\"', '\n'
, '\"None of your concern. I\'m calling because I have a case for you.\"', '\n'
, '\"I gave up that gig a long time ago. Contact Detective Adytum. He should be able to help you out.\" you replied about to hang up your cell phone.', '\n'
, '\"He\'s dead.\"', '\n'
, '\n'
, 'Your mind and body jolt awake. Detective Adytum may not have been the best detective at the agency but he was far from incompetent. He was actually your senior but you rose through the ranks faster than him. People called you lucky but deep down they and you knew that it was far from luck.', '\n'
, '\n'
, '\"Come again?\" you ask.', '\n'
, 'The voice continues, \"The police called just a few minutes ago. They didn\'t go into details but they said one word: Mutilation.\"', '\n'
, '\"Mutilation? What were the circumstances surrounding this? How did it happen?\" you quickly asked.', '\n'
, '\"Look, like I said, the police didn\'t go into details. I\'m calling you because I need \"you\" to take on Detective Adytum\'s case.\" she bluntly said.', '\n'
, '\n'
'You search your mind for a few moments and finally asked \"You mean the haunted mansion case?\"', '\n'
'\"Yes.\" she said curtly.', '\n'
, '\n'
, 'The haunted mansion. Now there\'s a case you haven\'t heard in long time. You heard about it for the first time when you started at the agency. While normal cases were completed a few weeks after being assigned, this haunted mansion case was an ongoing on. Detectives normally assigned to it... left for mysterious reasons. One detective resigned with no apparent reason. Another one was committed to an asylum shortly after their first report. Detective Starfire and her assistant went missing. For one reason or another, this case never was completed. And now Detective Adytum fell to a similar, albeit more gruesome fate. You wonder...', '\n'
, '\n'
, sep='')

pages = {
    'intro': {'desc' : '\"Detective Bear? I don\'t have a lot of time. Do you want to take the case or not?\"', 
              'choices' : [('\"Sure, why not. Might as well do something.\"', 'intro_cont'),
                         ('\"This detective work is behind me now.\"', 'intro_end')]},

    'intro_end': {'desc': '\"Look, I gave up this gig for a reason. Call Detective Zhang and she\'ll help you out.\" You immediately hang up.', 
        'end': 'intro_end'},

    'intro_cont': {'desc' : 'You sigh. \"I better get paid well for this. What\'s the plan?\", \n \"Not on the phone. Meet me at the coffee shop at Broadway and Chelesa at 10 a.m. We\'ll chat then.\" \n\n Without another word she hangs up the phone. A dead detective, a call in the middle of the night, and an old, ongoing case. Also, how will she recognize me you thought. Several things occupy your mind as you lie in bed. Your mind is swimming with questions but at the same time, your body and brain are running on little sleep.', 
              'choices' : [('Do some background research on the Haunted Mansion case.', 'chapter1_res'),
                         ('Try to get some rest before the 10 a.m. meeting.', 'chapter1_sle')],
              'stats_adj' : [[-1,0,1,0],[1,0,-1,0]]},

    'chapter1_res': {'desc' : 'Fuck it you thought. You get out of bed and start the coffee maker. You hop into the shower and the steam from the hot water wakes and refreshes you. You throw on some clothes, grab a hot cup of coffee and begin sifting through old papers and internet searches to catch up on the case. \n\n Several hours pass by and you rub your eyes as you push back from the table. Papers and notes are strewned all over but you have a better grasp of the details of the case. You look at you watch: \"9:30 a.m.\" Plenty of time to get to the meeting point you thought as you yawn. You pocket the notes that you took and grabbed your coat as you head out the front door. You feel mentally exhausted but feel more prepared for the meeting with... that\'s right, you still don\'t know who you\'re meeting you thought. \n\n As you enter the coffee shop, you look at your watch: \"9:56 a.m.\" Plenty of time to spare you thought. You peer around the shop and your eyes fall on a familiar person. You walk over to booth where the person is sitting and slide into the opposite side. \n \"Detective Zhang?\" you ask curiously. \n \"Detective Bear, it has been awhile she says.\" She looks at her watch. \"Early, that\'s a surprise.\" she said. \n \"I stayed up after your call to review the facts and details of the case.\" \n She raises an eyebrow. \"So you\'re running on no sleep then for this very important case?\" she inquires? \n \"It\'s something I\'m used to doing when I worked for the agency.\" I lied. Maybe I should\'ve gotten that extra sleep... \n\n A server comes up to you and asks, \"What would you like to order hun?\" as she raises her notepad and pen.', 
              'choices' : [('Coffee.', 'chapter1_cof'),
                         ('Latte.', 'chapter1_lat'),
                         ('Pumpkin Spice Frappuccino.', 'chapter1_fap'),
                         ('Nothing.', 'chapter1_not')],
              'stats_adj' : [[0,1,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]},

    'chapter1_sle': {'desc' : 'You attempt to go back to sleep but your mind is racing. You remember some sleeping pills that you were prescribed years ago when you worked for the agency. You head to the bathroom and fumble in your medicine bag for those sleeping pills. With the light from outside, you can barely make out the faded text on the prescripting sleeping pills. You haven\'t had to take these for years since your last case you thought. You open the bottle and swallow a pill, chasing it with some water from the sink. You head back to bed, setting an alarm for 15 minutes till 10 a.m. As you lay down, you don\'t even remember falling asleep. \n\n You suddenly wake up to the blaring of your alarm. Is it really 15 till you thought? Your question is confirmed as you look over at your clock: \"9:45 a.m.\" You get out of bed, use the bathroom, throw on the nearest set of clothes within reach, and exit your apartment door. The sun blinds you as you open the door. You feel like crap but you know that a cup of coffee will soon wake you up.\n\n As you enter the coffee shop, you look at your watch: \"10:08 a.m.\" 8 minutes late but the damage is done. You peer around the shop and your eyes fall on a familiar person. You walk over to booth where the person is sitting and slide into the opposite side. \n \"Detective Zhang?\" you ask curiously. \n \"Detective Bear, it has been awhile she says.\" She looks at her watch. \"Late as usual it seems. Not much seems to change it seems.\" she said dryly. \n \"Look, I\'m here. Do you want to talk or not?\" \n\n A server comes up to you and asks, \"What would you like to order hun?\" as she raises her notepad and pen.', 
              'choices' : [('Coffee.', 'chapter1_cof'),
                         ('Latte.', 'chapter1_lat'),
                         ('Pumpkin Spice Frappuccino.', 'chapter1_fap'),
                         ('Nothing.', 'chapter1_not')],
              'stats_adj' : [[0,1,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]},

    'chapter1_cof': {'desc' : '\"Coffee, black please. Thanks.\" \n \"Sure thing hon, be back in a minute.\" she says as she walks away.', 
              'choices' : [('Continue.', 'chapter1_cont')]},

    'chapter1_lat': {'desc' : '\"Latte please, with oatmilk. Thanks.\" \n \"Sure thing hon, be back in a minute.\" she says as she walks away.', 
              'choices' : [('Continue.', 'chapter1_cont')]},

    'chapter1_fap': {'desc' : '\"Venti Pumpkin Spice Frappuccino, with extra creamy oat milk, 3 pumps of pumpkin spice, extra whipped cream, and lined with caramel sauce. Thanks. \n Detective Zhang looks at your and raises an eyebrow. \n The server gives you a hard stare and states \"I hope that you understand that this is no Starbucks. If you want to order something like that, there\'s an ice cream shop down the street. So, I\'ll ask again, what would you like to order?\"', 
              'choices' : [('Coffee.', 'chapter1_cof'),
                         ('Latte.', 'chapter1_lat'),
                         ('Nothing.', 'chapter1_not')],
              'stats_adj' : [[0,1,0,0],[0,1,0,0],[0,0,0,0]},

    'chapter1_not': {'desc' : '\"I\'m good. Thanks.\" \n She walks away without saying anything. \n \"Did you quit drinking coffee Bear?\" \"No, just didn\'t feel like it this morning.\"', 
              'choices' : [('Continue.', 'chapter1_cont')]},

    'chapter1_cont': {'desc' : 'The coffee was poisoned. You fall onto the ground as the world fades to black.', 
              'end': 'die'}, 

    # '': {'desc' : '', 
    #           'choices' : [('', ''),
    #                      ('', '')]},
}


    
#### Machinery for running all games

# Beginning Stats
stats_beg =  {'stats': {'hp' : 3, 'mind' : 3, 'know' : 2, 'luck' : 0}}

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
        if not choices and end not in ("win","intro_end","die","stats"):
            print (pageid), ": no choices, but end not one of win|die"
            allok = False
    return allok

#Win and lose descriptions
def win():
    # When the player wins the game
    win_phrases = ['You push open the heavy oak door and a rush of cold, fresh air hits your face. You close your eyes and take a deep breath, savioring the rush of cold air as it enters your lungs. Your body aches, your clothes are covered in blood... but you and Detective Zhang are alive. \n\n \"You are a hell of a detective. How about coming back to the agency?\" Detective Zhang asked. \n You turn your head and look at Detective Zhang. Like you, she\'s covered in blood but her eyes are filled with fire, something that only younger detectives only have. \"How about a drink instead? You\re buying.\"']
    return random.choice(win_phrases)

def intro_end():
    # When the player quits early in the introduction
    lose_phrases = ['You toss and turn but sleep didn\'t come until the wee hours of the morning. You wake up the following day thinking that it must have just been all a dream. A few days later that you read in the newspapers that the body of Detective Zhang was found outside the city limits. Perhaps you could\'ve solved the case to prevent her death. She should\'ve left when you left you thought.']
    return random.choice(lose_phrases)

def hp_death():
    # When the player dies due to hp loss
    lose_phrases = ['You\'re not sure what happened. Perhaps it\'s the loss of blood or maybe your head separated from your body. It doesn\'t matter anymore. The last thing you see is the world slowly fading to black. All the good and bad moments flash before your eyes. Your last thoughts are of the things you have regretted and planned to do. Unfortunately, this is the end.']
    return random.choice(lose_phrases)

def mind_death():
    # When the player dies due to craze
    lose_phrases = ['The haunted mansion was a bit too much for you. You step back with a crazed look on your face. Your mind races, your vision becomes filled with montrosities you thought didn\'t exist. You run out of the mansion shouting: \"It\'s alive, it\'s alive and it\'s coming for all of you! \" as you point. Suddenly, you are thrown to the ground and the last thing you feel is a small prick on the back of your neck. \n\n As you wake up, your senses are dulled. You are surrounded by people in white coats. You yell at them, trying to explain the visions and things you learned at the mansion but are only met with puzzled looks. Try and try again you do but are only met with injections and puzzled looks. Days, weeks, years pass by. You see fewer and fewer people. Your senses become duller and duller as you sit on the hard, cold floor staring at verticle steel bars with each day the same as the last.']
    return random.choice(lose_phrases)

def lose():
    #''' a string to be printed when the player loses.'''
    lose_phrases = ['dead']
    return random.choice(lose_phrases)

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
               , 'know' : stats_beg['stats']['mind'] + stats_adj[i][1]
               , 'know' : stats_beg['stats']['know'] + stats_adj[i][2]
               , 'luck' : stats_beg['stats']['luck'] + stats_adj[i][3]
               }

    if int(stats_adj[i][0]) < 0 and int(stats_adj[i][3]) < 0:
        print('You lose ', int(stats_adj[i][0])*-1, ' hp. You lose ', int(stats_adj[i][3])*-1, ' knowledge.', sep = '')
    elif int(stats_adj[i][0]) > 0 and int(stats_adj[i][3]) < 0:
        print('You gain ', stats_adj[i][0], ' hp. You lose ', int(stats_adj[i][3])*-1, ' knowledge.', sep = '')
    elif int(stats_adj[i][0]) < 0 and int(stats_adj[i][3]) > 0:
        print('You lose ', int(stats_adj[i][0])*-1, ' hp. You gain ', stats_adj[i][3], ' knowledge.', sep = '')
    elif int(stats_adj[i][0]) > 0 and int(stats_adj[i][3]) > 0:
        print('You gain ', stats_adj[i][0], ' hp. You gain ', stats_adj[i][3], ' knowledge.', sep = '')
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
    
    while not page.get("end",None):

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

    if page['end'] == 'win':
        print(win())
    elif page['end'] == 'intro_end':
        print(intro_end())
    elif page['end'] == 'die':
        print(lose())
    elif stats_beg['stats']['hp'] <= 0:
        print(hp_death())
    elif stats_beg['stats']['mind'] <= 0:
        print(mind_death())
    else:
        print ("this shouldn't happen!")
    
    print ("\n" + pages.get("OUTRO","Thank you for playing, come back soon!")) 


## actually start the game, with our data
if __name__ == "__main__":
    game_cli(pages,"intro")