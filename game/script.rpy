# The script of the game goes in this file.

init python in mystore:

    seenList = []

    def checkListForItem(id):
        if id not in seenList:
            seenList.append(id)
            print(len(seenList))
    
    def checkListLength():
        #47 unique passages
        if len(seenList) >= 35:
            renpy.show_screen("countdown")

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define unknown = Character("???")
define narrator = Character("Narrator")
define you = Character("You")
define stephen = Character("Stephen")
define madison = Character("Madison")
define george = Character("George")
define daniel = Character("Daniel")
define derek = Character("Derek")
define shannon = Character("Shannon")

default time = 600

default accusation_mode = False

define talked_to_stephen_about_madison = False
define are_korean = False
define saw_daniel_at_bar = False

define met_stephen = False
define met_madison = False
define met_george = False
define met_daniel = False
define met_derek = False
define met_shannon = False

#defining images
image bg_storefront = "images/mall_storefront.png"
image bg_fountain = "images/mall_fountain.png"
image bg_booth = "images/mall_booth.png"
image bg black_screen = "images/blackscreen.png"

image daniel neutral = "images/Daniel1WithPillar.png"
image daniel excited = "images/Daniel2WithPillar.png"
image daniel murderous = "images/Daniel3WithPillar.png"

image derek neutral = "images/Derek_Neutral.png"
image derek distressed = "images/Derek_Distressed.png"

image george mad = "images/George_Mad.png"
image george madder = "images/George_Madder.png"

image madison neutral = "images/Madison_Neutral.png"
image madison happy = "images/Madison_Happy.png"
image madison scared = "images/Madison_Scared.png"

image shannon neutral = "images/Shannon2.png"
image shannon excited = "images/Shannon1.png"

image stephen neutral = "images/Stephen_Neutral.png"
image stephen thinking = "images/Stephen_Thinking.png"


transform resize:
    size (900, 1200)
    xcenter 0.5



# The game starts here.

label start:
    scene bg black_screen
    play music "audio/Detective Theme Loop.mp3"

    show text "It is Halloween night. The year is 2003."
    with fade
    pause 3
    show text "You are a detective sent to investigate a series of killings that has plagued the small town."
    with fade
    pause 5
    show text "After deducing the pattern of victims, you have concluded that the killer is set to strike again tonight at the town mall." 
    with fade
    pause 5
    show text "You must now discover the identity of the killer before someone else meets an early grave..."
    pause 8
    menu:
        "Enter Mall":
            jump mall_beginning

label mall_beginning:

    scene bg_storefront

    narrator "The mall is crowded tonight, with the scent of cheap candy flavoring the air. Pop radio trash on the airwaves, flooded out by the laughter and chatter of a crowd feeling the Halloween spirit."

    narrator "The numbers are high tonight. Anyone can be a suspect."

    menu:
        "Time to investigate":
            jump mall_storefront
            
label mall_storefront:
    
    scene bg_storefront
    with fade
    show screen button

    menu:
        "Talk to Stephen" if met_stephen:
            jump stephen_menu
        "Talk to little boy" if met_stephen == False:
            jump stephen_1
        "Talk to Shannon" if met_shannon:
            jump shannon_menu
        "Talk to goatwoman" if met_shannon == False:
            jump shannon_1
        "Go to fountain":
            jump mall_fountain
        "Go to sunglasses booth":
            jump mall_booth

label mall_fountain:

    scene bg_fountain
    with fade
    show screen button

    menu:
        "Talk to Daniel" if met_daniel:
            jump daniel_menu
        "Talk to Honey Island Swamp Monster" if met_daniel == False:
            jump daniel_1
        "Talk to George" if met_george:
            jump george_menu
        "Talk to Mothman" if met_george == False:
            jump george_1
        "Go to storefront":
            jump mall_storefront
        "Go to sunglasses booth":
            jump mall_booth

label mall_booth:

    scene bg_booth
    with fade
    show screen button

    menu:
        "Talk to Derek" if met_derek:
            jump derek_menu_returning
        "Talk to moon man" if met_derek == False:
            jump derek_1
        "Talk to Madison" if met_madison:
            jump madison_menu
        "Talk to werewolf" if met_madison == False:
            jump madison_1
        "Go to storefront":
            jump mall_storefront
        "Go to fountain":
            jump mall_fountain

label stephen_1:

    scene bg_storefront
    show stephen neutral at resize
    play sound "audio/Stephen.wav"
    with dissolve
    $ met_stephen = True

    you "Hey kid, you're not in trouble. I just want to talk to you."
    stephen "Hello officer. How are you today, sir?"
    you "Oh, uh. I'm doing well. I just wanted to ask you a few questions."
    stephen "Of course. That is the nature of your job, and I hardly think you would bother speaking to a child like me if you didn't have questions of some sort."
    you "You are very well-spoken for your age. "
    stephen "Thank you, sir."
    you "Are you here with your parents?"
    stephen "Oh no, sir. Just me tonight."
    you "Just you? That can be dangerous. Make sure you're sticking with people you know alright? I'll be back with more questions."
    play sound "audio/Stephen.wav"
    stephen "Will do, officer."

    jump mall_storefront

label stephen_menu:
    
    scene bg_storefront
    show stephen neutral at resize
    with dissolve
    show screen button
    play sound "audio/Stephen.wav"
    stephen "Hello again officer. How is your investigation going, sir?"
    you "It could be better. I have some more questions to ask you."
    stephen "I'll help however I can, sir."
    menu:
        "Ask about the murder of Dorothy":
            jump stephen_2
        "Ask about the murder of Sora":
            jump stephen_3
        "Ask about the murder of Tom":
            jump stephen_4
        "Leave":
            jump mall_storefront
        "Accuse him of murder" if accusation_mode:
            jump stephen_5

label stephen_2:

    scene bg_storefront
    show stephen thinking at resize
    $ talked_to_stephen_about_madison = True

    $ mystore.checkListForItem(0)
    $ mystore.checkListLength()
    
    you "Where were you the night of October 7th?"
    stephen "That was the night of the parent-teacher conference. I attended with my caregivers and left promptly at 800PM alongside the rest of the students."
    you "Do you remember anyone else who was there that night?"
    stephen "I was with the rest of the team, the football team that is. I play quarterback for the school. "
    stephen "We were running shotgun roll out drills, but my team was struggling to get the snap to me."
    stephen "Of the 38 times we ran that drill, I was not able to receive the snap 11 times. After receiving the snap, things went smoothly and of the remaining 27 passes, 26 were successfully completed."
    stephen "I attribute the single failure to my awkward grip on that specific ball. One could argue that was partially a result of the snap as well."
    you "So your team was there?"
    stephen "I can personally attest that all of them were present at that conference. The cheerleaders were also all in attendance, including Daniel and poor Veronica, although I remember her being quite giddy that night."
    stephen "As the conference ended and we students began our scattered journeys home, I remember the cheerleaders dispersing and out emerged an obviously distressed Madison." 
    stephen "She fled, tears streaking down her face and went home."
    you "What time would you say this was?"
    stephen "Oh about 8:00PM. Same as the rest of the student body."
    you "Thank you for being so helpful, I think that'll be it for now."
    play sound "audio/Stephen.wav"
    stephen "Of course."

    jump mall_storefront

label stephen_3:

    scene bg_storefront
    show stephen thinking at resize
    you "Where were you on October 15th?"
    stephen "..."
    you "Stephen?"
    play sound "audio/Stephen.wav"
    stephen "Quiet officer. I'm trying to remember. What day of the week was October 15th?"
    you "That was a Wednesday."
    stephen "On Wednesdays I have football practice after school. After practice I always get picked up by my parents."
    menu:
        "When do you get picked up?":
            jump stephen_3_1
        "Did you do anything else that night?":
            jump stephen_3_2

label stephen_3_1:
    scene bg_storefront
    show stephen neutral at resize

    $ mystore.checkListForItem(1)
    $ mystore.checkListLength()

    you "When do you get picked up?"
    stephen "My parents know to always get me exactly at 5:30PM every Monday, Wednesday, and Friday. Holidays excepted of course"

    jump stephen_3_end

label stephen_3_2:
    scene bg_storefront
    show stephen neutral at resize

    $ mystore.checkListForItem(2)
    $ mystore.checkListLength()

    you "Did you do anything else that night?"
    stephen "Nothing that I don't normally do, officer. I ate dinner, did my homework, and was in bed by bedtime."
    you "And what time would that be?"
    stephen "9:00PM"

    jump stephen_3_end

label stephen_3_end:
    scene bg_storefront
    show stephen neutral at resize
    you "I see. I'll come back if I have any more questions. Take care of yourself."
    play sound "audio/Stephen.wav"
    stephen "Of course, officer."

    jump mall_storefront

