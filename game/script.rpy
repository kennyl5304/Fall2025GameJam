# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define unknown = Character("???")
define narrator = Character("Narrator")
define you = Character("you")
define stephen = Character("stephen")
define madison = Character("Madison")
define george = Character("George")
define daniel = Character("Daniel")
define derek = Character("Derek")
define shannon = Character("Shannon")




# The game starts here.

label start:

    #need to figure out how to do the title crawl

    scene bg black_screen

    narrator "It is Halloween night. The year is 2003."

    narrator "you are a detective sent to investigate a series of killings that has plagued the small town."

    narrator "After deducing the pattern of victims, you have concluded that the killer is set to strike again tonight at the town mall." 

    narrator "you must now discover the identity of the killer before someone else meets an early grave."

        menu:
            "Enter Mall":
                jump mall_beginning

label mall_beginning:

    scene bg mall_storefront

    narrator "The mall is crowded tonight, with the scent of cheap candy flavoring the air. Pop radio trash on the airwaves, flooded out by the laughter and chatter of a crowd feeling the Halloween spirit."

    narrator "The numbers are high tonight. Anyone can be a suspect."

        menu:
            "Time to investigate":
                jump mall_storefront

label mall_storefront:
    
    scene bg_storefront

label mall_fountain:

    scene bg_fountain

label mall_booth:

    scene bg_booth

label stephen_1:

    scene bg_fountain

    you "Hey kid, you're not in trouble. I just want to talk to you."
    stephen "Hello officer. How are you today, sir?"
    you "Oh, uh. I'm doing well. I just wanted to ask you a few questions."
    stephen "Of course. That is the nature of your job, and I hardly think you would bother speaking to a child like me if you didn't have questions of some sort."
    you "you are very well-spoken for your age. "
    stephen "Thank you, sir."
    you "Are you here with your parents?"
    stephen "Oh no, sir. Just me tonight."
    you "Just you? That can be dangerous. Make sure you're sticking with people you know alright? I'll be back with more questions."
    stephen "Will do, officer."

label stephen_2:

label stephen_3:

label stephen_4:

label stephen_5:

label stephen_6:



label example: 

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "you've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

#stephen Scene 1
you: "Hey kid, you're not in trouble. I just want to talk to you."
stephen: "Hello officer. How are you today, sir?"
you: "Oh, uh. I'm doing well. I just wanted to ask you a few questions."
stephen: "Of course. That is the nature of your job, and I hardly think you would bother speaking to a child like me if you didn't have questions of some sort."
you: "you are very well-spoken for your age. "
stephen: "Thank you, sir."
you: "Are you here with your parents?"
stephen: "Oh no, sir. Just me tonight."
you: "Just you? That can be dangerous. Make sure you're sticking with people you know alright? I'll be back with more questions."
stephen: "Will do, officer."

#stephen Scene 2
stephen: "Hello again officer. How is your investigation going, sir?"
you: "It could be better. I have some more questions to ask you."
stephen: "I'll help however I can, sir."
    Choice: "<ask about the murder of Dorothy> Where were you the night of October 7th?"
stephen: "That was the night of the parent-teacher conference. I attended with my caregivers and left promptly at 8:00PM alongside the rest of the students."
you: "Do you remember anyone else who was there that night?"
stephen: "
I was with the rest of the team, the football team that is. I play quarterback for the school. "
stephen: "
We were running shotgun roll out drills, but my team was struggling to get the snap to me. Of the 38 times we ran that drill, I was not able to receive the snap 11 times. After receiving the snap, things went smoothly and of the remaining 27 passes, 26 were successfully completed. I attribute the single failure to my awkward grip on that specific ball. One could argue that was partially a result of the snap as well. "
you: "So your team was there?"
stephen: "I can personally attest that all of them were present at that conference. The cheerleaders were also all in attendance, including Daniel and poor Veronica, although I remember her being quite giddy that night."
stephen: "As the conference ended and we students began our scattered journeys home, I remember the cheerleaders dispersing and out emerged an obviously distressed Madison."
stephen: "She fled, tears streaking down her face and went home."
you: "What time would you say this was?"
stephen: "Oh about 8:00PM. Same as the rest of the student body."
you: "Thank you for being so helpful, I think that'll be it for now."
stephen: "Of course."

#stephen Scene 3
stephen: "Hello again officer. How is your investigation going, sir?"
you: "It could be better. I have some more questions to ask you."
stephen: "I'll help however I can, sir."
    Choice: "<ask about the murder of Sora> Where were you on October 15th?"
stephen: "…"
you: "stephen?"
stephen: "Quiet officer. I'm trying to remember. What day of the week was October 15th?"
you: "That was a Wednesday."
stephen: "On Wednesdays I have football practice after school. After practice I always get picked up by my parents."
    Choice1: "When do you get picked up?"
stephen: "My parents know to always get me exactly at 5:30PM every Monday, Wednesday, and Friday. Holidays excepted of course"
    Choice2: "Did you do anything else that night?"
stephen: "Nothing that I don't normally do, officer. I ate dinner, did my homework, and was in bed by bedtime."
you: "And what time would that be?"
stephen: "9:00PM"
you: "I see. I'll come back if I have any more questions. Take care of yourself."
stephen: "Of course, officer."

#stephen Scene 4
stephen: "Hello again officer. How is your investigation going, sir?"
you: "It could be better. I have some more questions to ask you."
stephen: "I'll help however I can, sir."
    Choice: "<Ask about the murder of Tom> What were you doing last Thursday?"
