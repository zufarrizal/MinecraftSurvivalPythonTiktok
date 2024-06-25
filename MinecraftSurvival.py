import time
import datetime
import tkinter as tk
from tkinter import messagebox
import mcrcon
import time
from TikTokLive import TikTokLiveClient
from TikTokLive.events import CommentEvent, ConnectEvent, GiftEvent, LikeEvent, FollowEvent, ShareEvent, JoinEvent
con = mcrcon.MCRcon("localhost", "123", 25575)

expiry_date = datetime.date(2025, 1, 1)

# Username
client: TikTokLiveClient = TikTokLiveClient(unique_id="@mjup96")

# Connect
@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    with con as mcr:
        print("Connected to Room ID:", client.room_id)
        mcr.command('tellraw @a {"text":"Running Application", "color":"green"}')
        mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')

# Join
@client.on(JoinEvent)
async def on_join(event: JoinEvent):
    with con as mcr:
        mcr.command('tellraw @a [{"text":"Welcome ", "color":"yellow"},{"text":"' + event.user.nickname + '", "color":"red"}]')

@client.on(LikeEvent)
async def on_like(event: LikeEvent):
    if event.count > 10:   
        with con as mcr:
            mcr.command('title @a subtitle {"text":"sent Zombie", "color":"white"}')
            mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
            mcr.command('execute at @p run summon minecraft:zombie ~ ~ ~')

# Comment
@client.on(CommentEvent)
async def on_comment(event: CommentEvent):
    with con as mcr:
        mcr.command('tellraw @a [{"text":"' + event.user.nickname + '", "color":"red"},{"text":" -> ", "color":"white"},{"text":"' + event.comment + '", "color":"yellow"}]')
        mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')

# Follow
@client.on(FollowEvent)
async def on_follow(event: FollowEvent):
    with con as mcr:
        mcr.command('tellraw @a [{"text":"' + event.user.nickname + '", "color":"red"},{"text":" Following Streamers!", "color":"yellow"}]')
        mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
        mcr.command('execute at @p run give @p minecraft:enchanted_golden_apple')
# Share
# @client.on(ShareEvent)
# async def on_share(event: ShareEvent):
#     with con as mcr:
#         mcr.command('tellraw @a [{"text":"' + event.user.nickname + '", "color":"red"},{"text":"-> Share", "color":"yellow"}]')
#         mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')

