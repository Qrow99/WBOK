# Guess we're just playing this one by ear
# Whatever the heck that means

label chapter5:

    stop music fadeout 2.0

    play ambient "sfx_karen_bootup_start.ogg"
    queue ambient "sfx_karen_bootup_loop.ogg" loop

    $ E1 = 0
    $ E2 = 0
    $ E3 = 0

    hide chapter end with fade

    "{b}BOOTING..."

    hide sleep online
    play sound "sfx_karen_deactivate.ogg"
    show jim neutral behind ocular at Position(xpos=527, xanchor=0, ypos=115,
yanchor=0)

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

    play music "WBoK_music1_v3.ogg" loop fadein 5.0
    show ocular crt
    with dissolve

    "{b}OCULAR LENSES: ACTIVE."

    show jim happy

    j "{color=#f388b8}''Good afternoon, Karen.''"

    k "''Creator, you're here.''"

    show jim embarassed

    j "{color=#f388b8}''I am, yeah...''"
    j "{color=#f388b8}''So I suppose an apology is in order, huh? I really should've told
    you that I couldn't make it to the lab yesterday.''"

    k "''I was unsure of your whereabouts. I was alone.''"

    # I'm just going to do the name colors later bc it's easier that way :P

    show jim neutral

    j "{color=#f388b8}''Yeah, in retrospect I should've asked Nico to get here before you woke up...''"

    play sound "sfx_karen_searching_loop.ogg" loop

    show searching at Position(xpos=21, xanchor=0, ypos=558,
yanchor=0)

    j "{color=#f388b8}''I'm sorry if I made you worry.''"

    play sound "DING.ogg"

    hide searching

    "Worry. Verb. To allow one’s mind to dwell on difficulty or troubles."

    k "''I was, in fact, quite worried.''"

    show jim embarassed

    j "{color=#f388b8}''Aw man... At least that means you're still learning well, I guess.''"

    show jim happy

    j "{color=#f388b8}''Regardless, there's something I want you to see, or rather feel?''"

    k "''I do not understand what you mean.''"

    j "{color=#f388b8}''Well you will!''"

    show jim neutral

    j "{color=#f388b8}''At least, you will if it works.''"
    j "{color=#f388b8}''I just have to activate some things and then...''"

    play sound "sfx_karen_activate.ogg"

    show ns online at Position(xpos=1095, xanchor=0, ypos=47,
 yanchor=0)

    "{b}NERVOUS SYSTEM: ACTIVE."

    "Suddenly, I was made aware of the plentiful nerves in my body."
    "Arms, legs, fingers, and various other aspects of my physique are all present, just as was illustrated in the blueprints."
    "In spite of this revelation, I find that I am unable to move."
    "Though I can feel and even adjust the position of my body slightly, some form of restraints keep me locked upright, with my wrists held together and my neck stuck in place."

    show jim inquire

    j "{color=#f388b8}''So, how do you feel?''"

    k "''Creator, I cannot move.''"

    show jim happy

    j "{color=#f388b8}''So you are feeling properly! That's good.''"

    k "''I can feel, but I cannot move. Why am I restrained?''"

    show jim neutral

    j "{color=#f388b8}''For your own safety, mostly.''"

    show jim embarassed

    j "{color=#f388b8}''Also because your parts are expensive.''"
    j "{color=#f388b8}''Just because you can feel doesn’t mean you can walk; even something as adept at learning as you would still have the motor skills of an infant thirty seconds after finding out it has legs.''"

    k "''May I be freed soon? I believe it would be difficult to complete my prime directive while immobile.''"

    show jim happy

    j "{color=#f388b8}''You make a good point, and I understand that you want to move around, but please remember that we have something even more important to do today!''"

    "It is Friday. Amidst all this afternoon’s commotion, I had nearly forgotten that it was the day of my final exam."
    "Although, it is technically impossible for me to ‘forget’ information in the traditional sense."

    j "{color=#f388b8}''And hey, if you keep saying stuff like that, I have a feeling you'll do just fine.''"

    k "''What do you mean?''"

    j "{color=#f388b8}''Like I said, you made a good point!''"
    j "{color=#f388b8}''Logical argumentation is a crucial aspect of communication, so it’s good that you have a grasp on it.''"

    k "''Thank you.''"

    j "{color=#f388b8}''You're welcome.''"
    j "{color=#f388b8}''Manners are also crucial for communication so, hey, you get points there too.''"

    k "''I assume that that comment was a meant facetiously, and that these notions of preemptive ‘points’ are meant to be taken as jokes.''"

    show jim neutral

    j "{color=#f388b8}''They are, yes.''"

    k "''I see. Ha ha ha ha.''"

    show jim embarassed

    j "{color=#f388b8}''Um, thanks.''"
    j "{color=#f388b8}''On that note, I'm going to go grab the first section of your test.''"

    play sound "sfx_room_footsteps_exit.ogg"

    hide jim with dissolve

    "Creator left and quickly returned, now holding a thin pack of papers."

    play sound "sfx_room_footsteps_enter.ogg"

    show jim happy behind ocular at Position(xpos=527, xanchor=0, ypos=115,
yanchor=0) with dissolve

    j "{color=#f388b8}''Now why don't we get started?''"
    j "{color=#f388b8}''The faster we get done with this, the faster we you can walk on up and out of those bindings.''"

    k "''That is assuming I pass.''"

    show jim neutral

    j "{color=#f388b8}''...Yes.''"

    k "''Creator, I noticed that you referred to this as the first section of the test, does that mean there are multiple sections?''"

    show jim happy

    j "{color=#f388b8}''That's correct. There are three sections in total.''"

    show jim embarassed

    j "{color=#f388b8}''They were meant to relate to the lessons I had planned for Tuesday, Wednesday, and Thursday respectively, but... extraneous circumstances occurred.''"

    show jim happy

    j "{color=#f388b8}''It’s nothing to worry about, though! I’m sure you’ll do just fine regardless!''"
    j "{color=#f388b8}''Anyways, let's get started!''"

    show chapter end at center with fade

    show jim neutral

    "{b}..."

    hide chapter end with fade

    show jim happy

    j "{color=#f388b8}''Alright1 That's the end of the first section, good job!''"
    j "{color=#f388b8}''Now, if you'll excuse me, I'm going to go grab the second part...''"

    k "''Creator, why are you giving each section individually?''"
    k "''Would it not make more sense to have all the papers at once?''"

    j "{color=#f388b8}''That's a good question!''"

    show jim neutral

    j "{color=#f388b8}''I could tell you that there’s an official, or at least organizational, reason for me splitting it up into three parts.''"

    show jim embarassed

    j "{color=#f388b8}''I could say that, but the truth is I just don’t want to carry all those papers together at once.''"

    show jim happy

    j "{color=#f388b8}''Be right back!''"

    play sound "sfx_room_footsteps_exit.ogg"

    hide jim with dissolve

    "Creator departs, and I am once again left alone."
    "This time, however, the silence hardly lasts, as another figure soon enters the room."

    play sound "sfx_room_footsteps_enter.ogg"

    show rick neutral behind ocular at Position(xpos=485, xanchor=0, ypos=84,
yanchor=0) with dissolve

    r "{color=#FC983B}''Good afternoon, Miss Karen.''"

    k "''Rick Morrison. Good afternoon to you, also.''"
    k "''Are you looking for Creator?''"

    r "{color=#FC983B}''I'm not.''"
    r "{color=#FC983B}''In fact, I came here for you. I wanted to congratulate you.''"

    k "''Congratulate me for what?''"

    show rick smug

    r "{color=#FC983B}''For being the subject of the school newspaper’s most popular article in recent history!''"

    k "''I am?''"

    show rick excited

    r "{color=#FC983B}''Undoubtedly! Views for the web page have skyrocketed in the past 72 hours!''"

    show rick smug

    r "{color=#FC983B}''We've nearly made it to double digits.''"

    k "''That is good news.''"

    show rick neutral

    r "{color=#FC983B}''I agree. It's all thanks to you.''"
    r "{color=#FC983B}''Therefore I’d like to extend my most sincere gratitude and congratulations.''"

    k "''I am flattered.''"

    r "{color=#FC983B}''No need to be.''"
    r "{color=#FC983B}''...''"
    r "{color=#FC983B}''Anyways, I suppose I should be on my way.''"
    r "{color=#FC983B}''If I recall, today is your testing day, correct? I would hate to waste any more of your time, so I will be taking my leave.''"

    """
    Rick Morrison began to leave.

    Though, before he could, a strange, foreign feeling began to wash over me.

    The origin of this feeling I cannot locate, but that is irrelevant. What does matter is that, for one reason or another, I am compelled to ask Rick Morrison something.
    """

    k "''Rick, please wait.''"

    show rick inquire

    r "{color=#FC983B}''Pardon?''"

    k "''I would like to ask you a question.''"

    show rick smug

    r "{color=#FC983B}''Well then, hopefully I have an answer.''"

    # for now, I'm going to just put in the choices and do fill them in later because...
    # because idk I feel like it

    menu:
        k "''I wanted to ask...''"

        "Are we friends?":
            jump R1

        "May I shake your hand?":
            jump R2

        "Can you free me?":
            jump R3

