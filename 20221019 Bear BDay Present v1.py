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
, 'The haunted mansion. Now there\'s a case you haven\'t heard in long time. You heard about it for the first time when you started at the agency. While normal cases were completed a few weeks after being assigned, this haunted mansion case was an ongoing on. Detectives normally assigned to it... left for mysterious reasons. One detective resigned with no apparent reason. Another one was committed to an asylum shortly after their first report. Detective Florace and her assistant went missing. For one reason or another, this case never was completed. And now Detective Adytum fell to a similar, albeit more gruesome fate. You wonder...', '\n'
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

##########################################################################################################################################################
#Chapter 1
##########################################################################################################################################################

    'chapter1_res': {'desc' : 'Chapter 1 \n\n Fuck it you thought. You get out of bed and start the coffee maker. You hop into the shower and the steam from the hot water wakes and refreshes you. You throw on some clothes, grab a hot cup of coffee and begin sifting through old papers and internet searches to catch up on the case. \n\n Several hours pass by and you rub your eyes as you push back from the table. Papers and notes are strewned all over but you have a better grasp of the details of the case. You look at you watch: \"9:30 a.m.\" Plenty of time to get to the meeting point you thought as you yawn. You pocket the notes that you took and grabbed your coat as you head out the front door. You feel mentally exhausted but feel more prepared for the meeting with... that\'s right, you still don\'t know who you\'re meeting you thought. \n\n As you enter the coffee shop, you look at your watch: \"9:56 a.m.\" Plenty of time to spare you thought. You peer around the shop and your eyes fall on a familiar person. You walk over to booth where the person is sitting and slide into the opposite side. \n \"Detective Zhang?\" you ask curiously. \n \"Detective Bear, it has been awhile she says.\" She looks at her watch. \"Early, that\'s a surprise.\" she said. \n \"I stayed up after your call to review the facts and details of the case.\" \n She raises an eyebrow. \"So you\'re running on no sleep then for this very important case?\" she inquires? \n \"It\'s something I\'m used to doing when I worked for the agency.\" I lied. Maybe I should\'ve gotten that extra sleep... \n\n A server comes up to you and asks, \"What would you like to order hun?\" as she raises her notepad and pen.', 
              'choices' : [('Coffee.', 'chapter1_cof'),
                         ('Latte.', 'chapter1_lat'),
                         ('Pumpkin Spice Frappuccino.', 'chapter1_fap'),
                         ('Nothing.', 'chapter1_not')],
              'stats_adj' : [[0,1,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]]},

    'chapter1_sle': {'desc' : 'You attempt to go back to sleep but your mind is racing. You remember some sleeping pills that you were prescribed years ago when you worked for the agency. You head to the bathroom and fumble in your medicine bag for those sleeping pills. With the light from outside, you can barely make out the faded text on the prescripting sleeping pills. You haven\'t had to take these for years since your last case you thought. You open the bottle and swallow a pill, chasing it with some water from the sink. You head back to bed, setting an alarm for 15 minutes till 10 a.m. As you lay down, you don\'t even remember falling asleep. \n\n You suddenly wake up to the blaring of your alarm. Is it really 15 till you thought? Your question is confirmed as you look over at your clock: \"9:45 a.m.\" You get out of bed, use the bathroom, throw on the nearest set of clothes within reach, and exit your apartment door. The sun blinds you as you open the door. You feel like crap but you know that a cup of coffee will soon wake you up.\n\n As you enter the coffee shop, you look at your watch: \"10:08 a.m.\" 8 minutes late but the damage is done. You peer around the shop and your eyes fall on a familiar person. You walk over to booth where the person is sitting and slide into the opposite side. \n \"Detective Zhang?\" you ask curiously. \n \"Detective Bear, it has been awhile she says.\" She looks at her watch. \"Late as usual it seems. Not much seems to change it seems.\" she said dryly. \n \"Look, I\'m here. Do you want to talk or not?\" \n\n A server comes up to you and asks, \"What would you like to order hun?\" as she raises her notepad and pen.', 
              'choices' : [('Coffee.', 'chapter1_cof'),
                         ('Latte.', 'chapter1_lat'),
                         ('Pumpkin Spice Frappuccino.', 'chapter1_fap'),
                         ('Nothing.', 'chapter1_not')],
              'stats_adj' : [[0,1,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]]},

    'chapter1_cof': {'desc' : '\"Coffee, black please. Thanks.\" \n \"Sure thing hon, be back in a minute.\" she says as she walks away.', 
              'choices' : [('Continue.', 'chapter1_cont')]},

    'chapter1_lat': {'desc' : '\"Latte please, with oatmilk. Thanks.\" \n \"Sure thing hon, be back in a minute.\" she says as she walks away.', 
              'choices' : [('Continue.', 'chapter1_cont')]},

    'chapter1_fap': {'desc' : '\"Venti Pumpkin Spice Frappuccino, with extra creamy oat milk, 3 pumps of pumpkin spice, extra whipped cream, and lined with caramel sauce. Thanks. \n Detective Zhang looks at your and raises an eyebrow. \n The server gives you a hard stare and states \"I hope that you understand that this is no Starbucks. If you want to order something like that, there\'s an ice cream shop down the street. So, I\'ll ask again, what would you like to order?\"', 
              'choices' : [('Coffee.', 'chapter1_cof'),
                         ('Latte.', 'chapter1_lat'),
                         ('Nothing.', 'chapter1_not')],
              'stats_adj' : [[0,1,0,0],[0,1,0,0],[0,0,0,0]]},

    'chapter1_not': {'desc' : '\"I\'m good. Thanks.\" \n She walks away without saying anything. \n \"Did you quit drinking coffee Bear?\" \"No, just didn\'t feel like it this morning.\"', 
              'choices' : [('Continue.', 'chapter1_cont')]},

    'chapter1_cont': {'desc' : '\"I\'ll get right to the point Detective Bear. Detective Adytum is dead and HQ has put me in charge with this investigation. As you know, this case has been ongoing for sometime and previous detectives on this case have not had very fortunate endings. I was hoping that you and I could work this case together.\"\n While I knew that I would be working this case, I didn\'t expect to work side by side with Detective Zhang. When you left the agency, she was still a junior detective. However, she probably rose through the ranks to become one of the more senior detectives. \n \"So we would be working together then?\" I asked. \n \"HQ put be in charge of this case and asked me to find another detective to work with me on it. I reviewed several files and while you have had a... colorful past, I believe that we can work well together with me as the lead detective of course.\"', 
              'choices' : [('\"I should be the lead detective.\".', 'chapter1_led'),
                         ('\"I don\'t mind following your lead on this case\"', 'chapter1_fol'),
                         ('\"What other files did you review?\".', 'chapter1_oth')]}, 

    'chapter1_oth': {'desc' : '\"Detective Katamal was quite qualified to work this case but when her sister, Detctive Florace, went missing, she took a leave of absence and hasn\'t been reachable since. Detective Shoshie was another consideration but her methods on solving cases... let\'s just say that she is a bit too direct at times. Finally, I looked into Detective Nesane. While she has a great track record on completing cases, the majority of cases she has been working were simple and straightfoward. As you know, this case is anything but.\"',  
              'choices' : [('\"I should be the lead detective.\".', 'chapter1_led'),
                         ('\"I don\'t mind following your lead on this case\"', 'chapter1_fol')]}, 

    'chapter1_led': {'desc' : '\"I have more experience in investigations Detective Zhang and I believe I should be the one to lead this case.\" I stated. \n \"The agency specifically asked me to lead this case. There isn\'t any room for negotiation on this. Either you let me lead this case or I will continue on this case without you.\" You know from experience that the agency tends to be... inflexible at times. Also, detectives in the field tend to play loose with \"who is the lead detective and all of that.\"', 
              'choices' : [('Put your foot down. Either you lead or you\'re out.', 'chapter1_fol1'),
                         ('Take a back seat and let Detective Zhang lead.', 'chapter1_fol2')]},

    'chapter1_fol1': {'desc' : '\"I insist that I will be the one leading this investigation Detective Zhang. There\'s no room to bargain with me on this\" \n \"Then there\'s nothing more to say.\" Detective Zhang curtly stated as she got up out of the booth. \"I can see why the agency forced you into early retirement.\" She picked up her coat and bag and headed out of the coffee shop. \n',  
        'end': 'chapter1_end'},

    'chapter1_fol': {'desc' : '\"I\'ve had my share of leading cases and following your lead would be a nice change of pace. So, what\'s the plan?\"', 
              'choices' : [('Continue.', 'chapter1_nex')]},

    'chapter1_nex': {'desc' : '\"I appreciate your understanding but I do realize that you have more experience than me in these matters, so don\'t be surprised if I asked for your input. As for next steps, I suggest to make any sort of preparations you think you may need. Unfortunately, because we never had a detective return from this case alive, we don\'t know what to plan for. Use your best judgement. Otherwise, let\'s plan on meeting at the mansion at dusk tonight.\" ', 
              'choices' : [('Take a nap. You could use the additional sleep.', 'chapter1_nap'),
                         ('Meditate at your apartment.', 'chapter1_med'),
                         ('Do some additional research on the case.', 'chapter1_res1'),
                         ('You don\'t trust Detective Zhang. Tail her.', 'chapter1_tal')],
              'stats_adj' : [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,0]]},

    'chapter1_nap': {'desc' : '\"There are somethings I need to take care of back home. I\'ll meet you at dusk at the mansion.\" you tell Detective Zhang. \n \"Very well. See you at dusk.\" she said. \n She pays for the coffee and you both head out in separate directions. Of course, the thing you need to do at home is catch up on that sweet, sweet sleep. You bed looks inviting as you head home and you barely remember as you jump into bed. \n\n You wake up just before sunset and you make your way over to the mansion, where you already see Detective Zhang waiting for you.', 
              'choices' : [('Continue.', 'chapter2')]},

    'chapter1_med': {'desc' : '\"I will meditate on this and meet you at dusk at the mansion.\" you tell Detective Zhang. \n She raises an eyebrow. \"Very well. See you at dusk.\" she said. \n She pays for the coffee and you both head out in separate directions. As you head back to your apartment, you tidy up a little bit and sit in a comfortable position on the floor. As you close your eyes, you empty your mind and focus on yourself and breathing. \n\n You finish your meditation just before sunset and you make your way over to the mansion, where you already see Detective Zhang waiting for you.', 
              'choices' : [('Continue.', 'chapter2')]},

    'chapter1_res1': {'desc' : '\"I will meditate on this and meet you at dusk at the mansion.\" you tell Detective Zhang. \n She raises an eyebrow. \"Very well. See you at dusk.\" she said. \n She pays for the coffee and you both head out in separate directions. As you head back to your apartment, you tidy up a little bit and sit in a comfortable position on the floor. As you close your eyes, you empty your mind and focus on yourself and breathing. \n\n You finish your meditation just before sunset and you make your way over to the mansion, where you already see Detective Zhang waiting for you.', 
              'choices' : [('Continue.', 'chapter2')]},

    'chapter1_tal': {'desc' : '\"There are a few things I have to take care of back in the apartment.\" you lie. \n \"Very well. See you at dusk.\" she said. \n She pays for the coffee and you both head out in separate directions. You pretend to head your separate ways and pretend to use your phone while keeping an eye on her. You can\'t put your finger on it but you just don\'t trust her. \n You ut your phone away and follow her, keeping a safe distince from her. After about 15 minutes, she approaches a door on the first floor and enters. You quickly hop into the bush and proceed to spy on her from the window.',  
        'end': 'chapter1_zha'},

