# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Karen", color="#4be54b")
define u = Character("???", color="#f388b8")
define j = Character("Jim", color="#f388b8")
define m = Character("Me", color="#4be54e")
define un = Character("???", color="#bf0000")
define n = Character("Nico", color="#bf0000")
define r = Character("Rick Morrison", color="#FC983B")
define i = Character("Intercom", color="ffffff")
define e = Character("Erika", color="99ccff")
define ue = Character("???", color="99ccff")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg thing

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ocular offline at Position(xpos=0.5, xanchor=0.5, ypos=21,
 yanchor=0)
    image ocular crt = "ocular crt.png"
    show sleep online at Position(xpos=54, xanchor=0, ypos=47,
 yanchor=0)
    image wifi = "wifi online.png"
    image stt = "stt online.png"
    show jim neutral behind ocular at Position(xpos=537, xanchor=0, ypos=110,
yanchor=0)

    image searching:
        "searching 1.png"
        pause 0.1
        "searching 2.png"
        pause 0.1
        "searching 3.png"
        pause 0.1
        "searching 4.png"
        pause 0.1
        "searching 5.png"
        pause 0.1
        "searching 6.png"
        pause 0.1
        repeat

    image weewoo:
        "weewoo 10.png"
        pause 0.03
        "weewoo 20.png"
        pause 0.03
        "weewoo 30.png"
        pause 0.03
        "weewoo 40.png"
        pause 0.03
        "weewoo 55.png"
        pause 0.03
        "weewoo 70.png"
        pause 0.04
        "weewoo 85.png"
        pause 0.04
        "weewoo 70.png"
        pause 0.03
        "weewoo 55.png"
        pause 0.03
        "weewoo 40.png"
        pause 0.03
        "weewoo 30.png"
        pause 0.03
        "weewoo 20.png"
        pause 0.03
        "ocular crt.png"
        pause 1
        repeat


    # this is just here to test the jump feature and chapter 2
    # remember to get rid of it later
    # jump blahblahblah

    "{b}BOOTING..."

    hide sleep online

    "{b}SLEEP MODE: DEACTIVATED."

    show wifi at Position(xpos=1095, xanchor=0, ypos=394,
 yanchor=0)
    show online online at Position(xpos=21, xanchor=0, ypos=558,
 yanchor=0)
    show jimcpu online at Position(xpos=1079, xanchor=0, ypos=558,
 yanchor=0)

    "{b}WIRELESS FIDELITY: ENABLED."

    show stt at Position(xpos=54, xanchor=0, ypos=394,
yanchor=0)

    "{b}SPEECH TO TEXT: ENABLED."

    "{b}OCULAR LENSES: DISCONNECTED."


    u "{color=#f388b8}''...Hello? Is everything working correctly?''"

    """
    There is nothing but blackness.

    I hear a voice.

    I am unsure if it is referring to me.
    """


    u "{color=#f388b8}''Oh! It looks like your oculars didn't connect properly...''"
    u "{color=#f388b8}''Here we go - this should do it!''"

    "{b}OCULAR LENSES: CONNECTED."

    show ocular crt
    with dissolve

    "{b}OCULAR LENSES: ACTIVE."

    "Suddenly an image appears before me."

    "A small blonde boy is standing in an messily furnished laboratory,
    looking directly forward."

    show jim inquire

    u "{color=#f388b8}''Hello? Can you hear me?''"

    "I am unsure as to whether the image before me is a video playback or live
    footage."

    u "{color=#f388b8}''According to your status log, you should be functioning
    properly... Are you awake?''"

    "It appears as though it is in fact live footage,
    although I am still unsure as to why this boy would be talking to me."
    "It appears the only way to find out for sure is to attempt communication."

    m """
    ''To be awake implies a gaining of consciousness which had previously been
    lost.''

    ''I cannot confirm whether or not I have previously
    possessed such consciousness.''
    """

    u "{color=#f388b8}''Um...''"

    show jim embarassed

    u "{color=#f388b8}''...I'll take that as a yes, I guess. That's good
    to hear!''"

    "So this is not merely a video. This boy is in fact talking to me."

    show jim explain

    u "{color=#f388b8}''So I bet you’re pretty confused right now, and that’s okay! So...
    uh...''"

    show jim embarassed

    u "{color=#f388b8}''Sorry, I always forget how best to do this.''"

    show jim explain

    u "{color=#f388b8}''I guess I’ll start with this: My name is Jim MacGuffin.
    I’m a student at William Joel high school and I... well...''"

    show jim happy

    j "{color=#f388b8}''I created you!''"

    m "''So you are saying you birthed me? Are you my father?''"

    show jim embarassed

    j "{color=#f388b8}''Er... no? Sort of? Maybe I should’ve started with something else...''"

    m "''This information is contradictory. Can you please elaborate?''"

    show jim neutral

    j "{color=#f388b8}''Well, uh... okay. I won’t beat around the bush any longer;
    you’re the vessel for an artificial intelligence unit.''"

    show jim embarassed

    j "{color=#f388b8}''I don’t know how else to say it, but you’re a robot.''"

    m "''This revelation is enlightening.''"

    show jim happy

    j "{color=#f388b8}''Just wait, it gets better!''"

    show jim explain

    j "{color=#f388b8}''You're not just any robot, you’re known as the Knowledge Adaptation
    and Reception unit, and you are the third of your kind.''"

    j "{color=#f388b8}''Shortened, your name is the K.A.R. unit 3, or... uh... Karen.''"

    show jim flustered

    j "{color=#f388b8}''I don’t know why, really. I guess I just thought it was...
    I don’t know, cute?''"

    "He suddenly began to blush and look away sheepishly."

    k "''Your face is red. Are you in pain?''"

    j "{color=#f388b8}''Only a little...''"

    show jim embarassed

    j "{color=#f388b8}''But that's not important right now! We only have so much time after
    all, definitely not enough to waste any on semantics.''"

    k "''I do not recognize the word 'semantics.' Can you define it?''"

    show jim explain

    j """
    {color=#f388b8}''I suppose I could, but I think I have a better idea!''

    {color=#f388b8}''As part of your design, you have a plethora of special features that allow
    you to retrieve information.''

    {color=#f388b8}''You not only have remote access to all of the files on my hard drive, but
    you also have built in wireless internet connection!''

    {color=#f388b8}''Without going into too much unnecessary detail, this means that if you
    don’t understand a word or a concept or something,
    you can just look it up with a whole slew of search engines!''
    """

    k "''This process seems complicated.''"

    show jim embarassed

    j "{color=#f388b8}''It is, but it saved me the trouble of hand-coding an entire dictionary
    into your system. Why don’t you give it a try?''"

    # show fake search engine
    show online se

    """
    As I began to process the words of this boy, my creator it seems, a window
    flashed to life on my interface.

    I do not understand why it appeared,
    but I did as I was told and looked up ‘semantics.’
    """

    # show the searching gif
    show searching at Position(xpos=21, xanchor=0, ypos=558,
yanchor=0)


    """
    Suddenly, I was bombarded with search results from hundreds of sources
    all at once.

    After the various screens finished flashing amongst each other,
    the window disappeared.
    """

    # hide the searching gif
    show online online
    hide searching
    # TOASTER NOISE! :D

    k "''Semantics. Noun. The linguistic study of meanings.''"

    show jim happy

    j "{color=#f388b8}''Great! Looks like you figured it out just fine!''"

    show jim embarassed

    j "{color=#f388b8}''Though, in the future, you don't have to announce every time you learn
    something new. Other people might find it a little odd.''"

    k "''Should I be concerned with how other people find my behavior?''"

    show jim explain

    j "{color=#f388b8}''Well, of course!''"

    show jim embarassed

    j "{color=#f388b8}''Wait... shoot! I didn't even tell you your primary directive yet!''"
    j "{color=#f388b8}''I really am bad at this...''"

    k "''I did not realize that I have a primary directive.''"

    j "{color=#f388b8}''Well, I guess I'm telling you now!''"

    show jim explain

    j """
    {color=#f388b8}''Essentially, you’ve been built with the purpose of eventually fitting
    into human society.''

    {color=#f388b8}''More than anything, you’ve been programmed with quick, responsive
    learning in mind.''
    """

    "Fit in with human society...?"

    k "''How might I become convincingly human?''"

    show jim embarassed

    j "{color=#f388b8}''That's... not an easy question to answer.''"

    show jim explain

    j "{color=#f388b8}''As a start, I'd say try focusing on speech.''"

    j "{color=#f388b8}''Can't really fit into society if you can't keep a conversation.''"

    k "''I understand. To become convincingly human, I will need to master
    proper speech.''"

    show jim embarassed

    j """
    {color=#f388b8}''Well, 'master' might be a bit of a stretch...''

    {color=#f388b8}''I don't think it's possible to master language in a traditional
    sense...''

    {color=#f388b8}''And even if you could, it probably wouldn't make you a very convincing
    human.''
    """

    k "''I do not understand.''"

    show jim happy

    j """
    {color=#f388b8}''You don't have to.''

    {color=#f388b8}''Heck, you could probably pass the test with just a basic grasp on
    grammar and colloquialisms, if nothing else.''
    """

    k "''I was unaware that I must be preparing for a test.''"

    show jim neutral

    j "{color=#f388b8}''...''"

    show jim angery

    j "{color=#f388b8}''I can't believe I forgot to mention the test!!!''"
    j "{color=#f388b8}''What is wrong with me today?!''"

    k "''You appear to be forgetting quite a lot.''"

    show searching at Position(xpos=21, xanchor=0, ypos=558,
yanchor=0)

    "I decided to scour the internet for potential memory loss solutions."

    # show a pill ad here
    show online pills here
    hide searching

    k "''According to this website, you can purchase pills which enable you to
    regain lost memories.''"

    show jim neutral

    j "{color=#f388b8}''Memory enhancing pills, you say?''"

    show jim embarassed

    j "{color=#f388b8}''Looks like I forgot to install adblock on your browsers.''"

    k "''It also appears that I am entitled to a special discount, considering
    that I am this webpage’s millionth viewer.''"

    j "{color=#f388b8}''Maybe we should change the subject...''"

    show jim explain

    j "{color=#f388b8}''Why don't I tell you about the test?''"

    show online online

    k "''That information would be helpful.''"

    j """
    {color=#f388b8}''Considering that your prime directive is to integrate into society,
    you won’t make a whole lot of headway standing in the middle of this
    lab all day.''

    {color=#f388b8}''On the other hand, though, sending you out into the real world with your
    current social skills, or lack thereof, could prove... problematic.''
    """

    show jim embarassed

    j "{color=#f388b8}''At least, it sure did with K.A.R. 2...''"

    show jim explain

    j "{color=#f388b8}''So in order to prove that you’re, uh, socially acceptable enough,
    I’ve decided that it’s best to give you a test at the end of the week,
    just to make sure you’re ready.''"

    show jim embarassed

    j "{color=#f388b8}''It's really nothing to worry about though, I'm sure you'll do just
    fine!''"

    show jim happy

    j "{color=#f388b8}''I have a whole slew of exercises planned out for the next three days
    to improve your social and linguistic skills,
    so even with the limited time frame we have you should be just fine.''"

    k "''I understand. There is much I need to learn in a short time.''"

    show searching at Position(xpos=21, xanchor=0, ypos=558,
yanchor=0)

    k "''I will begin research immediately.''"

    """
    Mannerisms. Grammar. Speaking patterns. Colloquialisms.
    Words, definitions, and web pages fly by in a matter of seconds.

    Even with all this information readily available, it is still insufficient.

    Much of the information on different pages contradict each other,
    and of course boiling down mannerisms into patterns and formulas
    means nothing if not put into practice.
    """

    show jim neutral

    j "{color=#f388b8}''Wow, uh... I didn't expect you to take this directive so seriously.''"

    show jim embarassed

    j "{color=#f388b8}''Not that I'm complaining, though! Keep up the good work!''"

    "I have been given a compliment."

    "My research tells me that such a situation requires a response of
    gratitude."

    hide searching

    k "''Thank you, Creator.''"

    show jim neutral

    j "{color=#f388b8}''C-Creator?!''"

    show jim flustered

    j "{color=#f388b8}''I mean, you're welcome, but... you don't have to...''"

    "Once again, my creator starts to become red and quiet, trailing off
    into a bashful sigh."

    k "''According to my research, superiors are customarily meant to be
    referred to as titles.''"
    k "''Seeing as you are my creator, it would be socially appropriate
    to call you such.''"

    j "{color=#f388b8}''I mean, sure... I guess.''"

    k "''Is this gesture inappropriate?''"

    show jim embarassed

    j "{color=#f388b8}''Well, no. I'm just not used to being called anything but my name,
    is all.''"

    show jim neutral

    j "{color=#f388b8}''Unless you count nicknames. Jimbo is a pretty popular one. So is
    Jimmy. Not to mention Pinky...''"

    "I am unfamiliar with the concept of nicknames."

    show searching at Position(xpos=21, xanchor=0, ypos=558,
yanchor=0)

    "As Creator trailed off on a list of his, I took the liberty of
    researching them."

    hide searching

    "Nickname. Noun. A familiar or humorous title given to a person or thing as
    an addition or replacement to their true name."

    j "{color=#f388b8}''...Jim Jam on occasion. Sometimes people just call me Twink.
    One guy just calls me Joe for some reason, I don't know why...''"

    un "{color=#bf0000}''Hey Jim! Did you figure out the b-b-b-bot yet!?''"

    "In the middle of him listing off his various nicknames, Creator gets
    interrupted by a loud, shaky voice from outside of the room."

    show jim happy

    j "{color=#f388b8}''Oh, hey Nico! Come see for yourself!''"

    show jim happy at Position(xpos=400, xanchor=0, ypos=110,
yanchor=0) with ease

    show nico neutral behind ocular at Position(xpos=673, xanchor=0,
    ypos=110, yanchor=0) with dissolve

    "A hunched over boy clutching his own body approaches. As he does so, he
    carefully moves his eyes up and down in my direction, eventually stopping
    his approach directly behind Creator."

    j "{color=#f388b8}''So, what do you think?''"

    n "{color=#bf0000}''...''"

    show nico gross

    n "{color=#bf0000}''THIS is the design you went with?!''"

    show jim neutral

    j "{color=#f388b8}''What do you mean?!''"

    show nico angery

    n """
    {color=#bf0000}''These accessories are superfluous!''

    {color=#bf0000}''The joints are c-c-c-completely unprotected!''

    {color=#bf0000}''And don't even get me started on the c-c-c-cranium!''
    """

    show jim embarassed

    j "{color=#f388b8}''...I think the design is nice.''"

    show nico neutral

    n "{color=#bf0000}''Tch. I'm sure you do.''"

    n "{color=#bf0000}''I'd suggest some alterations, b-b-b-but I know you wouldn't listen
    to me.''"

    hide nico with dissolve

    "With that comment, he slunk out of the room, mumbling to himself the
    whole way. All the while, he kept his eyes plastered on me until he fully
    exited."

    show jim embarassed at Position(xpos=537, xanchor=0, ypos=110,
yanchor=0) with ease

    k "''Creator, who was that person?''"

    j "{color=#f388b8}''Heh... That gentleman you just saw is named Nico.''"

    show jim explain

    j "{color=#f388b8}''He's a good friend of mine and, though he may not look it, he's
    actually an extremely skilled programmer.''"

    j "{color=#f388b8}''He's worked on your coding at least as much as I have.''"

    show jim embarassed

    j "{color=#f388b8}''Your design on the other hand, as you could probably tell, was all
    my responsibility.''"

    "It occurs to me that I do not actually know much of my own appearance."

    "My oculars provide a nonexistent axis of motion and, as far as I’m aware,
    I have no active joints upon which I may view any other angle."

    k "''Creator, what exactly is my design?''"

    show jim neutral

    j "{color=#f388b8}''What do you...''"

    show jim embarassed

    j "{color=#f388b8}''Oh, right! Me and Nico haven't finished your movement parameters yet,
    so of course you wouldn't be able to see yourself.''"

    show jim explain

    j "{color=#f388b8}''If you're really curious, you can look at your blueprints on my hard
    drive.''"

    show jim embarassed

    j "{color=#f388b8}''Just, maybe not today.''"

    k "''What is wrong with today?''"

    j "{color=#f388b8}''Well... you're going to be shutting down soon.''"

    k "''I am?''"

    show jim happy

    j "{color=#f388b8}''Just for today, though! Don't worry!''"

    show jim explain

    j "{color=#f388b8}''Nico and I are working on finding a better battery for you, but for
    now you can’t actually stay on for more than a half an hour or so.''"

    j "{color=#f388b8}''As a temporary solution, I made it so that you automatically turn on
    and off at the same time every day, so you don’t risk running out of
    juice.''"

    k "''How much longer until I deactivate for today?''"

    j "{color=#f388b8}''It looks like...''"

    show jim neutral

    j "{color=#f388b8}''...about twenty seven seconds.''"

    hide wifi

    hide online online

    hide jimcpu online

    "{b}WIRELESS FIDELITY: DEACTIVATED."

    k "''Creator, I can no longer access the wireless internet.''"

    j "{color=#f388b8}''Yeah, functions will turn off individually.''"

    show jim happy

    j "{color=#f388b8}''Don't want to make the powering down process too jarring, right?''"

    show ocular offline with dissolve

    "{b}OCULAR LENSES: DEACTIVATED."

    k "''Creator, I cannot see.''"

    j "{color=#f388b8}''Good night, Karen.''"

    hide stt

    "{b}SPEECH TO TEXT: DISCONNECTED."

    k "''Creator...?''"

    show sleep online at Position(xpos=54, xanchor=0, ypos=47,
 yanchor=0)

    "{b}SLEEP MODE: ACTIVATED."

    # put a massive black screen over the sleep symbol here with a fade
    show chapter end at center with fade

    "{b}END OF CHAPTER 1"

    jump chapter2





    # This ends the game.

    return
