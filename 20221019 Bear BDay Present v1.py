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

##########################################################################################################################################################
#Prelude
##########################################################################################################################################################

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
, 'The haunted mansion. Now there\'s a case you haven\'t heard in long time. You heard about it for the first time when you started at the agency. While normal cases were completed a few weeks after being assigned, this haunted mansion case was has been ongoing for years. Detectives normally assigned to it... left or disappeared for mysterious reasons. One detective resigned with no apparent reason. Another one was committed to an asylum shortly after their first report. Detective Florace and her assistant went missing. For one reason or another, this case never was completed. And now Detective Adytum fell to a similar, albeit more gruesome fate. You wonder...', '\n'
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

    'chapter1_sle': {'desc' : 'Chapter 1 \n\n You attempt to go back to sleep but your mind is racing. You remember some sleeping pills that you were prescribed years ago when you worked for the agency. You head to the bathroom and fumble in your medicine bag for those sleeping pills. With the light from outside, you can barely make out the faded text on the prescripting sleeping pills. You haven\'t had to take these for years since your last case you thought. You open the bottle and swallow a pill, chasing it with some water from the sink. You head back to bed, setting an alarm for 15 minutes till 10 a.m. As you lay down, you don\'t even remember falling asleep. \n\n You suddenly wake up to the blaring of your alarm. Is it really 15 till you thought? Your question is confirmed as you look over at your clock: \"9:45 a.m.\" You get out of bed, use the bathroom, throw on the nearest set of clothes within reach, and exit your apartment door. The sun blinds you as you open the door. You feel like crap but you know that a cup of coffee will soon wake you up.\n\n As you enter the coffee shop, you look at your watch: \"10:08 a.m.\" 8 minutes late but the damage is done. You peer around the shop and your eyes fall on a familiar person. You walk over to booth where the person is sitting and slide into the opposite side. \n \"Detective Zhang?\" you ask curiously. \n \"Detective Bear, it has been awhile she says.\" She looks at her watch. \"Late as usual it seems. Not much seems to change it seems.\" she said dryly. \n \"Look, I\'m here. Do you want to talk or not?\" \n\n A server comes up to you and asks, \"What would you like to order hun?\" as she raises her notepad and pen.', 
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
                         ('Take a back seat and let Detective Zhang lead.', 'chapter1_fol')]},

    'chapter1_fol1': {'desc' : '\"I insist that I will be the one leading this investigation Detective Zhang. There\'s no room to bargain with me on this\" \n \"Then there\'s nothing more to say.\" Detective Zhang curtly stated as she got up out of the booth. \"I can see why the agency forced you into early retirement.\" She picked up her coat and bag and heads out of the coffee shop. \n',  
        'end': 'chapter1_end'},

    'chapter1_fol': {'desc' : '\"I\'ve had my share of leading cases and following your lead would be a nice change of pace. So, what\'s the plan?\"', 
              'choices' : [('Continue.', 'chapter1_nex')]},

    'chapter1_nex': {'desc' : '\"I appreciate your understanding but I do realize that you have more experience than me in these matters, so don\'t be surprised if I ask for your input. As for next steps, I suggest to make any sort of preparations you think you may need. Unfortunately, because we never had a detective return from this case alive, we don\'t know what to plan for. Use your best judgement. Otherwise, let\'s plan on meeting at the mansion at dusk tonight.\" ', 
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

    'chapter1_tal': {'desc' : '\"There are a few things I have to take care of back in the apartment.\" you lie. \n \"Very well. See you at dusk.\" she said. \n She pays for the coffee and you both head out in separate directions. You pretend to head your separate ways and pretend to use your phone while keeping an eye on her. You can\'t put your finger on it but you just don\'t trust her. \n You put your phone away and follow her, keeping a safe distince from her. After about 15 minutes, she approaches a door on the first floor and enters. You quickly hop into the bush and proceed to spy on her from the window.',  
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

    'chapter2_fnt': {'desc' : 'You point at the massive oak doors behind Detective Zhang. \"Let\'s pick up from where Detective Adytum left off from.\" you said. \n\n As Detective Zhang steps aside, you attempt to push the door open; however it doesn\'t budge. You then further braced yourself and as you put more weight into it, the door begins to slowly creak and moan open. Once wide enough, you and Detective Zhang enter the mansion. You can barely make out the room until two beams of light light up what looks to be the two grand staircases that lead up to the second floor. You feel Detective Zhang tap you on the shoulder and hands you one of the flashlights. \"Thanks.\" you said. \n\n \"The mansion has a simple layout. There are two floors and the basement. The second floor are where the 5 bedrooms are. The first floor has several rooms: Kitchen, dining room, living room, billard\'s room, and servant\'s quarters. There are bedrooms on the second floor and we are currently in the hall.\" she explained. \"Where should we explore first?\" \n\n You ponder your options and decide to explore the:', 
              'choices' : [('Hall (current)', 'chapter2_hall'),
                         ('Kitchen', 'chapter2_kit'),
                         ('Dining Room', 'chapter2_din'),
                         ('Living Room', 'chapter2_liv'),
                         ('Billard\'s Room', 'chapter2_bil'),
                         ('Servant\'s Quarters', 'chapter2_ser'),
                         ('Bedroom', 'chapter2_bed')]},

    'chapter2_bak': {'desc' : 'You decide to take the road less travel and enter the mansion through the back door. As you circle around to the back of the mansion, you can barely make out what seems to be a gate blocking your path. You attempt to open the gate. Locked. You turn back towards Detective Zhang and say \"I thought you mentioned that we can get in through the back door. Didn\'t you check to make sure that the gate was unlocked?\" you snapped. \n \"That\'s odd. The gate wasy unlocked when I checked.\" She walks towards the gate and attempts to open the door but reaches the same conclusion as you. \n\n You sigh and look up at the sky closing your eyes. Off to a great start you thought. As you open your eyes, you noticed that while the gate door is lock, the gate itself isn\'t that tall and you could probably manage to get over and unlock the gate door from the inside. You were able to tell Detective Zhang this when she said, \"You can circle around to the otherside of the gated area and see if there\'s a door that we can use to enter the gated area to access. What do you think?\"', 
              'choices' : [('Circle around to the otherside', 'chapter2_oth'),
                           ('Ask Detective Zhang to give you a boost over the gate.', 'chapter2_boo')]},

    'chapter2_boo': {'desc' : '\"Give me a boost over the gate and I\'ll unlock it from the other side.\" you said. \n \"Good idea.\" she said. She puts her back to the gate and you step into her folder hands as she boosts you up. You briefly stand on her shoulders and easily hop over the gate.',  
        'end': 'chapter2_boo'},

    'chapter2_oth': {'desc' : '\"Let\'s circle around to the otherside of the gate and explore that area. Better to have more than less information.\" you stated. \n\n As you and Detective Zhang circle around to the otherside of the mansion, you don\'t notice anything out of the ordinary. Overgrown bushes, cracked windows, and weeds galore cover the lawn around the mansion. As you round the last corner, you see a similar gate door; as you try the gate door handle, you notice that it is unlocked. You open the gate door and enter with Detective Zhang following close behind you. \n\n Detective Zhang hands you a flashlight and you armored statues on either side of both gate doors holding a spear. All 4 are difficult to see due to the untrimmed bushes that are over 10 feet tall. As you go further into the rear of the mansion, you see the back door of the mansion to your left and a small shed to your right.', 
              'choices' : [('Enter the shed.', 'chapter2_shed'),
                         ('Enter the back door.', 'chapter2_back')]},

    'chapter2_shed': {'desc' : '\"Let\'s check out the shed.\" you suggested to Detective Zhang. As you are about to reach for the doorknob, you feel a hand on your shoulder. \n \"Let me go in first.\" Detective Zhang said. \"Trust me.\"', 
              'choices' : [('Let Detective Zhang go in first.', 'chapter2_shed_z'),
                         ('Ignore her and go in first.', 'chapter2_shed_end')]},

    'chapter2_shed_end': {'desc' : 'You shrug her hand and suggestion off. \"I got it.\" you quickly replied and opened the shed door.',  
        'end': 'chapter2_shed_end'},

    'chapter2_shed_z': {'desc' : 'You nod and take a step back as Detective Zhang steps between you and the door. You notice that she doesn\'t open the door right away and instead peers throw the little window in the door. You see her take out a flashlight and shine it inside the shed. \n \"Just as I thought. There is poisonous gas in the shed.\" she stated. \"Look, you can tell because there is a green and yellow tint. This is common in small, sealed rooms with various dangerous chemicals. Let\'s skip the shed and head towards the back door.\"', 
              'choices' : [('Skip the dangerous shed and enter the mansion through the back door.', 'chapter2_back'),
                           ('Ignore her and enter the shed.','chapter2_shed_end1')]},

    'chapter2_shed_end1': {'desc' : '\"A little gas isn\'t going to stop me. I have encounter worst things in my career.\" you said as you pushed Detective Zhang aside and open the shed door.',  
        'end': 'chapter2_shed_end'},

    'chapter2_back': {'desc' : '\"I think I am done exploring this rear area behind the mansion. Let\'s just enter through the back door.\" you said. \n Detective Zhang nods, \"Yes, let\'s.\" \n\n You walk towards the back door and enter the mansion. Your eyes tries to make sense of what you\'re seeing but it\'s diffcult now without the moonlight. Suddenly, you see two beams of light shine on the room. You feel Detective Zhang nudge you as she hands you a flashlight. As you hold up the flashlight, it becomes clear you are in the kitchen: Knives, island countertop, stove, etc all covered in a layer of dust. \n \"There are several rooms that we can explore, namely the hall, kitchen, dining room, living room, billard\'s room, and servant\'s quarters. There are bedrooms on the second floor.\" \n\n You ponder your options and decide to explore the:', 
              'choices' : [('Hall', 'chapter2_hall'),
                         ('Kitchen (current)', 'chapter2_kit'),
                         ('Dining Room', 'chapter2_din'),
                         ('Living Room', 'chapter2_liv'),
                         ('Billard\'s Room', 'chapter2_bil'),
                         ('Servant\'s Quarters', 'chapter2_ser'),
                         ('Bedrooms', 'chapter2_bed')]},

##########################################################################################################################################################
#Chapter 2: Hall
##########################################################################################################################################################

    'chapter2_hall': {'desc' : '\"Let\'s explore the hall.\ you decided. Detective Zhang nods and you begin your exploration of the hall. \n\n The hall is normally the first room that people see when entering the mansion. You notice several large windows to allow natural light in, although that is debateable due to the vines that cover the cracked windows. You notice several luxurious armchairs along with two sets of staircases that you guess lead to the second floor. Finally, you notice a very ornate chandelier in the middle of the ceiling, which was most likely to awe guests when they first enter." \n\n \"Why did you agree to join me on the haunted mansion case?\" Detective Zhang suddenly ask while looking around the hall with her flashlight. \"While it is great to work along side you, I honestly was a bit surprised by your answer.\"', 
              'choices' : [('\"I owe it to Detective Adytum. He taught me everything about being a detective.\"', 'chapter2_hall_det'),
                         ('\"I was bored and thinking about coming out of retirement. You were the catalyst you could say.\"', 'chapter2_hall_ret')]},

    'chapter2_hall_det': {'desc' : '\"That\'s admirable of you.\" she said. \"I had the pleasure of working closely with him until... well, you know\" she said as her voice trailed off. \"I\'ll be honest, he was like a mentor to me also, so losing him has been tough but I am glad that I have you to work on this case.\"', 
              'choices' : [('Continue', 'chapter2_hall_next')]},

    'chapter2_hall_ret': {'desc' : '\"Really? Most of the detectives that I have worked with all want to retire except for Detective Florace. She always joked that she wanted to die while on the job. Unfortunately, she went missing about a year ago and her whereabouts are still unknown.\"', 
              'choices' : [('Continue', 'chapter2_hall_next')]},

    'chapter2_hall_next': {'desc' : 'As we continued exploring the hall, Detective Zhang came across a lever towards the back of the hall. \"It looks like a rusted lever but I\'m not sure what it\'s for. I don\'t see any sort of cables or wires that lead from it. What should be do?\" she inquires.',  
              'choices' : [('Pull on the lever, see what it does.', 'chapter2_hall_lever'),
                         ('Best to play it safe. Ignore the lever.', 'chapter2_choice')]},

    'chapter2_hall_lever': {'desc' : '\"No sense in finding it and not testing it. Let\'s pull it.\"', 
              'choices' : [('Detective Bear pulls the lever.', 'chapter2_hall_bear'),
                           ('Detective Zhang pulls the lever.','chapter2_hall_zhang')],
              'stats_adj' : [[0,-1,0,0],[-2,0,0,0]]},

    'chapter2_hall_bear': {'desc' : '\"Here, allow me.\" I said as I step towards the lever and pull it. At first, the lever didn\'t budge; probably because it was rushed. However, with additional convincing, it did. At first, nothing happened. And then, a creak and snap. Suddenly, a loud crash from behind me. I quickly whirrled around to see that the chandelier has crashed down on Detecive Zhang, who was standing in the middle of the room. \n \"Detective Zhang!\" I yelled as I rushed to her side. \"Are you alright?\" \n You see her on the floor holding her left leg covered in blood. \"Ughhh. I\'m, I\'m okay I think. The chandelier scrapped me but just barely.\" she stammered. You see her reach a cloth bandage from her coat and wrap it around her left leg. \"That should hold until we get out. Don\'t worry about me. Let\'s continue.\" she said.', 
              'choices' : [('Continue', 'chapter2_choice')]},

    'chapter2_hall_zhang': {'desc' : '\"Why don\'t you pull the lever Detective Zhang as you found it.\" I said. She hestitated for a moment and then placed her hands on the lever. After a few tries, the lever finally moved. At first, nothing happened. And then, a creak and snap. Suddenly, a loud crash and a sharp pain shoot through my left arm. The chandelier that was on the ceiling fell on me, narrowly missing my head. The shock of the sound disoriented me and then, moments, later, my brain registered the pain. I stumbled backwards until I tripped over the rug and fell. \n \"Detective Bear!\" you heard Detective Zhang shout as she ran towards you. \"Are you alright?\" \n I clutch my arm and said \"I think so. I should be okay.\" \n \"Here, let me bandage that up for you.\" she said as she reaches into her coat for a cloth bandage and wraps my left arm. \n \"Thanks.\" \n \"That should hold until we get out of here.\"', 
              'choices' : [('Continue', 'chapter2_choice')]},

##########################################################################################################################################################
#Chapter 2: Kitchen
##########################################################################################################################################################

    'chapter2_kit': {'desc' : '\"Let\'s explore the kitchen. Perhaps we can get some grub.\" you joke. You turn your head to see if Detective Zhang cracked a smile but the silence says that she probably didn\'t. The kitchen is a fairly large space. You imagine that the size allowed several cooks, servers, and butlers to all be working at once, perhaps in preparations for a feast for several guests. As you shine your flightlight around, you don\'t notice anything out of the ordinary except for a door, which you think leads to a broom or cleaning closet of sorts and what looks like a large freezer door. You ponder your options and decide to:', 
              'choices' : [('\"Let\'s try this broom closet.\"', 'chapter2_kit_broom'),
                         ('\"The freezer door seems interesting enough.\"', 'chapter2_kit_freezer'),
                         ('\"Let\'s play it safe and move to a different room.\"', 'chapter2_kit_none')]},

    'chapter2_kit_broom': {'desc' : '\"Sounds like a plan.\" Detective Zhang confirms. She approaches the broom or cleaning closet door and asks: \"You ready?\"', 
              'choices' : [('\"Yeah, go ahead and open it.\"', 'chapter2_kit_broom_yes'),
                         ('\"Yeah but let me open the door.\"', 'chapter2_kit_broom_no')]},

    'chapter2_kit_broom_yes': {'desc' : 'She opens the door without issue and you both shine your flashlights on the unknown room. From behind Detective Zhang, all you can see are see shelves and shelves of cleaning supplies covered in cobwebs. You also see several brooms and stacks of buckets in a corner. For such a large mansion, you notice that this is quite a small cleaning closet. \n \"Something seems off about this closet it. Do you see what I mean?\" Detective Zhang asked.', 
              'choices' : [('Yes', 'chapter2_kit_broom_yes1'),
                         ('No', 'chapter2_kit_broom_no1')]},

    'chapter2_kit_broom_yes1': {'desc' : '\"Yes? I think so but if you could point it out, that would be great.\" \n You thought you hear a sigh but before you could process that, she says \"There\'s something odd. There are several large, empty bottles of lye. While it is a cleaning solution, it\'s not normal to have this much. It could perhaps before for...\" Her voice trails off and you put the pieces together. \"To dispose of a body.\" you say as you complete her thought. She nods. You both stood there in silence as you process this information. Detective Zhang then breaks the silence and asks', 
              'choices' : [('\"Yup, that\'s next on the list.\"', 'chapter2_kit_freezer'),
                         ('\"On second thought, I think I\'m done exploring the kitchen.\"', 'chapter2_choices')]},

    'chapter2_kit_broom_no1': {'desc' : '\"No, I don\'t think so. I think we\'ve explored as much of this room as possible.\" you said. Detective Zhang shrugs and asks \"Shall we take a look at the freezer door?\"', 
              'choices' : [('\"Yup, that\'s next on the list.\"', 'chapter2_kit_freezer'),
                         ('\"On second thought, I think I\'m done exploring the kitchen.\"', 'chapter2_choices')]},

    'chapter2_kit_broom_no': {'desc' : 'You open door without issue and you both shine your flashlights on the unknown room. Cleaning supplies on various shelves, brooms, mops, and buckets. Nothing out of the ordinary you thought. You take another moment and then close the door. \"Unremarkable.\" you said. \n \"Shall we take a look at the freezer door?\" Detective Zhang queried.', 
              'choices' : [('\"Yup, that\'s next on the list.\"', 'chapter2_kit_freezer'),
                         ('\"On second thought, I think I\'m done exploring the kitchen.\"', 'chapter2_choices')]},

    'chapter2_kit_freezer': {'desc' : 'You both walk over to the freezer. It\'s a tall, stainless steel door. As you shine your flashlight on it, you notice that the door has several scratches and the handle is quite worn, meaning that it was used quite a lot. If you stand quietly enough, you can hear a gentle hum. Hum? \"Detective Zhang, does this mansion still have all the utilities connected and running you ask?\" \n \"As far I know yes. All the bills and everything are paid in full and on time. I tried looking into who is paying the bills and it seems that the estate has a tidy sum of money that just continues to pay the bills. Actually, the estate fund is so much that the interest itself is enough to pay all the bills in perpetuity.\" she said. \n \"Interesting. Thanks for looking into that.\" you said. That\'s quite impressive that she was able to look into and find all that information. \n \"Let me get this door.\" you said.', 
              'choices' : [('Continue', 'chapter2_kit_freezer1')]},

    'chapter2_kit_freezer1': {'desc' : 'You place you hand on the cold, worn handle of the freezer and as you open it, you feel a rush of frigid air smack you in the face. You shine your flashlight in the freezer room and see different cuts of meat on meathooks. Cow, goat, lamb. You even see some other meat that you don\'t recognize, probably something exotic you thought. \n \"Do you see the door all the way in the back?\" asked Detective Zhang. \"Should we explore it?\"', 
              'choices' : [('\"Yes but stand guard and hold this door open while I explore.\"', 'chapter2_kit_freezer1_bear'),
                         ('\"Yes but I\'ll stand guard and hold this door open while you explore.\"', 'chapter2_kit_freezer1_zhang'),
                         ('\"No, I think we\'ve seen enough.\"','chapter2_choices')],
              'stats_adj' : [[-1,0,0,0],[0,0,0,0],[0,0,0,0]]},

    'chapter2_kit_freezer1_bear': {'desc' : 'Detective Zhang nods and you step deeper into the freezer. You begin to shiver as you didn\'t dress appropriately to  be in sub-zero temperatures. As you approach the inner freezer door, you notice it is a bit smaller but still made out of stainless steel. You place your hand on the freezing handle and gave it a good pull. No dice. You try again and again, no dice. You look around the edges of the door and notice ice around it due to condensation. You spot a crowbar nearby and within a few short moments, got rid of all the ice around the door. You attempt to pull the door open and after a few tries, you hear a crunch and groan as the door open.', 
              'choices' : [('Continue', 'chapter2_kit_freezer1_bear1')]},

    'chapter2_kit_freezer1_bear1': {'desc' : 'Simutaneously, you hear a scream and a thud from behind you followed by a slamming of a door. You quickly turn around and with you flashlight, you see that Detective Zhang on the floor. You quickly look behind her and see that the door is no longer open. \"Are you okay? What happened?\" you frantically asked. \n \"Someone pushed me from behind!\" she said gasping for air. She too turned around and found a handle. However, upon using it, it didn\'t seem to be working. \"No good. The door handle isn\'t working.\" \n Your stomach drops. You\'re trapped. You then realized that you haven\'t explored the other room that you opened and rush to see if there is perhaps another way out.', 
        'end': 'chapter2_kit_freezer_end'},

    'chapter2_kit_freezer1_zhang': {'desc' : 'You see her hesitate but you reassure her, saying \"Don\'t worry, I got it.\" She nods and steps deeper into the freezer. You see her shine her flashlight on the door and have trouble opening it. You see her look around, pick something up, knocking ice all around the door. She attempts to open the door and when she succeeds, you feel a powerful push from behind you. \n\n You fall to the ground and you feel a sharp pain shoot up through you left leg. You scream in pain but you aim your flashlight in the doorway where you were standing. Nothing. You thtought you saw a fleeting shadow but no one was there. \n\n \"Are you alright? What happened?\" Detective Zhang frantically asked. \n \"Someone pushed me from behind and tried to close the freezer door on us. Luckily, my leg kept the door open. Ughh.\" you say as the pain in your leg throbbed. \n \"Let\'s get out of the freezer first.\" she said. You helped you up and moved you to the center of the kitchen. As she tended to your leg, you scanned the kitchen, looking for the fleeting shadow that you thought you saw. Nothing. \n \"Your leg is okay but it could be a fracture. I\'ll make a makeshift splint that should hold until we get out of here.\" she said. You nod and with a wooden spoon from a kitchen drawer and some twine, she helped stablized your left leg. \n\n That was close you thought. The worst part of it is that you and Detective Zhang aren\'t alone.', 
              'choices' : [('Continue', 'chapter2_choice')]},

##########################################################################################################################################################
#Chapter 2: Dining Room
##########################################################################################################################################################

    'chapter2_din': {'desc' : '\"I think the dining room is a good room to explore next.\" you said. You and Detective Zhang stroll over to the dining room, which is right next to the kitchen. The dining room is immaculate. You note the ornate dining table and chairs in addition to the flatware and silverware on the table. You notice that windows aren\'t cracked and there doesn\'t seem to be a speck of dust on the furniture. However, that is what makes it unsettling. Supposedly, no one has been inside the mansion since Detective Adytum, so for the dining room to be spotless is out of place to say the least. \n \"Are you seeing what I am seeing?\" Detective Zhang asked as she shines her flashlight at spot on the dining table. Your old eyes must\'ve missed it but you do see it: Two plates, with food on them. You both gave each other a concerned look and walked over to the plates of food. \n\n A closer look shows that it\'s mashed potatoes and gravy along with asparagus and green beans. You also see a few slices of white meat, which you guess to be either chicken or turkey breast. You also see a glass of redish liquid in a wine glass and a glass of clear liquid in a cup. Finally, the food is piping hot. It\'s been a long journey and you and Detective Zhang are famish. You decided that you should:', 
              'choices' : [('Eat the food.', 'chapter2_din_eat'),
                           ('Ignore the food.', 'chapter2_din_noeat')],
              'stats_adj' : [[2,1,0,0],[0,-1,0,0]]},

    'chapter2_din_noeat': {'desc' : 'You and Detective Zhang summon all your might and courage and ignore the food. You believe that\'s the safest course of action but you feel your sanity wavier. All the way at the other end of the table, you could see two cats, sitting at attention next to each other, stare at you two. From the light of the moon, you could tell that one was pure black and the other was pure white. While studying them, they both took a short moment to groom themselves before staring at both of you again.', 
              'choices' : [('Pet the black cat.', 'chapter2_din_black'),
                         ('Pet the white cat.', 'chapter2_din_white'),
                         ('Pet both cats.', 'chapter2_din_both'),
                         ('Don\'t pet either cat.', 'chapter2_din_nopet')],
              'stats_adj' : [[0,0,0,2],[0,0,0,1],[0,0,0,-2],[0,0,0,-1]]},

    'chapter2_din_eat': {'desc' : 'Your hunger outweighs the disturbing nature of how the food came to be. You look at Detective Zhang and she too seems to be in a similar boat. \"I\'m going to take a chance.\" you said as you walk toward the food and sit down. The chair is extremely comfortable and you figure each chair must\'ve cost several thousand dollars and be able to be sat in at least 50,000 times before the fabric would show signs of wear. Detective Zhang seems to have come to the same conclusions as you about the chair also, minus the durability though. You smell the food and it smells... like food, really good food. You take the fork in your hand and take a bit of the vegetables; so does Detective Zhang. You both look at each other as you chew and nervously swallow. An eerie silence hangs in the air and you both seem fine. On top of that, the food is extremely delicious and you both start eating without saying a word to each other. In a few minutes, the food has disappeared from both of your plates. You need to quench your thrist and you both decide to:', 
              'choices' : [('Drink the redish liquid.', 'chapter2_din_wine'),
                         ('Drink the clear liquid.', 'chapter2_din_water'),
                         ('Drink the redish and clear liquids.', 'chapter2_din_water')]},

    'chapter2_din_water': {'desc' : 'You reach for the glass with the clear liquid and glup it down; Detective Zhang follows suit. It tastes like water and it refreshes your palette. You let out a pleasant sigh and say \"That was one great meal wasn\'t it?\" \n Detective Zhang nods. \"Yes and it couldn\'t have came at a more perfect time. This meal was a great way to break up this detective work.\" \n You agree and you and Detective Zhang chatted for a few minutes. You both decided to get a bit more comfortable and retired to 2 overstuffed arm chairs in the dining room. As you continue your conversation, you noticed that Detective Zhang was slurring her words; and you also noticed that ou were slurring your words also.', 
        'end': 'chapter2_din_water_end'},

    'chapter2_din_wine': {'desc' : 'You reach for the red liquid and swirl it in the wine glass. You give whiff and could smell the aroma of the grapes that were used to create it. \"It\'s wine.\" you said to Detective Zhang as you gave it a sip. She followed suit. You let out a pleasant sigh and say \"That was one great meal wasn\'t it?\" \n Detective Zhang nods. \"Yes and it couldn\'t have came at a more perfect time. This meal was a great way to break up this detective work.\" \n\n You chat for a few moments enjoy the break in the case when you had a feeling that someone or ones were watching you and Detective Zhang. All the way at the other end of the table, you could see two cats, sitting at attention next to each other, stare at you two. From the light of the moon, you could tell that one was pure black and the other was pure white. While studying them, they both took a short moment to groom themselves before staring at both of you again.', 
              'choices' : [('Pet the black cat.', 'chapter2_din_black'),
                         ('Pet the white cat.', 'chapter2_din_white'),
                         ('Pet both cats.', 'chapter2_din_both'),
                         ('Don\'t pet either cat.', 'chapter2_din_nopet')],
              'stats_adj' : [[0,0,0,2],[0,0,0,1],[0,0,0,-2],[0,0,0,-1]]},

    'chapter2_din_black': {'desc' : 'You both approach the black cat. Slowly, you reach out with your hand. The black cat sniffs your hand and marks you and white cat jumps down from the dining table and walks away. You give it a little scratch behind the ears and it begins to purr. The black cat stares at you with its big, green eyes, which you interpret as happiness and comfort. Detective Zhang reaches out and also begins to pet the black cat, who continues to purr. Within a few minutes, the black cat jumps down from the dining table, stretches and disappears into the shadows. While black cats are normally associated with bad omens, you both feel good about this encounter.', 
              'choices' : [('Continue', 'chapter2_choice')]},

    'chapter2_din_white': {'desc' : 'You approach the white cat. Slowly, you reach out with your hand. The white cat doesn\'t react to your hand but you see the black cat jump down from the dining table and walks off into the shadows. You and Detective Zhang begin to pet it and you can hear a very faint purring. It stares at you with it\'s blue eyes, full of sadness. As you give it more pets, you notice a collar on the white cat that reads: \"Waffles\". After a few more moments of petting, the white cat jumps downs and darts into the shadows.', 
              'choices' : [('Continue', 'chapter2_choice')]},

    'chapter2_din_both': {'desc' : 'You approach both cats and slowly reach out to pet both of them. Abruptly, they both hiss at you and jump down and dart into the shadows. Perhaps you were too greedy and you should\'ve just pet one cat.', 
              'choices' : [('Continue', 'chapter2_choice')]},

    'chapter2_din_nopet': {'desc' : 'Cats are bad omens, especially in a haunted mansion such as this. You see Detective Zhang approach the cats but you put a hand on her shoulder. She looks back at you and gestures to the two cats but you shake your head. She sighs, understanding what you mean. You both stand there looking at the two cats as they are looking at you. A few moments later, both cats jump down and walk off, disappearing into the shadows. ', 
              'choices' : [('Continue', 'chapter2_choice')]},

##########################################################################################################################################################
#Chapter 2: Living Room
##########################################################################################################################################################

    'chapter2_liv': {'desc' : '\" Let\'s check out the living room. There are no dangeous or sharp objects there normally, so it should be safer than the other rooms.\" you say. Detective Zhang nods and leads the way to the living room. \n\n In a few minutes, you are greeted with a massive double glass door. Detective Zhang opens the doors and you see one of the largest rooms you ever came across. From a rough estimate, you believe that this living can fit at least 2, may 3 of your tiny apartment. You look around with you flashlight and like most of the mansion, the sofas are covered in dirt and dust as if they have not been used in a long time. Coffee tables, expensive but torn rugs, and end tables, all old and some even broken. However, in one corner of the room, you see what appears to be a fairly clean, overstuffed sofa. It looks quite tempting and you feel as if it\'s inviting you to take a load of your feet.', 
              'choices' : [('It\'s been a long night. Take a break on the sofa.', 'chapter2_liv_sofa'),
                         ('It seems sus. Ignore the temptation.', 'chapter2_liv_cont')],
              'stats_adj' : [[1,1,0,0],[0,0,0,0]]},

    'chapter2_liv_sofa': {'desc' : '\"Let\'s take a seat Detective Zhang.\" you say as you gesture towards to the inviting, sofa. She looks at the sofa questioningly and then glances at you. You give her a nod and gesture at the sofa again as if saying: \"It\'s fine. There\'s nothing to worry about.\" You walk over the L-shaped sofa and take a seat. You immediately feel relaxed as the sofa seems to conform to your sore and aching body. You look at Detective Zhang and pat the sofa cushion next to you. She seems to relax as she sees you and takes a seat on the couch just a few feet away from you. You can also immediately see the tension and stress leave her body. \n\n \"Tell me about Detective Shoshie. You mention that her methods were... a bit more direct than other detectives. What did you mean by that?\" you askd Detective Zhang. \n She slowly opened her eyes when you asked her that question. After a few moments, she said \"While her methods were unusual, she got results. And fast. Most detectives would take days or even weeks to either solve a case but not Shoshie. She would be able to wrap up a case in just a matter of a day or two. I believe her longest case took her a week but that was a particularly complex case.\" \n \"What case was that?\" you asked. \n Detective Zhang gave you a confused look. \"You mean you never heard or read about it? I\'m a bit surprised because it was a famous case at the agency. Basically, Detective Shoshie\'s case was about a missing rocket. You would think: How does one lose a rocket? Piece by piece is seems according to what Shoshie found. However, the case didn\'t stop there and executives kept asking for more and more information. The case kept going on until the seventh day when Shoshie submitted her final report on the case along with her resignation.\" \n \"I heard she was working though but you said that she resigned?\" \n \"Just because she submitted her resignation doesn\'t mean the agency allowed her to resign. She was one of their best detectives; they couldn\'t afford to have her resign. They gave her a huge pay bump and two weeks of paid leave.\"', 
              'choices' : [('Continue', 'chapter2_liv_sofa1')]},

    'chapter2_liv_sofa1': {'desc' : 'You both continued chatting, unsure of how much time has passed. You didn\'t notice until just now but it seems that you have been sinking into the sofa. You look over and it also seems that Detective Zhang has been sinking into the couch too. Your pulse quickens at the thought that the sofa has a mind of its own and could perhaps be trying to swallow you.', 
              'choices' : [('Fight the urge to sink into the couch.', 'chapter2_liv_sofa1_fig'),
                           ('Trust the sofa, what has it ever done to you?', 'chapter2_liv_sofa1_tru')],
              'stats_adj' : [[0,-2,0,0],[1,0,0,0]]},

    'chapter2_liv_sofa1_fig': {'desc' : 'As comfortable as it is, you fight the urge to let yourself further sink into the couch. You summon all your energy and might to push yourself out of the sofa. You failed. You try and try again and after several attempts, you are able to free yourself of the sofa. You look back at where you sat and see a deep imprint of your torso, butt and tights. You could stand to lose pounds you thought. You then suddenly remember Detective Zhang. You quickly turn towards her direction and run over to her. You see her also trying to fight to get out of the sofa. You quickly grab both of her hands and attempt to help pull her out of the sofa. After a few attempts, you give a big pull and freed Detective Zhang. Unfortunately, you both lost your balance and she lands on top of you.', 
              'choices' : [('Push her off of you and ask if she\'s okay.', 'chapter2_liv_sofa1_fig1'),
                           ('Kiss her.', 'chapter2_liv_sofa1_fig_kiss')]},

    'chapter2_liv_sofa1_fig_kiss': {'desc' : 'You\'re not sure what came over you. Maybe it was the warmth of her body or the smell of her hair. Without thinking, you lean over and kiss her in the heat of the moment. A silence hung in the air and it seems as if everything stood still. You are jolted awake with a searing slap to the face.', 
        'end': 'chapter2_liv_sofa1_fig_kiss_end'}, 

    'chapter2_liv_sofa1_fig1': {'desc' : 'You push her off of you. Once you get up, you help her up. \"You alright?\" you asked her. \n You can see the adrenaline rushing through her. \"Could be better. But at least I\'m alive. Thanks.\" she said. A few moments hung in the air as you both stared at the sofa. The indentations that your bodies made in the cushions slowly disappear. As you stare at the sofa, you suddenly feel a tug to sit in it again. You then feel a hand on your shoulder, bringing you back to reality. \"You ready to explore the rest of the living room?\" Detective Zhang asked. ', 
              'choices' : [('\"Let\'s see what\'s up with that chimney.\"', 'chapter2_liv_cont'),
                         ('\"I think I\'m done exploring this room. What\'s next?\"', 'chapter2_choice')]},

    'chapter2_liv_sofa1_tru': {'desc' : 'You push away those thoughts and close your eyes. You feel as if the sofa is gently cradling your tired, worn body. Moments, minutes, hours seem to pass by. \n\n \"Detective Bear? Are you awake?\" said Detective Zhang. You open your eyes and you see her standing in front of you. \"How long have I been asleep?\" you asked. \n \"Not long. Maybe 10 or 15 minutes. Shall we get moving?\". You nod and slowly get up from the sofa. You feel quite well rested for a 10 to 15 minute power nap. You really should get information on who makes this couch and the brand you thought.', 
              'choices' : [('Check the sofa out for the make and model.', 'chapter2_liv_sofa1_tru_model'),
                          ('Ignore the sofa. It\'s probably too expensive anyway.', 'chapter2_liv_cont')],
              'stats_adj' : [[0,-5,0,0],[0,0,0,0]]},

    'chapter2_liv_sofa1_tru_model': {'desc' : '\"Give me a second. I want to see if I can purchase this exact sofa for my apartment.\" you said as you turn back towards the sofa. You walk around the sofa seeing if there is a tag of sorts but see nothing. You don\'t find any sofa pillows and begin to lift the cushion to see where the tag could be. As you lift the cushion up, you see bones, sinew, skin, most likely human skin. You feel the blood rush from your face and a cold chill runs up your spine. You feel a cold sweat come over you as your push the cushion back down and back away from the sofa, tripping in the process. \n \"What happened? What\'s wrong?\" Detctive Zhang asked hurriedly. \n You look at her, wided eye. You can feel your heart beating through you chest.', 
              'choices' : [('Continue', 'chapter2_liv_cont')]},

    'chapter2_liv_cont': {'desc' : '\"I believe the last thing for us to check out is the fireplace over there.\" You see her pointing at a massive brick chimney against the wall. You vaguely remembering seeing from the outside of the mansion but it was difficult due to the overgrown vegetation. You ponder whether you should explore it or not.', 
              'choices' : [('\"Let\'s see what\'s up with that chimney.\"', 'chapter2_liv_chim'),
                         ('\"I think I\'m done exploring this room. What\'s next?\"', 'chapter2_choice')]},

    'chapter2_liv_chim': {'desc' : '', 
              'choices' : [('', ''),
                         ('', '')]},

    # '': {'desc' : '', 
    #           'choices' : [('', ''),
    #                      ('', '')]},

    # '': {'desc' : '', 
    #           'choices' : [('', ''),
    #                      ('', '')]},

    # '': {'desc' : '', 
    #           'choices' : [('', ''),
    #                      ('', '')]},

    # '': {'desc' : '', 
    #           'choices' : [('', ''),
    #                      ('', '')]},

##########################################################################################################################################################
#Chapter 2: Billard's Room
##########################################################################################################################################################

    'chapter2_bil': {'desc' : '', 
              'choices' : [('', ''),
                         ('', '')]},

    # '': {'desc' : '', 
    #           'choices' : [('', ''),
    #                      ('', '')]},

    # '': {'desc' : '', 
    #           'choices' : [('', ''),
    #                      ('', '')]},

##########################################################################################################################################################
#Chapter 2: Servant's Quarters
##########################################################################################################################################################

    'chapter2_ser': {'desc' : '', 
              'choices' : [('', ''),
                         ('', '')]},

    # '': {'desc' : '', 
    #           'choices' : [('', ''),
    #                      ('', '')]},

    # '': {'desc' : '', 
    #           'choices' : [('', ''),
    #                      ('', '')]},
    
##########################################################################################################################################################
#Chapter 2: Bedrooms
##########################################################################################################################################################

    'chapter2_bed': {'desc' : '\"Let\'s go explore the bedrooms.\" you suggest. As you begin to walk to the Hall and go up the stairs, Detective Zhang said, \"I think we only should head upstairs once we\'ve finished exploring the first floor. Are you ready to head up stairs?\"', 
              'choices' : [('\"No, you\'re right. Let\'s finish exploring the first floor.\"', 'chapter2_choice'),
                           ('\"Yes, I\'m ready. Let\'s see what\'s on the second floor.\"', 'chapter2_bed1')]},

    'chapter2_choice': {'desc' : '\"We still have rooms to explore in this mansion Detective Bear. Where should we head next?\" \n\n You ponder your options and decide to explore the:', 
              'choices' : [('Hall', 'chapter2_hall'),
                         ('Kitchen', 'chapter2_kit'),
                         ('Dining Room', 'chapter2_din'),
                         ('Living Room', 'chapter2_liv'),
                         ('Billard\'s Room', 'chapter2_bil'),
                         ('Servant\'s Quarters', 'chapter2_ser'),
                         ('Bedrooms', 'chapter2_bed')]},

    # '': {'desc' : '', 
    #           'choices' : [('', ''),
    #                      ('', '')]},
}


    
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
        if not choices and end not in ("win","intro_end","chapter1_end","chapter1_zha","chapter2_boo","chapter2_shed_end","chapter2_kit_freezer_end","chapter2_din_water_end","chapter2_liv_sofa1_fig_kiss_end","die","stats"):
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

def chapter2_boo():
    # When the player gets a boost over the gate
    lose_phrases = ['As gravity takes you down through the bushes, you scream as you feel a sudden, sharp pain near your left thigh and in your right shoulder. With the full moon out, you quickly see the horror: You leapt over a gate onto a spear being held by a statue covered in plate armor that was hidden in the overgrown bushes. You struggle to find something to grasp onto to to use a leverage to perhaps push yourself off. In the horror and pain, you are barely able to hear Detective Zhang scream and mutter something into her cell phone. Soon, you feel the pain less and less. The full moon becomes dimmer and dimmer until suddenly you vision fails you and the world becomes a permanent black.']
    return random.choice(lose_phrases)

def chapter2_shed_end():
    # When the player enters the shed first
    lose_phrases = ['As you enter the shed, the first thing you notice is a sweet smell along with old machinary used to care for the outside of the mansion such as rakes, a couple of lawn mowers, and hedge trimmers. After taking a few additional steps, you begin gasping for air as you are unable to breathe. You suddenly feel light headed and dizzy. As you turn your head to see where Detective Zhang is, you noticed that not only has she not entered the shed but she took a few steps back. As you tried to listen to what she is saying, you suddenly lose your balance and fall on to the cold ground of the shed. Still gasping for air, the last thing you remember is trying to crawl out of the shed before being overcome by a sense of heaviness and calm.']
    return random.choice(lose_phrases) 

def chapter2_kit_freezer_end():
    # When the player enters the shed first
    lose_phrases = ['As you open the door, you see bodies. Bodies on hooks. You drop your flashlight as you step back. You feel that you fate sealed and that your future is on one of these hooks. You turn around and start banging on the door, screaming that you and Detective Zhang be let out. After several minutes, the cold starts to reach your bones and you throat feels rasp. As the cold begins to settle in, you consciousness fades in and out. You\'re not sure but you feel you can hear shuffling and the ticking of a clock, just outside of the freezer door.']
    return random.choice(lose_phrases)

def chapter2_din_water_end():
    # When the player enters the shed first
    lose_phrases = ['You both suddenly realized that you both were getting sleepier and sleepier. Could it be a food coma you thought? It was good food but it wasn\'t a large amount to warrant that you thought. You see Detective Zhang try to stand up from the chair but failing. You tried to do the same but you couldn\'t either. Your eyelids suddenly got heavier and heavier until you couldn\'t keep them open anymore. Your hearing was the last of your senses to fail you and you a shuffling that got louder and louder. The last thing you heard was a groan from Detective Zhang and what sounded like she was being picked up. You tried to say something but whatever you drank, finally overcame you.']
    return random.choice(lose_phrases)

def chapter2_liv_sofa1_fig_kiss_end():
    # When the player enters the shed first
    lose_phrases = ['You see Detective Zhang jump up. You can\'t tell whether she\'s blushing or furious. \n\n \"What are you doing?\" she screamed \"This is not the time for something like that. Besides, Detective Ad... Wait, I don\'t have to explain myself to you. Also, no one can know about this.\" You see her reach into her coat and take out a revolver. \n\n You quickly stand up. \"Wait a second, it was a mistake. It was all in the moment.\" you quickly said holding your hand up. You begin to slowly walk over to her. \"Don\'t do this. We can just say that nothing happened and forget about it see?\" \n\n Suddenly, you hear two deafening shots from in front of you. You feel your chest explode with fire as you stumble and fall on the ground. You feel weaker and colder with every passing moment until you are unable to feel anything.']
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
    elif page['end'] == 'intro_end':
        print(intro_end())
    elif page['end'] == 'chapter1_end':
        print(chapter1_end())
    elif page['end'] == 'chapter1_zha':
        print(chapter1_zha())
    elif page['end'] == 'chapter2_boo':
        print(chapter2_boo())
    elif page['end'] == 'chapter2_shed_end':
        print(chapter2_shed_end())
    elif page['end'] == 'chapter2_kit_freezer_end':
        print(chapter2_kit_freezer_end())
    elif page['end'] == 'chapter2_din_water_end':
        print(chapter2_din_water_end())
    elif page['end'] == 'chapter2_liv_sofa1_fig_kiss_end':
        print(chapter2_din_water_end())
    elif page['end'] == 'die':
        print(lose())
    else:
        print ("this shouldn't happen!")
    
    print ("\n" + pages.get("OUTRO","The End.")) 


## actually start the game, with our data
if __name__ == "__main__":
    game_cli(pages,"intro")