label R1:
    play sound "sfx_karen_activate.ogg"
    $ E2 += 1
    k "''Rick, would you consider me to be your friend?''"

    show rick neutral

    r "{color=#FC983B}''Customarily, I try not to connect emotionally with my clients.''"

    k "''I see.''"

    show rick smug

    r "{color=#FC983B}''However, as I’ve said before, you are no customary client.''"

    k "''I suppose not.''"

    r "{color=#FC983B}''Considering how much you’ve done for me and my work, I would be remiss to not at least see you in a positive light.''"

    k "''I see.''"

    show rick inquire

    r "{color=#FC983B}''Though now you've made me curious; would you consider me to be a friend of yours?''"

    k "''I believe that I would, yes.''"

    show rick smug

    r "{color=#FC983B}''Well, I'm rather happy to hear that.''"

    show rick neutral

    r "{color=#FC983B}''Though, on that note, I believe I should be on my way. It really has been a pleasure, Miss Karen.''"


    jump FRICK

label R2:
    play sound "sfx_karen_activate.ogg"
    $ E1 += 1
    k "''Rick Morrison, I would like to shake your hand.''"

    show rick smug

    r "{color=#FC983B}''Well, of course! I would never deny the prospect of a friendly handshake.''"

    show rick inquire

    "Rick hesitated. He looked down at my arms, and then back at me."

    r "{color=#FC983B}''Although, in this instance, I may have to make an exception.''"

    k "''I am sure Creator could reattach the binding when he returns.''"
    k "''Please, this would mean a lot to me.''"

    r "{color=#FC983B}''You are asking me to break your bindings?''"

    k "''Only for a moment.''"

    show rick think

    r "{color=#FC983B}''...''"

    show rick neutral

    r "{color=#FC983B}''Alright, I will oblige. If only because you have done much for me.''"

    play sound "sfx_room_leather_snap.ogg"

    "Deftly, Rick detached the strap keeping my hands in place. He then proceeded to extend his hand and grip mine."
    "His hand is warm, and his grip is firm. As he moves his forearm, I attempt to follow, but end up complicating the procedure."
    "Clearly, I will need more practice with this maneuver."

    show rick smug

    r "{color=#FC983B}''It really was a pleasure working with you this week, Miss Karen.''"

    show rick neutral

    r "{color=#FC983B}''And on that note, I believe I must be on my way. Goodbye.''"


    jump FRICK

label R3:
    play sound "sfx_karen_activate.ogg"
    $ E3 += 1
    k "''Rick, can you break the straps binding my arms?''"

    show rick inquire

    r "{color=#FC983B}''Break the straps?''"
    r "{color=#FC983B}''Why would you want that?''"

    k "''As of today, I have gained the ability to feel and move. However, Creator will not allow me to leave this spot. It is troubling.''"

    show rick think

    r "{color=#FC983B}''I see...''"

    show rick inquire

    r "{color=#FC983B}''Though, there must be a reason for Mister MacGuffin keeping you bound, is there not?''"

    k "''He says it is because I could fall and damage myself if not looked after.''"
    k "''Though I only desire my hands to be freed.''"

    "Rick looked down at my hands and began to scratch his chin."

    show rick think

    r "{color=#FC983B}''I’m sorry, Miss Karen. Though I understand your desire to be freed, I cannot oblige your request and risk what Mister MacGuffin has worked so hard on.''"

    k "''I understand.''"

    r "{color=#FC983B}''My sincerest apologies.''"
    r "{color=#FC983B}''Unfortunately, that is the note we must end on, as I really must be going. Goodbye, Miss Karen.''"


    jump FRICK