stephen: "I was eating ice cream, officer. Mint chocolate chip. Here in the mall with my parents."
you: "What time was this?"
stephen: "Right after school. I remember it being an oddly warm day for October, so my father, ever the fiend for sugary treats, suggested it. He cited my age as an excuse which I resent somewhat, but I cannot deny. Ice cream is good."
you: "What did you do after that?"
stephen: "After finishing our confections I informed my parents of the homework I had yet to do, so we returned home hastily. I cannot state a specific time, in fear of being incorrect, but I can give a relative time."
stephen: "When we went home the sun was still shining."
you: "Thank you stephen, that should be all for now. I'll return if I have any more questions."
stephen: "Of course."

#stephen Scene 5
stephen: "Hello again officer. How is your investigation going, sir?"
Choice: "<Accuse him of murder> I'm arresting you on suspicion of murder. you're coming with me."
stephen: "Officer, surely there must be some sort of mistake?"
narrator: "you tackle stephen to the ground and handcuff him before he can escape."
Crawl: "you escorted stephen back to the police station. While cooperative before, at the station he refused to speak without his parents present."
"Once they arrive, he recites the same exact information he told you without flaw."
"The next morning, you find that there has been another murder committed at the mall shortly after you escorted stephen off of the premises."
"The victim was a moonman named Derek."
"The killer is still on the loose."

#Madison Scene 1
you: "Excuse me, may I have a word?"
Madison: "Oh? Oh, yes, what is it?"
you: "Someone's awfully quiet this Halloween night."
Madison: "Yeah, well… it's loud enough already don't you think?"
    Choice1: "Yeah, that's fair"
    Madison: "Besides, I don't think anyone really wants me talking"
    
    Choice2: "Could be worse"
    Madison: "Well, I don't think there's anywhere louder than this place on Halloween night."
you: "you come here alone?"
Madison: "Yeah… I've never really been good with others."
you: "It's quite dangerous lately, with all these killings and all. Hope you're keeping yourself safe"
Madison: "Yeah, I heard about them. Quite a frightening thought "
you: "I'll get back to you if I have any more questions"
Madison: "Oh, sure"

#Madison Scene 2
Madison: "Oh, hi… good to see you again"
Choice: "<ask about the murder of Tom> Where were you on the night of October 23rd?"
Madison: "I was in the mall, just like tonight…"
you: "What were you doing here?"
Madison: "I was looking to buy some new headphones… someone busted my old ones and I needed some new ones for my iPod"
you: "When did you leave?"
Madison: "Around 9:30? "
    Choice1: "What do you listen to?"
    Madison: "Oh, it's a small band called My Chemical Romance"
    Madison: "They just released their first album, I've been listening to it nonstop"
    Madison: "The other kids think it's lame, but I just think they're neat"
    
    Choice2: "Any other stores you visited?"
    Madison: "I just checked out the classics section and Barnes and Noble"
    Madison: "I was really just browsing. I kinda left after eating dinner"
    you: "Have you noticed anything about the booths that night?"
    Madison: "Well, the fried chicken stand was unoccupied when I got there… I suppose that was when… you know."
    Madison: "I was gonna get some chicken for dinner that night, but it was empty, so I just got a sandwich at Sandy's."
    you: "Did you encounter anyone else there?"
    Madison: "Well, that weird moon guy also tried selling me some tacky glasses while I was on the way out. He was packing up his stand, but I guess he just wanted to squeeze one more customer."
you: "I'll get back to you if I have any more questions"
Madison: "Oh, sure"

#Madison Scene 3
Madison: "Oh, hi… good to see you again"
Choice: "<ask about the murder of Sora> Where were you on the night of October 15th?"
Madison: "I was at a friend's house. We have this literature club we do every Wednesday. We just read and listen to music. "
you: "Were you at the town square at any point that day?"
Madison: "I was there in the afternoon. That's where we all meet up beforehand."
you: "What timeframe were you there?"
Madison: "I'd say about three to five?"
    Choice1: "Did you see anything suspicious while there? <increase suspicion>"
    Madison: "Not really. I saw the moon sales guy heading into the bar before I left, but that's all really. Never thought I'd see him outside of the mall."
    Choice2: "Is there anyone who can verify your presence?"
    Madison: "you can go talk to some of my friends. I think I saw them leave a while ago though."
you: "Okay, I think that's it for now"
you: "I'll get back to you if I have any more questions"
Madison: "Oh, sure"

#Madison Scene 4
Madison: "Oh, hi… good to see you again"
Choice: "<ask about the murder of Dorothy> What can you tell me about the murder of Dorothy Williams?"
Madison: "Oh right, Veronica's mother… It's quite awful what happened to her."
you: "What was your relationship with Veronica Williams?"
Madison: "Well, she was always picking on me since we were in elementary school. She kept calling me \"half-developed\". It was horrible."
Choice1: "Do you think she knows how it feels now?"
Madison: "Well, she was always horrible to everyone, thought she was better than us just because she's pretty. Maybe now, she'll be a bit more sympathetic to everyone."
Choice2: "I'm sorry about that"
Madison: "Yeah. Can't imagine what she's going through now, losing her mother like that."
you: "Where were you that night?"
Madison: "Oh, I skipped the parent teacher conference. My grades are pretty good, so there wasn't really a need for me to be there, you know?"
Madison: "I was at home all night checking my picture comments on MySpace."
    #CONDITIONAL HERE!
    Choice <if you talked to stephen>: "That's a lie. I've got a testimony saying you were seen at the conference that night."
    Madison: "What? Who told- Alright, I lied!"
    Madison: "Veronica and her friends were being horrible to me that night. The night it happened…"
    Madison: "She won the talent show the week before. Everyone was raving about it. She was rubbing it in my face again, about how I'd never make the team… because I wasn't fully \"developed\"..."
    Madison: "How would it look? If I had told you what really happened?"
    you: "I'd say that gives you a prime motive."
    Madison: "But I did not kill her mother! I swear!"
    you: "That remains to be seen…"
    
    Choice2: "Seems reasonable. Normal teenager stuff. I'll never understand it."
    Madison: "Best if you don't."
    Madison: "Is there… anything else?"
