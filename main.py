from discord.ext import commands
import os
import traceback

import datetime
import discord
import json
import random
import requests

with open ("token.txt") as tkn:
    token = tkn.read() #トークンを文字列として読み込み

#token = os.environ['DISCORD_BOT_TOKEN'] #Config Barに書き込んだトークン読んでもらう

#接続に必要なオブジェクト生成
client = discord.Client()

@client.event
async def on_ready():
    print("TESTログイン")

@client.event
async def on_message(message):
    cnt = 0
    if message.content.find("test") != -1:
        if message.author.bot:
            return
        await message.channel.send(f"{message.author.mention},ワンワンッ！！お呼びですか〜？")
    
    elif (message.content == ("UUUM")) or (message.content == ("thinking")):
        await message.delete()
        await message.channel.send(":thinking:")
    
    elif message.content.find("NG") != -1:
        if (message.content.find("ING") != -1) or (message.content.find("NGO") != -1):
            return
    
        elif message.content == ("NG"):
            await message.delete()
        await message.channel.send(":ng:")
    
    elif message.content.find("sexy") != -1:
        emoji = client.get_emoji(751817150834016297)
        await message.add_reaction(emoji) # :pornhub:リアクションを追加
    
    elif message.content == ("/happy"):
        await message.channel.send(f"{message.author.mention},(便乗)")

    elif message.content == ("/flash"):
        return
    
    elif message.content.find("/") != -1:
        if (message.author.bot) or (message.content.find("/") >= 2):
            return
        
        elif message.content == ("/"):
            await message.channel.send("```コマンドが指定されていません。\n/list で利用可能なコマンド一覧を取得します。```")
            return
        
        elif message.content == ("/list"):
            await message.channel.send("```cat:弊鯖内の猫系Botを呼び出すコマンドです。\ndango:特に意味はないです。\nflash:強力な攻撃で汚れたメッセージ履歴を(見た感じ)一掃します\nget:様々な値を取得します。\nhappy:使用が推奨されていないコマンドです。```")
        
        elif message.content == ("/cat"):
            await message.channel.send(f"{message.author.mention},にゃおん(迫真)")
        
        elif message.content == ("/dango"):
            while cnt <= 2:
                if random.randrange(30) == 3:
                    await message.channel.send(":pleading_face:")
                else:
                    await message.channel.send(":thinking:")
                cnt += 1
        
        elif message.content.find("/get") != -1:
            if message.content == ("/get"):
                await message.channel.send("```Error:引数が指定されていません。\n/get list で利用可能な引数一覧を表示します。```")
            
            elif message.content == ("/get point"):
                #Point notice 
                endp = requests.get("https://bonychops.com/experiment/discord-police/api/getGoglerPoint.php") #エンドポイント
                data = json.loads(endp.text) #data関数にjson内の情報をブチコ
                dt_now = datetime.datetime.now() #現在時刻を取得
            
                for member in data["data"].values():
                    # Point警告機能
                    if int(member["point"]) >= 50000:
                        embed = discord.Embed(title = "**DANGER**",description = "Gogler Pointが**5万pt超過、非常に危険です！！**\n**即座に開発を中止し命を守る行動を取ってください**。\n\n" + dt_now.strftime('%Y/%m/%d %H:%M:%S'),color = 0x800080)
                        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/711485944213012502/764523690964287498/pngwing.com.png")

                    elif int(member["point"]) >= 25000:
                        embed = discord.Embed(title = "**WARNING**",description = "Gogler Pointの値が**かなり高く**なっています。\n**限界開発を自粛し、健康時間帯での活動をしてください。**\n\n" + dt_now.strftime('%Y/%m/%d %H:%M:%S'),color = 0xff0000)
                        embed.set_thumbnail(url = "https://i.imgur.com/3wSKpGi.png")

                    elif int(member["point"]) >= 10000:
                        embed = discord.Embed(title = "**CAUTION**",description = "Gogler Pointが少し高いようです。\n健康時間帯でのコミットやタスク終了でGogler Pointを減らすことができます。\n\n" + dt_now.strftime('%Y/%m/%d %H:%M:%S'),color = 0xFFFF00)
                        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/711485944213012502/764526697370222602/pngwing.com_1.png")

                    else:
                        pass
                    
                    embed.set_author(name = "Gogler Point Notice",icon_url = "https://pbs.twimg.com/profile_images/1253698378686320642/ndnIvdlN_400x400.jpg")
                    
                    await message.channel.send(f'{member["name"]}さんは現在**{member["point"]}pt**です。')
                    await message.channel.send(embed=embed) # send embed
        
            elif message.content == ("/get day"):
                await message.channel.send(f"{message.author.mention},(便乗)")
            
            elif message.content == ("/get list"):
                await message.channel.send("```/get day:現在の日付および日時をお知らせします。(この機能いるのか？)\n/get point:各DevelperのGogler Pointを表示します。```")
        
            else :
                await message.channel.send(f"{message.author.mention}\n```Error:Invalid syntax```")
        else :
            await message.channel.send(f"{message.author.mention}\n```Error:Unknown command```")

client.run(token)