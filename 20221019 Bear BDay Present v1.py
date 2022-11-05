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
                         ('\"No, I think we\'ve seen enough.\"','chapter2_choices')]},
              'stats_adj' : [[-1,0,0,0],[0,0,0,0],[0,0,0,0]],

    'chapter2_kit_freezer1_bear': {'desc' : 'Detective Zhang nods and you step deeper into the freezer. You begin to shiver as you didn\'t dress appropriately to  be in sub-zero temperatures. As you approach the inner freezer door, you notice it is a bit smaller but still made out of stainless steel. You place your hand on the freezing handle and gave it a good pull. No dice. You try again and again, no dice. You look around the edges of the door and notice ice around it due to condensation. You spot a crowbar nearby and within a few short moments, got rid of all the ice around the door. You attempt to pull the door open and after a few tries, you hear a crunch and groan as the door open.', 
              'choices' : [('Continue', 'chapter2_kit_freezer1_bear1')]},

    'chapter2_kit_freezer1_bear1': {'desc' : 'Simutaneously, you hear a scream and a thud from behind you followed by a slamming of a door. You quickly turn around and with you flashlight, you see that Detective Zhang on the floor. You quickly look behind her and see that the door is no longer open. \"Are you okay? What happened?\" you frantically asked. \n \"Someone pushed me from behind!\" she said gasping for air. She too turned around and found a handle. However, upon using it, it didn\'t seem to be working. \"No good. The door handle isn\'t working.\" \n Your stomach drops. You\'re trapped. You then realized that you haven\'t explored the other room that you opened and rush to see if there is perhaps another way out.', 
        'end': 'chapter2_kit_freezer_end'},

    'chapter2_kit_freezer1_zhang': {'desc' : 'You see her hesitate but you reassure her, saying \"Don\'t worry, I got it.\" She nods and steps deeper into the freezer. You see her shine her flashlight on the door and have trouble opening it. You see her look around, pick something up, knocking ice all around the door. She attempts to open the door and when she succeeds, you feel a powerful push from behind you. \n\n You fall to the ground and you feel a sharp pain shoot up through you left leg. You scream in pain but you aim your flashlight in the doorway where you were standing. Nothing. You thtought you saw a fleeting shadow but no one was there. \n\n \"Are you alright? What happened?\" Detective Zhang frantically asked. \n \"Someone pushed me from behind and tried to close the freezer door on us. Luckily, my leg kept the door open. Ughh.\" you say as the pain in your leg throbbed. \n \"Let\'s get out of the freezer first.\" she said. You helped you up and moved you to the center of the kitchen. As she tended to your leg, you scanned the kitchen, looking for the fleeting shadow that you thought you saw. Nothing. \n \"Your leg is okay but it could be a fracture. I\'ll make a makeshift splint that should hold until we get out of here.\" she said. You nod and with a wooden spoon from a kitchen drawer and some twine, she helped stablized your left leg. \n\n That was close you thought. The worst part of it is that you and Detective Zhang aren\'t alone.', 
              'choices' : [('Continue', 'chapter2_choice')]},

##########################################################################################################################################################
#Chapter 2: Dining Room
##########################################################################################################################################################

    'chapter2_din': {'desc' : '', 
              'choices' : [('', ''),
                         ('', '')]},

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
        if not choices and end not in ("win","intro_end","chapter1_end","chapter1_zha","chapter2_boo","chapter2_shed_end","chapter2_kit_freezer_end","die","stats"):
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
    lose_phrases = ['As you open the door, you see bodies. Bodies on hooks. You drop your flashlight as you step back. You feel that you fate sealed and that your future is on one of these hooks. You turn around and start banging on the door, screaming that you and Detective Zhang be let out. After several minutes, the cold starts to reach your bones and you throat feels rasp. As the cold begins to settle in, you consciousness fades in and out. You\'re not sure but you feel you can hear shuffling and the ticking of a clock, just outside of the freezer door. ']
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
    elif page['end'] == 'die':
        print(lose())
    else:
        print ("this shouldn't happen!")
    
    print ("\n" + pages.get("OUTRO","The End.")) 


## actually start the game, with our data
if __name__ == "__main__":
    game_cli(pages,"intro")