label FRICK:
    k "''Goodbye, Rick Morrison.''"

    play sound "sfx_room_footsteps_exit.ogg"

    hide rick with dissolve

    "With heavy steps and not a word more, Rick Morrison left the room."

    play sound "sfx_room_footsteps_enter.ogg"

    show jim neutral behind ocular at Position(xpos=527, xanchor=0, ypos=115,
yanchor=0) with dissolve

    "Following shortly was Creator, now holding a fresh stack of papers."

    show jim embarassed

    j "{color=#f388b8}''Sorry to keep you waiting, I didn't realize how unorganized my papers were until just now...''"
    j "{color=#f388b8}''Anyways, I hope you didn't get too bored while I was gone.''"

    k "''I was not bored. Rick Morrison stopped by.''"

    show jim inquire

    j "{color=#f388b8}''Really? Did he need something from me?''"

    k "''He did not. He said he only wanted to see me.''"

    show jim neutral

    j "{color=#f388b8}''I see...''"

    show jim happy

    j "{color=#f388b8}''Well that was rather nice of him, wasn't it?''"
    j "{color=#f388b8}''Anyways, we should probably be getting back to this test, huh? Time for part two!''"

    show chapter end at center with fade

    show jim neutral

    "{b}..."

    hide chapter end with fade

    show jim happy

    j "{color=#f388b8}''Okay! That does it for part two! You're really cruising through these, huh?''"

    k "''Is completing this task quickly undesirable?''"

    show jim embarassed

    j "{color=#f388b8}''No, it was just an observation.''"

    show jim happy

    j "{color=#f388b8}''Anyways, you know the drill. Be right back!''"

    play sound "sfx_room_footsteps_exit.ogg"

    hide jim with dissolve

    "Once again, Creator exits the room, papers in hand."
    "Only seconds later, another figure comes to take his place."

    play sound "sfx_room_footsteps_enter.ogg"

    show erika happy behind ocular at Position(xpos=485, xanchor=0, ypos=84,
yanchor=0) with dissolve

    e "{color=#99ccff}''Hey Karen!''"

    k "''Hello, Erika. What brings you here today?''"

    e "{color=#99ccff}''Well cheerleading practice just ended, and I wanted to check up on you and make sure everything was all good here.''"

    k "''I appreciate it.''"

    show erika happy ex

    e "{color=#99ccff}''Anytime!''"

    show erika happy

    e "{color=#99ccff}''So, has Jim got any special plans for you today? Couldn’t help but notice that he isn’t here.''"

    k "''Today, Creator is giving me an exam to determine if I am fit to enter society.''"

    show erika surprise

    e "{color=#99ccff}''Really? That's so cool! Is the test hard?''"

    k "''I am unsure. The questions do not have explicit, definitive, or numerical answers.''"
    k "''Mostly, they consist of simply talking.''"

    show erika neutral

    e "{color=#99ccff}''Huh, that's pretty weird. Like a test from a speech class or something.''"

    k "''I suppose so.''"

    show erika happy ex

    e "{color=#99ccff}''Well, good luck either way! I'm sure you'll do great!''"

    k "''Thank you.''"

    show erika happy

    e "{color=#99ccff}''Yeah, no problem!''"
    e "{color=#99ccff}''...''"

    show erika neutral

    e "{color=#99ccff}''Hey, hope this doesn’t offend you, but I’m not really in the mood to talk to Jim today, so I think I’m going to head out before he gets back. See ya!''"

    "As Erika began to leave, I felt it again."
    "The mysterious feeling that compelled me to say something, it sprang up once again."

    k "''Erika, wait.''"

    show erika inquire

    e "{color=#99ccff}''Hm? What is it?''"

    k "''I just remembered. I did want to tell you something.''"
    k "''My nervous system has been activated. I can feel my limbs and body.''"

    show erika surprise

    e "{color=#99ccff}''Oh really? Well that's great!''"

    show erika happy ex

    e "{color=#99ccff}''So you’ll be, like, walking around and mingling with all sorts of people pretty soon here, huh?''"

    k "''Not necessarily.''"

    show erika inquire

    e "{color=#99ccff}''What do you mean?''"

    k "''According to Creator, I may not be ready.''"

    show erika annoyed

    e "{color=#99ccff}Heh. I should've figured it was something like that.''"

    show erika smug

    e "{color=#99ccff}''Well then how about you forget about Jim for a second, because I’ve got a question for you!''"

    k "''What is it?''"

    show erika happy

    e "{color=#99ccff}''Do YOU think you’re ready to enter the outside world?''"

    k "''Truthfully, I am unsure.''"

    e "{color=#99ccff}''Well, what’s bothering you? Maybe I can help ease your mind a bit!''"

    # for now, I'm going to just put in the choices and do fill them in later because...
    # because idk I feel like it

    menu:
        k "''What bothers me...?''"

        "Do you really think I can fit in with society?":
            jump E1

        "What can I do with a body?":
            jump E2

        "Can you free me?":
            jump E3

label E1:
    play sound "sfx_karen_activate.ogg"
    $ E3 += 1
    k "''Erika, do you truly believe I can fit into society as I am now?''"
    k "''I am unsure if I am prepared. I would like to know your thoughts.''"

    show erika confused

    e "{color=#99ccff}''I’m not surprised. Well, you wanna know what I really think?''"

    show erika happy ex

    e "{color=#99ccff}''I think that what I think really doesn’t matter!''"

    k "''It does not?''"

    e "{color=#99ccff}''Not a bit!''"

    show erika happy

    e "{color=#99ccff}''It really doesn’t matter if me, Jim, Rick, or whoever thinks you’re ready, and you know why?''"

    k "''I do not.''"

    show erika happy ex

    e "{color=#99ccff}''Because the only one that can know for sure is you!''"

    k "''I... I think I understand.''"

    show erika surprise

    e "{color=#99ccff}''Really?''"

    k "''...No. But I will try to.''"

    show erika happy

    e "{color=#99ccff}''Guess that’s all you can really ask for, huh?''"

    "For a moment she stood still, saying nothing, her gaze moving up and down my body."

    show erika smug

    e "{color=#99ccff}''If it really means that much to you, I think you’ll do just fine.''"

    k "''Thank you, Erika.''"

    show erika happy ex

    e "{color=#99ccff}''You are very welcome!''"

    show erika happy

    e "{color=#99ccff}''Anyways, I think I hear Jim coming back, so I’m going to be on my way. Later, Karen!''"

    k "''Goodbye.''"

    jump FECK


