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
        mcr.command('title @a subtitle {"text":"' + event.user.nickname + '", "color":"red"}')
        mcr.command('title @a title {"text":"Welcome", "color":"green"}')
        mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')

@client.on(LikeEvent)
async def on_like(event: LikeEvent):
    if LikeEvent.count == 25:
        with con as mcr:
            mcr.command('title @a subtitle {"text":"Spawn Zombie", "color":"white"}')
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

# Share
@client.on(ShareEvent)
async def on_share(event: ShareEvent):
    with con as mcr:
        mcr.command('tellraw @a [{"text":"' + event.user.nickname + '", "color":"red"},{"text":" Sharing this live!", "color":"yellow"}]')
        mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')

#Gift
@client.on(GiftEvent)
async def on_gift(event: GiftEvent):
    #Streakable Gift      
    print(f"{event.user.nickname} -> {event.gift.id} STREAK")
    if event.gift.streakable and not event.streaking:
        #Gift Rose = Golden Carrots
        if event.gift.id == 5655:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Golden Carrots", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run give @p minecraft:golden_carrot')
                time.sleep(0.05)
                i+=1
        #Gift Coffe = Creeper
        elif event.gift.id == 5333:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Creeper", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:creeper ~ ~ ~')
                time.sleep(0.05)
                i+=1
        #Gift Tiktok = Skeleton
        elif event.gift.id == 5269:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Skeleton", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:skeleton ~ ~ ~')
                time.sleep(0.05)
                i+=1
        #Gift Friendship = Witch
        elif event.gift.id == 9947:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x 2 Witch", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:witch ~ ~ ~')
                    time.sleep(0.05)
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:witch ~ ~ ~')
                    time.sleep(0.05)
                    i+=1
        #Gift Coffee Big = Vindicator
        elif event.gift.id == 5933:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x 3 Vindicator", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:vindicator ~ ~ ~')
                    time.sleep(0.1)
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:vindicator ~ ~ ~')
                    time.sleep(0.1)
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:vindicator ~ ~ ~')
                    time.sleep(0.1)
                    i+=1
        #Gift Finger Heart = Totem of Undying
        elif event.gift.id == 5487:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x 3 Totem of Undying", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run give @p minecraft:totem_of_undying')
                time.sleep(0.05)
                i+=1
        #Gift GG = Enchanted Golden Apple
        elif event.gift.id == 6064:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Golden Apple", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run give @p minecraft:enchanted_golden_apple 1')
                time.sleep(0.05)
                i+=1
        #Gift Nasi Lemak = Ender Pearl
        elif event.gift.id == 5588:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Ender Pearl", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run give @p minecraft:ender_pearl 1')
                time.sleep(0.05)
                i+=1
        #Gift I Love You = Nausea
        elif event.gift.id == 5779:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Nausea", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run effect give @p minecraft:nausea 30')
                i+=1
        #Gift Parfume = Ender Eye
        elif event.gift.id == 5658:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x 20 Ender Eye", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run give @p minecraft:ender_eye 32')
                time.sleep(0.05)
                i+=1
        #Gift Orange Juice = Iron Ingot
        elif event.gift.id == 5778:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Iron Ingot", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run give @p minecraft:iron_ingot 1')
                time.sleep(0.05)
                i+=1
        #Gift Cantik Dehh = Levitation
        elif event.gift.id == 7024:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Levitation", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute as @p run effect give @p minecraft:levitation 2')
                time.sleep(2)
                i+=1
        #Gift Ice Tea = Spider
        elif event.gift.id == 5464:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Spider", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:spider ~ ~ ~')
                time.sleep(0.05)
                i+=1
        #Gift Doughnut = Evoker
        elif event.gift.id == 5879:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x 3 Evoker", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:evoker')
                    time.sleep(0.05)
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:evoker')
                    time.sleep(0.05)
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:evoker')
                    time.sleep(0.05)
                i+=1
        #Gift Bouquet Flower = Lava Pool
        elif event.gift.id == 5780:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' Lava Pool", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run fill ~2 ~ ~2 ~-2 ~ ~-2 lava')
                time.sleep(0.05)
                i+=1
        #Gift Rosa = Iron Golem
        elif event.gift.id == 8913:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x 5 Iron Golem", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:iron_golem ~ ~ ~')
                    time.sleep(0.1)
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:iron_golem ~ ~ ~')
                    time.sleep(0.1)
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:iron_golem ~ ~ ~')
                    time.sleep(0.1)
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:iron_golem ~ ~ ~')
                    time.sleep(0.1)
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:iron_golem ~ ~ ~')
                    time.sleep(0.1)
                    i+=1
        #Gift DJ Set = Full Armor + Tool Iron
        elif event.gift.id == 6248:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x Full Armor Iron + Tool", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run give @p iron_helmet{Enchantments:[{lvl:10,id:"minecraft:unbreaking"}]}')
                    mcr.command('execute at @p run give @p iron_chestplate{Enchantments:[{lvl:10,id:"minecraft:unbreaking"}]}')
                    mcr.command('execute at @p run give @p iron_leggings{Enchantments:[{lvl:10,id:"minecraft:unbreaking"}]}')
                    mcr.command('execute at @p run give @p iron_boots{Enchantments:[{lvl:10,id:"minecraft:unbreaking"}]}')
                    mcr.command('execute at @p run give @p iron_axe{Enchantments:[{lvl:10,id:"minecraft:unbreaking"}]}')
                    mcr.command('execute at @p run give @p iron_pickaxe{Enchantments:[{lvl:10,id:"minecraft:unbreaking"}]}')
                    mcr.command('execute at @p run give @p iron_sword{Enchantments:[{lvl:10,id:"minecraft:unbreaking"}]}')
                    mcr.command('execute at @p run give @p iron_shovel{Enchantments:[{lvl:10,id:"minecraft:unbreaking"}]}')
                    mcr.command('execute at @p run give @p bow{Enchantments:[{lvl:10,id:"minecraft:unbreaking"}]}')
                    mcr.command('execute at @p run give @p arrow 64')
                i+=1
        else:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent ' + str(event.repeat_count) + ' x ' + str(event.gift.info.name) + '", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            return
    #Non Streakable Gift          
    elif not event.gift.streakable:
        print(f"{event.user.nickname} -> {event.gift.id} NON STREAK")
        #Gift Heart Me = TNT
        if event.gift.id == 7934:
            with con as mcr:
                mcr.command('title @a subtitle {"text":"sent Gift Heart Me 5 TNT", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while i < 5:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('execute at @p run summon minecraft:tnt ~ ~ ~ {Fuse:40}')
                time.sleep(0.05)
                i+=1
        #Gift Confetti = Enderman
        elif event.gift.id == 5585:
            with con as mcr:
                mcr.command('title @a subtitle {"text":"sent Enderman", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
                mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                mcr.command('execute at @p run summon minecraft:enderman ~ ~ ~')
                mcr.command('execute at @p run summon minecraft:enderman ~ ~ ~')
                mcr.command('execute at @p run summon minecraft:enderman ~ ~ ~')
                mcr.command('execute at @p run summon minecraft:enderman ~ ~ ~')
        #Gift Confetti Member = Enderman
        elif event.gift.id == 7121:
            with con as mcr:
                mcr.command('title @a subtitle {"text":"sent Enderman", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
                mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                mcr.command('execute at @p run summon minecraft:enderman ~ ~ ~')
                mcr.command('execute at @p run summon minecraft:enderman ~ ~ ~')
                mcr.command('execute at @p run summon minecraft:enderman ~ ~ ~')
                mcr.command('execute at @p run summon minecraft:enderman ~ ~ ~')
        #Gift Origami = Elytra
        elif event.gift.id == 5659:
            with con as mcr:
                mcr.command('title @a subtitle {"text":"sent Elytra", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
                mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                mcr.command('execute at @p run give @p minecraft:firework_rocket 128')
                mcr.command('execute as @p run give @p minecraft:elytra{Enchantments:[{lvl:100,id:"minecraft:blast_protection"},{lvl:100,id:"minecraft:fire_protection"},{lvl:100,id:"minecraft:projectile_protection"},{lvl:100,id:"minecraft:protection"},{lvl:103,id:"minecraft:thorns"},{lvl:100,id:"minecraft:unbreaking"}]}')
        #Gift Swan = Delete Inventory
        elif event.gift.id == 5897:
            with con as mcr:
                mcr.command('title @a subtitle {"text":"sent Delete Inventory", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while event.repeat_count > i:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('clear @p')
                time.sleep(0.05)
                i+=1
        #Gift Corgi = Destroy Area
        elif event.gift.id == 6267:
            with con as mcr:
                mcr.command('title @a subtitle {"text":"sent Destroy Area", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
            i = 0
            while i < 15:
                with con as mcr:
                    mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                    mcr.command('fill ~-15 ~-15 ~-15 ~15 ~0 ~15 minecraft:air')    
                time.sleep(1)
                i+=1
        #Gift Duck = TNT PRISON
        elif event.gift.id == 6265:
            with con as mcr:
                mcr.command('title @a subtitle {"text":"sent TNT Prison", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
                mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                mcr.command('execute at @p run fill ~-7 ~-2 ~-7 ~7 ~14 ~7 tnt')
                mcr.command('execute at @p run fill ~-5 ~0 ~-5 ~ ~12 ~ air')
                mcr.command('execute at @p run summon minecraft:tnt ~ ~ ~ {Fuse:100}')
        #Gift Train = SERVER CRASH
        elif event.gift.id == 5978:
            with con as mcr:
                mcr.command('title @a subtitle {"text":"sent Server Crash", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
                time.sleep(1)
                mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                mcr.command('title @a subtitle {"text":"Countdown", "color":"white"}')
                mcr.command('title @a title {"text":"3", "color":"yellow"}')
                time.sleep(1)
                mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                mcr.command('title @a subtitle {"text":"Countdown", "color":"white"}')
                mcr.command('title @a title {"text":"2", "color":"yellow"}')
                time.sleep(1)
                mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                mcr.command('title @a subtitle {"text":"Countdown", "color":"white"}')
                mcr.command('title @a title {"text":"1", "color":"yellow"}')
                time.sleep(1)
                mcr.command('stop')
        #Gift Hand Hearts = Creative Mode 30 Seconds
        elif event.gift.id == 5660:
            with con as mcr:
                mcr.command('title @a subtitle {"text":"sent Creative Mode 30 Seconds", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
                mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                mcr.command('gamemode creative @p')
                time.sleep(30)
                mcr.command('gamemode survival @p')
        #Gift Kiss = Warden
        elif event.gift.id == 5577:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent Warden", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
                mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                mcr.command('execute at @p run summon minecraft:warden')
        #Gift Sunglasses = Wither
        elif event.gift.id == 5509:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent Wither", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
                mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                mcr.command('execute at @p run summon minecraft:wither')
        #Gift Money Gun = Kill All Entities
        elif event.gift.id == 7168:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent Kill", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
                mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                mcr.command('kill @e')
        #Gift Money Gun = Kill All Entities
        elif event.gift.id == 5739:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent Kill", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
                mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                mcr.command('kill @e')
        #Gift Money Gun = Kill All Entities
        elif event.gift.id == 7122:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent Kill", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
                mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                mcr.command('kill @e')
        #Gift Gold Necklace = Random Teleport
        elif event.gift.id == 5599:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent Random Teleport", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
                mcr.command('execute at @p run playsound minecraft:entity.enderman.teleport master @a ~ ~ ~ 10 1')
                mcr.command('spreadplayers ~ ~ 0 1000 false @a')
        
        #Gift Hat and Mustache = Full Armor + Tool Nether Enchanted
        elif event.gift.id == 6427:
            with con as mcr:
                mcr.command('title @a subtitle {"text":" sent Full Armor + Tool Nether Enchanted", "color":"white"}')
                mcr.command('title @a title {"text":"' + event.user.nickname + '", "color":"yellow"}')
                mcr.command('execute at @p run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 10 1')
                # Helmet
                mcr.command('execute at @p run give @p netherite_helmet{Enchantments:[{lvl:100,id:"minecraft:aqua_affinity"},{lvl:100,id:"minecraft:blast_protection"},{lvl:100,id:"minecraft:fire_protection"},{lvl:100,id:"minecraft:projectile_protection"},{lvl:100,id:"minecraft:protection"},{lvl:100,id:"minecraft:respiration"},{lvl:100,id:"minecraft:thorns"},{lvl:100,id:"minecraft:unbreaking"}]}')
                # Chestplate
                mcr.command('execute at @p run give @p netherite_chestplate{Enchantments:[{lvl:100,id:"minecraft:blast_protection"},{lvl:100,id:"minecraft:fire_protection"},{lvl:100,id:"minecraft:projectile_protection"},{lvl:100,id:"minecraft:protection"},{lvl:100,id:"minecraft:thorns"},{lvl:100,id:"minecraft:unbreaking"}]}')
                # Leggings
                mcr.command('execute at @p run give @p netherite_leggings{Enchantments:[{lvl:100,id:"minecraft:blast_protection"},{lvl:100,id:"minecraft:fire_protection"},{lvl:100,id:"minecraft:projectile_protection"},{lvl:100,id:"minecraft:protection"},{lvl:100,id:"minecraft:swift_sneak"},{lvl:100,id:"minecraft:thorns"},{lvl:100,id:"minecraft:unbreaking"}]}')
                # Boots
                mcr.command('execute at @p run give @p netherite_boots{Enchantments:[{lvl:100,id:"feather_falling"},{lvl:100,id:"minecraft:depth_strider"},{lvl:100,id:"minecraft:projectile_protection"},{lvl:100,id:"minecraft:feather_falling"},{lvl:100,id:"minecraft:fire_protection"},{lvl:100,id:"minecraft:frost_walker"},{lvl:100,id:"minecraft:protection"},{lvl:100,id:"minecraft:soul_speed"},{lvl:100,id:"minecraft:thorns"},{lvl:100,id:"minecraft:unbreaking"}]}')
                # Axe
                mcr.command('execute at @p run give @p netherite_axe{Enchantments:[{id:"minecraft:bane_of_arthropods",lvl:1},{id:"minecraft:efficiency",lvl:1},{id:"minecraft:fortune",lvl:1},{id:"minecraft:sharpness",lvl:1},{id:"minecraft:silk_touch",lvl:1},{id:"minecraft:smite",lvl:1},{id:"minecraft:unbreaking",lvl:1}]}')
                # Pickaxe
                mcr.command('execute at @p run give @p netherite_pickaxe{Enchantments:[{id:"minecraft:efficiency",lvl:1},{id:"minecraft:fortune",lvl:1},{id:"minecraft:silk_touch",lvl:1},{id:"minecraft:unbreaking",lvl:100}]}')
                # Sword
                mcr.command('execute at @p run give @p netherite_sword{Enchantments:[{id:"minecraft:bane_of_arthropods",lvl:100},{id:"minecraft:fire_aspect",lvl:100},{id:"minecraft:knockback",lvl:100},{id:"minecraft:looting",lvl:100},{id:"minecraft:sharpness",lvl:100},{id:"minecraft:silk_touch",lvl:100},{id:"minecraft:smite",lvl:100},{id:"minecraft:sweeping",lvl:100},{id:"minecraft:unbreaking",lvl:100}]}')
                # Bow
                mcr.command('execute at @p run give @p bow{Enchantments:[{id:"minecraft:flame",lvl:1},{id:"minecraft:infinity",lvl:1},{id:"minecraft:power",lvl:1},{id:"minecraft:punch",lvl:1},{id:"minecraft:unbreaking",lvl:100}]}')
                mcr.command('execute at @p run give @p arrow 192')
                mcr.command('execute at @p run give @p minecraft:netherite_shovel{Enchantments:[{id:"minecraft:silk_touch",lvl:1},{id:"minecraft:unbreaking",lvl:100}]}')
        else:
            with con as mcr:
                mcr.command('title @a subtitle {"text":"sent ' + str(event.gift.info.name) + '", "color":"white"}')
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
    root.geometry('250x100')
    root.resizable(False, False)

    start_button = tk.Button(root, text="Start", command=start_client)
    start_button.pack()

    root.mainloop()