label stephen_4:

    $ mystore.checkListForItem(3)
    $ mystore.checkListLength()

    scene bg_storefront
    show stephen neutral at resize
    you "What were you doing last Thursday?"   
    stephen "I was eating ice cream, officer. Mint chocolate chip. Here in the mall with my parents."
    you "What time was this?"
    stephen "Right after school. I remember it being an oddly warm day for October, so my father, ever the fiend for sugary treats, suggested it. He cited my age as an excuse which I resent somewhat, but I cannot deny. Ice cream is good."
    you "What did you do after that?"
    stephen "After finishing our confections I informed my parents of the homework I had yet to do, so we returned home hastily. I cannot state a specific time, in fear of being incorrect, but I can give a relative time."
    stephen "When we went home the sun was still shining."
    you "Thank you Stephen, that should be all for now. I'll return if I have any more questions."
    play sound "audio/Stephen.wav"
    stephen "Of course."

    jump mall_storefront

label stephen_5:
    scene bg_storefront
    show stephen neutral at resize
    you "I'm arresting you on suspicion of murder. You're coming with me."
    stephen "Officer, surely there must be some sort of mistake?"
    narrator "You tackle Stephen to the ground and handcuff him before he can escape."
    scene bg_storefront with fade
    jump stephen_6

label stephen_6:

    scene bg black_screen with dissolve

    show text "You escorted Stephen back to the police station. While cooperative before, at the station he refused to speak without his parents present."
    with fade
    pause 5
    show text "Once they arrive, he recites the same exact information he told you without flaw."
    with fade
    pause 5
    show text "The next morning, you find that there has been another murder committed at the mall shortly after you escorted stephen off of the premises." 
    with fade
    pause 5
    show text "The victim was a moonman named Derek."
    with fade
    pause 5
    show text "The killer is still on the loose."

label madison_1:

    scene bg_booth
    show madison neutral at resize
    with dissolve
    $ met_madison = True
    play sound "audio/Madison.wav"
    you "Excuse me, may I have a word?"
    madison "Oh? Oh, yes, what is it?"
    you "Someone's awfully quiet this Halloween night."
    madison "Yeah, well... it's loud enough already don't you think?"
    
    menu:
        "Yeah, that's fair":
            jump madison_1_1
        "Could be worse":
            jump madison_1_2

label madison_1_1:
    scene bg_booth
    show madison scared at resize
    play sound "audio/Madison.wav"    
    you "Yeah, that's fair"
    madison "Besides, I don't think anyone really wants me talking"

    jump madison_1_end

label madison_1_2:
    scene bg_booth
    show madison scared at resize
    play sound "audio/Madison.wav"
    you "Could be worse"
    madison "Well, I don't think there's anywhere louder than this place on Halloween night."

    jump madison_1_end

label madison_1_end:
    scene bg_booth
    show madison neutral at resize
    play sound "audio/Madison.wav"

    you "you come here alone?"
    madison "Yeah... I've never really been good with others."
    you "It's quite dangerous lately, with all these killings and all. Hope you're keeping yourself safe"
    madison "Yeah, I heard about them. Quite a frightening thought "
    you "I'll get back to you if I have any more questions"
    madison "Oh, sure"

    jump mall_booth

label madison_menu:
    
    scene bg_booth
    show madison happy at resize
    with dissolve
    show screen button
    play sound "audio/Madison.wav"

    madison "Oh, hi... good to see you again"
    menu:
        "Ask about the murder of Dorothy":
            jump madison_4
        "Ask about the murder of Sora":
            jump madison_3
        "Ask about the murder of Tom":
            jump madison_2
        "Leave":
            jump mall_booth
        "Accuse her of murder" if accusation_mode:
            jump madison_6

label madison_2:

    scene bg_booth
    show madison neutral at resize
    play sound "audio/Madison.wav"

    you "Where were you on the night of October 23rd?"
    madison "I was in the mall, just like tonight..."
    you "What were you doing here?"
    madison "I was looking to buy some new headphones... someone busted my old ones and I needed some new ones for my iPod"
    you "When did you leave?"
    madison "Around 9:30?"
    menu:
        "What do you listen to?":
            jump madison_2_1
        "Any other stores you visited?":
            jump madison_2_2

label madison_2_1:
    scene bg_booth
    show madison happy at resize
    play sound "audio/Madison.wav"

    $ mystore.checkListForItem(4)
    $ mystore.checkListLength()

    you "What do you listen to?"
    madison "Oh, it's a small band called My Chemical Romance"
    madison "They just released their first album, I've been listening to it nonstop"
    madison "The other kids think it's lame, but I just think they're neat"

    jump madison_2_end

label madison_2_2:
    scene bg_booth
    show madison neutral at resize
    play sound "audio/Madison.wav"

    $ mystore.checkListForItem(5)
    $ mystore.checkListLength()

    you "Any other stores you visited?"
    madison "I just checked out the classics section and Barnes and Noble"
    madison "I was really just browsing. I kinda left after eating dinner"

    jump madison_2_end

label madison_2_end:
    scene bg_booth
    show madison neutral at resize
    play sound "audio/Madison.wav"
    you "Have you noticed anything about the booths that night?"
    madison "Well, the fried chicken stand was unoccupied when I got there... I suppose that was when... you know."
    madison "I was gonna get some chicken for dinner that night, but it was empty, so I just got a sandwich at Sandy's."
    you "Did you encounter anyone else there?"
    madison "Well, that weird moon guy also tried selling me some tacky glasses while I was on the way out. He was packing up his stand, but I guess he just wanted to squeeze one more customer."
    you "I'll get back to you if I have any more questions"
    madison "Oh, sure"

    jump mall_booth

label madison_3:
    
    scene bg_booth
    show madison neutral at resize
    play sound "audio/Madison.wav"
    you "Where were you on the night of October 15th?"
    madison "I was at a friend's house. We have this literature club we do every Wednesday. We just read and listen to music. "
    you "Were you at the town square at any point that day?"
    madison "I was there in the afternoon. That's where we all meet up beforehand."
    you "What timeframe were you there?"
    madison "I'd say about three to five?"

    menu:
        "Did you see anything suspicious while there?":
            jump madison_3_1
        "Is there anyone who can verify your presence?":
            jump madison_3_2

label madison_3_1:

    scene bg_booth
    show madison neutral at resize
    play sound "audio/Madison.wav"

    $ mystore.checkListForItem(6)
    $ mystore.checkListLength()

    you "Did you see anything suspicious while there?"
    madison "Not really. I saw the moon sales guy heading into the bar before I left, but that's all really. Never thought I'd see him outside of the mall."

    jump madison_3_end

label madison_3_2:

    scene bg_booth
    show madison neutral at resize
    play sound "audio/Madison.wav"

    $ mystore.checkListForItem(7)
    $ mystore.checkListLength()

    you "Is there anyone who can verify your presence?"
    madison "you can go talk to some of my friends. I think I saw them leave a while ago though."

    jump madison_3_end

label madison_3_end:

    scene bg_booth
    show madison neutral at resize
    play sound "audio/Madison.wav"
    you "Okay, I think that's it for now"
    you "I'll get back to you if I have any more questions"
    madison "Oh, sure"

    jump mall_booth


label madison_4:

    scene bg_booth
    show madison neutral at resize
    play sound "audio/Madison.wav"
    you  "What can you tell me about the murder of Dorothy Williams?"
    madison "Oh right, Veronica's mother... It's quite awful what happened to her."
    you "What was your relationship with Veronica Williams?"
    madison "Well, she was always picking on me since we were in elementary school. She kept calling me \"half-developed\". It was horrible."
    menu:
        "Do you think she knows how it feels now?":
            jump madison_4_11
        "I'm sorry about that":
            jump madison_4_12

label madison_4_11:
    scene bg_booth
    show madison neutral at resize
    play sound "audio/Madison.wav"

    $ mystore.checkListForItem(8)
    $ mystore.checkListLength()

    you "Do you think she knows how it feels now?"
    madison "Well, she was always horrible to everyone, thought she was better than us just because she's pretty. Maybe now, she'll be a bit more sympathetic to everyone."
    jump madison_4_mid1

label madison_4_12:
    scene bg_booth
    show madison neutral at resize
    play sound "audio/Madison.wav"

    $ mystore.checkListForItem(9)
    $ mystore.checkListLength()

    you "I'm sorry about that"
    madison "Yeah. Can't imagine what she's going through now, losing her mother like that."
    jump madison_4_mid1