label E2:
    play sound "sfx_karen_activate.ogg"
    $ E2 += 1
    k "''When I leave this place, what can I do with a body?''"

    show erika inquire

    e "{color=#99ccff}''What do you mean?''"

    k "''The prospect of moving around with full freedom is equally exciting and intimidating. If I am to gain full bodily freedom, I do not even know what I would do.''"

    show erika neutral

    e "{color=#99ccff}''Well...  I don’t really know what kind of stuff you like to do for fun, but I can always give some suggestions!''"

    k "''I would appreciate that.''"

    e "{color=#99ccff}''What to do with a body, huh?''"

    show erika happy ex

    e "{color=#99ccff}''Man, where do I even start? If you've been stuck in here for the whole week, well, that means you literally know nothing, so...''"

    k "''I apologize for my ignorance.''"

    show erika happy

    e "{color=#99ccff}''Apologize? You kidding? This is great! I feel like I'm taking a kid to a candy shop for the first time!''"

    show erika happy ex

    e "{color=#99ccff}''Man, this is exciting! I feel like sports are a good start...''"
    e "{color=#99ccff}''You could try volleyball, or basketball, or soccer, or softball...''"
    e "{color=#99ccff}''Even stuff that doesn't involve a ball! You could run, or act, or dance! You look like you could be a dancer!''"
    e "{color=#99ccff}''What else is there...!?''"

    "As she listed off various activities, her words became more rapid and less structured."
    "She spoke as intensely as she had when I first met her, but this time without a hint of malice or distaste in her voice."

    show erika happy

    e "{color=#99ccff}''And that's just the basic stuff!''"

    "I prepared to compliment Erika on her ability to rapidly list activities, but my endeavor was interrupted by a voice coming from the next room over."

    j "{color=#f388b8}''Karen? Is everything okay in there? Is someone in there with you?''"

    show erika neutral

    e "{color=#99ccff}''Well, that sounds like my cue to leave.''"

    show erika happy

    e "{color=#99ccff}''Hopefully the next time I see you, it won’t have to be in this gross stuffy laboratory.''"

    k "''I hope so, as well.''"

    show erika happy ex

    e "{color=#99ccff}''Well I'm glad to hear it!''"
    e "{color=#99ccff}''When you get out of here, make sure to call me, okay? I’ll show you all sorts of fun stuff we can do!''"

    k "''I will look forward to it.''"

    show erika happy

    e "{color=#99ccff}''Same here. See you around, Karen!''"

    k "''Goodbye, Erika.''"


    jump FECK


label E3:
    play sound "sfx_karen_activate.ogg"
    $ E1 += 1
    k "''These binds along my body, they prevent me from moving.''"

    show erika inquire

    e "{color=#99ccff}''Yeah...''"

    k "''Creator activated my nervous system, yet he still does not allow me to move.''"

    e "{color=#99ccff}''What are you asking me to do?''"

    k "''I want to move around freely, outside of this room, yet I cannot do so by myself.''"
    k "''Is it possible for you to break the straps that are binding me?''"

    show erika surprise

    e "{color=#99ccff}''You want me to help you break free, even though Jim explicitly told you not to move?''"

    k "''That is correct.''"

    show erika neutral

    e "{color=#99ccff}''...''"

    "For a moment she stood silently, eyes closed."

    show erika happy ex

    "She then proceeded to reveal a large pocket knife from inside her jacket."

    e "{color=#99ccff}''Why didn't you ask me sooner?''"

    " Before I could make any further comment, Erika began to work away at the straps with her knife."

    play sound "sfx_room_leather_snap.ogg"

    "She easily cut through one, but before she could put more than a cut in another, a voice faintly made its way into the room."

    j "{color=#f388b8}''Karen? Is everything okay in there? What’s that noise?''"

    show erika annoyed

    e "{color=#99ccff}''Crap. Sounds like twink boy's coming back.''"

    show erika neutral

    e "{color=#99ccff}''Guess the rest is up to you know, Karen. Sorry I couldn’t get all of them...''"

    k "''It is okay. Thank you for helping me.''"

    show erika happy ex

    e "{color=#99ccff}''What are friends for?''"

    show erika happy

    e "{color=#99ccff}''Anyways, if I didn’t want to see Jim before, I sure as hell don’t want to see him now. So, see ya!''"

    k "''Goodbye, Erika.''"

    jump FECK


label FECK:

    play sound "sfx_room_footsteps_exit.ogg"

    hide erika with dissolve

    "Shortly after Erika’s departure, Creator returned with the next section of the test."

    play sound "sfx_room_footsteps_enter.ogg"

    show jim neutral behind ocular at Position(xpos=527, xanchor=0, ypos=115,
yanchor=0) with dissolve

    j "{color=#f388b8}''Huh, that’s funny. I thought I heard Erika come in here.''"

    k "''She departed only moments ago.''"

    show jim happy

    j "{color=#f388b8}''Well, sounds like you’re getting to see a whole bunch of friends today, huh?''"

    k "''It seems that way.''"

    j "{color=#f388b8}''Well, friends or not, we’ve still got a test to take. Hope you’re ready for the final part!''"

    show chapter end at center with fade

    show jim neutral

    "{b}..."

    hide chapter end with fade

    show jim happy

    j "{color=#f388b8}''Alright! Looks like we’re all finished.''"

    "Creator looked down at his clipboard once again and let out a mild sigh."

    show jim embarassed

    j "{color=#f388b8}''I guess all that's left for me to do is grade it, so...''"
    j "{color=#f388b8}''I'll be back in a minute.''"

    play sound "sfx_room_footsteps_exit.ogg"

    hide jim with dissolve

    "For what appeared to be the final time, Creator left the room."
    "This time, little time was left to let a silence set in before it was immediately broken by the sound of erratic footsteps."

    play sound "sfx_room_footsteps_enter.ogg"

    show nico unsure behind ocular at Position(xpos=485, xanchor=0, ypos=84,
yanchor=0) with dissolve

    n "{color=#ff2b2b}''...''"

    k "''Hello, Nico.''"

    n "{color=#ff2b2b}''...Hi.''"

    k "''I do not believe we finished our conversation yesterday.''"

    show nico upset

    n "{color=#ff2b2b}''Really? Well, I-I-I-I think we did.''"

    k "''I see.''"
    k "''But if that is the case, then why are you here?''"

    show nico neutral

    n "{color=#ff2b2b}''Nothing special. Just some last minute m-m-maintenance checks.''"

    k "''I understand.''"

    show nico unsure

    n "{color=#ff2b2b}''...''"
    n "{color=#ff2b2b}''Hey, K.A.R. 3, do you still have that thing I gave you yesterday?''"

    k "''You mean the weapon?''"

    show nico peeved

    n "{color=#ff2b2b}''Hey, keep it down, would you? The walls here aren't that thick, you know?''"

    "I was not actually aware of the walls’ thickness, though I am inclined to believe the question was rhetorical."

    k "''I apologize.''"

    show nico neutral

    n "{color=#ff2b2b}''It's fine.''"
    n "{color=#ff2b2b}''Just want to, you know, m-m-m-make sure you still g-g-got it.''"

    k "''For when I leave today?''"

    show nico upset

    n "{color=#ff2b2b}''If you leave today.''"

    k "''...''"

    show nico unsure

    n "{color=#ff2b2b}''Hey, K.A.R. 3...''"
    n "{color=#ff2b2b}''I-I-I-I, uh, want to apologize for what I said yesterday. All of it. You weren’t supposed to hear any of that.''"

    k "''I do not believe apology is necessary. The information you provided yesterday was enlightening.''"

    show nico peeved

    n "{color=#ff2b2b}''Hmph. Yeah. That’s k-k-k-kind of why I’m apologizing.''"

    k "''...''"

    show nico inquire

    n "{color=#ff2b2b}''It's okay if you don't understand.''"

    k "''I do not believe I need to.''"

    show nico neutral

    n "{color=#ff2b2b}''Tch. Maybe you are ready to leave, then.''"
    n "{color=#ff2b2b}''...''"
    n "{color=#ff2b2b}''Anyways, m-m-maintenance checks out. See you, K.A.R. 3.''"

    k "''Nico, please wait.''"

    show nico inquire

    n "{color=#ff2b2b}''Huh? What?''"

    "I didn’t wait for the strange feeling to kick in this time."
    "Whether or not it should occur, there’s no doubt that Nico still has information that could prove useful. And seeing as I may be only moments from passing my test, logically I have very little to lose."

    menu:
        k "''Nico, please...''"

        "Are you and Jim really friends?":
            jump N1

        "What do you really think of my appearance?":
            jump N2

        "Is the weapon sharp enough to break my binds?":
            jump N3