Choice1: "Tell me more about Dorothy"
Madison: "Well, Veronica always said she was following her mother's footsteps, so I always saw her as an old cheerleader. She was quite the big name in our school. "
Madison: "I heard people say that no one could work up a crowd like her."
Choice2: "Who would wish Dorothy any harm? <increase suspicion>"
Madison: "I'm not quite sure… Veronica was pretty popular, so I guess she'd have a lot of people who have it out for her"
Madison: "But I don't know if there would be anyone who's got something against her mom."
you: "I believe that's all"
you: "I'll get back to you if I have any more questions"
Madison: "Oh, sure"

#Madison Scene 5
Madison: "Oh, hi… good to see you again"
Choice <Ask about interests>: "So you're really into literature huh."
Madison: "Yeah..."
you: "Might I ask why?"
Madison: "Well, it helps me to feel like I can just get away from this crazy world for a bit y'know?"
you: "I get the feeling"
Madison: "Between you and me, I've been getting into writing lately. It's not enough for me to immerse myself anymore. I wanna create new stories too"
you: "What do you write about?"
Madison: "It's just a bunch of teen dramas, that's all. I've been working on one about this character who finally gets back at her bullies"
you: "Sounds very Carrie."
Madison: "Yeah, it's cliche, I know. I was working on it… until, y'know… all that stuff with Veronica…"
you: "you know that is very concerning behavior right?"
Madison: "Yeah, I know… but everything I've had to deal with my whole life…"
Madison: "Please don't tell anyone…"
you: "I won't make any promises"
you: "I'll get back to you if I have any more questions"
Madison: "Oh, sure"

#Madison Scene 6
Madison: "Oh, hi… good to see you again"
Choice: "<Accuse her of murder> I'm arresting you on suspicion of murder. you're coming with me."
Madison: "Wait, what? This must be some kind of mistake!"
Madison: "Please, I trusted you! I didn't do anything wrong I swear!"
you: "you can defend yourself all you want at the station"
narrator: "you tackle Madison to the ground and handcuff her before she can escape."
<fade to black>
Crawl: "you escorted Madison back to the police station and questioned her all night. She is scared and despite an anxiety attack, answers all the questions truthfully."
"The next morning, you find that there has been another murder committed at the mall shortly after you escorted Madison out of the premises."
"The victim was a moonman named Derek."
"The killer is still on the loose."

#George Scene 1
George: "you! Hey you!"
you: "Pardon?"
George: "you don't happen to be a dokkaebi, right?"
    Choice1: "Maybe I am"
    George: "you better watch yourself then. We don't want your kind here, and last I heard, y'all have been droppin' like flies."

    Choice2: "No."
    George: "Good! This town don't need more o' those roaming around. We've been diluted enough as it is. "
    you: "you got something against dokkaebis?"
    George: "Hell yeah I do! I ain't fought a war just to have the bastards I defended my country against livin here like it's nothin'."
    you: "One of them was killed a few weeks ago."
    George: "you know, I say the better for it!"
    you: "you don't have many friends do you."
    George: "Who needs any?"
    you: "That answers my question."
you: "I'll be back with some more questions for you."
George: "Heh??"

#George Scene 2
George: "Ehh?"
Choice: "<Ask about murder of Tom> Where were you on the night of October 23th?"
George: "Well I was at the mall, like I am right now. Shopping for some o' that new technology all the youngsters are ravin' about."
you: "What might that be?"
George: "A microwave."
you: "Uhm okay… when was this?"
George: "Around the evening. That damn moon man was shouting his ass off again. Waxin' poetic about his shay-dees. It's a miracle he even gets people to buy that crap."
    Choice1: "Anything else suspicious that you've seen? <increase suspicion>"
    George: "Tell you what I've seen. That damn Honey Islander's been acting real fishy lately. I know his kind when I see it. "
    George: "They're all a bunch of good for nothin' weirdos. Nothing's felt right since they started showing up in droves. I know I saw him running around trespassing in the employees room last week."
    
    Choice2: "Anyone else you've seen in the mall around that time?"
    George: "I saw a werewolf hanging around during the early evening. Looked real gnarly, like she wasn't fully a wolf yet."
    George: "Now I don't know what's up with her, but werewolves, those are real Americans right there. Not like any of the riffraff that claim they're one of us.  "
    you: "I'll keep this in mind."
    Choice1: "How long were you there?"
    George: "I don't know, like half past eight?"
    
    Choice2: "What did you do after?"
    George: "I went home, and tried to see if I could get the damn thing to work. Everything's so complicated these days, why can't we go back to the old ways of using the fireplace?"
George: "Heh??"

#George Scene 3
George: "Ehh?"
Choice: "<Ask about murder of Sora> What can you tell me about the murder of Sora Kim?"
George: "Ehh! The dokkaebi?! That damn trash gnome had it coming!"
you: "Is that an admission of guilt? Or…"
George (noticeably more nervous): "Now now now, I never said that-"
you: "Where were you on the night of the murder?"
George: "I was watching TV at home, classic cinema."
you: "What were you watching?"
George: "Birth of a Nation."
you: "…"
you: "Okay… when was this?"
George: "Around 8?"
    Choice1: "What were you doing at 11PM? <increase suspicion>"
    George: "Well I was sleeping! What are you, expectin' an ol' codger like me to be awake at the witching hour?!"
    you: "That's not the witching hour, but noted."
    
    Choice2: "Why were you watching that?"
    George: "Calms my nerves a bit"
you: "Do you know of anyone who would wish this man harm?"
George: "I tell ya, that's a lotta people"
George <if you tell him you're a dokkaebi>: "A lot of us wish your kind harm."
George <if you tell him you're not a dokkaebi>: "Between you and me, I'd say this town has it out for them. I just know it."
George: "I'm just the only one brave enough to speak my mind and say it as it is."
you: "I'll keep this in mind."
George: "Heh??"