label madison_4_mid1:
    scene bg_booth
    show madison neutral at resize
    play sound "audio/Madison.wav"
    you "Where were you that night?"
    madison "Oh, I skipped the parent teacher conference. My grades are pretty good, so there wasn't really a need for me to be there, you know?"
    madison "I was at home all night checking my picture comments on MySpace."
    menu:
        "That's a lie. I've got a testimony saying you were seen at the conference that night." if talked_to_stephen_about_madison:
            jump madison_4_1
        "Seems reasonable. Normal teenage stuff. I'll never understand it.":
            jump madison_4_2

label madison_4_1:
    
    scene bg_booth
    show madison scared at resize
    play sound "audio/Madison.wav"

    $ mystore.checkListForItem(10)
    $ mystore.checkListLength()

    you "That's a lie. I've got a testimony saying you were seen at the conference that night."
    madison "What? Who told- Alright, I lied!"
    madison "Veronica and her friends were being horrible to me that night. The night it happened..."
    madison "She won the talent show the week before. Everyone was raving about it. She was rubbing it in my face again, about how I'd never make the team... because I wasn't fully \"developed\"..."
    madison "How would it look? If I had told you what really happened?"
    you "I'd say that gives you a prime motive."
    madison "But I did not kill her mother! I swear!"
    you "That remains to be seen..."

    jump madison_4_mid

label madison_4_2:
    
    scene bg_booth
    show madison neutral at resize
    play sound "audio/Madison.wav"

    $ mystore.checkListForItem(11)
    $ mystore.checkListLength()

    you "Seems reasonable. Normal teenage stuff. I'll never understand it."
    madison "Best if you don't."

    jump madison_4_mid

label madison_4_mid:

    scene bg_booth
    show madison scared at resize
    play sound "audio/Madison.wav"
    madison "Is there... anything else?"

    menu:
        "Tell me more about Dorothy":
            jump madison_4_3
        "Who would wish Dorothy any harm?":
            jump madison_4_4


label madison_4_3:
    scene bg_booth
    show madison neutral at resize
    play sound "audio/Madison.wav"

    $ mystore.checkListForItem(12)
    $ mystore.checkListLength()
    
    you "Tell me more about Dorothy."
    madison "Well, Veronica always said she was following her mother's footsteps, so I always saw her as an old cheerleader. She was quite the big name in our school. "
    madison "I heard people say that no one could work up a crowd like her."

    jump madison_4_end

label madison_4_4:
    scene bg_booth
    show madison neutral at resize
    play sound "audio/Madison.wav"

    $ mystore.checkListForItem(13)
    $ mystore.checkListLength()

    you "Who would wish Dorothy any harm?"
    madison "I'm not quite sure... Veronica was pretty popular, so I guess she'd have a lot of people who have it out for her"
    madison "But I don't know if there would be anyone who's got something against her mom."

    jump madison_4_end

label madison_4_end:
    scene bg_booth
    show madison neutral at resize
    play sound "audio/Madison.wav"
    you "I believe that's all"
    you "I'll get back to you if I have any more questions"
    madison "Oh, sure"

    jump mall_booth

label madison_5:

    scene bg_booth
    show madison neutral at resize
    play sound "audio/Madison.wav"

    $ mystore.checkListForItem(14)
    $ mystore.checkListLength()

    you "So you're really into literature huh."
    madison "Yeah..."
    you "Might I ask why?"
    madison "Well, it helps me to feel like I can just get away from this crazy world for a bit y'know?"
    you "I get the feeling"
    madison "Between you and me, I've been getting into writing lately. It's not enough for me to immerse myself anymore. I wanna create new stories too"
    you "What do you write about?"
    madison "It's just a bunch of teen dramas, that's all. I've been working on one about this character who finally gets back at her bullies"
    you "Sounds very Carrie."
    madison "Yeah, it's cliche, I know. I was working on it... until, y'know... all that stuff with Veronica..."
    you "you know that is very concerning behavior right?"
    madison "Yeah, I know... but everything I've had to deal with my whole life..."
    madison "Please don't tell anyone..."
    you "I won't make any promises"
    you "I'll get back to you if I have any more questions"
    madison "Oh, sure"

    jump mall_booth

label madison_6:
    scene bg_booth
    show madison scared at resize
    play sound "audio/Madison.wav"
    you "I'm arresting you on suspicion of murder. You're coming with me."
    madison "Wait, what? This must be some kind of mistake!"
    madison "Please, I trusted you! I didn't do anything wrong I swear!"
    you "You can defend yourself all you want at the station"
    narrator "You tackle Madison to the ground and handcuff her before she can escape"
    scene bg_booth with fade
    jump madison_7


label madison_7:

    scene bg black_screen with dissolve

    show text "you escorted Madison back to the police station and questioned her all night."
    with fade
    pause 5
    show text "She is scared and despite an anxiety attack, answers all the questions truthfully."
    with fade
    pause 5
    show text "The next morning, you find that there has been another murder committed at the mall shortly after you escorted Madison off of the premises." 
    with fade
    pause 5
    show text "The victim was a moonman named Derek."
    with fade
    pause 5
    show text "The killer is still on the loose."

label george_1:

    scene bg_fountain
    show george mad at resize
    with dissolve
    $ met_george = True

    play sound "audio/George.wav"

    george "You! Hey you!"
    you "Pardon?"
    george "You don't happen to be a dokkaebi, right?"

    menu: 
        "Maybe I am":
            jump george_1_1
        "No.":
            jump george_1_2

label george_1_1:

    scene bg_fountain
    show george madder at resize
    $ are_korean = True

    you "Maybe I am"
    play sound "audio/George.wav"
    george "You better watch yourself then. We don't want your kind here, and last I heard, y'all have been droppin' like flies."

    jump george_1_end

label george_1_2:

    scene bg_fountain
    show george mad at resize
    $ are_korean = False

    you "No."
    play sound "audio/George.wav"
    george "Good! This town don't need more o' those roaming around. We've been diluted enough as it is."

    jump george_1_end

label george_1_end:

    scene bg_fountain
    show george madder at resize
    you "You got something against dokkaebis?"
    george "Hell yeah I do! I ain't fought a war just to have the bastards I defended my country against livin here like it's nothin'."
    you "One of them was killed a few weeks ago."
    play sound "audio/George.wav"
    george "You know, I say the better for it!"
    you "You don't have many friends do you."
    george "Who needs any?"
    you "That answers my question."
    you "I'll be back with some more questions for you."
    george "Heh??"

    play sound "audio/George.wav"

    jump mall_fountain

label george_menu:
    scene bg_fountain
    show george mad at resize
    with dissolve
    show screen button
    play sound "audio/George.wav"
    george "Ehh?"
    menu:
        "Ask about murder of Dorothy":
            jump george_4
        "Ask about murder of Sora":
            jump george_3
        "Ask about murder of Tom":
            jump george_2
        "Ask about his background":
            jump george_5
        "Leave":
            jump mall_fountain
        "Accuse him of murder" if accusation_mode:
            jump george_6

label george_2:

    scene bg_fountain
    show george mad at resize

    you "Where were you on the night of October 23th?"
    george "Well I was at the mall, like I am right now. Shopping for some o' that new technology all the youngsters are ravin' about."
    you "What might that be?"
    george "A microwave."
    you "Uhm okay... when was this?"
    george "Around the evening. That damn moon man was shouting his ass off again. Waxin' poetic about his shay-dees. It's a miracle he even gets people to buy that crap."

    menu:
        "Anything else suspicious that you've seen?":
            jump george_2_1
        "Anyone else you've seen in the mall around that time?":
            jump george_2_2

label george_2_1:
    
    scene bg_fountain
    show george madder at resize

    $ mystore.checkListForItem(15)
    $ mystore.checkListLength()

    you "Anything else suspicious that you've seen?"
    play sound "audio/George.wav"
    george "Tell you what I've seen. That damn Honey Islander's been acting real fishy lately. I know his kind when I see it. "
    george "They're all a bunch of good for nothin' weirdos. Nothing's felt right since they started showing up in droves. I know I saw him running around trespassing in the employees room last week."

    jump george_2_mid

label george_2_2:
    
    scene bg_fountain
    show george mad at resize

    $ mystore.checkListForItem(16)
    $ mystore.checkListLength()

    you "Anyone else you've seen in the mall around that time?"
    play sound "audio/George.wav"
    george "I saw a werewolf hanging around during the early evening. Looked real gnarly, like she wasn't fully a wolf yet."
    george "Now I don't know what's up with her, but werewolves, those are real Americans right there. Not like any of the riffraff that claim they're one of us."

    jump george_2_mid

label george_2_mid:
    
    scene bg_fountain
    show george mad at resize
    you "I'll keep this in mind."
    menu:
        "How long were you there?":
            jump george_2_3
        "What did you do after?":
            jump george_2_4

label george_2_3:
    
    scene bg_fountain
    show george mad at resize

    $ mystore.checkListForItem(17)
    $ mystore.checkListLength()

    you "How long were you there?"
    george "I don't know, like half past eight?"

    jump george_2_end