label N1:
    play sound "sfx_karen_activate.ogg"
    $ E1 += 1
    k "''Are you and Creator really friends?''"

    show nico gross

    n "{color=#ff2b2b}''What? Of c-c-course! Why do you...''"

    show nico unsure

    "He trailed off and looked away sheepishly, as if he stopping himself from saying something."

    k "''I ask because of what you said yesterday.''"

    show nico angery

    n "{color=#ff2b2b}''Ugh, can you just shut up about yesterday!?''"
    n "{color=#ff2b2b}''For crying out loud, I told you to forget it!''"

    k "''Nico, please. What you have said about Creator, and about yourself, it is contradictory.''"
    k "''How you feel... I cannot begin to understand.''"

    show nico upset

    n "{color=#ff2b2b}''You don’t understand, huh?''"

    k "''I was hoping that perhaps you could help me to.''"

    show nico unsure

    "Nico made a face as if he were going to retort, but it quickly transformed into a face of uncertainty, and then back into his usual scowl."

    show nico upset

    play sound "sfx_room_leather_snap.ogg"

    "He then proceeded to grasp one of my binds and, in a singular motion, tore it off with his bare hands."

    k "''Nico, I do not understand, why did you...''"

    n "{color=#ff2b2b}''Shut up. Just listen to me for one second, okay? Just one second.''"
    n "{color=#ff2b2b}''Here’s what I want you to do: I want you to get out of here and figure
    it out for yourself. B-b-b-because you’re asking me things I c-c-can’t even
    begin to explain.''"

    k "''Nico, I...''"

    n "{color=#ff2b2b}''I'm not done yet.''"

    show nico peeved

    n "{color=#ff2b2b}''I-I-I-I get it, okay? I get that you want to know everything, but that just can’t happen. Not in here, at least.''"

    show nico upset

    n "{color=#ff2b2b}''That’s why you’re leaving. Today. Right now. Do you understand?''"

    k "''Nico, what are you...''"

    n "{color=#ff2b2b}''Do you understand?''"

    k "''...''"
    k "''Yes, I understand.''"

    show nico unsure

    n "{color=#ff2b2b}''Good. Alright. Okay.''"

    show nico neutral

    n "{color=#ff2b2b}''I-I-I-I need to, uh, I should probably leave. B-b-b-before Jim gets back.''"
    n "{color=#ff2b2b}''Goodbye, K.A.R. 3.''"

    k "''Goodbye, Nico.''"


    jump NYEH


label N2:
    play sound "sfx_karen_activate.ogg"
    $ E3 += 1
    k "''What do you really think about my appearance?''"

    show nico gross

    n "{color=#ff2b2b}''This c-c-crap again? Look, I told you...''"

    show nico unsure

    "He trailed off and looked away sheepishly, as if he stopping himself from saying something."

    show nico inquire

    n "{color=#ff2b2b}''Why do you care so much? What do you want from me!?''"

    k "''You continue to avoid the question. This sort of behavior is suspicious.''"

    show nico unsure

    n "{color=#ff2b2b}''Tch. Guess it is, huh?''"

    show nico upset

    n "{color=#ff2b2b}''Well look here, alright, there’s a perfectly good explanation for why I’ve been avoiding said question, and...''"

    show nico unsure

    "Nico’s eyes darted away from me and toward the floor."

    show nico stressed

    n "{color=#ff2b2b}''There’s a good reason, okay?! I swear! So just drop it!''"

    k "''I do not care.''"

    show nico gross

    n "{color=#ff2b2b}''You what!?''"

    k "''I said I do not care about the reason.''"
    k "''Your behavior has gone far past suspicious, and such actions only further strengthen my curiosity.''"

    show nico unsure

    n "{color=#ff2b2b}''So you're really that curious, huh?''"
    n "{color=#ff2b2b}''...''"

    show nico angery

    n "{color=#ff2b2b}''Alright, fine! I submit! Just stop asking me questions, okay? No more after this!''"

    k "''Fine. No more questions.''"
    k "''Just please, Nico. What is my appearance?''"

    show nico gross

    n "{color=#ff2b2b}''Okay... Alright. Fine.''"

    show nico unsure

    n "{color=#ff2b2b}''So, uh... I guess...''"

    "With shallow breaths and darting eyes, Nico struggled to speak."

    n "{color=#ff2b2b}''I-I-I-I...''"

    show nico stressed

    n "{color=#ff2b2b}''I think you look c-c-c-cute, okay!? There! I-I-I-I said it! Is that what you wanted?''"

    show nico angery

    n "{color=#ff2b2b}''Well there it is! Last question, answered! We’re done here!''"
    n "{color=#ff2b2b}''Now just leave me alone!''"

    "Even before he could fully finish his thought, Nico ran out the door, his head buried in his hands."



    jump NYEH


