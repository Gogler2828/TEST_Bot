import discord
import random
import requests
import json

with open ("token/main_token.txt") as tkn:
    TOKEN = tkn.read() #トークンを文字列として読み込み

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
            await message.channel.send(f"{message.author.mention}")
            await message.channel.send(":thinking:")
        elif message.content.find("NG") != -1:
            if (message.content.find("ING") != -1) or (message.content.find("NGO") != -1):
                return
            elif message.content == ("NG"):
                await message.delete()
            await message.channel.send(f"{message.author.mention}")
            await message.channel.send(":ng:")
        elif message.content.find("sexy") != -1:
                emoji = client.get_emoji(751817150834016297)
                await message.add_reaction(emoji) # :pornhub:リアクションを追加
        elif message.content == ("/happy"):
                await message.channel.send(f"{message.author.mention},(便乗)")
        elif message.content.find("/") != -1:
            if message.author.bot:
                return
            
            elif message.content == ("/"):
                await message.channel.send("```コマンドが指定されていません。\n/list で利用可能なコマンド一覧を取得します。```")
                return
            
            elif message.content == ("/list"):
                await message.channel.send("```happy:使うと幸せになれるコマンドです。 \ncat:猫の鳴き声であなたを癒やします。\ndango:特に意味はないです。\nget:様々な値を取得します。```")

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
                
                    for member in data["data"].values():
                        await message.channel.send(f'```{member["name"]}は現在{member["point"]}ptです。```')
                        # Point警告機能
                        if int(member["point"]) >= 50000:
                            await message.channel.send("**DANGER**\n" + f'{member["name"]}さん、Gogler Pointの値が**異常**です!!高すぎます!!')
                        elif int(member["point"]) >= 10000:
                            await message.channel.send("**WARNING**\n" + f'{member["name"]}さん、Gogler Pointが**かなり**高いです!!')
                        elif int(member["point"]) >= 5000:
                            await message.channel.send("**CAUTION**\n" + f'{member["name"]}さん、Gogler Pointが**高くなってきています**!!')
                        elif int(member["point"]) >= 1000:
                            await message.channel.send(f'{member["name"]}さん、Gogler Pointが**少し**高いようです。')
            
                elif message.content == ("/get day"):
                    await message.channel.send(f"{message.author.mention},(便乗)")

                elif message.content == ("/get list"):
                    await message.channel.send("```/get day:現在の日付および日時をお知らせします。(この機能いるのか？)\n/get point:各DevelperのGogler Pointを表示します。```")
            
                else :
                    await message.channel.send("```Invalid syntax```")
            else :
                await message.channel.send("```Unknown command```")
    
    client.run(TOKEN)