##########################################################################################################################################################
#Chapter 2
##########################################################################################################################################################

    'chapter2': {'desc' : 'Chapter 2 \n\n Daylight slowly speeds away as you walk towards Detective Zhang. You\'ve seen the mansion in pictures and the news: A 2 story tall retanglar home with colonial style windows. Everything about the mansion scream opulence. Well, at least it used to 50 years ago. With dusk quickly approaching, you can tell barely make out the creeping vines along the cracks in the wall, the roof missing several tiles, and the overgrown bushes in front of the mansion. \n \"Good evening Detective Bear. I did an initial scout of the mansion and there are two ways to enter. We can enter through the front door or through the back door. The front door is where all previous detectives used while the back door, while known, has not been used before but is unlocked.\"', 
              'choices' : [('Let\'s pick up where the other detectives left off. Front door.', 'chapter2_fnt'),
                         ('Let\'s carve out own path. Back door.', 'chapter2_bak'),
                         ('Let\'s try to find another way in. Look around.','chapter2_lok')],
              'stats_adj' : [[0,0,0,0],[0,0,0,0],[-1,0,0,0]]},

    'chapter2_lok': {'desc' : 'You decide to look around the mansion in search of another entrance. However, 30 minutes later, you are where you started with additional scraps and scratches from the bushes that you explored. Unfortunately, you options have little changed.', 
              'choices' : [('Let\'s pick up where the other detectives left off. Front door.', 'chapter2_fnt'),
                         ('Let\'s carve out own path. Back door.', 'chapter2_bak')]},

    'chapter2_fnt': {'desc' : 'You point at the massive oak doors behind Detective Zhang. \"Let\'s pick up from where Detective Adytum left off from.\" you said. \n\n As Detective Zhang steps aside, you attempt to push the door open; however it doesn\'t budge. You then further braced yourself and as you put more weight into it, the door begins to slowly creak and moan open. Once wide enough, you and Detective Zhang enter the mansion. You can barely make out the room until two beams of light light up what looks to be the two grand staircases that lead up to the second floor. You feel Detective Zhang tap you on the shoulder and hands you one of the flashlights. \"Thanks.\" you said. \n\n ', 
              'choices' : [('', ''),
                         ('', '')]},

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
        if not choices and end not in ("win","intro_end","chapter1_end","chapter1_zha","die","stats"):
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