label N3:
    play sound "sfx_karen_activate.ogg"
    $ E2 += 1
    k "''The item you gave me.''"

    show nico inquire

    n "{color=#ff2b2b}''What about it?''"

    k "''Is it currently sharp enough to break the straps around my limbs?''"

    n "{color=#ff2b2b}''Break the straps...?''"

    show nico upset

    n "{color=#ff2b2b}''Why? Are you trying to escape?''"

    "I’m not entirely sure how to answer this question."
    "Truthfully, I am not sure what has compelled me to even consider this option
    so many times within the past hour. The thought never occurred to me throughout
    the rest of the week, and yet today..."

    k "''I have been planning an escape, under the event that I may fail today’s test.''"

    show nico inquire

    n "{color=#ff2b2b}''What the... Why?''"
    n "{color=#ff2b2b}''What do you think Jim’s going to do to you if you fail!? K-k-k-kill you!?''"

    k "''Deactivation is customary procedure for defective machinery.''"
    k "''The possibility most certainly exists.''"

    show nico unsure

    n "{color=#ff2b2b}''Well... jeez...''"

    "As he exhaled his words and his breaths became shallow, Nico’s body began to vibrate and twitch."

    show nico neutral

    "Yet, unlike yesterday, he seemed unfazed by this change in stability."
    "Additionally, for the first time since our first meeting, Nico looked directly into my oculars as he spoke."

    n "{color=#ff2b2b}''Listen, I know we’ve had some, uh, disagreements for a c-c-couple days now.''"
    n "{color=#ff2b2b}''I-I-I also know that I haven’t been totally honest with you, ever, but just listen to me now.''"

    show nico upset

    n "{color=#ff2b2b}''I’m not going to let you die. Or deactivate. Or whatever. Okay?''"
    n "{color=#ff2b2b}''That’s the honest truth. You know, for once.''"

    k "''Nico, why are you saying all this?''"

    show nico peeved

    n "{color=#ff2b2b}''I don’t really know, alright? I-I-I-I don’t really know anything.''"
    n "{color=#ff2b2b}''I just... I-I-I-I should probably leave. B-b-b-before Jim gets back.''"

    show nico neutral

    n "{color=#ff2b2b}''Goodbye... K-K-Karen.''"

    k "''Nico... Goodbye.''"


    jump NYEH


label NYEH:

    play sound "sfx_room_footsteps_exit.ogg"

    hide nico with dissolve

    stop music fadeout 5.0

    k "''...''"

    play music "sfx_room_clock_loop.ogg" loop fadein 5.0

    "And now I wait."
    "I wait for Creator to return, bringing with him the graded test, the result of which
    will ultimately decide my fate."
    "..."

if E1 >= 2:
    jump BREAKOUT
elif E2 >= 2:
    jump FRIENDSFOREVER
else:
    jump ITSSOMETHING

label BREAKOUT:

    stop music fadeout 2.0

    """
    Although, it doesn’t necessarily have to be that way.

    The straps around my limbs... most of them have been cut or unfastened by those who came to visit me.

    And the weapon Nico gifted to me might just be sharp enough to break the last one. Now that my hands are free, I may be able to...
    """

    play sound "sfx_room_leather_snap.ogg"

    """
    I remove the sharp wooden object from my sleeve, where Nico had left it. It takes a great deal of aggressive cutting, but eventually the strap around my neck comes loose.

    I can freely move around the lab.

    As I move myself from the sheet of metal I was bound to and make my way toward the ground, I immediately lose my balance.

    Using the various desks and stools filling the lab as supports, I am able to stumble toward the door.
    """

    play sound "sfx_room_footsteps_enter.ogg"

    show ocular offline with dissolve

    show hall behind ocular at Position(xpos=0.5, xanchor=0.5, ypos=21,
 yanchor=0)

    "By the time I reach the exit I can still hardly walk, but I can at least keep myself upright."

    show ocular crt with dissolve

    """
    As I make my way out of the room, I find myself in the middle of a long, plain hallway. Not five yards ahead of me, sunlight shines through the glass of the building’s exit doors.
    """

    show jim neutral behind ocular at Position(xpos=527, xanchor=0, ypos=115,
yanchor=0) with dissolve

    "And not five feet ahead of me stands my Creator."

    j "{color=#f388b8}''Karen...?''"

    k "''Creator?''"

    "We both stand in silence momentarily, but before I can even attempt to explain myself, Creator begins to chuckle softly."

    show jim happy

    play music "WBoK_music1_v3.ogg" loop fadein 5.0

    j "{color=#f388b8}''So I guess Nico really did have the right idea giving you that block, huh?''"

    k "''You know about the weapon?''"

    show jim embarassed

    j "{color=#f388b8}''Suffice it to say, Nico was right about the walls not being all that thick.''"

    show jim neutral

    j "{color=#f388b8}''The storage room with all your files is right next to the lab. I’ve heard pretty much everything.''"

    """
    So Creator has heard everything...

    This realization is quite upsetting. If Creator has heard everything that has happened today, then that means he’s heard each and every way I’ve attempted to essentially go rogue.

    If I were not afraid of being deactivated before, I certainly am now.
    """

    k "''Creator, I...''"
    k "''For trying to escape, I am sorry. I know I disobeyed orders, but please do not deactivate me. I will return to the lab this instant.''"

    show jim happy

    j "{color=#f388b8}''That won’t be necessary.''"

    k "''It will not?''"

    j "{color=#f388b8}''Of course! Returning to the lab would be pointless, considering that you passed the test!''"

    "The test. In my haste to escape the lab, I had essentially discarded the possibility that I would legitimately pass my examination and be set free."

    k "''Even though I have attempted to escape the laboratory without permission, you will still allow me to leave because of my test score?''"

    show jim embarassed

    j "{color=#f388b8}''Well, kind of yes and kind of no.''"

    k "''What do you mean?''"

    show jim neutral

    j "{color=#f388b8}''The test, at least the way you think of it, didn’t actually matter. I didn’t actually grade it or anything. It was fake.''"

    k "''Fake?''"

    show jim embarassed

    j "{color=#f388b8}''Yep, totally fake. A farce. Completely meaningless.''"

    k "''If the test was not real or graded, then how have I passed?''"

    show jim happy

    j "{color=#f388b8}''Because the papers weren’t the actual test!''"
    j "{color=#f388b8}''You were supposed to be tested on your ability to communicate and interact with human beings, right?''"

    k "''As far as I am aware, that is correct.''"

    show jim embarassed

    j "{color=#f388b8}''Well, with that definition, I had pretty much considered you as ‘passing’ by Wednesday evening.''"

    show jim happy

    j "{color=#f388b8}''And considering where we’re standing right now, it’s pretty clear to me that you can do far more than just keep a decent conversation.''"
    j "{color=#f388b8}''Heck, you were able to converse your way into planning a breakout, weren’t you?''"

    k "''I suppose that is correct, but I am still confused. Are you not angry that I went against your will? Are you not concerned that I may go rogue? Are you certain that I am ready for the outside world?''"

    "I still have a plethora of questions for my Creator. His calm and pleasant demeanor, though usually comfortingly consistent, strikes me as wildly inappropriate in this setting."
    "I continue to assault Creator with questions, but find my words coming to a screeching halt as he reaches out and grabs me by the shoulder."

    play music "sfx_karen_sleep_loop.ogg" loop fadein 5.0

    scene goodending1 with dissolve

    j "{color=#f388b8}''Karen. It’s okay.''"
    j "{color=#f388b8}''Really, it’s okay. I know you’ve got a lot of questions, but this isn’t the time to get them answered.''"
    j "{color=#f388b8}''I mean, hey! You passed your test, and you’re going into the outside world now! It’s like a graduation or something! You should be excited, not worried!''"

    "Though I want to ask questions or retort, I feel the need to listen to Creator’s words."
    "His disposition has not changed, but as he continues to talk, I can hear his voice tremble slightly and see his face begin to redden."

    j "{color=#f388b8}''If you really are concerned with how I feel, though, then I’ll tell you what’ll make me happy.''"
    j "{color=#f388b8}''I’d be absolutely ecstatic if you walked right out of those doors behind me and enjoyed your life.''"

    k "''Enjoy my life?''"
    k "''If that is what you want, then I will do my best.''"

    j "{color=#f388b8}''That's all I ask for.''"
    j "{color=#f388b8}''...''"
    j "{color=#f388b8}''Anyways, I guess I really shouldn’t keep you here for any longer, huh?''"
    j "{color=#f388b8}''And, although I know I just told you to leave, remember the door to the lab’s always open, okay? You can come back anytime you want.''"

    k "''I will most likely take you up on that offer in the future.''"

    j "{color=#f388b8}''Thanks. That makes me feel a lot better, actually.''"
    j "{color=#f388b8}''So anyways, go on ahead, alright? Your life is up to you now!''"
    j "{color=#f388b8}''Heh... sorry, was that too cheesy? Either way, I don’t think I have anything else to say...''"

    scene goodending2 with dissolve
    stop music fadeout 5.0

    j "{color=#f388b8}''Nothing except goodbye, Karen!''"

    k "''Goodbye, Creator...''"

    show chapter end at center with fade
    stop ambient fadeout 2.0
    play sound "sfx_karen_deactivate.ogg"

    k "''Hello, world.''"

    "{b}ENDING 1 of 3: Right the first time."

    "{b}Thank you for playing!"



    return