label george_2_4:
    
    scene bg_fountain
    show george mad at resize

    $ mystore.checkListForItem(18)
    $ mystore.checkListLength()

    you "What did you do after?"
    george "I went home, and tried to see if I could get the damn thing to work. Everything's so complicated these days, why can't we go back to the old ways of using the fireplace?"
    
    jump george_2_end

label george_2_end:
    
    scene bg_fountain
    show george mad at resize   
    you "Alright, thanks for the help."
    george "Heh??"
    play sound "audio/George.wav"

    jump mall_fountain

label george_3:

    scene bg_fountain
    show george madder at resize
    you "What can you tell me about the murder of Sora Kim?"
    george "Ehh! The dokkaebi?! That damn trash gnome had it coming!"
    you "Is that an admission of guilt? Or..."
    george "Now now now, I never said that-"
    you "Where were you on the night of the murder?"
    george "I was watching TV at home, classic cinema."
    you "What were you watching?"
    george "Birth of a Nation."
    you "..."
    you "Okay... when was this?"
    george "Around 8?"
    menu:
        "What were you doing at 11PM?":
            jump george_3_1
        "Why were you watching that?":
            jump george_3_2

label george_3_1:

    scene bg_fountain
    show george madder at resize

    $ mystore.checkListForItem(19)
    $ mystore.checkListLength()

    you "What were you doing at 11PM?"
    george "Well I was sleeping! What are you, expectin' an ol' codger like me to be awake at the witching hour?!"
    you "That's not the witching hour, but noted."

    jump george_3_end

label george_3_2:

    scene bg_fountain
    show george mad at resize

    $ mystore.checkListForItem(20)
    $ mystore.checkListLength()

    you "Why were you watching that?"
    george "Calms my nerves a bit"

    jump george_3_end

label george_3_end:

    scene bg_fountain
    show george madder at resize
    you "Do you know of anyone who would wish this man harm?"
    george "I tell ya, that's a lotta people"
    if are_korean:
        george  "A lot of us wish your kind harm." 
    else:
        george  "Between you and me, I'd say this town has it out for them. I just know it."
    george "I'm just the only one brave enough to speak my mind and say it as it is."
    you "I'll keep this in mind."
    george "Heh??"
    play sound "audio/George.wav"

    jump mall_fountain

label george_4:

    scene bg_fountain
    show george mad at resize
    you "Where were you on the night of October 7th?"
    george "Eh that was a lifetime ago. I was at the school."
    menu:
        "What were you doing there?":
            jump george_4_1
        "You realize that was the site of a gruesome murder?":
            jump george_4_2

label george_4_1:
    
    scene bg_fountain
    show george mad at resize

    $ mystore.checkListForItem(21)
    $ mystore.checkListLength()

    you "What were you doing there?"
    george "There was a parent-teacher conference. My niece was sick, so I went on behalf of her daughter."

    jump george_4_mid

label george_4_2:
    
    scene bg_fountain
    show george mad at resize

    $ mystore.checkListForItem(22)
    $ mystore.checkListLength()

    you "You realize that was the site of a gruesome murder?"
    george "Ehhh? First I ever heard of it. When was that?"
    you "October 7th."

    jump george_4_mid

label george_4_mid:
    
    scene bg_fountain
    show george mad at resize
    you "How long were you in the building for?"
    george "Roughly 6-9?"
    george "Those damn gorgons held me up. Wouldn't shut up about sculpturing. Felt like I was stone for three hours."
    play sound "audio/George.wav"
    george "What has this country come to? Having gorgons educate our children?!"
    you "What did you do after? Say, an hour after that?"
    george "I took my niece's daughter home. We live a neighborhood away."
    you "Who else was in the school at the time that's here tonight?"
    george "All the children here of course. High schoolers and elementary alike. I also saw that goat woman over there among the fray. At least this place has some real Americans."

    menu:
        "When did they leave?":
            jump george_4_3
        "Would any of them have a reason to harm the victim?":
            jump george_4_4

label george_4_3:
    
    scene bg_fountain
    show george mad at resize

    $ mystore.checkListForItem(23)
    $ mystore.checkListLength()

    you "When did they leave?"
    george "I think that goatwoman left around 9PM?"

    jump george_4_end

label george_4_4:
    
    scene bg_fountain
    show george madder at resize

    $ mystore.checkListForItem(24)
    $ mystore.checkListLength()

    you "Would any of them have a reason to harm the victim?"
    george "How should I know?! I tell you what, it's probably some damn foreigner tryna rid this country of its rightful population!"

    play sound "audio/George.wav"

    jump george_4_end
label george_4_end:
    
    scene bg_fountain
    show george mad at resize
    you "I'll keep this in mind."
    george "Heh??"

    jump mall_fountain


label george_5:

    scene bg_fountain
    show george mad at resize

    $ mystore.checkListForItem(25)
    $ mystore.checkListLength()

    you "You said you fought in the war?"
    george "What else do you need to know? Served my country well in the war. Drafted back in '51. Honorable discharge. "
    george "Killed a whole lotta dokkaebis, and seen some of my best friends die at their hand."
    you "What about after?"
    george "Went back to crop dustin'. It's all I was ever good at."
    you "You're a crop duster?"
    george "All my life. Then I took a tumble back in '76. Doctors said I could never do it again. The hell do they know?!"
    george "Pair that with that new invention the youngsters made, and I was out of a job"
    you "What invention was that?"
    george "The aeroplane."
    george "Damn youngins these days can't tell the good end of a hoe even if it smacked 'em in the ass."
    george "What they all need is a good few years o' hard old fashioned labor"
    if are_korean:
        george "You must be one o' the good ones."
    else:
        george "Heh, you really know how to keep an old soul good company."

    you "I'm glad you're alright. I'll talk to you if I have anymore questions."
    george "Heh??"

    play sound "audio/George.wav"
    
    jump mall_fountain

label george_6:
    scene bg_fountain
    show george madder at resize
    
    you "I'm arresting you on suspicion of murder. You're coming with me."
    george "What the hell?!"
    george "I knew it! There was something fishy about you from the start! Your kind's made this country hell to live on, you hear me?!"
    george "Hard working men like me have to suffer because of freaks like you!"
    you "Save the insults for the interrogation, gramps."
    narrator "You tackle George to the ground and handcuff him before he can escape."
    scene bg_booth with fade
    jump derek_7

label george_7:

    scene bg black_screen with dissolve

    show text "You escorted George back to the police station and questioned him all night."
    with fade
    pause 5
    show text "He is agitated and hostile, but begrudgingly answers all the questions truthfully."
    with fade
    pause 5
    show text "The next morning, you find that there has been another murder committed at the mall shortly after you escorted George off of the premises." 
    with fade
    pause 5
    show text "The victim was a moonman named Derek."
    with fade
    pause 5
    show text "The killer is still on the loose."

label daniel_1:

    scene bg_fountain
    show daniel neutral at resize
    with dissolve
    $ met_daniel = True
    play sound "audio/DanielRegular.wav"

    you "Hello, I'd like to ask you a few questions."
    daniel "..."
    you "Excuse me? Behind the pillar? "
    daniel "..."
    you "Just a few questions, you're not in trouble."
    daniel "hello..."
    you "Hi, what's your name?"
    daniel "..."
    you "I'm with the local police department, it's alright."
    daniel "daniel..."
    you "Daniel! That's a great name. Like Daniel Radcliffe. you know, like Harry Potter?"
    show daniel excited at resize
    daniel "Daniel Radcliffe? I love Daniel Radcliffe! I love how he isn't afraid to do what no one else will do for the sake of a great show! "
    daniel "If you ask me, that's a great performer. Someone who will put it all on the line, dignity and prestige and fame and wealth, everything. For the sake of the performance."
    daniel "But not just the performance! Oh no. Just for performance... that would be so... gaudy. "
    daniel "Horrible. No, no. Radcliffe. He's different. He, he, he just. He pokes at your brain and asks you, \"Do you believe me? I am the world's strangest person, the world's strangest THING. BELIEVE ME.\""
    you "Yeah, he's a... you know what you said. A great performer. Anyways, I'd love to ask you a few questions, Daniel. Just a few it won't tak-"
    show daniel neutral at resize
    daniel "..."
    you "Okay... I'll come back to ask you a few questions later, alright Daniel?"
    daniel "..."

    jump mall_fountain

label daniel_menu:
    
    scene bg_fountain
    show daniel neutral at resize
    with dissolve
    show screen button
    play sound "audio/DanielRegular.wav"
    you "Hey Daniel. I'd like to ask you a few questions if that's alright."
    daniel "...ok"

    menu:
        "Ask him about performance":
            jump daniel_2
        "Ask him about the murder of Dorothy":
            jump daniel_3
        "Ask about the murder of Sora":
            jump daniel_4
        "Ask about the murder of Tom":
            jump daniel_5
        "Leave":
            jump mall_fountain
        "Accuse him of murder" if accusation_mode:
            jump daniel_6

