import discord
from datetime import datetime

client = discord.Client()

now = datetime.now()


@client.event
async def on_ready():
    game = discord.Game("!설명")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):

    print("실행 성공")

    if message.content.startswith("!블메"):
        await message.channel.send("버러지")

    if message.content.startswith("!실행시간"):
        await message.channel.send(now)

    if message.content.startswith("!Jesse Lingard"):
        await message.channel.send("축신 황가드")

    if message.content.startswith("!Steven Gerrard"):
        await message.channel.send("자! 끊어내고 올라갑니다\n"
                                   "뎀바바! 골키퍼와 일대일 기회 뎀바바!\n"
                                   "뎀바바! 골!!!\n"
                                   "첼시가 선제골을 뽑아냅니다\n"
                                   "자! 전반전내내 약간 끌려갔었는데 제라드의 치명적인 실수입니다\n"
                                   "결정적인 실책을 스티븐 제라드가 하나요\n"
                                   "자 리버풀의 심장 제라드가 전반전 막판에 집중력을 잃었습니다\n"
                                   "안필드에서 선제골을 뽑아낸건 무리뉴의 첼시 뎀바바입니다\n"
                                   "자 그리고 실수한건 안필드의 심장이자 주인공인 제라든데요\n"
                                   "자 여기서 공을 흘리고 넘어지고 말았습니다\n"
                                   "아 정말 치명적인 실책입니다.\n"
                                   "키퍼와 일대일 찬스를 뎀바바가 놓치지 않았습니다.\n"
                                   "파리 셍제르맹, 스완지시티와 경기에서 연속해서 결승골을 터트렸던 뎀바바인데요.\n"
                                   "자 이번 기회를 놓치지 않으면서 전반전 자 하프타임을 하프타임에 돌입할때 앞선 상황에서 돌입할수 있겠습니다.\n"
                                   "사실 올시즌 리버풀이 우승을 한다면 일등공신이 수아레즈도 있습니다만\n"
                                   "연승의 시발점 뒷라인 플레이메이커부터 아주 역할수행을 잘한 제라드였거든요\n"
                                   "근데 이거 마지막 마무리를 잘해야 하는데 이러한 실책이 제라드에게 나왔어요")

    if message.content.startswith("!설명"):
        await message.channel.send("FM20.4 순정 로스터 기준으로 히든과 포텐을 검색 해줍니다.\n"
                                   "현재는 -포텐만 지원하며 사용은 !영어 선수명을 치면 됩니다.\n"
                                   "히든이 0이면 랜덤입니다.\n"
                                   "- 포텐 목록을 보고 싶으시면 !9.5, !9 이런식으로 치시면 목록이 나옵니다.\n"
                                   "여건이 된다면 24세 이하 고정 포텐 160이상도 지원할 예정입니다.\n"
                                   "선수 이름은 파스칼 표기법으로 시작 문자를 대문자로 시작하셔야 합니다.")

    # FM 20.4 기준 -10포텐은 없음.
    # FM 20.4 기준 -9.5포텐
    if message.content.startswith("!9.5"):
        await message.channel.send("Vinicius Junior, Matthijs de Ligt, Eduardo Camavinga,\n"
                                   "Gianluigi Donnarumma, Rodrygo, Ansu Fati, Pedri")

    # FM 20.4 기준 -9포텐
    elif message.content.startswith("!9"):
        await message.channel.send("Declan Rice, Callum Hudson-Odoi, Myron Boadu, Nicolò Zaniolo, Calvin Stengs,\n"
                                   "Justin Kluivert, William Saliba, Dominik Szoboszlai, Sandro Tonali,\n"
                                   "Samuel Chukwueze, Dejan Kulusevski, Mason Greenwood, Ryan Gravenberch,\n"
                                   "Mohammed Ihattaren, Hamed Junior Traore, Joshua Zirkzee, Fabio Silva,\n"
                                   "Marco Kana, Naci Unuvar, Sergio Gomez, Troy Parrott, Yari Verschaeren,\n"
                                   "Emanuel Vignato, Jonathan David, Thiago Almada, Reinier, Sebastiano Esposito,\n"
                                   "Antony, Karim Adeyemi, Diego Laínez, Ilaix Moriba, Maarten Vandevoordt,\n"
                                   "Hannibal Mejbri, Rayan Cherki, Jude Bellingham")

    ##########

    if message.content.startswith("!Matthijs de Ligt"):
        await message.channel.send("-9.5(160-190) 포텐, 적응력 7, 포부 13, 논쟁성 3, 의리 12, 압박감 대처 14, 프로의식 16\n"
                                   "스포츠맨십 13, 참을성 10, 더티 플레이 8, 꾸준함 13, 중요경기 12, 부상빈도 7, 다재다능 12")

    if message.content.startswith("!Eduardo Camavinga"):
        await message.channel.send("-9.5(160-190) 포텐, 적응력 0, 포부 13, 논쟁성 5, 의리 14, 압박감 대처 0, 프로의식 15\n"
                                   "스포츠맨십 0, 참을성 0, 더티 플레이 6, 꾸준함 12, 중요경기 15, 부상빈도 0, 다재다능 0")

    if message.content.startswith("!Gianluigi Donnarumma"):
        await message.channel.send("-9.5(160-190) 포텐, 적응력 0, 포부 16, 논쟁성 5, 의리 12, 압박감 대처 10, 프로의식 11\n"
                                   "스포츠맨십 15, 참을성 14, 더티 플레이 7, 꾸준함 15, 중요경기 15, 부상빈도 4, 다재다능 1")

    if message.content.startswith("!Rodrygo"):
        await message.channel.send("-9.5(160-190) 포텐, 적응력 0, 포부 13, 논쟁성 5, 의리 14, 압박감 대처 13, 프로의식 15\n"
                                   "스포츠맨십 15, 참을성 15, 더티 플레이 7, 꾸준함 13, 중요경기 12, 부상빈도 9, 다재다능 11")

    if message.content.startswith("!Ansu Fati"):
        await message.channel.send("-9.5(160-190) 포텐, 적응력 15, 포부 14, 논쟁성 5, 의리 14, 압박감 대처 15, 프로의식 14\n"
                                   "스포츠맨십 13, 참을성 15, 더티 플레이 5, 꾸준함 12, 중요경기 15, 부상빈도 5, 다재다능 15")

    if message.content.startswith("!Pedri"):
        await message.channel.send("-9.5(160-190) 포텐, 적응력 12, 포부 14, 논쟁성 5, 의리 12, 압박감 대처 13, 프로의식 13\n"
                                   "스포츠맨십 14, 참을성 14, 더티 플레이 5, 꾸준함 12, 중요경기 15, 부상빈도 5, 다재다능 15")

    if message.content.startswith("!Vinicius Junior"):
        await message.channel.send("-9.5(160-190) 포텐, 적응력 12, 포부 15, 논쟁성 8, 의리 12, 압박감 대처 14, 프로의식 12\n"
                                   "스포츠맨십 10, 참을성 10, 더티 플레이 8, 꾸준함 10, 중요경기 8, 부상빈도 5, 10")

    ############

    if message.content.startswith("!Declan Rice"):
        await message.channel.send("-9(150-180) 포텐, 적응력 12, 포부 16, 논쟁성 5, 의리 15, 압박감 대처 14, 프로의식 15\n"
                                   "스포츠맨십 16, 참을성 14, 더티 플레이 12, 꾸준함 14, 중요경기 13, 부상빈도 6, 다재다능 16")

    if message.content.startswith("!Callum Hudson-Odoi"):
        await message.channel.send("-9(150-180) 포텐, 적응력 0, 포부 18, 논쟁성 7, 의리 0, 압박감 대처 15, 프로의식 15\n"
                                   "스포츠맨십 16, 참을성 14, 더티 플레이 0, 꾸준함 14, 중요경기 13, 부상빈도 0, 다재다능 0")

    if message.content.startswith("!Myron Boadu"):
        await message.channel.send("-9(150-180) 포텐, 적응력 0, 포부 13, 논쟁성 5, 의리 12, 압박감 대처 13, 프로의식 12\n"
                                   "스포츠맨십 14, 참을성 12, 더티 플레이 4, 꾸준함 10, 중요경기 12, 부상빈도 12, 다재다능 12")

    if message.content.startswith("!Nicolò Zaniolo"):
        await message.channel.send("-9(150-180) 포텐, 적응력 13, 포부 17, 논쟁성 15, 의리 12, 압박감 대처 16, 프로의식 9\n"
                                   "스포츠맨십 10, 참을성 10, 더티 플레이 14, 꾸준함 12, 중요경기 14, 부상빈도 5, 다재다능 15")

    if message.content.startswith("!Calvin Stengs"):
        await message.channel.send("-9(150-180) 포텐, 적응력 0, 포부 0, 논쟁성 0, 의리 0, 압박감 대처 0, 프로의식 0\n"
                                   "스포츠맨십 0, 참을성 0, 더티 플레이 3, 꾸준함 8, 중요경기 13, 부상빈도 0, 다재다능 13")

    if message.content.startswith("!Justin Kluivert"):
        await message.channel.send("-9(150-180) 포텐, 적응력 13, 포부 16, 논쟁성 13, 의리 9, 압박감 대처 13, 프로의식 14\n"
                                   "스포츠맨십 12, 참을성 12, 더티 플레이 12, 꾸준함 11, 중요경기 12, 부상빈도 4, 다재다능 0")

    if message.content.startswith("!William Saliba"):
        await message.channel.send("-9(150-180) 포텐, 적응력 0, 포부 15, 논쟁성 6, 의리 0, 압박감 대처 14, 프로의식 14\n"
                                   "스포츠맨십 0, 참을성 0, 더티 플레이 0, 꾸준함 12, 중요경기 0, 부상빈도 8, 다재다능 0 ")

    if message.content.startswith("!Dominik Szoboszlai"):
        await message.channel.send("-9(150-180) 포텐, 적응력 12, 포부 14, 논쟁성 8, 의리 12, 압박감 대처 13, 프로의식 13\n"
                                   "스포츠맨십 13, 참을성 12, 더티 플레이 5, 꾸준함 10, 중요경기 9, 부상빈도 7, 다재다능 9")

    if message.content.startswith("!Sandro Tonali"):
        await message.channel.send("-9(150-180) 포텐, 적응력 0, 포부 17, 논쟁성 3, 의리 10, 압박감 대처 18, 프로의식 18\n"
                                   "스포츠맨십 15, 참을성 19, 더티 플레이 13, 꾸준함 16, 중요경기 14, 부상빈도 2, 다재다능 12")

    if message.content.startswith("!Samuel Chukwueze"):
        await message.channel.send("-9(150-180) 포텐, 적응력 0, 포부 14, 논쟁성 0, 의리 0, 압박감 대처 14, 프로의식 0\n"
                                   "스포츠맨십 0, 참을성 0, 더티 플레이 5, 꾸준함 11, 중요경기 0, 부상빈도 6, 다재다능 0")

    if message.content.startswith("!Dejan Kulusevski"):
        await message.channel.send("-9(150-180) 포텐, 적응력 16, 포부 17, 논쟁성 10, 의리 10, 압박감 대처 15, 프로의식 14\n"
                                   "스포츠맨십 12, 참을성 10, 더티 플레이 11, 꾸준함 15, 중요경기 13, 부상빈도 6, 다재다능 14")

    if message.content.startswith("!Mason Greenwood"):
        await message.channel.send("-9(150-180) 포텐, 적응력 0, 포부 15, 논쟁성 5, 의리 0, 압박감 대처 18, 프로의식 15\n"
                                   "스포츠맨십 12, 참을성 16, 더티 플레이 4, 꾸준함 14, 중요경기 0, 부상빈도 4, 다재다능 10")

    if message.content.startswith("!Ryan Gravenberch"):
        await message.channel.send("-9(150-180) 포텐, 적응력 15, 포부 16, 논쟁성 2, 의리 13, 압박감 대처 15, 프로의식 11\n"
                                   "스포츠맨십 12, 참을성 10, 더티 플레이 4, 꾸준함 12, 중요경기 0, 부상빈도 0, 다재다능 9")

    if message.content.startswith("!Mohammed Ihattaren"):
        await message.channel.send("-9(150-180) 포텐, 적응력 0, 포부 16, 논쟁성 10, 의리 17, 압박감 대처 13, 프로의식 12\n"
                                   "스포츠맨십 14, 참을성 12, 더티 플레이 0, 꾸준함 0, 중요경기 0, 부상빈도 0, 다재다능 0 ")

    if message.content.startswith("!Hamed Junior Traore"):
        await message.channel.send("-9(150-180) 포텐, 적응력 16, 포부 17, 논쟁성 10, 의리 10, 압박감 대처 15, 프로의식 14\n"
                                   "스포츠맨십 12, 참을성 10, 더티 플레이 11, 꾸준함 15, 중요경기 13, 부상빈도 5, 다재다능 14")

    if message.content.startswith("!Joshua Zirkzee"):
        await message.channel.send("-9(150-180) 포텐, 적응력 14, 포부 18, 논쟁성 13, 의리 6, 압박감 대처 16, 프로의식 12\n"
                                   "스포츠맨십 8, 참을성 8, 더티 플레이 8, 꾸준함 12, 중요경기 16, 부상빈도 7, 다재다능 5")

    if message.content.startswith("!Fabio Silva"):
        await message.channel.send("-9(150-180) 포텐, 적응력 0, 포부 15, 논쟁성 8, 의리 8, 압박감 대처 17, 프로의식 16\n"
                                   "스포츠맨십 12, 참을성 10, 더티 플레이 5, 꾸준함 15, 중요경기 13, 부상빈도 8, 다재다능 12")

    if message.content.startswith("!Marco Kana"):
        await message.channel.send("-9(150-180) 포텐, 적응력 0, 포부 0, 논쟁성 0, 의리 0, 압박감 대처 0, 프로의식 0\n"
                                   "스포츠맨십 0, 참을성 0, 더티 플레이 0, 꾸준함 12, 중요경기 0, 부상빈도 0, 다재다능 0")

    if message.content.startswith("!Naci Unuvar"):
        await message.channel.send("-9(150-180) 포텐, 적응력 0, 포부 0, 논쟁성 0, 의리 0, 압박감 대처 0, 프로의식 0\n"
                                   "스포츠맨십 0, 참을성 0, 더티 플레이 0, 꾸준함 10, 중요경기 13, 부상빈도 5, 다재다능 6")

    if message.content.startswith("!Sergio Gomez"):
        await message.channel.send("-9(150-180) 포텐, 적응력 11, 포부 17, 논쟁성 8, 의리 7, 압박감 대처 14, 프로의식 13\n"
                                   "스포츠맨십 10, 참을성 12, 더티 플레이 8, 꾸준함 11, 중요경기 15, 부상빈도 6, 다재다능 15")

    if message.content.startswith("!Troy Parrott"):
        await message.channel.send("-9(150-180) 포텐, 적응력 0, 포부 0, 논쟁성 0, 의리 0, 압박감 대처 0, 프로의식 0\n"
                                   "스포츠맨십 0, 참을성 0, 더티 플레이 0, 꾸준함 0, 중요경기 0, 부상빈도 0, 다재다능 0")

    if message.content.startswith("!Yari Verschaeren"):
        await message.channel.send("-9(150-180) 포텐, 적응력 14, 포부 14, 논쟁성 0, 의리 12, 압박감 대처 14, 프로의식 14\n"
                                   "스포츠맨십 0, 참을성 0, 더티 플레이 0, 꾸준함 12, 중요경기 0, 부상빈도 0, 다재다능 0")

    if message.content.startswith("!Emanuel Vignato"):
        await message.channel.send("-9(150-180) 포텐, 적응력 0, 포부 14, 논쟁성 5, 의리 13, 압박감 대처 13, 프로의식 15\n"
                                   "스포츠맨십 15, 참을성 14, 더티 플레이 3, 꾸준함 13, 중요경기 13, 부상빈도 3, 다재다능 13")

    if message.content.startswith("!Jonathan David"):
        await message.channel.send("-9(150-180) 포텐, 적응력 11, 포부 14, 논쟁성 0, 의리 0, 압박감 대처 0, 프로의식 11\n"
                                   "스포츠맨십 0, 참을성 0, 더티 플레이 0, 꾸준함 12, 중요경기 0, 부상빈도 0, 다재다능 0")

    if message.content.startswith("!Thiago Almada"):
        await message.channel.send("-9(150-180) 포텐, 적응력 0, 포부 15, 논쟁성 5, 의리 13, 압박감 대처 13, 프로의식 14\n"
                                   "스포츠맨십 14, 참을성 7, 더티 플레이 5, 꾸준함 10, 중요경기 12, 부상빈도 5, 다재다능 12")

    if message.content.startswith("!Reinier"):
        await message.channel.send("-9(150-180) 포텐, 적응력 0, 포부 0, 논쟁성 0, 의리 0, 압박감 대처 0, 프로의식 0\n"
                                   "스포츠맨십 0, 참을성 0, 더티 플레이 0, 꾸준함 0, 중요경기 0, 부상빈도 0, 다재다능 0")

    if message.content.startswith("!Sebastiano Esposito"):
        await message.channel.send("-9(150-180) 포텐, 적응력 12, 포부 16, 논쟁성 8, 의리 13, 압박감 대처 14, 프로의식 16\n"
                                   "스포츠맨십 13, 참을성 10, 더티 플레이 7, 꾸준함 14, 중요경기 13, 부상빈도 5, 다재다능 13")

    if message.content.startswith("!Antony"):
        await message.channel.send("-9(150-180) 포텐, 적응력 0, 포부 15, 논쟁성 8, 의리 12, 압박감 대처 13, 프로의식 12\n"
                                   "스포츠맨십 10, 참을성 12, 더티 플레이 8, 꾸준함 13, 중요경기 10, 부상빈도 0, 다재다능 0")

    if message.content.startswith("!Karim Adeyemi"):
        await message.channel.send("-9(150-180) 포텐, 적응력 12, 포부 18, 논쟁성 7, 의리 10, 압박감 대처 13, 프로의식 15\n"
                                   "스포츠맨십 12, 참을성 13, 더티 플레이 0, 꾸준함 9, 중요경기 0, 부상빈도 0, 다재다능 0")

    if message.content.startswith("!Diego Laínez"):
        await message.channel.send("-9(150-180) 포텐, 적응력 13, 포부 14, 논쟁성 5, 의리 11, 압박감 대처 14, 프로의식 13\n"
                                   "스포츠맨십 12, 참을성 14, 더티 플레이 6, 꾸준함 11, 중요경기 13, 부상빈도 0, 다재다능 14")

    if message.content.startswith("!Ilaix Moriba"):
        await message.channel.send("-9(150-180) 포텐, 적응력 10, 포부 15, 논쟁성 10, 의리 14, 압박감 대처 15, 프로의식 15\n"
                                   "스포츠맨십 14, 참을성 10, 더티 플레이 6, 꾸준함 12, 중요경기 15, 부상빈도 8, 다재다능 12")

    if message.content.startswith("!Maarten Vandevoordt"):
        await message.channel.send("-9(150-180) 포텐, 적응력 0, 포부 0, 논쟁성 12, 의리 0, 압박감 대처 0, 프로의식 0\n"
                                   "스포츠맨십 0, 참을성 0, 더티 플레이 0, 꾸준함 10, 중요경기 0, 부상빈도 0, 다재다능 0")

    if message.content.startswith("!Hannibal Mejbri"):
        await message.channel.send("-9(150-180) 포텐, 적응력 0, 포부 18, 논쟁성 10, 의리 7, 압박감 대처 13, 프로의식 14\n"
                                   "스포츠맨십 8, 참을성 10, 더티 플레이 14, 꾸준함 11, 중요경기 12, 부상빈도 7, 다재다능 10")

    if message.content.startswith("!Rayan Cherki"):
        await message.channel.send("-9(150-180) 포텐, 적응력 0, 포부 14, 논쟁성 0, 의리 14, 압박감 대처 0, 프로의식 0\n"
                                   "스포츠맨십 0, 참을성 0, 더티 플레이 6, 꾸준함 0, 중요경기 0, 부상빈도 7, 다재다능 16")

    if message.content.startswith("!Jude Bellingham"):
        await message.channel.send("-9(150-180) 포텐, 적응력 10, 포부 15, 논쟁성 5, 의리 16, 압박감 대처 15, 프로의식 18\n"
                                   "스포츠맨십 15, 참을성 14, 더티 플레이 6, 꾸준함 12, 중요경기 10, 부상빈도 5, 다재다능 10")
    ######################

    # FM20.4 데이터베이스 기준 -8.5 포텐
    if message.content.startswith("!Martin Odegaard"):
        await message.channel.send("-8.5(140-170) 포텐, 적응력 7, 포부 16, 논쟁성 6, 의리 12, 압박감 대처 13, 프로의식 18\n"
                                   "스포츠맨십 12, 참을성 8, 더티 플레이 4, 꾸준함 3, 중요경기 12, 부상빈도 4")

    if message.content.startswith("!Ezequiel Barco"):
        await message.channel.send("-8.5(140-170) 포텐, 적응력 9, 포부 16, 논쟁성 14, 의리 12, 압박감 대처 5, 프로의식 8\n"
                                   "스포츠맨십 13, 참을성 10, 더티 플레이 8, 꾸준함 10, 중요경기 14, 부상빈도 9")

    if message.content.startswith("!Mason Mount"):
        await message.channel.send("-8.5(140-170) 포텐, 적응력 16, 포부 18, 논쟁성 6, 의리 0, 압박감 대처 14, 프로의식 16\n"
                                   "스포츠맨십 16, 참을성 17, 더티 플레이 6, 꾸준함 12, 중요경기 14, 부상빈도 8")

    if message.content.startswith("!Moussa Diaby"):
        await message.channel.send("-8.5(140-170) 포텐, 적응력 8, 포부 15, 논쟁성 1, 의리 15, 압박감 대처 10, 프로의식 15\n"
                                   "스포츠맨십 14, 참을성 9, 더티 플레이 4, 꾸준함 14, 중요경기 13, 부상빈도 6")

    if message.content.startswith("!Donyell Malen"):
        await message.channel.send("-8.5(140-170) 포텐, 적응력 12, 포부 11, 논쟁성 7, 의리 9, 압박감 대처 11, 프로의식 12\n"
                                   "스포츠맨십 11, 참을성 12, 더티 플레이 0, 꾸준함 12, 중요경기 11, 부상빈도 10")

    if message.content.startswith("!Reece James"):
        await message.channel.send("-8.5(140-170) 포텐, 적응력 0, 포부 17, 논쟁성 4, 의리 0, 압박감 대처 16, 프로의식 18\n"
                                   "스포츠맨십 15, 참을성 12, 더티 플레이 4, 꾸준함 16, 중요경기 12, 부상빈도 5")

    if message.content.startswith("!Ryan Sessegnon"):
        await message.channel.send("-8.5(140-170) 포텐, 적응력 0, 포부 14, 논쟁성 8, 의리 14, 압박감 대처 13, 프로의식 12\n"
                                   "스포츠맨십 10, 참을성 15, 더티 플레이 4, 꾸준함 12, 중요경기 13, 부상빈도 2")

    if message.content.startswith("!Paulinho"):
        await message.channel.send("-8.5(140-170) 포텐, 적응력 8, 포부 17, 논쟁성 12, 의리 8, 압박감 대처 15, 프로의식 11\n"
                                   "스포츠맨십 7, 참을성 11, 더티 플레이 8, 꾸준함 10, 중요경기 16, 부상빈도 6")

    if message.content.startswith("!Karamoko Dembele"):
        await message.channel.send("-8.5(140-170) 포텐, 적응력 7, 포부 16, 논쟁성 6, 의리 12, 압박감 대처 13, 프로의식 18\n"
                                   "스포츠맨십 12, 참을성 8, 더티 플레이 4, 꾸준함 3, 중요경기 12, 부상빈도 4")

    if message.content.startswith("!Martin Odegaard"):
        await message.channel.send("-8.5(140-170) 포텐, 적응력 20, 포부 15, 논쟁성 1, 의리 14, 압박감 대처 0, 프로의식 0\n"
                                   "스포츠맨십 0, 참을성 0, 더티 플레이 1, 꾸준함 9, 중요경기 0, 부상빈도 1")

    if message.content.startswith("!Martin Odegaard"):
        await message.channel.send("-8.5(140-170) 포텐, 적응력 7, 포부 16, 논쟁성 6, 의리 12, 압박감 대처 13, 프로의식 18\n"
                                   "스포츠맨십 12, 참을성 8, 더티 플레이 4, 꾸준함 3, 중요경기 12, 부상빈도 4")

    if message.content.startswith("!Martin Odegaard"):
        await message.channel.send("-8.5(140-170) 포텐, 적응력 7, 포부 16, 논쟁성 6, 의리 12, 압박감 대처 13, 프로의식 18\n"
                                   "스포츠맨십 12, 참을성 8, 더티 플레이 4, 꾸준함 3, 중요경기 12, 부상빈도 4")

    if message.content.startswith("!Martin Odegaard"):
        await message.channel.send("-8.5(140-170) 포텐, 적응력 7, 포부 16, 논쟁성 6, 의리 12, 압박감 대처 13, 프로의식 18\n"
                                   "스포츠맨십 12, 참을성 8, 더티 플레이 4, 꾸준함 3, 중요경기 12, 부상빈도 4")

    if message.content.startswith("!Martin Odegaard"):
        await message.channel.send("-8.5(140-170) 포텐, 적응력 7, 포부 16, 논쟁성 6, 의리 12, 압박감 대처 13, 프로의식 18\n"
                                   "스포츠맨십 12, 참을성 8, 더티 플레이 4, 꾸준함 3, 중요경기 12, 부상빈도 4")

    if message.content.startswith("!Martin Odegaard"):
        await message.channel.send("-8.5(140-170) 포텐, 적응력 7, 포부 16, 논쟁성 6, 의리 12, 압박감 대처 13, 프로의식 18\n"
                                   "스포츠맨십 12, 참을성 8, 더티 플레이 4, 꾸준함 3, 중요경기 12, 부상빈도 4")

    if message.content.startswith("!Martin Odegaard"):
        await message.channel.send("-8.5(140-170) 포텐, 적응력 7, 포부 16, 논쟁성 6, 의리 12, 압박감 대처 13, 프로의식 18\n"
                                   "스포츠맨십 12, 참을성 8, 더티 플레이 4, 꾸준함 3, 중요경기 12, 부상빈도 4")

    if message.content.startswith("!Martin Odegaard"):
        await message.channel.send("-8.5(140-170) 포텐, 적응력 7, 포부 16, 논쟁성 6, 의리 12, 압박감 대처 13, 프로의식 18\n"
                                   "스포츠맨십 12, 참을성 8, 더티 플레이 4, 꾸준함 3, 중요경기 12, 부상빈도 4")

    if message.content.startswith("!Martin Odegaard"):
        await message.channel.send("-8.5(140-170) 포텐, 적응력 7, 포부 16, 논쟁성 6, 의리 12, 압박감 대처 13, 프로의식 18\n"
                                   "스포츠맨십 12, 참을성 8, 더티 플레이 4, 꾸준함 3, 중요경기 12, 부상빈도 4")

    if message.content.startswith("!Martin Odegaard"):
        await message.channel.send("-8.5(140-170) 포텐, 적응력 7, 포부 16, 논쟁성 6, 의리 12, 압박감 대처 13, 프로의식 18\n"
                                   "스포츠맨십 12, 참을성 8, 더티 플레이 4, 꾸준함 3, 중요경기 12, 부상빈도 4")

    if message.content.startswith("!Martin Odegaard"):
        await message.channel.send("-8.5(140-170) 포텐, 적응력 7, 포부 16, 논쟁성 6, 의리 12, 압박감 대처 13, 프로의식 18\n"
                                   "스포츠맨십 12, 참을성 8, 더티 플레이 4, 꾸준함 3, 중요경기 12, 부상빈도 4")

client.run("Njk5NTYwNjQyMjg1NDA0MjAy.XpWKuQ.lqJUR1w9b4HUQ6il18k21uXetPQ")
# 699497966934818917