#George Scene 4
George: "Ehh?"
Choice: "<Ask about murder of Dorothy> Where were you on the night of October 7th?"
George: "Eh that was a lifetime ago. I was at the school."
    Choice1: "What were you doing there?"
    George: "There was a parent-teacher conference. My niece was sick, so I went on behalf of her daughter."
    
    Choice2: "you realize that was the site of a gruesome murder?"
    George: "Ehhh? First I ever heard of it. When was that?"
    you: "October 7th."
you: "How long were you in the building for?"
George: "Roughly 6-9?"
George: "Those damn gorgons held me up. Wouldn't shut up about sculpturing. Felt like I was stone for three hours."
George: "What has this country come to? Having gorgons educate our children?!"
you: "What did you do after? Say, an hour after that?"
George: "I took my niece's daughter home. We live a neighborhood away."
you: "Who else was in the school at the time that's here tonight?"
George: "All the children here of course. High schoolers and elementary alike. I also saw that goat woman over there among the fray. At least this place has some real Americans."
    Choice1: "When did they leave?"
    George: "I think that goatwoman left around 9PM?"
    
    Choice2: "Would any of them have a reason to harm the victim? <increase suspicion>"
    George: "How should I know?! I tell you what, it's probably some damn foreigner tryna rid this country of its rightful population!"
you: "I'll keep this in mind."
George: "Heh??"

#George Scene 5
George: "Ehh?"
Choice: "<Ask about background> you said you fought in the war?"
George: "What else do you need to know? Served my country well in the war. Drafted back in '51. Honorable discharge. "
George: "Killed a whole lotta dokkaebis, and seen some of my best friends die at their hand."
you: "What about after?"
George: "Went back to crop dustin'. It's all I was ever good at."
you: "you're a crop duster?"
George: "All my life. Then I took a tumble back in '76. Doctors said I could never do it again. The hell do they know?!"
George: "Pair that with that new invention the youngsters made, and I was out of a job"
you: "What invention was that?"
George: "The aeroplane."
George: "Damn youngins these days can't tell the good end of a hoe even if it smacked 'em in the ass."
George: "What they all need is a good few years o' hard old fashioned labor"
George <if you tell him you're a dokkaebi>: "Heh, you really know how to keep an old soul good company. "
George <if you tell him you're a dokkaebi>: "you must be one o' the good ones."

#George Scene 6
George: "Ehh?"
Choice: "<Accuse him of murder> I'm arresting you on suspicion of murder. you're coming with me."
George: "What the hell?!"
George: "I knew it! There was something fishy about you from the start! your kind's made this country hell to live on, you hear me?!"
George: "Hard working men like me have to suffer because of freaks like you!"
you: "Save the insults for the interrogation, gramps."
narrator: "you tackle George to the ground and handcuff him before he can escape."
<fade to black>
"Crawl: you escorted George back to the police station and questioned him all night. "
"He is agitated and hostile, but begrudgingly answers all the questions truthfully."
"The next morning, you find that there has been another murder committed at the mall shortly after you escorted George out of the premises."
"The victim was a moonman named Derek."
"The killer is still on the loose."

#Daniel Scene 1
you: "Hello, I'd like to ask you a few questions."
Daniel: "…"
you: "Excuse me? Behind the pillar? "
Daniel: "…"
you: "Just a few questions, you're not in trouble."
Daniel: "hello…"
you: "Hi, what's your name?"
Daniel: "…"
you: "I'm with the local police department, it's alright."
Daniel: "daniel…"
you: "Daniel! That's a great name. Like Daniel Radcliffe. you know, like Harry Potter?"
Daniel: "(jumps out from behind the pillar startlingly quickly) Daniel Radcliffe? I love Daniel Radcliffe! I love how he isn't afraid to do what no one else will do for the sake of a great show! "
Daniel: "If you ask me, that's a great performer. Someone who will put it all on the line, dignity and prestige and fame and wealth, everything. For the sake of the performance."
Daniel: "But not just the performance! Oh no. Just for performance… that would be so… gaudy. Horrible. No, no. Radcliffe. He's different. He, he, he just. He pokes at your brain and asks you, \"Do you believe me? I am the world's strangest person, the world's strangest THING. BELIEVE ME.\""
you: "Yeah, he's a… you know what you said. A great performer. Anyways, I'd love to ask you a few questions, Daniel. Just a few it won't tak-"
Daniel: "(slinks back behind the pillar) …"
you: "Okay… I'll come back to ask you a few questions later, alright Daniel?"
Daniel: "…"

#Daniel Scene 2
you: "Hey Daniel. I'd like to ask you a few questions if that's alright."
Daniel: "…ok"
Choice: "<Ask him about performance> It seems like you really like Daniel Radcliffe. Are you a performer too?"
Daniel: "(jumps out from behind the pillar) I LOVE PERFORMING. It's art, it's gorgeous, it's beautiful. There isn't anything like it. "
    Choice1: "That's really cool! Are you a dancer?"
    Daniel: "No, no. Dancers don't get enough performances. I need more. "
    Daniel: "I'm a cheerleader. We get to perform at every game, and after school every day we practice outdoors. "
    Daniel: "Rain or shine. Everyone will see us, see me."
    
    Choice2: "That's really cool! Are you an actor in your school's theater program?"
    Daniel: "Acting? In my school's theater program?"
    you: "Yeah, like Cats? Phantom of the Opera?"
    Daniel: "Those children don't even know the first thing about putting on a show. To call them actors is to spit in the face of all performers."
    Daniel: "All of them. All that rehearsal to put on a SINGLE shoddy performance, to then receive an undeserving, paltry applause."
    you: "That's quite harsh."
    Daniel: "And yet true. I could never be part of that circus. No. I'm a cheerleader."
    Daniel: "Rain or shine, snow or sleet, we are there outdoors every day after school without fail. "
    Daniel: "That's performance. That's dedication. Everyday, we are admired. "