label daniel_2:

    scene bg_fountain
    show daniel neutral at resize

    you  "It seems like you really like Daniel Radcliffe. Are you a performer too?"
    show daniel excited at resize
    play sound "audio/DanielRegular.wav"
    daniel "I LOVE PERFORMING. It's art, it's gorgeous, it's beautiful. There isn't anything like it."
    menu:
        "That's really cool! Are you a dancer?":
            jump daniel_2_1
        "That's really cool! Are you an actor in your school's theater program?":
            jump daniel_2_2

label daniel_2_1:

    scene bg_fountain
    show daniel excited at resize

    $ mystore.checkListForItem(26)
    $ mystore.checkListLength()

    you "That's really cool! Are you a dancer?"
    daniel "No, no. Dancers don't get enough performances. I need more."
    play sound "audio/DanielRegular.wav"
    daniel "I'm a cheerleader. We get to perform at every game, and after school every day we practice outdoors."
    daniel "Rain or shine. Everyone will see us, see me."

    jump daniel_2_end

label daniel_2_2:

    scene bg_fountain
    show daniel excited at resize

    $ mystore.checkListForItem(27)
    $ mystore.checkListLength()

    you "That's really cool! Are you an actor in your school's theater program?"
    daniel "Acting? In my school's theater program?"
    you "Yeah, like Cats? Phantom of the Opera?"
    play sound "audio/DanielRegular.wav"
    daniel "Those children don't even know the first thing about putting on a show. To call them actors is to spit in the face of all performers."
    daniel "All of them. All that rehearsal to put on a SINGLE shoddy performance, to then receive an undeserving, paltry applause."
    you "That's quite harsh."
    daniel "And yet true. I could never be part of that circus. No. I'm a cheerleader."
    play sound "audio/DanielRegular.wav"
    daniel "Rain or shine, snow or sleet, we are there outdoors every day after school without fail."
    daniel "That's performance. That's dedication. Everyday, we are admired."

    jump daniel_2_end

label daniel_2_end:

    scene bg_fountain
    show daniel excited at resize
    you "Alright... I'll come back if I have more questions for you."
    show daniel neutral at resize
    daniel "...okay"

    jump mall_fountain

label daniel_3:

    scene bg_fountain
    show daniel neutral at resize

    you "Do you remember where you were the night of October 7th?"
    play sound "audio/DanielRegular.wav"
    daniel "...school. parent-teacher conference..."
    you "And how long were you there for?"
    daniel "8. "
    daniel "...everyone left at 8."
    you "Do you remember anyone else being there?"
    daniel "football players... cheerleaders..."
    daniel "and madison."

    menu:
        "Did you see if any of them stayed past 8?":
            jump daniel_3_1
        "Who's Madison?":
            jump daniel_3_2


label daniel_3_1:
    
    scene bg_fountain
    show daniel neutral at resize

    $ mystore.checkListForItem(28)
    $ mystore.checkListLength()

    you "Did you see if any of them stayed past 8?"
    daniel "...no... everyone left at the same time."

    jump daniel_3_end

label daniel_3_2:
    
    scene bg_fountain
    show daniel neutral at resize

    $ mystore.checkListForItem(29)
    $ mystore.checkListLength()

    you "Who's Madison?"
    daniel "..."
    play sound "audio/DanielRegular.wav"
    daniel "student... werewolf."
    you "Did something happen with her?"
    daniel "... the cheerleaders talked with her. I wasn't part of that."
    you "Talked with her how?"
    daniel "bad. she cried and ran away..."
    you "Did they hurt her?"
    daniel "...no. it's normal..."

    jump daniel_3_end

label daniel_3_end:
    
    scene bg_fountain
    show daniel neutral at resize
    you "I see. Well thanks for speaking with me, Daniel."
    you "I'll return if I have more questions."
    daniel "...okay."

    jump mall_fountain

label daniel_4:

    scene bg_fountain
    show daniel neutral at resize
    you "Where were you on October 15th?"
    show daniel excited at resize
    play sound "audio/DanielRegular.wav"
    daniel "I was home of course. Practicing my cheer routines"
    you "Were you at school? October 14th was a Wednesday."
    daniel "Well, yes obviously. Cheer practice is after school."
    daniel "After cheer I was furious because I couldn't get this move down."
    play sound "audio/DanielRegular.wav"
    daniel "I just can't STAND it when that happens. So I went home to keep practicing."
    menu:
        "I have someone who claims they saw you at the town square that day. Care to explain?" if saw_daniel_at_bar:
            jump daniel_4_1
    jump daniel_4_2

label daniel_4_1:

    scene bg_fountain
    show daniel excited at resize

    $ mystore.checkListForItem(30)
    $ mystore.checkListLength()

    you "I have someone who claims they saw you at the town square that day. Care to explain?"
    show daniel neutral at resize
    daniel "..."
    play sound "audio/DanielRegular.wav"
    daniel "I forgot..."
    daniel "I walk through the town square to get home..."
    daniel "..."

    jump daniel_4_end

label daniel_4_2:

    scene bg_fountain
    show daniel excited at resize

    $ mystore.checkListForItem(31)
    $ mystore.checkListLength()

    you "Were you able to get that move down?"
    daniel "Oh yes! The process was quite... inelegant. But the result was well worth it. Beautiful."
    you "I'm glad it went well!"


    jump daniel_4_end

label daniel_4_end:

    scene bg_fountain
    show daniel neutral at resize
    you "Well that's all I have for now. I'll talk to you again if I have any more questions."
    daniel "...okay."

    jump mall_fountain

label daniel_5:

    scene bg_fountain
    show daniel neutral at resize

    $ mystore.checkListForItem(32)
    $ mystore.checkListLength()

    you "Where were you on the night of October 23rd?"
    play sound "audio/DanielRegular.wav"
    daniel "at the mall."
    you "Are you aware there was a murder that night?"
    daniel "...no. who?"
    you "Tom Chatawa. The fried chicken vendor down by Wetzel's Pretzals. Do you remember seeing him there that day?"
    daniel "...yes."
    you "About what time would you say you saw him?"
    daniel "6:30... I saw him on my way out."
    daniel "too many people..."
    you "So you're saying you saw him and left at 630PM?"
    daniel "...yes."
    you "Did you see anyone else there?"
    daniel "...too many people. can't remember."
    you "I see. Well thanks for trying, Daniel."
    you "I'll come back if I have any more questions to ask you"
    daniel "...okay."

    jump mall_fountain

label daniel_6:
    scene bg_fountain
    show daniel neutral at resize
    daniel "..."
    show daniel murderous at resize
    with hpunch
    play sound "audio/DanielMurder.wav"
    daniel "DIE THEN."
    narrator "Daniel lunges at you, but you're ready for it. You wrestle him to the ground and handcuff him."
    you  "You have the right to remain silent. Anything you say can and will be used against you in a court of law. You have the right to talk to a lawyer for advice before we ask you any questions. You have the ri-"
    daniel "DON'T READ THIS DRIVEL TO ME. A SCRIPT?? PUTRID. YOU DISGUST ME."
    you "If you cannot afford a lawyer, one will be appointed for you before any questioning if you wish. If you decide to answer questions now without a lawyer present, you have the right to stop answering at any time."
    narrator "Daniel fights the whole way as you take him to the police station."
    scene bg_fountain with fade
    jump daniel_7


label daniel_7:
    scene bg black_screen with dissolve

    show text "Daniel is convicted of all three murders."
    with fade
    pause 5
    show text "After some intense interrogation, you discover that he was planning to kill Derek that night."
    with fade
    pause 5
    show text "When he learned you were on to him, he decided to kill you instead."
    with fade
    pause 5
    show text "You didn't just save the town."
    with fade
    pause 3
    show text "You saved yourself."
    with fade
    pause 5 
    show text "Killer captured."

    return

label daniel_8:
    scene bg_fountain
    narrator "You try to sift your way through the crowd, but end up in a large crush of visitors. You can’t help but feel an ominous pair of eyes on you."
    show daniel neutral at resize
    daniel "..."
    show daniel murderous at resize
    with hpunch
    play sound "audio/DanielMurder.wav"
    daniel "YOU DIE NOW."
    narrator "Daniel lunges at you, and quickly plunges a knife into your chest. The last thing you see is Daniel’s face glancing at you, manically laughing as he continues his flurry of stabs while you take your last breath."    
    daniel "It's all a part of the show..."
    scene bg_fountain with fade
    jump daniel_9