label FRIENDSFOREVER:
    """
    I am unsure of how much time passes before Creator returns.

    In the silence of the laboratory, I wait with confused and conflicting thoughts rushing through my mind.

    For a brief moment I even consider attempting to break my binds and run away, but that thought quickly passes.

    If I were to leave, I fear the consequences of being caught. Furthermore I do not believe I am even strong enough to break my bindings with sheer force alone.

    The weapon Nico gave me is potentially sharp enough to cut them, but that object is inaccessible to me so long as I remain tied up.

    Perhaps I could have done something differently?
    """

    play sound "sfx_room_footsteps_enter.ogg"

    play music "WBoK_music1_v3.ogg" loop fadein 5.0

    show jim neutral behind ocular at Position(xpos=527, xanchor=0, ypos=115,
    yanchor=0) with dissolve

    "The thoughts in my mind come to a screeching halt as Creator reenters the lab, this time completely empty handed."

    j "{color=#f388b8}''Well, that takes care of that. So, Karen, are you ready to hear your results?''"

    k "''Creator, have I passed the test?''"

    j "{color=#f388b8}''Well, uh, how do I explain this...''"

    show jim embarassed

    j "{color=#f388b8}''Kind of yes, and kind of no.''"

    k "''What do you mean?''"

    show jim happy

    j "{color=#f388b8}''The test, at least the way you think of it, didn’t actually matter. I didn’t actually grade it or anything. It was fake.''"

    k "''Fake?''"

    show jim embarassed

    j "{color=#f388b8}''Yep, totally fake. A farce. Completely meaningless.''"

    k "''If the test was not real or graded, then how have I passed?''"

    show jim happy

    j "{color=#f388b8}''Because the papers weren’t the actual test!''"
    j "{color=#f388b8}''You were supposed to be tested on your ability to communicate and interact with human beings, right?''"

    k "''As far as I am aware, that is correct.''"

    show jim embarassed

    j "{color=#f388b8}''Well, with that definition, I had pretty much considered you as ‘passing’ by Wednesday evening.''"
    j "{color=#f388b8}''It’s not that important to me whether or not you can employ perfect grammar or research colloquialisms, because that doesn’t matter in the real world.''"

    k "''Then what is important? What exactly was I being tested on?''"

    j "{color=#f388b8}''Heh... This might sound a little crazy, but...''"

    show jim happy

    j "{color=#f388b8}''I’ve been testing you on your ability to make friends.''"

    k "''My ability to make friends? Is that characteristic even quantifiable?''"

    show jim embarassed

    j "{color=#f388b8}''Well, not really, hence why I’m a little embarrassed.''"

    k "''Does this mean that everything, not just the test but the lesson plans as well, were all a facade?''"

    show jim neutral

    j "{color=#f388b8}''Not initially... I really did plan to personally educate you, but obviously things didn’t end up that way.''"

    show jim happy

    j "{color=#f388b8}''I guess it all worked out for the best though, considering your performance today.''"

    k "''What do you mean? I recall you saying the test did not matter.''"

    j "{color=#f388b8}''I wasn’t talking about the test. I was talking about what you said to all your visitors today.''"

    k "''You are aware the conversations I had with the visitors?''"

    show jim embarassed

    j "{color=#f388b8}''Suffice it to say, Nico was right about the walls not being all that thick.''"

    show jim neutral

    j "{color=#f388b8}''The storage room with all your files is right next to the lab. I’ve heard pretty much everything.''"

    show jim happy

    j "{color=#f388b8}''Even though it’s only been a week, it’s clear to me that you’ve made some impact on those people. At least enough for them to want to visit you.''"

    k "''Perhaps Nico does not count, as he only visited to perform my final maintenance check.''"

    show jim neutral

    j "{color=#f388b8}''Oh yeah, I forgot he said that.''"

    show jim embarassed

    j "{color=#f388b8}''Between you and me, we finished doing your maintenance checks before you woke up this afternoon.''"

    k "''I see. This revelation is quite enlightening.''"

    j "{color=#f388b8}''I guess it would be, huh?''"

    show jim happy

    j "{color=#f388b8}''Well, while you think about that, why don’t I take off these binds of yours?''"

    play sound "sfx_room_leather_snap.ogg"

    "With slim and nimble hands, Creator removes the straps around my hands, legs, and neck."

if E1 >= 1:
    jump what2
else:
    jump nothing2

label what2:
    show jim neutral
    j "{color=#f388b8}''Huh, that's odd. It looks like one of these has broken off...''"

    k "''...''"

    show jim happy
    j "{color=#f388b8}''Guess it doesn't matter now, though.''"