you: "Alright… I'll come back if I have more questions for you."
Daniel: "(goes back to hiding behind the pillar)...okay"

#Daniel Scene 3
you: "Hey Daniel. I'd like to ask you a few questions if that's alright."
Daniel: "…ok"
Choice: "<Ask about the murder of Dorothy> Do you remember where you were the night of October 7th?"
Daniel: "…school. parent-teacher conference…"
you: "And how long were you there for?"
Daniel: "8. "
Daniel: "…everyone left at 8."
you: "Do you remember anyone else being there?"
Daniel: "football players… cheerleaders…"
Daniel: "and madison."

    Choice1 <Ask if anyone else stayed past 8>: "Did you see if any of them stayed past 8?"
    Daniel: "…no… everyone left at the same time."

    Choice2 <Ask about Madison>: "Who's Madison?"
    Daniel: "…"
    Daniel: "student… werewolf."
    you: "Did something happen with her?"
    Daniel: "… the cheerleaders talked with her. I wasn't part of that."
    you: "Talked with her how?"
    Daniel: "bad. she cried and ran away…"
    you: "Did they hurt her?"
    Daniel: "…no. it's normal…"
you: "I see. Well thanks for speaking with me, Daniel."
you: "I'll return if I have more questions."
Daniel: "…okay."

#Daniel Scene 4
you: "Hey Daniel. I'd like to ask you a few questions if that's alright."
Daniel: "…ok"
Choice: "<Ask about the murder of Sora> Where were you on October 15th?"
Daniel: "<pops out from behind the pillar> I was home of course. Practicing my cheer routines"
you: "Were you at school? October 14th was a Wednesday."
Daniel: "Well, yes obviously. Cheer practice is after school."
Daniel: "After cheer I was furious because I couldn't get this move down. "
Daniel: "I just can't STAND it when that happens. So I went home to keep practicing."
    Choice1: "<If Derek stated that he saw Daniel at the town square> I have someone who claims they saw you at the town square that day. Care to explain?"
    Daniel: "(jumps back behind the pillar) …"
    Daniel: "I forgot…"
    Daniel: "I walk through the town square to get home…"
    Daniel: "…"

    Choice2: "Were you able to get that move down?"
    Daniel: "Oh yes! The process was quite… inelegant. But the result was well worth it. Beautiful."
    you: "I'm glad it went well!"
you: "Well that's all I have for now. I'll talk to you again if I have any more questions."
Daniel: "…okay."

#Daniel Scene 5
you: "Hey Daniel. I'd like to ask you a few questions if that's alright."
Daniel: "…ok"
Choice: "<Ask about the murder of Tom> Where were you on the night of October 23rd?"
Daniel: "at the mall."
you: "Are you aware there was a murder that night?"
Daniel: "…no. who?"
you: "Tom Chatawa. The fried chicken vendor down by Wetzel's Pretzals. Do you remember seeing him there that day?"
Daniel: "…yes."
you: "About what time would you say you saw him?"
Daniel: "6:30… I saw him on my way out."
Daniel: "too many people…"
you: "So you're saying you saw him and left at 6:30PM?"
Daniel: "…yes."
you: "Did you see anyone else there?"
Daniel: "…too many people. can't remember."
you: "I see. Well thanks for trying, Daniel."
you: "I'll come back if I have any more questions to ask you"
Daniel: "…okay."

#Daniel Scene 6
Daniel: "…"
Choice: "<Accuse him of murder> I'm arresting you on suspicion of murder. you're coming with me."
Daniel: "…"
Daniel: "(pops out from behind the pillar really fast) DIE THEN."
narrator: "Daniel lunges at you, but you're ready for it. you wrestle him to the ground and handcuff him."
you: "you have the right to remain silent. Anything you say can and will be used against you in a court of law. you have the right to talk to a lawyer for advice before we ask you any questions. you have the ri-"
Daniel: "DON'T READ THIS DRIVEL TO ME. A SCRIPT?? PUTRID. you DISGUST ME."
you: "If you cannot afford a lawyer, one will be appointed for you before any questioning if you wish. If you decide to answer questions now without a lawyer present, you have the right to stop answering at any time."
narrator: "Daniel fights the whole way as you take him to the police station."
"<fade to black>"
Crawl: "Daniel is convicted of all three murders."
"After some intense interrogation, you discover that he was planning to kill Derek that night."
"When he learned you were on to him, he decided to kill you instead."
"you didn't just save the town."
"you saved yourself."
"Killer captured."

#Daniel Scene 7
narrator:"You try to sift your way through the crowd, but end up in a large crush of visitors. You can’t help but feel an ominous pair of eyes on you."
Daniel: "…"
Daniel: "(pops out from behind the pillar really fast) YOU DIE NOW."
narrator: "Daniel lunges at you, and quickly plunges a knife into your chest. The last thing you see is Daniel’s face glancing at you, manically laughing as he continues his flurry of stabs while you take your last breath."
Daniel: "It’s all a part of the show…"

Crawl: "Your investigation has probed the suspicion of the killer, placing you directly into their crosshairs."
	"You were unable to deduce the killer’s identity in time."
	"Your name has now become another in a long line of obituaries."
	"Despite a large crowd, with a quick escape, the killer managed to evade capture again."
	"The killer is still on the loose."