def chapter1_end():
    # When the player quits early in the introduction
    lose_phrases = ['She had some nerve you thought to call you in the middle of the night and ask you to follow \"her\" lead on this case when you clearly had more experience in the field. You got up from the booth and headed back home. \n\n Days and weeks pass. Having nothing to work on has a way of making time blur together. You turn on the TV one evening and suddenly became pale at what you heard: \n\n \"This has just came in. Detective Zhang of the agency was found dead in the outskirts of town. Police are still investigating but there is currently no lead on who committed this crime. More on this tonight at 11.\" \n\n Your stomach begins twisting and you feel sick to the point you had to sit down in your dusty old recliner. You just spoke to her a few weeks ago. Perhaps if you put aside your ego, the outcome would have been differnt.']
    return random.choice(lose_phrases)

def chapter1_zha():
    # When the player decides to stalk Detective Zhang
    lose_phrases = ['She suddenly stops in the middle of her room and takes out her cell phone. After a few minutes, she puts it away and enters another room. You shift to a different window but she angled the door such that you can\'t see what she\'s doing. The door suddenly opens. In a few moments, a flash, a crash, and mind numbing bang fills your ears. You fall on your back and feel a warm pool around your head. Blood. Your blood. As your mind fades to black, you see Detective Zhang looking down on you and shaking her head. \"What are you even doing?\" she asks. You see her make a call on her phone but you don\'t catch any of the words as the world fades away.']
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
    elif page['end'] == 'chapter1_end':
        print(chapter1_end())
    elif page['end'] == 'chapter1_zha':
        print(chapter1_zha())
    elif page['end'] == 'die':
        print(lose())
    elif stats_beg['stats']['hp'] <= 0:
        print(hp_death())
    elif stats_beg['stats']['mind'] <= 0:
        print(mind_death())
    else:
        print ("this shouldn't happen!")
    
    print ("\n" + pages.get("OUTRO","The End.")) 


## actually start the game, with our data
if __name__ == "__main__":
    game_cli(pages,"intro")