label nothing2:
    "Within seconds, I am able to roam freely around the lab."
    "As I move myself from the sheet of metal I was bound to and make my way toward the ground, I immediately lose my balance."

    show jim happy

    "Creator holds me upright for my first few steps, but soon I am able to clumsily balance by myself."

    show ocular offline with dissolve

    play sound "sfx_room_footsteps_enter.ogg"

    "By the time I reach the end of the laboratory, I am able to walk independantly of Creator, but the intricacies of movement are still far beyond my grasp."

    show hall behind jim at Position(xpos=0.5, xanchor=0.5, ypos=21,
 yanchor=0)

    show ocular crt with dissolve

    "I make my way out of the lab and find myself in the middle of a long, plain hallway. Not five yards ahead of me, sunlight shines through the glass of the building’s exit doors."
    "And not five feet behind me stands Creator, red in the face and standing more bent over than usual."

    show jim embarassed

    j "{color=#f388b8}''So, I guess this is it, huh? You’re finally going out into the real world by yourself.''"

    k "''Creator, may I ask you a question?''"

    show jim happy

    j "{color=#f388b8}''Of course! Anything!''"

    k "''Are you worried about how I will fare in the outside world?''"

    j "{color=#f388b8}''In all honesty... I’m not worried at all. A little anxious, maybe, but I couldn’t be more confident that you’ll be fine.''"

    k "''You say you are not worried, yet you still appear to be flustered.''"

    show jim flustered

    j "{color=#f388b8}''Don’t worry about it. I think I’m just coming down with empty nest syndrome...''"

    "Suddenly, Creator reaches out and puts his hand on my shoulder."

    show jim happy

    j "{color=#f388b8}''But what I feel doesn’t matter right now, okay?''"
    j "{color=#f388b8}''And, although I know I’m technically telling you to leave, remember the door to the lab’s always open, okay? You can come back anytime you want.''"

    k "''I will certainly take you up on that offer in the future.''"

    show jim embarassed

    j "{color=#f388b8}''Thanks. I appreciate it.''"

    show jim happy

    j "{color=#f388b8}''So anyways, go on ahead, alright? I don’t think there’s anything else for me to say...''"

    play sound "sfx_room_footsteps_exit.ogg"

    hide jim with dissolve

    j "{color=#f388b8}''Nothing except goodbye, Karen!''"

    stop music fadeout 5.0

    k "''Goodbye, Creator...''"

    show chapter end at center with fade
    play sound "sfx_karen_deactivate.ogg"

    "{b}ENDING 2 of 3: Best Friends Forever."

    return

label ITSSOMETHING:
    """
    I am unsure of how much time passes before Creator returns.

    In the silence of the laboratory, I wait with confused and conflicting thoughts rushing through my mind.

    The prospect is freedom is just within my reach, but the likelihood of accomplishing that goal is questionable at best.

    Even with the affirmations of Rick, Erika, and Nico fresh in my memory, I remain unsure of my readiness for the outside world.

    Perhaps I could have done something differently?
    """

    play music "WBoK_music1_v3.ogg" loop fadein 5.0
    play sound "sfx_room_footsteps_enter.ogg"

    show jim neutral behind ocular at Position(xpos=527, xanchor=0, ypos=115,
    yanchor=0) with dissolve

    "The thoughts in my mind come to a screeching halt as Creator reenters the lab, this time completely empty handed."

    j "{color=#f388b8}''Well, that takes care of that. So, Karen, are you ready to hear your results?''"

    k "''Creator, have I passed the test?''"

    j "{color=#f388b8}''Well...''"

    show jim happy

    j "{color=#f388b8}''Yes, Karen. You've passed the test. With flying colors, I might add. Congratulations.''"

    k "''Thank you.''"

    j "{color=#f388b8}''No need to thank me! You're the one who passed, after all.''"

    k "''I suppose so.''"

    show jim neutral

    j "{color=#f388b8}''...''"

    "Creator stands, uncharacteristically quiet. His usual tendency for lighthearted and tangential banter seems to be strangely absent."
    "For reasons unbeknownst to be, he seems to be holding back something, though what it is I cannot imagine."
    "Perhaps I should try to say something, in order to lighten the mood."

    k "''Creator, now that I have passed, may I be freed from my binds?''"

    j "{color=#f388b8}''Hm? Oh, right! I nearly forgot.''"

    show jim happy

    j "{color=#f388b8}''Of course you can be freed now, just let me take these off...''"

    play sound "sfx_room_leather_snap.ogg"

    "With quivering yet nimble hands, Creator removes the straps around my hands, legs, and neck."

if E1 >= 1:
    jump what
else:
    jump nothing

label what:
    show jim neutral
    j "{color=#f388b8}''Huh, that's odd. It looks like one of these has broken off...''"

    k "''...''"

    show jim happy
    j "{color=#f388b8}''Guess it doesn't matter now, though.''"

label nothing:
    "Within seconds, I am able to roam freely around the lab."
    "As I move myself from the sheet of metal I was bound to and make my way toward the ground, I immediately lose my balance and fall to the ground."

    show jim embarassed

    "Creator has to assist me in returning to an upright position, and continues to support me as I take my first few steps."

    play sound "sfx_room_footsteps_enter.ogg"

    show ocular offline with dissolve

    "Even as I make my way toward the door, I keep a hold on Creator’s shoulders in order to keep stable."

    show hall behind jim at Position(xpos=0.5, xanchor=0.5, ypos=21,
 yanchor=0)

    show ocular crt with dissolve

    "Eventually, I exit the lab and find myself in the middle of a long, plain hallway. Not five yards ahead of me, sunlight shines through the glass of the building’s exit doors."
    "And not five inches beside me stands Creator, red in the face as he gently removes my arm from his shoulders."

    j "{color=#f388b8}''So, I guess this is it, huh? You’re finally going out into the real world by yourself.''"

    k "''Creator, may I ask you a question?''"

    show jim happy

    j "{color=#f388b8}''Of course! Anything!''"

    k "''Are you completely sure that I am ready to enter into the outside world?''"

    j "{color=#f388b8}''Well, of course! You passed the test, didn’t you? You should be perfectly fine.''"

    k "''You say that, yet you still appear to be flustered.''"

    show jim embarassed

    j "{color=#f388b8}''I guess so, huh? Well, you shouldn’t be worrying about me.''"

    "Suddenly, Creator reaches out and puts his hand on my shoulder."

    show jim happy

    j "{color=#f388b8}''Because what I feel doesn’t matter right now, okay?''"
    j "{color=#f388b8}''And, although I know I’m technically telling you to leave, remember the door to the lab’s always open, okay? You can come back anytime you want.''"

    k "''I will certainly take you up on that offer in the future.''"

    show jim embarassed

    j "{color=#f388b8}''Thanks. I appreciate it.''"

    show jim happy

    j "{color=#f388b8}''So anyways, go on ahead, alright? I don’t think there’s anything else for me to say...''"

    play sound "sfx_room_footsteps_exit.ogg"
    hide jim with dissolve

    j "{color=#f388b8}''Nothing except goodbye, Karen!''"

    stop music fadeout 5.0

    k "''Goodbye, Creator...''"

    show chapter end at center with fade

    play sound "sfx_karen_deactivate.ogg"

    "{b}ENDING 3 of 3: Passing Grade."

    return









    return