#Derek Scene 1
Derek (holding out sunglasses): "Hey champ! Care for a pair?"
you: "What? "
Derek: "Of screaming shades! They're all the rave these days! Tell ya what, I can swing you a first time buyer discount, for the spooky season!"
    Choice1: "Sure, I'm busy at the moment, but I'll be back"
    Derek: "Oh joy! A prospective customer! Ya won't regret this pal, I promise you that!"
    
    Choice2: "No thanks…"
    Derek (blank stare; takes off his sunglasses): "Oh.. I see."
    "<Sad Trombone>"
    Derek: "Oh don't mind me, that's just the sound of my heart getting kicked down an elevator shaft. Sinking deeper and deeper into the darkest pits of hell."
you: "Anyway, what's your deal?"
Derek: "you mean, you don't know? Why I'm Derek, of course! Sunglass producer extraordinaire! "
Derek: "I'm kind of a big deal around here"
you: "Never heard of you."
Derek: "W-wha?! Damn…"
    Choice1: "So you sell sunglasses?"
    Derek: "Guilty as charged! No other retailer can guarantee you the Derek seal of approval I'll tell you that!"
    
    Choice2: "How's business?"
    Derek: "Absolutely splendid! We sell out our stock every week! The customers can't get enough of them!"
    narrator: "you doubt that."
    you: "Yeah, well Luxottica might have something to say about that"
    Derek: "I have no idea what you mean!"
you: "Well, carry on, but I have a few questions to ask you when I get back."
Derek: "Don't be a stranger! And make sure you tell all your friends that Derek's shades are where it's at!"

#Derek Scene 2
Derek: "Why if it isn't my favorite prospective customer! What can I do for you?"
Choice: "<Ask about murder of Tom> What can you tell me about the murder of Tom Chatawa?"
Derek: "Oh, it's all so terrible… The coppers booked me last week for questioning. They think I did it! It's ridiculous!"
Derek: "Why are you asking about Tom?"
    Choice1: "I heard you and him were close"
    Derek: "Well, close isn't the word I would use…"
    
    Choice2: "I'm investigating these killings. <increases suspicion>"
    Derek: "On your own? Or…"
    you: "I work with the police."
    Derek: "Oh, you're a detective? I guess I have no choice but to cooperate then"
Derek: "His chicken was the talk of the town! \"No one could make fried chicken like ol' Tom Chatawa!\" Sooner or later, that stand became all anyone ever wanted to go to in this place. "
Derek: "I'd be lying if I said I was crying over spilled milk. The lad did not deserve what happened to him, "
Derek: "But hey, maybe with him outta the way, there might be more visitors willing to buy some of Derek's shades"
Choice1: "Where were you at the time he was killed?"
Derek: "I already told the other officers this. I was running my stand as usual, you know how it is. Peak mall hours are down by 10, so I was already on my way out when they found him."
you: "Can anyone vouch for that?"
Derek: "Well, I'm not exactly keeping track of every face I see can I? But you gotta believe me"
Choice2: "Who else was in the mall at the time of the killing? Anyone here you recognize from that night? <increase suspicion>"
Derek: "Well, I'm not exactly keeping track of every face I see. If I recall correctly, I believe I noticed that one goatwoman near Spirit Halloween shopping around last week. She was here around 7 to 8 and I didn't see her after. There was also this weird kid who looked quite empty inside. Probably some elementary schooler. I think I saw him over there right now. I saw him leave the mall right as the sun was going down."
you: "I think that's enough. Thank you, Derek."
Derek: "Anything else you want to ask me?"

#Derek Scene 3
Derek: "Why if it isn't my favorite prospective customer! What can I do for you?"
Choice: "<ask about the murder of Sora> Where were you on the night of October 15th?"
Derek: "Oh, that was two weeks ago, I'm not sure if I fully remember…"
Derek: "I believe I was out drinking at the local bar."
    Choice1: "Near the town square? <increase suspicion>"
    Derek: "Well yeah, the best places are there. The best moonshine in town."
    you: "So was the body of a dokkaebi."
    Derek: "Oh yeah I heard about that. "
    
    Choice2: "When was this?"
    Derek: "I think I was up till midnight. I was on a real bender."
    you: "Do you remember anything else that might have happened that night?"
    Derek: "My memory's quite fuzzy. I had a lot of shots."
you: "Was there anyone you remember running into?"
Derek: "Well, there were a bunch of high schoolers out too, probably drinking. I mean, what are you gonna do? They're all bound to sooner or later."
    Choice1: "One of them happen to be a werewolf?"
    Derek: "I think I did see a couple of werewolves. you know, all furry and stuff. Bunch of them throughout the night."
    
    Choice2: "One of them happen to be a swamp monster? <increase suspicion>"
    Derek: "I think I did see a swamp monster that night. Probably here for a good time, but  I don't think I saw him take a single drink."
you: "When did you see them?"
Derek: "I'm telling you I don't remember much, but I guess it was around the time I was there, so sometime between the hours of 8-12."
you: "I think that's all. Thank you, Derek."
Derek: "Anything else you wanna ask me?"

#Derek Scene 4
Derek: "Why if it isn't my favorite prospective customer! What can I do for you?"
Choice: "<Ask about murder of Dorothy> Where were you on the night of October 7th?"
Derek: "That was quite a while ago, I'm not sure if I remember."
Derek: "Oh yes, I was heading home. I wrapped up, and took the bus back to my apartment."
you: "Can anyone confirm that?"
Derek: "I believe I ran into my neighbor Ava on the way back, but she ain't here right now."
    Choice1: "What time was this?"
    Derek: "I think it was around 10PM."
    
    Choice2: "And what did you do then?"
    Derek: "I took a shower and went to sleep?"
you: "And where do you live exactly?"
Derek: "you know I'm not gonna answer that."
Derek: "I live around Armour Hill"
Narrative: "This is a ten minute drive from the school where Dorothy was found."
you: "I think that's all. Thank you, Derek."
Derek: "Anything else you wanna ask me?"