label daniel_9:

    scene bg black_screen with dissolve

    show text "Your investigation has probed the suspicion of the killer, placing you directly into their crosshairs."
    with fade
    pause 5
    show text "You were unable to deduce the killer’s identity in time."
    with fade
    pause 5
    show text "Your name has now become another in a long line of forgotten obituaries." 
    with fade
    pause 5
    show text "Despite a large crowd, with a quick escape, the killer managed to evade capture again."
    with fade
    pause 5
    show text "The killer is still on the loose."

    return

label derek_1:

    scene bg_booth

    $ met_derek = True
    show derek distressed at resize
    with dissolve
    play sound "audio/Derek1.wav"
    #holding out sunglasses
    derek "Hey champ! Care for a pair?"
    you "What? "
    derek "Of screaming shades! They're all the rave these days! Tell ya what, I can swing you a first time buyer discount, for the spooky season!"
    menu:
        "Sure, I'm busy at the moment, but I'll be back":
            jump derek_1_1
        "No thanks...":
            jump derek_1_2

label derek_1_1:
    
    scene bg_booth
    show derek distressed at resize
    play sound "audio/Derek1.wav"
    you "Sure, I'm busy at the moment, but I'll be back"
    derek "Oh joy! A prospective customer! Ya won't regret this pal, I promise you that!"

    jump derek_1_mid
    
label derek_1_2:
    
    scene bg_booth
    show derek distressed at resize
    you "No thanks..."
    #takes off sunglasses
    show derek neutral at resize
    play sound "audio/Derek3.wav"
    derek "Oh.. I see."
    "<Sad Trombone>"
    derek "Oh don't mind me, that's just the sound of my heart getting kicked down an elevator shaft. Sinking deeper and deeper into the darkest pits of hell."

    jump derek_1_mid

label derek_1_mid:
    
    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"
    you "Anyway, what's your deal?"
    derek "You mean, you don't know? Why I'm Derek, of course! Sunglass producer extraordinaire! "
    derek "I'm kind of a big deal around here"
    you "Never heard of you."
    derek "W-wha?! Damn..."

    menu:
        "So you sell sunglasses?":
            jump derek_1_3
        "How's business?":
            jump derek_1_4


label derek_1_3:
    
    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"    
    you "So you sell sunglasses?"
    derek "Guilty as charged! No other retailer can guarantee you the Derek seal of approval I'll tell you that!"

    jump derek_1_end

label derek_1_4:
    
    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"    
    
    you "How's business?"
    derek "Absolutely splendid! We sell out our stock every week! The customers can't get enough of them!"
    narrator "You doubt that."
    you "Yeah, well Luxottica might have something to say about that"
    derek "I have no idea what you mean!"

    jump derek_1_end

label derek_1_end:
    
    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"    

    you "Well, carry on, but I have a few questions to ask you when I get back."
    derek "Don't be a stranger! And make sure you tell all your friends that Derek's shades are where it's at!"

    jump mall_booth


label derek_menu_returning:
    scene bg_booth
    show derek neutral at resize
    with dissolve
    show screen button
    play sound "audio/Derek1.wav"    
    
    derek "Why if it isn't my favorite prospective customer! What can I do for you?"
    menu:
        "Ask about the murder of Dorothy":
            jump derek_4
        "Ask about the murder of Sora":
            jump derek_3
        "Ask about the murder of Tom":
            jump derek_2
        "Ask about business":
            jump derek_5
        "Leave":
            jump mall_booth
        "Accuse him of murder" if accusation_mode:
            jump derek_6

label derek_menu:
    
    scene bg_booth
    show derek neutral at resize
    show screen button
    play sound "audio/Derek1.wav"    
    
    menu:
            "Ask about the murder of Dorothy":
                jump derek_4
            "Ask about the murder of Sora":
                jump derek_3
            "Ask about the murder of Tom":
                jump derek_2
            "Ask about business":
                jump derek_5
            "Leave":
                jump mall_booth
            "Accuse him of murder" if accusation_mode:
                jump derek_6
            

label derek_2:

    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"    

    you "What can you tell me about the murder of Tom Chatawa?"
    derek "Oh, it's all so terrible... The coppers booked me last week for questioning. They think I did it! It's ridiculous!"
    derek "Why are you asking about Tom?"
    menu:
        "I heard you and him were close":
            jump derek_2_1
        "I'm investigating these killings.":
            jump derek_2_2

label derek_2_1:

    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"    

    $ mystore.checkListForItem(33)
    $ mystore.checkListLength()

    you "I heard you and him were close"
    derek "Well, close isn't the word I would use..."

    jump derek_2_mid

label derek_2_2:

    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav" 

    $ mystore.checkListForItem(34)
    $ mystore.checkListLength()   

    you "I'm investigating these killings."
    derek "On your own? Or..."
    you "I work with the police."
    derek "Oh, you're a detective? I guess I have no choice but to cooperate then"

    jump derek_2_mid

label derek_2_mid:

    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"    

    derek "His chicken was the talk of the town! \"No one could make fried chicken like ol' Tom Chatawa!\" Sooner or later, that stand became all anyone ever wanted to go to in this place. "
    derek "I'd be lying if I said I was crying over spilled milk. The lad did not deserve what happened to him, "
    derek "But hey, maybe with him outta the way, there might be more visitors willing to buy some of Derek's shades"
    menu:
        "Where were you at the time he was killed?":
            jump derek_2_3
        "Who else was in the mall at the time of the killing? Anyone here you recognize from that night?":
            jump derek_2_4

label derek_2_3:

    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"    

    $ mystore.checkListForItem(35)
    $ mystore.checkListLength()

    you "Where were you at the time he was killed?"
    derek "I already told the other officers this. I was running my stand as usual, you know how it is. Peak mall hours are down by 10, so I was already on my way out when they found him."
    you "Can anyone vouch for that?"
    derek "Well, I'm not exactly keeping track of every face I see can I? But you gotta believe me"

    jump derek_2_end

label derek_2_4:

    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"

    $ mystore.checkListForItem(36)
    $ mystore.checkListLength()

    you "Who else was in the mall at the time of the killing? Anyone here you recognize from that night?"
    derek "Well, I'm not exactly keeping track of every face I see. If I recall correctly, I believe I noticed that one goatwoman near Spirit Halloween shopping around last week. She was here around 7 to 8 and I didn't see her after."
    derek "There was also this weird kid who looked quite empty inside. Probably some elementary schooler. I think I saw him over there right now. I saw him leave the mall right as the sun was going down."
    you "I think that's enough. Thank you, Derek."
    derek "Anything else you want to ask me?"

    jump derek_2_end

label derek_2_end:

    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"    
    
    you "I think that's enough. Thank you, Derek."
    derek "Anything else you want to ask me?"

    jump derek_menu


label derek_3:

    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"    
    
    you "Where were you on the night of October 15th?"
    derek "Oh, that was two weeks ago, I'm not sure if I fully remember..."
    derek "I believe I was out drinking at the local bar."
    menu:
        "Near the town square?":
            jump derek_3_1
        "When was this?":
            jump derek_3_2

label derek_3_1:
    
    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"

    $ mystore.checkListForItem(37)
    $ mystore.checkListLength() 
    
    you "Near the town square? <increase suspicion>"
    derek "Well yeah, the best places are there. The best moonshine in town."
    you "So was the body of a dokkaebi."
    derek "Oh yeah I heard about that."

    jump derek_3_mid

label derek_3_2:
    
    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"

    $ mystore.checkListForItem(38)
    $ mystore.checkListLength()
    
    you "When was this?"
    derek "I think I was up till midnight. I was on a real bender."
    you "Do you remember anything else that might have happened that night?"
    derek "My memory's quite fuzzy. I had a lot of shots."

    jump derek_3_mid

label derek_3_mid:
    
    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"    
    
    you "Was there anyone you remember running into?"
    derek "Well, there were a bunch of high schoolers out too, probably drinking. I mean, what are you gonna do? They're all bound to sooner or later."
    menu:
        "One of them happen to be a werewolf?":
            jump derek_3_3
        "One of them happen to be a swamp monster?":
            jump derek_3_4

label derek_3_3:
    
    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"

    $ mystore.checkListForItem(39)
    $ mystore.checkListLength()    
    
    you "One of them happen to be a werewolf?"
    derek "I think I did see a couple of werewolves. You know, all furry and stuff. Bunch of them throughout the night."

    jump derek_3_end

label derek_3_4:
    
    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"

    $ mystore.checkListForItem(40)
    $ mystore.checkListLength()    
    
    $ saw_daniel_at_bar = True

    you "One of them happen to be a swamp monster? <increase suspicion>"
    derek "I think I did see a swamp monster that night. Probably here for a good time, but  I don't think I saw him take a single drink."

    jump derek_3_end

