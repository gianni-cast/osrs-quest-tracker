#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports

# Local imports
from app import app
from models import db, Player, Quest, PlayerQuest

with app.app_context():
    print("Starting seed...")
    
    print("Deleting data...")
    Player.query.delete()
    Quest.query.delete()
    PlayerQuest.query.delete()

    print("Creating players...")
    player_1 = Player(name="Gc916", level='126')
    player_2 = Player(name="EugeneKrabz", level='126')
    player_3 = Player(name="mh892", level='126')
    player_4 = Player(name="Jtjack", level='109')
    player_5 = Player(name="Youni", level='93')
    players = [player_1, player_2, player_3, player_4, player_5]

    print("Creating quests...")

    quest_1 = Quest(name="Desert Treasure 2 - The Fallen Empire", description="During Gielinor's Second Age, the world was dominated by an empire the likes of which had never been seen. The areas now known as Asgarnia, Misthalin and even the Wilderness all once flourished under the banner of the Empty Lord. With the grand city of Senntisten at its heart, this civilisation washed over Gielinor like an unstoppable tide, pushing the boundaries of magic and science, while crushing any who stood in their way. Fast forward to today, the Fifth Age, and you won't find much trace of this ancient empire. Indeed, Saradominists and Zamorakians alike have spent many lifetimes purging all remnants of it. However, small fragments of this fallen empire remain, for those who know where to look. Perhaps you’ve already encountered some of these remains. Maybe you’ve met the monstrous Nex, sealed behind the Frozen Door for millennia. Or perhaps you’ve visited the bandits of the Kharidian Desert, the final human followers of the Empty Lord. You might even have encountered some mysterious Mahjarrat hidden away beneath those same sands. However, there are other parts of this forgotten empire that even you won’t have encountered yet. For example, this story begins deep in the desert, within a mysterious vault...")
    quest_2 = Quest(name="Dragon Slayer 2", description="30 years prior to the fateful day a mighty adventurer awakened Elvarg from her slumber, Crandor was a thriving and very much alive island, with a great tradition of mages and adventurers. The history of Crandor is a bold one, enough so that many a Crandorian earned the right to be part of the Champions Guild! The Crandor we know today is very different from that of the past and there are so many questions that remain unanswered - your chance to uncover the secrets of the past starts with Dragon Slayer II.")
    quest_3 = Quest(name="Monkey Madness 2", description="Glough, the war criminal set on eradicating humans and overthrowing Gielinor, has escaped the watch of the Grand Tree gnomes. With a history of leaving large-scale conflicts and warfare in his wake, Glough must be tracked down and stopped. King Narnode Shareen needs your help.")
    quest_4 = Quest(name="Song of the Elves", description="Our story begins with you, the hero, answering the call to adventure when Edmond, a resident of Ardougne, asks for your aid. By rescuing his daughter Elena from Plague City, the quarantined West Ardougne, you begin to unravel the mystery surrounding the disease. With her help, you discover the plague is a hoax - a plot by King Lathas to section off the West Ardougne. By confronting him, you find out this was done to protect the rest of Gielinor from the threat in the elven lands. The king sends you on a mission to travel through the Underground Pass and help his ally, Lord Iorwerth, in eradicating his brother King Tyras who threatens to revive the mysterious Dark Lord. After an arduous journey through the pass, you meet with Iorwerth and his forces to end Tyras' evil once and for all. Upon your return to Lathas you are intercepted by Arianwyn, a rebel elf who opposes Lord Iorwerth. He informs you of Lathas and Iorwerth's deception. They manipulated you into removing their final opposition and were now free to bring the Dark Lord back to Gielinor for their own intentions. You work with the elven rebellion to discover the purpose of the plague was to disguise the digsite of the long lost Temple of Light. An ancient place that is key to bringing back the Dark Lord. To make amends for your past mistakes and put a halt in King Lathas' and Lord Iorwerth's plans, you solve the intricate light puzzle designed to protect the Death Altar within the temple. After sealing off the temple and preventing the return of the Dark Lord, it's now time to turn your attention to King Lathas and Lord Iorwerth to end their schemes once and for all in Song of the Elves.")
    quest_5 = Quest(name="While Guthix Sleeps", description="This Grandmaster quest sees you continue the Mahjarrat storyline, hunting down one of the most powerful artefacts in existence while ensuring it doesn't fall into the wrong hands. This artefact is known by many names – most recently, the Stone of Jas. It has shaped the course of Gielinor’s history, from the creation of the first Runes to the fall of Zaros. It was last seen at the devastating end of the God Wars, when Zamorak, in a fit of rage, used it to reduce the land of Forinthry to the Wilderness we know today. Angered by Zamorak’s actions, Guthix rose from his age-long slumber and banished the gods. He hid the Stone of Jas far underground, where it could never disturb the balance again... But while Guthix sleeps, nefarious forces have been gathering; the Mahjarrat. Shaped by war and deadly ritual, their plans for the Stone can only lead to catastrophe. Facing off against the Mahjarrat is nothing new for dedicated adventurers – at every turn, they seem to grow in power and wage war against the people of Gielinor. In their last attempt, we saw them set out to tear Varrock apart with an undead army in Defender of Varrock. What are they plotting now?")
    
    quests= [quest_1, quest_2, quest_3, quest_4, quest_5]

    print("Creating PlayerQuest...")

    pq1 = PlayerQuest(player = player_1, progress = "Not Started", quest = quest_1)
    pq2 = PlayerQuest(player = player_2, progress = "Not Started", quest = quest_2)
    pq3 = PlayerQuest(player = player_3, progress = "Not Started", quest = quest_3)
    pq4 = PlayerQuest(player = player_4, progress = "Not Started", quest = quest_4)
    pq5 = PlayerQuest(player = player_5, progress = "Not Started", quest = quest_5)
    playerQuests = [pq1, pq2, pq3, pq4, pq5]
    db.session.add_all(players)
    db.session.add_all(quests)
    db.session.add_all(playerQuests)
    db.session.commit()



    print("Seeding done!")