#Gift
@client.on(GiftEvent)
async def on_gift(event: GiftEvent):
    #Streakable Gift      
    print(f"{event.user.nickname} -> {event.gift.id} -> {event.gift.name} STREAK")
    if event.gift.streakable and not event.streaking:
        #Gift Rose = Skeleton
        if event.gift.id == 5655:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Skeleton", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:skeleton ~ ~ ~')
                time.sleep(0.2)
                i+=1
        #Gift Nasi Lemak = Spider
        elif event.gift.id == 5588:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Spider", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:spider ~ ~ ~')
                time.sleep(0.2)
                i+=1
        #Gift Coffee = Creeper
        elif event.gift.id == 5333:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Creeper", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:creeper ~ ~ ~')
                time.sleep(0.2)
                i+=1
        #Gift Rendang Chicken = Zombified Piglin
        elif event.gift.id == 10585:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Zombified Piglin", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:zombified_piglin ~ ~ ~')
                time.sleep(0.2)
                i+=1
        #Gift GG = Potato
        elif event.gift.id == 6064:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Baked Potato", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run give @p minecraft:baked_potato')
                time.sleep(0.2)
                i+=1
        #Gift Cantik Deh = Cooked Porkchop
        elif event.gift.id == 7024:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Cooked Porkchop", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run give @p minecraft:cooked_porkchop')
                time.sleep(0.2)
                i+=1
        #Gift Tiktok = Steak
        elif event.gift.id == 5269:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Steak", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run give @p minecraft:cooked_beef')
                time.sleep(0.2)
                i+=1
        #Gift Ice Cream Cone = Golden Carrot
        elif event.gift.id == 5827:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Golden Carrot", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run give @p minecraft:golden_carrot')
                time.sleep(0.2)
                i+=1
        #Gift Ice Cream Cone = Echanted Golden Apple
        elif event.gift.id == 5778:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Golden Apple", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run give @p minecraft:enchanted_golden_apple')
                time.sleep(0.2)
                i+=1
        #Gift Cakep = Iron Ingot
        elif event.gift.id == 9583:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Iron Ingot", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run give @p minecraft:iron_ingot')
                time.sleep(0.2)
                i+=1
        #Gift Tahu Tempe = Gold Ingot
        elif event.gift.id == 5462:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Gold Ingot", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run give @p minecraft:gold_ingot')
                time.sleep(0.2)
                i+=1
        #Gift Finger Heart = Diamond
        elif event.gift.id == 5487:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Diamond", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run give @p minecraft:diamond 2')
                time.sleep(0.2)
                i+=1
        #Gift Raya Rice = Ender Pearl
        elif event.gift.id == 8136:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Ender Pearl", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run give @p minecraft:ender_pearl')
                time.sleep(0.2)
                i+=1
        #Gift Rosa = Ender Eye
        elif event.gift.id == 8913:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Ender Eye", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run give @p minecraft:ender_eye 8')
                time.sleep(0.2)
                i+=1
        #Gift Rosa = Pillager
        elif event.gift.id == 5779:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x 3 Pillager", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:pillager ~ ~ ~')
                    mcr.command('execute at @p run summon minecraft:pillager ~ ~ ~')
                    mcr.command('execute at @p run summon minecraft:pillager ~ ~ ~')
                time.sleep(0.2)
                i+=1
        #Gift Cow = Witch
        elif event.gift.id == 10972:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x 3 Witch", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:witch ~ ~ ~')
                    mcr.command('execute at @p run summon minecraft:witch ~ ~ ~')
                    mcr.command('execute at @p run summon minecraft:witch ~ ~ ~')
                time.sleep(0.2)
                i+=1
        #Gift Hi Bear = Vindicator
        elif event.gift.id == 10293:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x 3 Vindicator", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:vindicator ~ ~ ~')
                    mcr.command('execute at @p run summon minecraft:vindicator ~ ~ ~')
                    mcr.command('execute at @p run summon minecraft:vindicator ~ ~ ~')
                time.sleep(0.2)
                i+=1
        #Gift Friendship Necklace = Totem of Undying
        elif event.gift.id == 9947:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x 2 Totem of Undying", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run give @p minecraft:totem_of_undying 2')
                time.sleep(0.2)
                i+=1
        #Gift Eid Adha = Iron Armor
        elif event.gift.id == 10971:
            with con as mcr:
                    mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Iron Armor", "color":"white"}')
                    mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run give @p iron_helmet{Enchantments:[{id:"minecraft:protection",lvl:4},{id:"minecraft:fire_protection",lvl:4},{id:"minecraft:blast_protection",lvl:4},{id:"minecraft:projectile_protection",lvl:4},{id:"minecraft:respiration",lvl:3},{id:"minecraft:aqua_affinity",lvl:1},{id:"minecraft:thorns",lvl:3},{id:"minecraft:unbreaking",lvl:3},{id:"minecraft:mending",lvl:1}]}')
                    mcr.command('execute at @p run give @p iron_chestplate{Enchantments:[{id:"minecraft:protection",lvl:4},{id:"minecraft:fire_protection",lvl:4},{id:"minecraft:blast_protection",lvl:4},{id:"minecraft:projectile_protection",lvl:4},{id:"minecraft:thorns",lvl:3},{id:"minecraft:unbreaking",lvl:3},{id:"minecraft:mending",lvl:1}]}')
                    mcr.command('execute at @p run give @p iron_leggings{Enchantments:[{id:"minecraft:protection",lvl:4},{id:"minecraft:fire_protection",lvl:4},{id:"minecraft:blast_protection",lvl:4},{id:"minecraft:projectile_protection",lvl:4},{id:"minecraft:thorns",lvl:3},{id:"minecraft:unbreaking",lvl:3},{id:"minecraft:mending",lvl:1}]}')
                    mcr.command('execute at @p run give @p iron_boots{Enchantments:[{id:"minecraft:protection",lvl:4},{id:"minecraft:fire_protection",lvl:4},{id:"minecraft:blast_protection",lvl:4},{id:"minecraft:projectile_protection",lvl:4},{id:"minecraft:feather_falling",lvl:4},{id:"minecraft:depth_strider",lvl:3},{id:"minecraft:frost_walker",lvl:2},{id:"minecraft:soul_speed",lvl:3},{id:"minecraft:thorns",lvl:3},{id:"minecraft:unbreaking",lvl:3},{id:"minecraft:mending",lvl:1}]}')
                    mcr.command('execute at @p run give @p iron_axe{Enchantments:[{id:"minecraft:sharpness",lvl:5},{id:"minecraft:smite",lvl:5},{id:"minecraft:bane_of_arthropods",lvl:5},{id:"minecraft:efficiency",lvl:5},{id:"minecraft:unbreaking",lvl:3},{id:"minecraft:fortune",lvl:3},{id:"minecraft:mending",lvl:1}]}')
                    mcr.command('execute at @p run give @p iron_pickaxe{Enchantments:[{id:"minecraft:efficiency",lvl:5},{id:"minecraft:unbreaking",lvl:3},{id:"minecraft:fortune",lvl:3},{id:"minecraft:mending",lvl:1}]}')
                    mcr.command('execute at @p run give @p iron_sword{Enchantments:[{id:"minecraft:sharpness",lvl:5},{id:"minecraft:smite",lvl:5},{id:"minecraft:bane_of_arthropods",lvl:5},{id:"minecraft:fire_aspect",lvl:2},{id:"minecraft:looting",lvl:3},{id:"minecraft:unbreaking",lvl:3},{id:"minecraft:sweeping_edge",lvl:3},{id:"minecraft:mending",lvl:1}]}')
                    mcr.command('execute at @p run give @p iron_shovel{Enchantments:[{id:"minecraft:efficiency",lvl:5},{id:"minecraft:unbreaking",lvl:3},{id:"minecraft:fortune",lvl:3},{id:"minecraft:mending",lvl:1}]}')
                    mcr.command('execute at @p run give @p bow{Enchantments:[{id:"minecraft:power",lvl:5},{id:"minecraft:punch",lvl:2},{id:"minecraft:flame",lvl:1},{id:"minecraft:infinity",lvl:1},{id:"minecraft:unbreaking",lvl:3},{id:"minecraft:mending",lvl:1}]}')
                    mcr.command('execute at @p run give @p arrow 64')
                time.sleep(0.2)
                i+=1
        #Gift Bucket = Diamond Armor
        elif event.gift.id == 5780:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Diamond Armor", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
                mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run give @p diamond_helmet{Enchantments:[{id:"minecraft:protection",lvl:4},{id:"minecraft:fire_protection",lvl:4},{id:"minecraft:blast_protection",lvl:4},{id:"minecraft:projectile_protection",lvl:4},{id:"minecraft:respiration",lvl:3},{id:"minecraft:aqua_affinity",lvl:1},{id:"minecraft:thorns",lvl:3},{id:"minecraft:unbreaking",lvl:3},{id:"minecraft:mending",lvl:1}]}')
                    mcr.command('execute at @p run give @p diamond_chestplate{Enchantments:[{id:"minecraft:protection",lvl:4},{id:"minecraft:fire_protection",lvl:4},{id:"minecraft:blast_protection",lvl:4},{id:"minecraft:projectile_protection",lvl:4},{id:"minecraft:thorns",lvl:3},{id:"minecraft:unbreaking",lvl:3},{id:"minecraft:mending",lvl:1}]}')
                    mcr.command('execute at @p run give @p diamond_leggings{Enchantments:[{id:"minecraft:protection",lvl:4},{id:"minecraft:fire_protection",lvl:4},{id:"minecraft:blast_protection",lvl:4},{id:"minecraft:projectile_protection",lvl:4},{id:"minecraft:thorns",lvl:3},{id:"minecraft:unbreaking",lvl:3},{id:"minecraft:mending",lvl:1}]}')
                    mcr.command('execute at @p run give @p diamond_boots{Enchantments:[{id:"minecraft:protection",lvl:4},{id:"minecraft:fire_protection",lvl:4},{id:"minecraft:blast_protection",lvl:4},{id:"minecraft:projectile_protection",lvl:4},{id:"minecraft:feather_falling",lvl:4},{id:"minecraft:depth_strider",lvl:3},{id:"minecraft:frost_walker",lvl:2},{id:"minecraft:soul_speed",lvl:3},{id:"minecraft:thorns",lvl:3},{id:"minecraft:unbreaking",lvl:3},{id:"minecraft:mending",lvl:1}]}')
                    mcr.command('execute at @p run give @p diamond_axe{Enchantments:[{id:"minecraft:sharpness",lvl:5},{id:"minecraft:smite",lvl:5},{id:"minecraft:bane_of_arthropods",lvl:5},{id:"minecraft:efficiency",lvl:5},{id:"minecraft:unbreaking",lvl:3},{id:"minecraft:fortune",lvl:3},{id:"minecraft:mending",lvl:1}]}')
                    mcr.command('execute at @p run give @p diamond_pickaxe{Enchantments:[{id:"minecraft:efficiency",lvl:5},{id:"minecraft:unbreaking",lvl:3},{id:"minecraft:fortune",lvl:3},{id:"minecraft:mending",lvl:1}]}')
                    mcr.command('execute at @p run give @p diamond_sword{Enchantments:[{id:"minecraft:sharpness",lvl:5},{id:"minecraft:smite",lvl:5},{id:"minecraft:bane_of_arthropods",lvl:5},{id:"minecraft:fire_aspect",lvl:2},{id:"minecraft:looting",lvl:3},{id:"minecraft:unbreaking",lvl:3},{id:"minecraft:sweeping_edge",lvl:3},{id:"minecraft:mending",lvl:1}]}')
                    mcr.command('execute at @p run give @p diamond_shovel{Enchantments:[{id:"minecraft:efficiency",lvl:5},{id:"minecraft:unbreaking",lvl:3},{id:"minecraft:fortune",lvl:3},{id:"minecraft:mending",lvl:1}]}')
                    mcr.command('execute at @p run give @p bow{Enchantments:[{id:"minecraft:power",lvl:5},{id:"minecraft:punch",lvl:2},{id:"minecraft:flame",lvl:1},{id:"minecraft:infinity",lvl:1},{id:"minecraft:unbreaking",lvl:3},{id:"minecraft:mending",lvl:1}]}')
                    mcr.command('execute at @p run give @p arrow 64')
                time.sleep(0.2)
                i+=1
        #Gift Doughnut = Lava Pool
        elif event.gift.id == 5879:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Lava Pool", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 lava')
                time.sleep(0.2)
                i+=1
        #Gift Blow a Kiss = Levitation
        elif event.gift.id == 10716:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Levitation 4 Detik", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run effect give @p minecraft:levitation 4 1 true')
                time.sleep(4)
                i+=1
        #Gift Perfume = Evoker
        elif event.gift.id == 5658:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Evoker", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:evoker ~ ~ ~')
                    mcr.command('execute at @p run summon minecraft:evoker ~ ~ ~')
                    mcr.command('execute at @p run summon minecraft:evoker ~ ~ ~')
                time.sleep(0.2)
                i+=1
        #Gift Fairy wings = Iron Golem
        elif event.gift.id == 9463:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Iron Golem", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:iron_golem ~ ~ ~')
                time.sleep(0.2)
                i+=1
        #Gift Sweet Sheep = Nausea
        elif event.gift.id == 9371:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Nausea 15 Detik", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run effect give @p minecraft:nausea 15 1 true')
                time.sleep(15)
                i+=1
        else:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x ' + str(event.gift.name) + '", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            return
    #Non Streakable Gift          
    elif not event.gift.streakable:
        print(f"{event.user.nickname} -> {event.gift.id} -> {event.gift.name} NON STREAK")
        #Gift Mishka Bear = Warden
        if event.gift.id == 5566:
            with con as mcr:
                mcr.command('title @a subtitle {"text":"sent Warden", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
                mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                mcr.command('execute at @p run summon minecraft:warden ~ ~ ~')
        #Gift heart Me = Enchanted Golden Apple
        if event.gift.id == 7934:
            with con as mcr:
                mcr.command('title @a subtitle {"text":"sent 5 Enchanted Golden Apple", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + ' Hadir!", "color":"yellow"}')
                mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                mcr.command('execute at @p run give @p minecraft:enchanted_golden_apple')
                mcr.command('execute at @p run give @p minecraft:enchanted_golden_apple')
                mcr.command('execute at @p run give @p minecraft:enchanted_golden_apple')
                mcr.command('execute at @p run give @p minecraft:enchanted_golden_apple')
                mcr.command('execute at @p run give @p minecraft:enchanted_golden_apple')
        #Gift Gold Necklace = Wither
        elif event.gift.id == 5599:
            with con as mcr:
                mcr.command('title @a subtitle {"text":"sent Wither", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
                mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                mcr.command('execute at @p run summon minecraft:wither ~ ~ ~')
        #Gift Hat and Mustache = Random Teleport
        elif event.gift.id == 6427:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent Random Teleport", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
                mcr.command('execute at @p run playsound minecraft:entity.enderman.teleport master @a ~ ~ ~ 10 1')
                mcr.command('spreadplayers ~ ~ 0 2000 false @a')
        #Gift Paper Crane = Darkness
        elif event.gift.id == 6427:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent Darkness 1 Menit", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
                mcr.command('execute at @p run playsound minecraft:entity.enderman.teleport master @a ~ ~ ~ 10 1')
                mcr.command('execute at @p run effect give @p minecraft:darkness 60 1 true')
        #Gift Confetti = Elytra
        elif event.gift.id == 5585:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent Elytra", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
                mcr.command('execute at @p run playsound minecraft:entity.enderman.teleport master @a ~ ~ ~ 10 1')
                mcr.command('execute at @p run give @p minecraft:elytra')
        #Gift Sunglasses = Clear Inventory
        elif event.gift.id == 5509:
            with con as mcr:
                mcr.command('title @a subtitle {"text":"sent Clear Inventory", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
                mcr.command('execute at @p run playsound minecraft:entity.enderman.teleport master @a ~ ~ ~ 10 1')
                mcr.command('clear @p')
        #Gift Duck = TNT PRISON
        # elif event.gift.id == 6265:
        #     with con as mcr:
        #         mcr.command('title @a subtitle {"text":"sent TNT Prison", "color":"white"}')
        #         mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
        #         mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
        #         mcr.command('execute at @p run fill ~-7 ~-2 ~-7 ~7 ~14 ~7 tnt')
        #         mcr.command('execute at @p run fill ~-5 ~ ~-5 ~5 ~12 ~5 air')
        #         mcr.command('execute at @p run summon minecraft:tnt ~ ~ ~ {Fuse:150}')
        #Gift Train = SERVER CRASH
        # elif event.gift.id == 5978:
        #     with con as mcr:
        #         mcr.command('title @a subtitle {"text":"sent Server Crash", "color":"white"}')
        #         mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
        #         time.sleep(1)
        #         mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
        #         mcr.command('title @a subtitle {"text":"Countdown", "color":"white"}')
        #         mcr.command('title @a title {"text":"3", "color":"yellow"}')
        #         time.sleep(1)
        #         mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
        #         mcr.command('title @a subtitle {"text":"Countdown", "color":"white"}')
        #         mcr.command('title @a title {"text":"2", "color":"yellow"}')
        #         time.sleep(1)
        #         mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
        #         mcr.command('title @a subtitle {"text":"Countdown", "color":"white"}')
        #         mcr.command('title @a title {"text":"1", "color":"yellow"}')
        #         time.sleep(1)
        #         mcr.command('stop')
        else:
            with con as mcr:
                mcr.command('title @a subtitle {"text":"sent ' + str(event.gift.name) + '", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            return

def start_client():
    client.run()

if datetime.date.today() > expiry_date:
    messagebox.showerror("Expired", "Aplikasi ini telah kedaluwarsa.")
else:
    # Your application code here
    root = tk.Tk()
    root.title("MASJUPLE")
    root.geometry('300x200')
    root.resizable(False, False)

    start_button = tk.Button(root, text="Start", command=start_client)
    start_button.pack()

    root.mainloop()