label derek_3_end:
    
    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"    
    
    you "When did you see them?"
    derek "I'm telling you I don't remember much, but I guess it was around the time I was there, so sometime between the hours of 8-12."
    you "I think that's all. Thank you, Derek."
    derek "Anything else you wanna ask me?"

    jump derek_menu


label derek_4:

    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"    
    
    you "Where were you on the night of October 7th?"
    derek "That was quite a while ago, I'm not sure if I remember."
    derek "Oh yes, I was heading home. I wrapped up, and took the bus back to my apartment."
    you "Can anyone confirm that?"
    derek "I believe I ran into my neighbor Ava on the way back, but she ain't here right now."
    menu:
        "What time was this?":
            jump derek_4_1
        "And what did you do then?":
            jump derek_4_2

label derek_4_1:

    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"

    $ mystore.checkListForItem(41)
    $ mystore.checkListLength()    
    
    you "What time was this?"
    derek "I think it was around 10PM."

    jump derek_4_end

label derek_4_2:

    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"

    $ mystore.checkListForItem(42)
    $ mystore.checkListLength()    
    
    you "And what did you do then?"
    derek "I took a shower and went to sleep. Gotta get my beauty sleep to sell shades!"

    jump derek_4_end

label derek_4_end:

    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"    
    
    you "And where do you live exactly?"
    derek "You know I'm not gonna answer that."
    derek "I live around Armour Hill"
    narrator "This is a ten minute drive from the school where Dorothy was found."
    you "I think that's all. Thank you, Derek."
    derek "Anything else you wanna ask me?"

    jump derek_menu

label derek_5:

    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek3.wav"    
    
    you "Awfully low turnaround today isn't it?"
    derek "Oh well, it's just typical seasonal blues! It's Halloween after all! Customers flock in droves to the Party City this time of year!"
    you "You told me earlier that your business is flourishing, and yet it's a Friday night and your stock seems to be in abundance. you've sold nothing."
    derek "Alright... if you really wish to know, I'm a failure."
    derek "The kiddos these days... they just don't know a good deal when it's staring them in the face."
    derek "*He stares at you for a solid couple of seconds*"
    you "But it was successful?"
    derek "Oh yes, the talk of the town in fact. These shades flew off the shelves... but then the copycats came."
    derek "\"Oh, look at that lad with the cheap stand! Might as well try our hand at it too!\""
    derek "It was fried chicken, watches, those shoe shiners, I mean, who even shines their shoes anymore?! It's crazy that these copies even drew in the numbers they did!"
    menu:
        "Do you know of anyone who would wish harm upon these owners?":
            jump derek_5_1
        "Would you have any reason to wish harm upon these owners?":
            jump derek_5_2

label derek_5_1:

    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"

    $ mystore.checkListForItem(43)
    $ mystore.checkListLength()    
    
    you "Do you know of anyone who would wish harm upon these owners? <increase suspicion>"
    derek "I'm not too sure. I know this one old mothman that hates anyone and everyone, but I don't know if he'd have the capability to kill."

    jump derek_5_end

label derek_5_2:

    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"

    $ mystore.checkListForItem(44)
    $ mystore.checkListLength()    
    
    you "Would you have any reason to wish harm upon these owners?"
    derek "Of course not! I may wish them nothing but the most soul crushing failure, but I would never wish harm upon them!"

    jump derek_5_end

label derek_5_end:

    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"    
    
    you "I think that's enough. Thank you, Derek."
    derek "Anything else you wanna ask me?"

    jump derek_menu

label derek_6:
    scene bg_booth
    show derek neutral at resize
    play sound "audio/Derek1.wav"    
    
    you "I'm arresting you on suspicion of murder. You're coming with me."
    derek "Wait what?!"
    derek "Surely this has gotta be some mistake!"
    you "You can prove that after I take you in."
    narrator "You tackle Derek to the ground and handcuff him before he can escape."
    scene bg_booth with fade
    jump derek_7

label derek_7:
    scene bg black_screen with dissolve

    show text "You escorted Derek back to the police station and questioned him all night."
    with fade
    pause 5
    show text "He is apprehensive and emotional, but answers all the questions truthfully."
    with fade
    pause 5
    show text "The next morning, you find that there has been another murder committed at the mall shortly after you escorted Derek off of the premises." 
    with fade
    pause 5
    show text "The victim was a goatwoman named Shannon."
    with fade
    pause 5
    show text "The killer is still on the loose."

label shannon_1:

    scene bg_storefront
    show shannon neutral at resize
    with dissolve
    play sound "audio/Shannon.wav"
    $ met_shannon = True

    shannon "Oh my dearest me, look at you! Aren't you the most precious thing in the world?"
    shannon "What are you supposed to be, dear?"
    you "Ma'am, I'd like to ask you a few questions if you have the time. I'm investigating a potential serial killer."
    show shannon excited at resize
    shannon "Oh wow! You have a backstory and everything! Now that's commitment to a costume!"
    shannon "You just don't get many people who are willing to really go all in on Halloween anymore. I remember when I was younger, oh! I loved Halloween. "
    shannon "I'd dress up with all my friends and we'd have ourselves a proper little party. I always loved the pumpkin pie, I still have it every year with my husband and my son, David and David Jr."
    shannon "Do you know them? David is a little bit of a celebrity around these parts on account of the success of his knife selling business."
    you "No, I don't believe I've had the pleasure of making his acquaintance. "
    you "Wait, I mean this isn't a costume. I'm a real homicide detective ma'am and I really do need to ask you some questions..."
    shannon "Of course, I'd love to answer any questions that you have... detective. *winks*"
    you "Alright... sorry, my head is all scrambled now. I'll be back with some questions for you Mrs..."
    shannon "Shannon Boer. But you can just call me Shannon, detective."
    you "Right, ok I'll be back."

    jump mall_storefront

label shannon_menu:

    scene bg_storefront
    show shannon neutral at resize
    play sound "audio/Shannon.wav"
    show screen button
    shannon "Detective! You're back! I was wondering if I'd see you again tonight. Gotten any leads yet?"
    you "I'm working on it. I've got some questions for you if you don't mind."
    shannon "Not at all! Fire away!"

    menu:
        "Ask about the murder of Dorothy":
            jump shannon_2
        "Ask about the murder of Sora":
            jump shannon_3
        "Ask about the murder of Tom":
            jump shannon_4
        "Leave":
            jump mall_storefront
        "Accuse her of murder" if accusation_mode:
            jump shannon_5

label shannon_2:

    scene bg_storefront
    show shannon neutral at resize
    play sound "audio/Shannon.wav"

    $ mystore.checkListForItem(45)
    $ mystore.checkListLength()

    you "Where were you the night of October 7th?"
    shannon "Oh dear. That was a horrible night..."
    shannon "You've really done your research, haven't you, dear? Alright well I suppose I'll tell you."
    shannon "That was the night of the parent teacher conference. David was tired from work, so I took Junior to the conference."
    shannon "He's been struggling a bit in school, they say he has trouble reading words. He's just like his dad, he is."
    shannon "I know that if he tries hard enough he'll get it eventually. You know some people just don't have enough patience. "
    shannon "Well anyways, so after the conference I got to talking with all the other moms, and one of them was Dorothy."
    shannon "We weren't too close, but we got to talking about her daughter, Veronica. She's quite a talented young woman I've been told. She won the talent show the week prior to... ah well."
    shannon "We got so caught up in talking, that it wasn't until sometime around I think 9PM that she and I went home."
    shannon "At that point everyone else was gone, so it was just me, Dorothy, Junior, and the stars in the sky."
    shannon "That's the last time I saw her. Swear on my heart."
    you "Do you remember who was there at the conference?"
    shannon "Oh, well I'd assume all of the students and hopefully all of their families as well!"
    shannon "I remember seeing that little one, Stephen I believe his name is."
    shannon "I worry about him. It can't be easy being so small and being in high school. I do hope he isn't being bullied."
    you "And you're sure everyone else had left?"
    shannon "Oh, I can't be too sure. You know sometimes I get so caught up in talking that I lose track of time and what's going on around me. I'm sure you understand."
    you "Yes...this has been very informative, Mrs. Boer."
    shannon "Please, call me Shannon. "
    shannon "Do you have any other questions for me?"
    you "Let me collect my thoughts and I'll let you know in a bit."
    show shannon excited at resize
    shannon "Alright detective! Make sure you get lots of candy!"

    jump mall_storefront