#Derek Scene 5
Derek: "Why if it isn't my favorite prospective customer! What can I do for you?"
Choice: "<Ask about business> Awfully low turnaround today isn't it?"
Derek: "Oh well, it's just typical seasonal blues! It's Halloween after all! Customers flock in droves to the Party City this time of year!"
you: "you told me earlier that your business is flourishing, and yet it's a Friday night and your stock seems to be in abundance. you've sold nothing."
Derek (takes off glasses): "Alright… if you really wish to know, I'm a failure."
Derek: "The kiddos these days… they just don't know a good deal when it's staring them in the face."
"<He stares at you for a solid couple of seconds>"
you: "But it was successful?"
Derek: "Oh yes, the talk of the town in fact. These shades flew off the shelves… but then the copycats came."
Derek: "\"Oh, look at that lad with the cheap stand! Might as well try our hand at it too!\""
Derek: "It was fried chicken, watches, those shoe shiners, I mean, who even shines their shoes anymore?! It's crazy that these copies even drew in the numbers they did!"
    Choice1: "Do you know of anyone who would wish harm upon these owners? <increase suspicion>"
    Derek: "I'm not too sure. I know this one old mothman that hates anyone and everyone, but I don't know if he'd have the capability to kill."
    
    Choice2: "Would you have any reason to wish harm upon these owners?"
    Derek: "Of course not! I may wish them nothing but the most soul crushing failure, but I would never wish harm upon them!"
you: "I think that's enough. Thank you, Derek."
Derek: "Anything else you wanna ask me?"

#Derek Scene 6
Derek: "Why if it isn't my favorite prospective customer! What can I do for you?"
Choice: "<Accuse him of murder> I'm arresting you on suspicion of murder. you're coming with me."
Derek: "Wait what?! "
Derek: "Surely this has gotta be some mistake!"
you: "you can prove that after I take you in."
narrator: "you tackle Derek to the ground and handcuff him before he can escape."
<fade to black>
Crawl: "you escorted Derek back to the police station and questioned him all night. "
"He is apprehensive and emotional, but answers all the questions truthfully."
"The next morning, you find that there has been another murder committed at the mall shortly after you escorted Derek out of the premises."
"The victim was a goatwoman named Shannon."
"The killer is still on the loose."

#Shannon Scene 1
Shannon: "Oh my dearest me, look at you! Aren't you the most precious thing in the world?"
Shannon: "What are you supposed to be, dear?"
you: "Ma'am, I'd like to ask you a few questions if you have the time. I'm investigating a potential serial killer."
Shannon: "Oh wow! you have a backstory and everything! Now that's commitment to a costume!"
Shannon: "you just don't get many people who are willing to really go all in on Halloween anymore. I remember when I was younger, oh! I loved Halloween. "
Shannon: "I'd dress up with all my friends and we'd have ourselves a proper little party. I always loved the pumpkin pie, I still have it every year with my husband and my son, David and David Jr."
Shannon: "Do you know them? David is a little bit of a celebrity around these parts on account of the success of his knife selling business."
you: "No, I don't believe I've had the pleasure of making his acquaintance. "
you: "Wait, I mean this isn't a costume. I'm a real homicide detective ma'am and I really do need to ask you some questions…"
Shannon: "Of course, I'd love to answer any questions that you have… detective. (winks)"
you: "Alright… sorry, my head is all scrambled now. I'll be back with some questions for you Mrs…"
Shannon: "Shannon Boer. But you can just call me Shannon, detective."
you: "Right, ok I'll be back."

#Shannon Scene 2
Shannon: "Detective! you're back! I was wondering if I'd see you again tonight. Gotten any leads yet?"
you: "I'm working on it. I've got some questions for you if you don't mind."
Shannon: "Not at all! Fire away!"
Choice <Ask about the murder of Dorothy>: "Where were you the night of October 7th?"
Shannon: "Oh dear. That was a horrible night…"
Shannon: "you've really done your research, haven't you, dear? Alright well I suppose I'll tell you."
Shannon: "That was the night of the parent teacher conference. David was tired from work, so I took Junior to the conference."
Shannon: "He's been struggling a bit in school, they say he has trouble reading words. He's just like his dad, he is."
Shannon: "I know that if he tries hard enough he'll get it eventually. you know some people just don't have enough patience. "
Shannon: "Well anyways, so after the conference I got to talking with all the other moms, and one of them was Dorothy."
Shannon: "We weren't too close, but we got to talking about her daughter, Veronica. She's quite a talented young woman I've been told. She won the talent show the week prior to… ah well."
Shannon: "We got so caught up in talking, that it wasn't until sometime around I think 9PM that she and I went home."
Shannon: "At that point everyone else was gone, so it was just me, Dorothy, Junior, and the stars in the sky."
Shannon: "That's the last time I saw her. Swear on my heart."
you: "Do you remember who was there at the conference?"
Shannon: "Oh, well I'd assume all of the students and hopefully all of their families as well!"
Shannon: "I remember seeing that little one, stephen I believe his name is."
Shannon: "I worry about him. It can't be easy being so small and being in high school. I do hope he isn't being bullied."
you: "And you're sure everyone else had left?"
Shannon: "Oh, I can't be too sure. you know sometimes I get so caught up in talking that I lose track of time and what's going on around me. I'm sure you understand."
you: "Yes…this has been very informative, Mrs. Boer."
Shannon: "Please, call me Shannon. "
Shannon: "Do you have any other questions for me?"
you: "Let me collect my thoughts and I'll let you know in a bit."
Shannon: "Alright detective! Make sure you get lots of candy!"

