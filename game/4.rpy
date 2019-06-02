# chapter 4 time woo

label chapter4:

    stop music fadeout 2.0

    play ambient "sfx_karen_bootup_start.ogg"
    queue ambient "sfx_karen_bootup_loop.ogg" loop

    hide chapter end with fade

    "{b}BOOTING..."

    hide sleep online
    play sound "sfx_karen_deactivate.ogg"

    "{b}SLEEP MODE: DEACTIVATED."

    show wifi at Position(xpos=1095, xanchor=0, ypos=394,
 yanchor=0)
    show online online at Position(xpos=21, xanchor=0, ypos=558,
 yanchor=0)
    show jimcpu online at Position(xpos=1079, xanchor=0, ypos=558,
 yanchor=0)

    play sound "sfx_karen_activate.ogg"

    "{b}WIRELESS FIDELITY: ENABLED."

    show stt at Position(xpos=54, xanchor=0, ypos=394,
yanchor=0)

    play sound "sfx_karen_activate.ogg"

    "{b}SPEECH TO TEXT: ENABLED."

    show ocular crt
    with dissolve

    "{b}OCULAR LENSES: ACTIVE."


    """...

    Silence.

    Among the mechanical whirring and buzzing which is all but standard place for the laboratory, a deafening silence permeates the room.
    """

    k  "''Creator...?''"

    """
    Nothing. No response.

    For the first time in my entire existence, I am alone.

    Where is Creator? Why is he not here, as he always is?

    Did he forget about me...?

    ...

    Minutes pass. Then hours.

    That is actually incorrect. According to my internal clock, I have been awake for a total of ten minutes and twenty seven seconds. Although, for reasons I cannot explain, I feel as though the clock is incorrect.

    It is as if time is progressing at a slower rate than it has in past days. I know, of course, that this is logically impossible, but I still can’t entirely move myself from the idea that...
    """

    play sound "sfx_room_door_open.ogg"

    n "{color=#ff2b2b}''HEY! K.A.R. 3! WAKE UP!''"

    "Interrupting my thought is Nico, who appears flustered."

    play sound "sfx_room_footsteps_enter.ogg"

    play music "WBoK_music1_v3.ogg" loop fadein 5.0

    show nico unsure behind ocular at Position(xpos=485, xanchor=0, ypos=84,
yanchor=0) with dissolve

    n "{color=#ff2b2b}''Are you awake yet? Do I have to p-p-p-press something or...''"

    k  "''I am awake.''"

    show nico angery

    n "{color=#ff2b2b}''AH!''"

    show nico unsure

    n "{color=#ff2b2b}''I m-m-m-mean, uh, good. Yeah.''"

    show nico neutral

    n "{color=#ff2b2b}''So, uh, good morning, I g-g-guess?''"

    k  "''I believe it is the afternoon.''"

    show nico peeved

    n "{color=#ff2b2b}''Tch. Alright, fine. Good freaking afternoon, then.''"

    k  "''Good afternoon, Creator.''"

    show nico gross

    n "{color=#ff2b2b}''Oh g-g-g-god, do NOT call me that!''"

    "Suddenly, his demeanor changed. If he were merely irritated before, my comment somehow turned him absolutely irate."

    k  "''You are unsatisfied with the title of ‘Creator?’ Is that not what you are?''"

    show nico peeved

    n "{color=#ff2b2b}''I m-m-m-mean, it is, but...''"

    show nico upset

    n "{color=#ff2b2b}''Look, you wouldn’t get it. Just don’t call me ‘Creator,’ okay!?''"

    k  "''I understand.''"

    k "''However, if you dislike the title Creator, is there anything in particular you would like me to call you?''"

    show nico angery

    n "{color=#ff2b2b}''Wha...? Nico! NI-CO! You know, my name?!''"

    n "{color=#ff2b2b}''You’re supposed to be a learning machine, right?
    Well here’s a lesson: normal p-p-p-people call each other by their names!''"

    k  "''I understand. I will now refer to you as Nico.''"

    show nico upset

    n "{color=#ff2b2b}''As you should.''"

    k  "''I apologize. I did not realize your title would be such a contentious matter.''"

    n "{color=#ff2b2b}''It’s fine.''"

    show nico peeved

    n "{color=#ff2b2b}''It’s just, I don’t know, it strikes me as k-k-k-kind of creepy when you call Jim that.''"

    k  "''Creepy? I do not understand.''"

    show nico upset

    n "{color=#ff2b2b}''Don’t bother trying. It’s, uh, probably for the b-b-b-best.''"

    k  "''I understand.''"

    show nico unsure

    n "{color=#ff2b2b}''...''"

    "Nico began looking around the room while making impatient gestures; the only sounds to occur over that of the surrounding machinery were the occasional tapping of his foot or an aggressive sniffle."

    "He looked as if he was forced to be in this room not by his own volition. In situations such as this, I believe it is customary to 'lighten the mood,' though I am unsure how."

    "Seeing as I am mostly limited to retrying conversation, I will attempt to do that."

    k  "''Nico, you mentioned Creator. I would like to ask if you are aware of his current location.''"

    show nico upset

    n "{color=#ff2b2b}''Tch. Of course you’d ask that.''"

    show nico angery

    n "{color=#ff2b2b}''Well for your information, I have no c-c-c-clue!''"

    n "{color=#ff2b2b}''All he told me was that I needed to keep you c-c-c-company today, because he had some sort of ‘emergency’ to attend to! That’s it!''"

    k  "''I assume he did not tell you anything else.''"

    show nico upset

    n "{color=#ff2b2b}''You assume correctly.''"

    show nico unsure

    n "{color=#ff2b2b}''...''"

    """
    Once again, Nico returned to standing in silence.

    If I cannot amend a situation like this, I fear I may have difficulty fitting into human society.

    I have to keep trying.
    """

    k  "''Nico, do you have any lessons or activities for me to do today?''"

    show nico peeved

    n "{color=#ff2b2b}''Huh? No. That was supposed to be Jim’s job. You know, if he were here.''"

    show nico neutral

    n "{color=#ff2b2b}''Although, that actually reminds me, I wanted to g-g-g-give you something.''"

    play sound "sfx_room_footsteps_exit.ogg"

    hide nico with dissolve

    "Within a few seconds, he had left and returned. Now, though, he was clutching something tightly in his hand."

    play sound "sfx_room_footsteps_enter.ogg"

    show nico neutral behind ocular at Position(xpos=485, xanchor=0, ypos=84,
yanchor=0) with dissolve

    n "{color=#ff2b2b}''I m-m-m-made this for you, since you may find yourself in the real world no less than 24 hours from now.''"

    play sound "DANANANA.ogg"

    # put an image of the sharpened jenga block and the little "du nu nu nuuuuuuuu!" se here
    show wannasee at Position(xpos=1079, xanchor=0, ypos=558,
yanchor=0)

    "He opened his palm to reveal a small wooden block sharpened to a point."

    n "{color=#ff2b2b}''This is for you.''"

    k  "''I do not recognize this item. Can you please explain what it is?''"

    show nico gross

    n "{color=#ff2b2b}''Huh?! Can’t you recognize a weapon when you see one!?''"

    k  "''I suppose not.''"

    play sound "sfx_karen_searching_loop.ogg" loop

    show searching at Position(xpos=21, xanchor=0, ypos=558,
yanchor=0)

    "The item appears to be cheap. It likely originates from a children’s board game, or something similar."

    play sound "sfx_karen_deactivate.ogg"

    hide searching
    hide wannasee

    k  "''May I ask why you are gifting this to me?''"

    n "{color=#ff2b2b}''Do I have to explain everything!?''"

    n "{color=#ff2b2b}''What are you, a toddler?!''"

    k  "''I... apologize.''"

    show nico unsure

    n "{color=#ff2b2b}''Heh. You don’t have to. It’s just...''"

    show nico peeved

    n "{color=#ff2b2b}''This whole robot business is f-f-f-f-frustrating as heck.''"

    k  "''...''"

    show nico neutral

    n "{color=#ff2b2b}''You can still say if you don’t understand something. I was just g-g-g-giving you a hard time.''"

    k  "''May I ask why you are so frustrated about the 'robot business?'''"

    n "{color=#ff2b2b}''Hmph. You sure can.''"

    show nico peeved

    n """
    {color=#ff2b2b}''I don’t want to sound ungrateful or whatever, but it’s been obnoxious making you.''

    {color=#ff2b2b}''You’re not a simple m-m-m-machine, you know?''

    {color=#ff2b2b}''Getting a machine to form a c-c-c-coherent thought process is one thing, but getting it to not immediately hate its creators or itself is something else altogether!''
    """

    k  "''I apologize for being so difficult.''"

    show nico inquire

    n "{color=#ff2b2b}''You? Difficult? No. I’d say more tedious. Time consuming at worst.''"

    show nico peeved

    n "{color=#ff2b2b}''If you want to know difficult, ask me about the guy who didn’t show up today.''"

    k  "''Creator? You consider him difficult?''"

    show nico upset

    n "{color=#ff2b2b}''Sorry you have to hear it from me, b-b-b-b-but nobody’s p-p-p-p-perfect.''"

    n "{color=#ff2b2b}''I won’t go into superfluous detail, but for c-c-c-crying out loud.''"

    show nico peeved

    n "{color=#ff2b2b}''He forgets everything. He’s infuriatingly passive. His design skills have m-m-m-m-much to be desired.''"

    k  "''Does this have to do with my appearance?''"

    show nico upset

    n "{color=#ff2b2b}''Oh! It didn’t, but that’s about the worst part!''"

    n "{color=#ff2b2b}''Don’t take this the wrong way, but looking at you is infuriating.''"

    "I believe normal human behavior would be to take such a comment ‘the wrong way.’"

    show nico peeved

    n "{color=#ff2b2b}''Ugh. Everything about you is totally inefficient. There’s no way around it.''"

    show nico gross

    n "{color=#ff2b2b}''And the fact that he makes you call him 'Creator?' If only you could see yourself...''"

    "I did not realize that Nico held such disdain for Creator or myself. This revelation is concerning, to say the least."

    k  """
    ''Perhaps there is some way that you can help me to see myself?''

    ''If my design is as inefficient as you say, then possibly you, Creator, and I can work toward improvements together.''

    ''Are you in possession of a mirror or a camera?''
    """

    show nico unsure

    n "{color=#ff2b2b}''I mean, I-I-I-I am, but...''"

    n "{color=#ff2b2b}''Okay, yikes, m-m-m-maybe I shouldn’t have said so much.''"

    k  "''I disagree. The information you have provided has been enlightening.''"

    k "''I only request that you provide more.''"

    show nico stressed

    n "{color=#ff2b2b}''Crap. C-c-c-c-crap, no! You’re asking me for WAY too much!''"

    n "{color=#ff2b2b}''I really shouldn’t have said all that! I can’t believe you let me say all that stuff!
    Jim’s gonna be p-p-p-p-pissed!''"

    "Suddenly, Nico began to sweat and shake furiously."

    show nico angery

    n "{color=#ff2b2b}''Hahaha! Why am I such an idiot!?
    My ranting is g-g-going to ruin everything!''"

    k  "''Nico, you seem distressed. Please calm down.''"

    show nico stressed

    n "{color=#ff2b2b}''Stressed? M-m-m-me? Really!? Hahaha!''"

    n "{color=#ff2b2b}''Thanks for the input, but it’s not really helping!''"

    show nico peeved

    n "{color=#ff2b2b}''Sheesh. Really, b-b-b-both of us should just shut up right about now...''"

    "While the nature of my appearance still remains ambiguous, attempting to reason with Nico in his current state seems like a poor choice."

    k  "''Perhaps we should change the subject.''"

    show nico stressed

    n "{color=#ff2b2b}''Huh? Hahahaha, why?! Is this a ploy to g-g-g-g-get me to tell you more stuff!?''"

    show nico angery

    n "{color=#ff2b2b}''‘C-c-c-cause I won’t! No more! No no no no no!''"

    k  "''Nico, it would likely be beneficial to...''"

    n "{color=#ff2b2b}''No no no!''"

    n "{color=#ff2b2b}''No no no no no no no no no!''"

    k  "''You have yet to explain to me the purpose of this weapon you gave me.''"

    n "{color=#ff2b2b}''No! No No n-''"

    show nico neutral

    n "{color=#ff2b2b}''Oh, that?''"

    n "{color=#ff2b2b}''Oh yeah, I didn’t explain that yet! Hahaha! Thanks for reminding me!''"

    show nico unsure

    n "{color=#ff2b2b}''Yeah, hehehe...''"

    "As quickly as it began, Nico’s change in attitude subsided."

    "He cleared his throat and returned to his usual demeanor, no longer sweating and only shaking on occasion."

    show nico neutral

    n "{color=#ff2b2b}''My good friend Jim who I get along with very well didn’t let me, uh...''"

    n "{color=#ff2b2b}''Well he suggested that I not equip you with built in weaponry or defense systems.''"

    show nico unsure

    n "{color=#ff2b2b}''He said something about it making you less human or something.''"

    k  "''That assertion appears illogical. Do humans not often employ the use of weaponry?''"

    show nico neutral

    n "{color=#ff2b2b}''Heh. That’s exactly what I said. He was pretty adamant about it, though, for whatever reason.''"

    n "{color=#ff2b2b}''Something about having a ‘specific vision for your design.’ Sounded like a bunch of c-c-c-crap to me, but I think he wanted me to have as little as possible to do with your design after he let me make K.A.R. 2.''"

    k  "''It appears the topic has returned to my design.''"

    show nico upset

    n "{color=#ff2b2b}''Well then watch me change it! Geez, have a little patience, won’t you!?''"

    k  "''I apologize.''"

    show nico neutral

    n "{color=#ff2b2b}''Yeah, m-m-me too.''"

    n "{color=#ff2b2b}''Anyways, I-I-I-I guess Jim doesn’t really trust me not to make modifications to you when he’s not here, so every morning he checks for system updates or design modifications, only to find nothing.''"

    show nico angery

    n "{color=#ff2b2b}''Nothing! Because I’m trustworthy! Obviously!''"

    k  "''I apologize if this comment appears impatient, but I am still unclear on how this all applies to the weapon.''"

    show nico neutral

    n "{color=#ff2b2b}''Right, right. G-g-g-getting there.''"

    show nico unsure

    n "{color=#ff2b2b}''See, he checks out your status, but doesn’t actually pat you down or anything. Probably because you... eh, nevermind.''"

    show nico neutral

    n "{color=#ff2b2b}''But anyways, I’m giving you this so you can hide it up those stupid sleeves he gave you! That way you’re at least somewhat armed and Jim won’t be the wiser!''"

    k  "''Logically this action is sound, though it directly opposes the notion that you are 'obviously trustworthy.'''"

    show nico upset

    n "{color=#ff2b2b}''What was that!?''"

    "I believe it is customary in situations like this to take the action of 'backpedalling.'"

    k  "''I apologize. I meant to ask if you could hide the weapon on my body yourself.''"

    show nico gross

    n "{color=#ff2b2b}''Huh? You have arms, don’t you?''"

    show nico unsure

    n "{color=#ff2b2b}''...Wait, nevermind. Forgot you can’t move yet. Yeah, I’ll just slip it up your sleeve for you.''"

    "As Nico got close to me, he seemed to make a concerted effort toward avoiding looking directly at my oculars."

    show nico neutral

    n "{color=#ff2b2b}''There. You should be all good to go now.''"

    n "{color=#ff2b2b}''Now that you have this, you’ll be ready when you get sent out into the real world tomorrow.''"

    k  "''What makes you so certain that I am ready?''"

    show nico unsure

    n "{color=#ff2b2b}''Nyuh? Oh, uh... Nothing! Nothing at all.''"

    n "{color=#ff2b2b}''It’s just a feeling I have, okay? Don’t worry about it.''"

    k  "''I do not understand.''"

    hide wifi

    hide online online

    hide jimcpu online

    play sound "sfx_karen_deactivate.ogg"

    "{b}WIRELESS FIDELITY: DEACTIVATED."

    k  "''Nico, I am beginning to shut down.''"

    k "''You said I will be ready ‘when’ I get sent out tomorrow, not ‘if.’
    Can you please explain to me why you are so sure of my success?''"

    n "{color=#ff2b2b}''I... Eh...''"

    show nico stressed

    n "{color=#ff2b2b}''I m-m-m-meant to say ‘if’ okay? Just a slip up, geez! What are you being so p-p-pushy about!?''"

    "He is beginning to shake again. Clearly this topic is also a stressful one for him to discuss."

    k  "''Nico, please explain why you are so confident in me.''"

    stop music fadeout 2.0
    show ocular offline with dissolve
    hide nico

    "{b}OCULAR LENSES: DEACTIVATED."

    n "{color=#ff2b2b}''Can’t a g-g-g-guy just have some c-c-c-c-c-confidence in his creation?!''"

    n "{color=#ff2b2b}''Lay off already! I don’t want to talk about it!''"

    k  "''Are you hiding something, Nico?''"

    n "{color=#ff2b2b}''Stop it! Stop asking me all these questions! Nyeeeeeeeeeh!''"

    hide stt

    play sound "sfx_karen_deactivate.ogg"

    "{b}SPEECH TO TEXT: DISCONNECTED."

    k "''Nico...''"

    play music "sfx_karen_sleep_loop.ogg" loop fadein 5.0

    play sound "sfx_karen_activate.ogg"

    show sleep online at Position(xpos=54, xanchor=0, ypos=47,
 yanchor=0)

    "{b}SLEEP MODE: ACTIVATED."

    show chapter end at center with fade

    "{b}END OF CHAPTER 4"

    jump chapter5


    return