label shannon_3:

    scene bg_storefront
    show shannon neutral at resize
    play sound "audio/Shannon.wav"

    $ mystore.checkListForItem(46)
    $ mystore.checkListLength()

    you "Do you remember what you were doing on October 15th?"
    shannon "Oh, now give me a second to think, detective. That was quite some time ago..."
    shannon "That was a weekday so I had to take Junior to school... David left bright and early as he always does...I had to take the trash out...I had to pick Junior up from school..."
    you "Did you go anywhere else besides school and your home?"
    shannon "I can't quite seem to remember, detective."
    you "Maybe you happened to go near the town square?"
    shannon "The town square... oh I see detective! Yes, yes of course the town square. I was there."
    you "You were? When?"
    shannon "Oh let's say about 11AM around lunch time. You know there's a great little cafe there called The Warbler. It's to die for! "
    shannon "I'm sure you're not too interested in that though... let's see. Maybe I saw a shadowy figure, roaming through the square."
    you "...did you?"
    shannon "Yes! Shifty eyes, looking for their next victim. Oh! And I followed them. No one would suspect someone like little old me!"
    shannon "And then I saw it! I saw it happen! They stole a purse and ran off. I ran after them screaming and hollering, \"Help! Help! Thief!\""
    shannon "But of course it was up to me to get them! I cornered them into an alleyway and said, \"Stop! I'm making a citizen's arrest. Return what you stole, thief!\""
    shannon "Of course they didn't listen. So I killed them. Oop! "
    you "You... killed them? What did they look like?"
    shannon "Detective! You should be listening! Shifty eyes, like a shadow. Sharp teeth, angry. Oh really angry. And very thief-like!"
    you "Right... Then what happened? After you... killed them?"
    shannon "Oh right! It can't end there. Well, I used my magical goat powers to clean them up. There are mystics in my blood you know! On my mother's side."
    shannon "All the blood and gore and gross things cleaned right up!"
    shannon "Then afterwards I picked up Junior and went straight home. I had to make dinner after all."
    you "And did you leave your house for anything else afterwards?"
    shannon "Oh do you need more, detective?"
    you "No, I mean I don't need anything. I want the truth."
    show shannon excited at resize
    shannon "Oh the truth! Well you should've said so!"
    shannon "Well then the truth is we had a perfectly pleasant night, Junior got tucked into bed and David and I had our nightly little whiskey chat."
    you "So to confirm, you didn't go out at all after you returned home?"
    shannon "Not after 4PM. "
    you "Alright, I think that'll be enough for now."
    you "I'll come back if I think of anything else."
    shannon "Alright detective! Good luck!"

    jump mall_storefront

label shannon_4:

    scene bg_storefront
    show shannon neutral at resize
    play sound "audio/Shannon.wav"

    $ mystore.checkListForItem(47)
    $ mystore.checkListLength()

    you "Last Thursday night on October 23rd a man named Tom Chatawa was murdered in the parking lot of this mall. Do you remember what you were doing that day?"
    shannon "Oh Tom. He was a wonderful man. Come, come detective. Let us have a moment of silence for him."
    you "Alright ma'am ..."
    shannon "..."
    shannon "Tom Chatawa we will remember you as a pillar of this community. The work you did brought joy to many families. "
    shannon "We will remember your kindness, your diligence, and the incredible taste of your chicken. "
    shannon "May you rest in peace with the Lord above."
    shannon "Amen."
    you "Amen..."
    shannon "Now that we have properly paid Tom his respects, I can say I saw him that day."
    you "What happened?"
    shannon "Well isn't that just the thing detective? Nothing really strange happened! "
    shannon "I remember that day Junior was feeling sick, so we let him stay home from school. Some sort of cold, he's doing well now."
    shannon "The whole week he had been begging me to go to Tom's to get some chicken. You know how boys are with meats. "
    shannon "I always say that both my Davids are like bottomless pits, they eat so much!"
    you "So you went to get chicken from the mall. Was this in the morning?"
    shannon "Well not early in the morning, maybe sometime around 11;30AM?"
    shannon "Then after that I went home to take care of Junior."
    shannon "And before you ask, detective. No, I didn't go anywhere else afterwards. Everyone knows I take care of my boy."
    you "Do you happen to remember anyone else there, or maybe anything that seemed out of place?"
    shannon "Well. I suppose it was busier than usual. I remember I was in line for much longer than usual. Of all the salesmen in the mall, Tom has been the one breakaway success. "
    shannon "There was Derek as well, but that was years ago. You know, I wouldn't be surprised if he had something to do with this! Something about jealousy or something what do you think, detective?"
    shannon "Isn't it strange that for both Dorothy and Tom something good happened to them before they were killed?"
    you "That is strange..."
    show shannon excited at resize
    shannon "I know right! I'm pretty good at this detective stuff. Maybe that'll be my costume next year!"
    you "You've given me a lot to think about, thank you Shannon."
    you "I'll be back if I have any more questions for you."
    shannon "Good luck detective!"

    jump mall_storefront

label shannon_5:
    scene bg_storefront
    show shannon neutral at resize
    play sound "audio/Shannon.wav"
    you "I'm arresting you on suspicion of murder. You're coming with me."
    shannon "Oh dear! Are you being serious right now?"
    you "I'm afraid so, Shannon. Please cooperate."
    narrator "Shannon solemnly holds her wrists out. You tackle her to the ground and handcuff her before taking her to the station."
    scene bg_storefront with fade
    jump shannon_6


label shannon_6:

    scene bg black_screen with dissolve

    show text "You escorted Shannon back to the police station and questioned her all night."
    with fade
    pause 5
    show text "At first she's still in disbelief, but soon she recovers to her chatty self."
    with fade
    pause 5
    show text "You learn a lot about her life and her suspicions, but nothing that would indicate she committed these murders."
    with fade
    pause 5
    show text "The next morning, you find that there has been another murder committed at the mall shortly after you escorted Shannon off of the premises." 
    with fade
    pause 5
    show text "The victim was a moonman named Derek."
    with fade
    pause 5
    show text "The killer is still on the loose."

transform one_fifth:
    zoom 0.2

screen button():
    zorder 100
    frame:
        align (0.02,0.02)
        background None
        imagebutton:
            idle "images/notepad.png" #Change image for button icon
            hover "images/notepad_highlight.png" #Change image for button icon
            at one_fifth
            action ToggleScreen("notepad")
    
screen notepad:
    tag notepad
    zorder 50
    frame:
        align (0.5,0.5)
        background "#0008"
        padding (200,200)
        vbox:
            spacing 20
            text "Previous Murders"
            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                has vbox:
                    spacing 30
                    frame:
                        background None
                        has vbox
                        text "1. Tuesday, October 7th 2003."
                        text "Dorothy Williams, the mother of Veronica Williams, a popular cheerleader at school, was found drowned next to the school's pool. Bruising around the wrists and a fractured rib cage. Estimated time of death 3:22 AM. There was a PTA meeting that night that ended at 7:30PM. The last person to see her was another mom named Shannon, who claims that she bid Dorothy goodbye in the parking lot after a conversation at around 9PM. The police received a call from the father, Tim, at 11:32PM. The body was found at the school shortly after. The last person at the school was the janitor who insisted he closed up and locked the swimming pool door at 10:00PM sharp as that is when he clocks out. The door to the swimming pool was found unlocked. Keys are given to several faculty members, the janitor, and several students involved in extracurriculars."
                    frame:
                        background None
                        has vbox
                        text "2. Wednesday, October 15th 2003."
                        text "Sora Kim, a retired dokkaebi pansori drummer, was found hanging by a noose from a lamppost in the town square. A painting was made using the shadow of Sora's hanging body cast by the streetlight. His body was found at 1:27AM the next day with an estimated time of death at 11:43PM. Despite the paint, police initially ruled it as a suicide, though scratch marks around the neck and additional bruises indicated a struggle, and the cause of death was revealed to be blunt force trauma to the skull. The investigation remains ongoing with the possibility of it being ruled as a hate crime on the table."
                    frame:
                        background None
                        has vbox
                        text "3. Thursday, October 23rd, 2003."
                        text "The body of Tom Chatawa, a local fried chicken stand owner, was found in the parking lot of the town mall. The victim was badly burnt and had lacerations across the torso. Local law enforcement questioned Derek, who asserts that he last saw Tom alive operating his chicken stand at 7:30PM before leaving for a smoke break and never returning. The body was eventually found at 10:26PM, suggesting the murder took place between 8-10PM. He was released as they were unable to find reasonable doubt in his story."

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

screen countdown:
    on "show" action Function(lambda: setattr(store, "accusation_mode", True))
    on "show" action Play("music", "/audio/Suspense Theme.mp3", loop=True, fadein=3)
    timer 0.01 repeat True action If(time>0, true=SetVariable('time', time-0.01),false=[Hide('countdown'), Jump('daniel_8')])
    bar value time range 600 xalign 0.9 yalign 0.1 xmaximum 300 at alpha_dissolve