#Shannon Scene 3
Shannon: "Detective! you're back! I was wondering if I'd see you again tonight. Gotten any leads yet?"
you: "I'm working on it. I've got some questions for you if you don't mind."
Shannon: "Not at all! Fire away!"
Choice <Ask about the murder of Dorothy>: "Do you remember what you were doing on October 15th?"
Shannon: "Oh, now give me a second to think, detective. That was quite some time ago…"
Shannon: "That was a weekday so I had to take Junior to school… David left bright and early as he always does…I had to take the trash out…I had to pick Junior up from school…"
you: "Did you go anywhere else besides school and your home?"
Shannon: "I can't quite seem to remember, detective."
you: "Maybe you happened to go near the town square?"
Shannon: "The town square… oh I see detective! Yes, yes of course the town square. I was there."
you: "you were? When?"
Shannon: "Oh let's say about 11AM around lunch time. you know there's a great little cafe there called The Warbler. It's to die for! "
Shannon: "I'm sure you're not too interested in that though… let's see. Maybe I saw a shadowy figure, roaming through the square."
you: "…did you?"
Shannon: "Yes! Shifty eyes, looking for their next victim. Oh! And I followed them. No one would suspect someone like little old me!"
Shannon: "And then I saw it! I saw it happen! They stole a purse and ran off. I ran after them screaming and hollering, \"
elp! Help! Thief!\""
Shannon: "But of course it was up to me to get them! I cornered them into an alleyway and said, \"Stop! I'm making a citizen's arrest. Return what you stole, thief!\""

Shannon: "Of course they didn't listen. So I killed them. Oop! "
you: "you… killed them? What did they look like?"
Shannon: "Detective! you should be listening! Shifty eyes, like a shadow. Sharp teeth, angry. Oh really angry. And very thief-like!"
you: "Right… Then what happened? After you… killed them?"
Shannon: "Oh right! It can't end there. Well, I used my magical goat powers to clean them up. There are mystics in my blood you know! On my mother's side."
Shannon: "All the blood and gore and gross things cleaned right up!"
Shannon: "Then afterwards I picked up Junior and went straight home. I had to make dinner after all."
you: "And did you leave your house for anything else afterwards?"
Shannon: "Oh do you need more, detective?"
you: "No, I mean I don't need anything. I want the truth."
Shannon: "Oh the truth! Well you should've said so!"
Shannon: "Well then the truth is we had a perfectly pleasant night, Junior got tucked into bed and David and I had our nightly little whiskey chat."
you: "So to confirm, you didn't go out at all after you returned home?"
Shannon: "Not after 4PM. "
you: "Alright, I think that'll be enough for now."
you: "I'll come back if I think of anything else."
Shannon: "Alright detective! Good luck!"

#Shannon Scene 4
Shannon: "Detective! you're back! I was wondering if I'd see you again tonight. Gotten any leads yet?"
you: "I'm working on it. I've got some questions for you if you don't mind."
Shannon: "Not at all! Fire away!"
Choice <Ask about the murder of Tom>: "Last Thursday night on October 23rd a man named Tom Chatawa was murdered in the parking lot of this mall. Do you remember what you were doing that day?"
Shannon: "Oh Tom. He was a wonderful man. Come, come detective. Let us have a moment of silence for him."
you: "Alright ma'am …"
Shannon: "…"
Shannon: "Tom Chatawa we will remember you as a pillar of this community. The work you did brought joy to many families. "
Shannon: "We will remember your kindness, your diligence, and the incredible taste of your chicken. "
Shannon: "May you rest in peace with the Lord above."
Shannon: "Amen."
you: "Amen…"
Shannon: "Now that we have properly paid Tom his respects, I can say I saw him that day."
you: "What happened?"
Shannon: "Well isn't that just the thing detective? Nothing really strange happened! "
Shannon: "I remember that day Junior was feeling sick, so we let him stay home from school. Some sort of cold, he's doing well now."
Shannon: "The whole week he had been begging me to go to Tom's to get some chicken. you know how boys are with mats. "
Shannon: "I always say that both my Davids are like bottomless pits, they eat so much!"
you: "So you went to get chicken from the mall. Was this in the morning?"
Shannon: "Well not early in the morning, maybe sometime around 11;30AM?"
Shannon: "Then after that I went home to take care of Junior."
Shannon: "And before you ask, detective. No, I didn't go anywhere else afterwards. Everyone knows I take care of my boy."
you: "Do you happen to remember anyone else there, or maybe anything that seemed out of place?"
Shannon: "Well. I suppose it was busier than usual. I remember I was in line for much longer than usual. Of all the salesmen in the mall, Tom has been the one breakaway success. "
Shannon: "There was Derek as well, but that was years ago. you know, I wouldn't be surprised if he had something to do with this! Something about jealousy or something what do you think, detective?"
Shannon: "Isn't it strange that for both Dorothy and Tom something good happened to them before they were killed?"
you: "That is strange…"
Shannon: "I know right! I'm pretty good at this detective stuff. Maybe that'll be my costume next year!"
you: "you've given me a lot to think about, thank you Shannon."
you: "I'll be back if I have any more questions for you."
Shannon: "Good luck detective!"

#Shannon Scene 5
Shannon: "Hello again detective! Were you able to figure out who it was?"
Choice: "<Accuse her of murder> I'm arresting you on suspicion of murder. you're coming with me."
Shannon: "Oh dear! Are you being serious right now?"
you: "I'm afraid so, Shannon. Please cooperate."
narrator: "Shannon solemnly holds her wrists out. you handcuff her and take her to the station."
<fade to black>
Crawl: "you questioned her all night."
"At first she's still in disbelief, but soon she recovers to her chatty self."
"you learn a lot about her life and her suspicions, but nothing that would indicate she committed these murders."
"The next morning, you find that there has been another murder committed at the mall shortly after you escorted Shannon out of the premises."
"The victim was a moonman named Derek."
"The killer is still on the loose."