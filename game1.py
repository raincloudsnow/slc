from sys import exit

def start():
    print("这里是，暴走英雄坛！")
    print("尊敬的玩家爸爸，欢迎使用本次转生系统。")
    print("为了提高您的游戏体验。系统自动升级到极致体验版.")
    print("系统自动升级中。。。１％")
    print("系统自动升级中。。。30％")
    print("系统自动升级中。。。60％")
    print("系统自动升级中。。。99％")
    print("哎呀，升级失败。。还原至一般体验系统..")
    print("您也可以找我们客户投诉   电话是：18302868075 ，至于卵不卵你，我就不管了。")
    print("现在请你对我们的系统作出评价：")
    
    
    choice = input("> ")
    if choice == "1":
        print("谢谢您的评价.")
        adventure_room()

    elif choice == "2":
        print("你不满意我有锤子个办法？")
        print("是否继续？　是／否.")
        choice = input("> ")
        if choice == "是":
            adventure_room()
        elif choice == "否":
            print("再见!")
            
    else:
        start()


def adventure_room():
    print("现在开始转生. 温馨提示：请保持双手的干净，防止影响主角光环的生成.")
    print("系统为您量身定制了几款豪华出生地，请选择一款......")
    print("1. 中原小镇.")
    print("2. 欧洲古堡.")
    print("3. 美国都市.")

    choice = input("> ")
    if "1" in choice:
        print("选择成功！")
        adventure_room2()
    
    elif "2" in choice:
        print("该地图暂未开放，敬请期待.")
        print("是否重新选择？　是／否。")
        choice = input("> ")
        if choice == "是":
            adventure_room()
        elif choice == "否":
            print("再见! ", end=' ')
    
    elif "3" in choice:
        print("该地图暂未开放，敬请期待.")
        print("是否重新选择？　是／否。")
        choice = input("> ")
        if choice == "是":
            adventure_room()
        elif choice == "否":
            print("再见! ")
    else:
        adventure_room()

def adventure_room2():
    print("已经选好出生地。")
    print("那么你选作男人，还是女人呢？？？")
    print("1. 男.")
    print("2. 女.")
    choice = input("> ")
    if choice == "1":
        adventure_room3()
    elif choice == "2":
        adventure_room3()
    else:
        adventure_room2()

def adventure_room3():
    print("鉴于你选的地图之贫瘠。。你的口味，咳咳！")
    print("本小姐，呸！是本大爷已赠送了你100000金条(这个算是系统内挂吧，咳咳)，任性的花ba！")
    print("你是...")
    print("1. 宛如路人 100金条.")
    print("2. 眉目有神 200金条.")
    print("3. 神采奕奕 300金条.")
    print("4. 普普通通 免费(猜你也不会选).")
    choice = input("> ")
    if choice == "1":
        adventure_room4()
    elif choice == "2":
        adventure_room4()
    elif choice == "3":
        adventure_room4()
    elif choice == "4":
        adventure_room4()
    else:
        adventure_room3()

def adventure_room4():
    print("你的身份？")
    print("1. 平民免费.")
    print("2. 镇长儿子(女儿)300金条.")
    print("3. 小白领50000000金条.")
    print("4. 土豪(这个适合你，哈哈)100000000000000000000金条.")
    choice = input("> ")
    if choice == "1":
        adventure_room5()
    elif choice == "2":
        adventure_room5()
    elif choice == "3":
        print("给我老实点，金条不够你还选！！！")
        adventure_room4()
    elif choice == "4":
        print("给我老实点，金条不够你还选！！！")
        adventure_room4()
    else:
        adventure_room4()

def  adventure_room5():
    print("你现在有了一个良好的出生.")
    print("你出生在了平安镇.")
    print("镇长来为你的出生庆祝.")
    print("你心想:我不是跳楼了吗,我转生了是么,天不让我死啊.既然来到了这里，就好好活下去吧.")
    print("你和父母一起生活着.")
    print("你帮着大人做家务.")
    print("生活无忧无虑.")
    print("直到你十三岁那一年......")
    print("你一觉醒来，发现爹娘不在了，只在桌上发现了一张字条，上面写着:")
    print("我们有我们要去寻找的重要事物，实在没办法了，我们不是故意的。隔壁老婆婆会帮助照顾你的，你虽然人小，但很机(wei)灵(suo)，要好好活着，以后一定有出息，若江湖有缘，我们今生还能相见，88。")
    print("你爹留，看完烧了。")
    print("就这样你在老婆婆的帮助下独自生活了下来.")
    print("在老婆婆慈(can)爱(bao)的关照下,日子艰辛且平淡,平淡到你怀疑人生.")
    print("直到一天.")
    print("一位身披黑色斗篷的神秘人从你背后闪现出来.")
    print("喂!小鬼,他叫住了你,", )
    print("过来让我看看你.")
    print("你：      谁，你谁啊？私闯民宅是犯法的，吓死人也是要偿命的，知道吗？")
    print("神秘人：   这就是他隐居的地方吗，还真是不起眼。来，小鬼，把手伸过来！")
    print("你：      你要干什么！难道。。你再过来我就报警了啊！")
    print("神秘人：   滚！我对你没兴趣，快把手伸过来。")
    print("1. 伸手.")
    print("2. 不伸手.")
    choice = input("> ")
    if choice == "1":
        adventure_room6()
    elif choice == "2":
        print("他给了你一巴掌，然后你委(shun)屈(cong)的把手伸了过去。。。")
        adventure_room7()
    else:
        adventure_room5()

def adventure_room6():
    print("神秘人：   小鬼，你运气来了，习武资质不错，想不想学武功啊？")
    print("你：      你这推销手段还真是新异，不过这个月我已经遇见十个了，没钱，不买！")
    print("神秘人：   不知好歹！我就在门前等半刻钟，不来就算了。")
    print("你：      到底去不去呢？")
    print("1. 去.")
    print("2. 不去.")
    choice = input("> ")
    if choice == "1":
        print("你走出了家门。。。")
        adventure_room8()
    elif choice == "2":
        print("你就一直继续着平淡的生活，也没有再遇见神秘人。。。")
        print("是否重来一次？　是／否。")
        choice = input("> ")
        if choice == "是":
            adventure_room6()
        elif choice == "否":
            print("再见！")
    else:
        adventure_room6()

def adventure_room7():
    print("神秘人：             小鬼，你运气来了，习武资质不错，想不想学武功啊？")
    print("你(捂着火辣辣的脸)：   你这推销手段还真是新异，不过这个月我已经遇见十个了，没钱，不买！")
    print("神秘人：             不知好歹！我就在门前等半刻钟，不来就算了。")
    print("你：                到底去不去呢？")
    print("1. 去.")
    print("2. 不去.")
    choice = input("> ")
    if choice == "1":
        print("你走出了家门。。。")
        adventure_room8()
    elif choice == "2":
        print("你就一直继续着平淡的生活，也没有再遇见神秘人。。。")
        print("是否重来一次？　是／否。")
        choice = input("> ")
        if choice == "是":
            adventure_room6()
        elif choice == "否":
            print("再见！")
    else:
        adventure_room7()

def adventure_room8():
    print("神秘人:   我就知道你会来，其实你不想继续当屌丝对吧？")
    print("你：      恩？连这都看得出来!果然是高人啊。")
    print("神秘人:   废话少说，既然出来了那就开始吧！")
    print("你：      等一下，我身上的压岁钱比隔壁小宝还少，别指望我会给钱！")
    print("神秘人:   你废话怎么这么多！！真想一巴掌拍屎你！")
    print("你：      师傅在上，请受徒儿一拜！")
    print("神秘人:   ..........")
    print("神秘人:   你这么无耻一定能成大器，我不过指点你几招罢了，算不得师傅，看好了！莫眨眼。")
    print("神秘人演示的招式甚是精妙，不知不久时间过去了。。")
    print("神秘人：   刚才那几招你记住了？")
    print("你：      啊？ 额，哦。。恩，记住了。")
    print("你：      原来前辈真是高人，小的有眼不识泰山，能不能直接传给我70年功力啥的？")
    print("神秘人:   你想多了。。。你是习武之(fei)才(chai),拿着这本秘籍，它能辅助你练功。")
    print("你打开秘笈，只觉全身充满了力量！　（系统提示：你获得5000潜能）")
    print("你：      谢师傅。")
    print("突然，远处传来一声尖叫.")
    print("你：      不好，是卖豆腐的小莲姐！我去看看。")
    print("神秘人:   去吧，武学之人应当行侠仗义～～（话音刚落，神秘人已不见了身影。。）")
    print("你跑到豆腐店，只见一伙强盗围住了小莲姐。")
    print("你挺身而出：   呔！光天化日之下干啥勒你们？")
    print("强盗：        哟呵，又来个不怕死的，兄弟们上！")
    print("你:          是时侯展现真正的技术了！")
    print("1. 上去干！(推荐)")
    print("2. 讲道理。。。")
    choice = input("> ")
    if choice == "1":
        print("看我刚学的武功！啊哒！")
        print("1. 寸拳.")
        print("2. 扫堂腿.")
        print("3. 拦腰侧踹")
        print("4. 过肩摔.")
        choice = input("> ")
        if choice == "1":
            print("你这一拳运足了全身的力量，衣服无风自动，轰的一声，你轰飞了６个强盗！！")
            adventure_room9()
        elif choice == "2":
            print("你半蹲下腰，以小腿发力，扭转360度，啪啪啪啪啪啪啪啪！扑通！你打残了８个强盗！！！")
            adventure_room9()
        elif choice == "3":
            print("你首当其冲，拦腰抱住一个强盗，两拳打在胸口，在飞旋180度踹飞强盗,后面一派７个强盗都被打趴下了。")
            adventure_room9()
        elif choice == "4":
            print("你抓住最前面一个壮硕的强盗的肩膀，双脚扣地，以大腿发力，将强盗过肩摔下。嘭的一声，所有强盗被吓住了。")
            adventure_room9()
    elif choice == "2":
        print("你被群欧打死了,结束了你的第二人生.....")
        print("是否选择重新投胎？　是／否。")
        choice = input("> ")
        if choice == "是":
            start()
        elif choice == "否":
            print("再见！")
    else:
        adventure_room8()

def adventure_room9():
    print("强盗：       这。。这小子怎们这么厉害？兄弟们撤！")
    print("强盗灰溜溜的被你打跑了。")
    print("小莲姐：     谢谢你了。")
    print("你：        没事，习武之人应该的．啊哈哈。")
    print("小莲姐：     这是一点心意请收下. (你获得了5块白玉豆腐。１块豆腐＋100饥饿值)")
    print("你两眼发光：  那我就不客气了啊哈哈哈！")
    print("远处传来一声小孩的哭喊：   呜呜，你这么厉害也来帮帮我啊！！")
    print("你：        。。我还是去帮帮小宝把.")
    print("你：        别哭，有什么事就说！")
    print("小宝：       阿娘给我买豆腐的钱被流氓肖绿绿抢去了...")
    print("1. 哪个没出息的连这点钱都要抢？")
    print("2. 你钱被抢了关我屁事！")
    choice = input("> ")
    if choice == "1":
        adventure_room10()
    elif choice == "2":
        print("小宝叫大人来把你打了一顿，打得你鼻青脸肿，只好认命。。。")
        adventure_room10()
    else:
        adventure_room9()

def adventure_room10():
    print("好吧，我去帮你把钱包要回来。。")
    print("你找到了流氓。那么。。")
    print("1. 一言不合冲上去就是干！")
    print("2. 讲讲道理。。")
    choice = input("> ")
    if choice == "1":
        print("还我钱包来！")
        print("1. 寸拳.")
        print("2. 扫堂腿.")
        print("3. 拦腰侧踹")
        print("4. 过肩摔.")
        choice = input("> ")
        if choice == "1":
            print("你这一拳运足了全身的力量，衣服无风自动，轰的一声，你轰飞了流氓。。。。的刀！！")
            print("你被打死了。。")
            print("是否重来一次？　是／否。")
            choice = input("> ")
            if choice == "是":
                adventure_room10()
            elif choice == "否":
                print("再见！")
        elif choice == "2":
            print("你半蹲下腰，以小腿发力，扭转360度，啪！扑通！你打趴了流氓，但他反应迅速，一招咸鱼翻身，操起大刀劈死了你。。！")
            print("是否重来一次？　是／否。")
            choice = input("> ")
            if choice == "是":
                adventure_room10()
            elif choice == "否":
                print("再见！")
        elif choice == "3":
            print("你首当其冲，拦腰抱住流氓，两拳打在胸口，在飞旋180度踹飞流氓,流氓身强力壮,你被反作用力振飞了,他趁机把你揍了一顿。。。")
            print("是否重来一次？　是／否。")
            choice = input("> ")
            if choice == "是":
                adventure_room10()
            elif choice == "否":
                print("再见！")
        elif choice == "4":
            print("你抓住流氓，双脚扣地，以大腿发力，将流氓过肩摔下。嘭的一声，流氓被摔的一脸懵逼,但不久他反应了过来，把你揍了一顿。。")
            print("是否重来一次？　是／否。")
            choice = input("> ")
            if choice == "是":
                adventure_room10()
            elif choice == "否":
                print("再见！")
    elif choice == "2":
        print("你：    你干嘛抢那点钱？要抢就抢大票子啊！")
        print("流氓:   恩。。你说的有道理，兄弟是道上的吧？给你就是了，下次我带你喝酒去啊。")
        print("你：    额，这么简单。。(你获得了一个破旧的钱包)")
        adventure_room11()
    else:
        adventure_room10()

def adventure_room11():
    print("你拿着小宝的钱包回到镇中。")
    print("小宝：哇，这就是我的钱包，谢谢你！")
    print("你：咳咳，感谢就算了，是不是要有小费啊？")
    print("小宝：你这是变相敲诈！呜呜呜。。")
    print("小宝：算了吧，我这里有一个金手镯，是我jian到的，就送你了吧")
    print("你：恩？这上面刻着一个名字，bitch。。。可能是丢了手镯的人把.")
    print("小宝：那你去找失主把")
    print("你：找不到的话。。嘿嘿嘿，那就名正言顺的归我了！")
    print("小宝：不要face.......")
    print("于是你开始寻找失主")
    print("你遇见了一个十分wei　suo的老爷爷，他叫住了你。")
    print("老爷爷:小子！你手上的手镯是我的！我知道你是三好青年，还给我吧。嘿嘿嘿!!")
    print("1. 还.")
    print("2. 不还.")
    choice = input("> ")
    if choice == "1":
        adventure_room12()
    elif choice == "2":
        print("老爷爷打官司，送你上法庭，打了你５０大板，把手镯还给了老爷爷。。")
        adventure_room12()
    else:
        adventure_room11()

def adventure_room12():
    print("你：给你就是了麻，凶啥子麻凶！")
    print("你转身就走了...")
    print("老爷爷:那么急着走干什么？我叫你走了吗！")
    print("你：你到底要干什么！！！")
    print("老爷爷:最近有人在跟踪我，我想请你帮我调查一下。。报酬３两！")
    print("你：我是用钱就能收买的人吗！！")
    print("老爷爷:４两。")
    print("你：呵呵呵，我是不会答应的。")
    print("老爷爷:５两.")
    print("你：。。。。。。")
    print("老爷爷:１０两。")
    print("你：好！你说是谁。")
    print("老爷爷:小兄弟真爽快！就是镇中心拿匕首的那个人.")
    print("你找到了拿着匕首的人")
    print("1. 一言不合冲上去就是干！")
    print("2. 询问他")
    choice = input("> ")
    if choice == "1":
        print("他一匕首把你do死了。。。。。")
        print("是否重来？是／否")
        choice = input("> ")
        if choice == "是":
            adventure_room12()
        elif choice == "否":
            print("再见！")
    elif choice == "2":
        print("你：说！你为什么要跟踪他？")
        print("人：不告诉你！")
        print("你：看来要采用老爷爷的手段了。。。")
        print("你：这是小意思，（你拿出了１０两银子）")
        print("人：好！我告诉你！你说的老爷爷，他知道江湖武林６０年前的黄金宝藏的秘密埋藏地！")
        print("你：!!!!!!....额。。好的谢谢！")
        print("你转身就跑..")
        adventure_room13()
    else:
        adventure_room12()

def adventure_room13():
    print("你：老爷爷！！你是不是知道黄金宝藏的秘密？")
    print("老爷爷:你怎么知道的......哎，告诉你也无防。。")
    print("黄金宝藏..就在镇中北郊的一棵歪脖子树下，绕树转三圈，在按下树上的开关就能发现密宝。。")
    print("你：这么轻易告诉我不会是假的把。。")
    print("老爷爷:哎，就算我拿到了也不会武功阿。。")
    print("你：哦！原来是武林密宝阿.")
    print("1. 去寻宝(推荐)。")
    print("2. .继续询问")
    choice = input("> ")
    if choice == "1":
        print("老爷爷白白！我去寻宝了!")
        adventure_room14()
    elif choice == "2":
        print("你个小鬼！还想干什么！不去寻宝？")
        print("你：好好好，我去我去。。")
        adventure_room14()
    else:
        adventure_room13()

def adventure_room14():
    print("你来到了北郊的歪脖子树下，按照老爷爷的方法，你成功打开了密室！")
    print("你：哦唷！(你看见了许多黄金，还有三件大器物。。)")
    print("1. 直接拿走黄金！")
    print("2. 看看那三件大器物.")
    choice = input("> ")
    if choice == "1":
        print("见识短浅的你拿走了黄金。。过上了土豪的日子，荒废了武学。。。")
    elif choice == "2":
        print("你走近了那三件大器物，一看大吃一惊！")
        print("第一件：传说中的屠龙刀！不过手感怪怪的。")
        print("第二件：传说中武林神学<九阴神功>残卷一（凑齐三章可练得神功）")
        print("第三件：《唐门暗器秘录》上 （这个就不用我说了吧。。。）")
        print("你刚刚看完三件神器，密室由于年分太久，要崩溃了！你决定先拿走一件！")
        print("1. 屠龙刀")
        print("2, 武林神学<九阴神功>残卷一")
        print("3. 《唐门暗器秘录》上")
        choice = input("> ")
        if choice == "1":
            print("你拿着屠龙刀冲出了洞穴")
            adventure_room15()
        elif choice == "2":
            print("你拿着《九阴神功１》冲出了洞穴")
            adventure_room15()
        elif choice == "3":
            print("你拿着《唐门秘录上》冲出了洞穴")
            adventure_room15()
    else:
        adventure_room14()

def adventure_room15():
    print("只听轰的一声密室崩溃了。")
    print("你：呼～～，好险！")
    print("你得到了你想要的，你拿着这件宝物走南闯北，行侠仗义，用你的武学潜能（共有5000）学习武功，帮助他人。")
    print("终于，这个小镇再也没有恶势力出现,你决定去江湖上'迷失的世界'看一看。。。")
    print("你出了小镇，乡亲们为你送行.....")
    print("几个时晨后，你第一次来到了。。迷失的世界！")
    print("这里有7个帮派，少林寺—太极派—无毒教—雪山剑派—血毒教—玉女阁—丐帮")
    print("每个武林豪杰都有一个帮派，你准备加入哪一个？")
    print("1. 少林寺       (武功绝学：少林棍法，轻身之术，玄天内功，玄玉手)")
    print("2. 太极派       (武功绝学：阴阳手法，太极圆润剑法，梯云纵，太极内功)")
    print("3. 五毒教       (武功绝学：五毒暗器，万毒手，五毒幻形，百毒秘术)")
    print("4. 雪山剑派     (武功绝学：雪山天剑，过雪无痕，梅花乱舞，雪花六出)")
    print("5. 血毒教       (武功绝学：血毒手，暗血吞噬，魔幻步伐，王之血龙掌)PS:想当坏人来这里哦")
    print("6. 玉女阁       (武功绝学：女王鞭法，玉女心经，鬼步行，群鞭乱舞)PS:只有女的")
    print("7. 丐帮         (武功绝学：打狗棒法，降龙十八掌，丐术内功，通天一条龙)")
    choice = input("> ")
    if choice == "1":
        print("你成功加入少林寺")
        print("1. 世界那么大，我要去看看。。")
        print("2. 老老实实学武功绝学.")
        choice = input("> ")
        if choice == "1":
            print("你刚刚出去2分钟就遇上了黑风寨的土匪，个个武艺高强，把你打死了。。")
        elif choice == "2":
            print("５年后，你学完了门派中所有武林绝学.")
            print("你从密室中拿出来的宝贝也练的炉火纯青。")
            print("你要去外面看一看。but，你刚刚出去2分钟就遇上了黑风寨的土匪，个个武艺高强.")
            print("但你身怀绝技，直接迎了上去，打败了土匪！")
            print("神秘人感到很欣慰，赠你一件宝物---海神三叉戟！（咳咳！不要在意这是什么，你只用知道这是宝物。。。）")
            print("从此你打败天下无敌手.")
            print("武林中留下了你的英名。。。话说你到底叫什么。。没错！这就是一个没有名字的游戏，啊哈哈。。")


            print("全剧，终。。。。")
    elif choice == "2":
        print("你成功加入太极派")
        print("1. 世界那么大，我要去看看。。")
        print("2. 老老实实学武功绝学.")
        choice = input("> ")
        if choice == "1":
            print("你刚刚出去2分钟就遇上了黑风寨的土匪，个个武艺高强，把你打死了。。")
        elif choice == "2":
            print("５年后，你学完了门派中所有武林绝学.")
            print("你从密室中拿出来的宝贝也练的炉火纯青。")
            print("你要去外面看一看。but，你刚刚出去2分钟就遇上了黑风寨的土匪，个个武艺高强.")
            print("但你身怀绝技，直接迎了上去，打败了土匪！")
            print("神秘人感到很欣慰，赠你一件宝物---海神三叉戟！（咳咳！不要在意这是什么，你只用知道这是宝物。。。）")
            print("从此你打败天下无敌手.")
            print("武林中留下了你的英名。。。话说你到底叫什么。。没错！这就是一个没有名字的游戏，啊哈哈。。")


            print("全剧，终。。。。")
    elif choice == "3":
        print("你成功加入五毒教")
        print("1. 世界那么大，我要去看看。。")
        print("2. 老老实实学武功绝学.")
        choice = input("> ")
        if choice == "1":
            print("你刚刚出去2分钟就遇上了黑风寨的土匪，个个武艺高强，把你打死了。。")
        elif choice == "2":
            print("５年后，你学完了门派中所有武林绝学.")
            print("你从密室中拿出来的宝贝也练的炉火纯青。")
            print("你要去外面看一看。but，你刚刚出去2分钟就遇上了黑风寨的土匪，个个武艺高强.")
            print("但你身怀绝技，直接迎了上去，打败了土匪！")
            print("神秘人感到很欣慰，赠你一件宝物---海神三叉戟！（咳咳！不要在意这是什么，你只用知道这是宝物。。。）")
            print("从此你打败天下无敌手.")
            print("武林中留下了你的英名。。。话说你到底叫什么。。没错！这就是一个没有名字的游戏，啊哈哈。。")


            print("全剧，终。。。。")
    elif choice == "4":
        print("你成功加入雪山剑派")
        print("1. 世界那么大，我要去看看。。")
        print("2. 老老实实学武功绝学.")
        choice = input("> ")
        if choice == "1":
            print("你刚刚出去2分钟就遇上了黑风寨的土匪，个个武艺高强，把你打死了。。")
        elif choice == "2":
            print("５年后，你学完了门派中所有武林绝学.")
            print("你从密室中拿出来的宝贝也练的炉火纯青。")
            print("你要去外面看一看。but，你刚刚出去2分钟就遇上了黑风寨的土匪，个个武艺高强.")
            print("但你身怀绝技，直接迎了上去，打败了土匪！")
            print("神秘人感到很欣慰，赠你一件宝物---海神三叉戟！（咳咳！不要在意这是什么，你只用知道这是宝物。。。）")
            print("从此你打败天下无敌手.")
            print("武林中留下了你的英名。。。话说你到底叫什么。。没错！这就是一个没有名字的游戏，啊哈哈。。")


            print("全剧，终。。。。")
    elif choice == "5":
        print("你成功加入血毒教")
        print("1. 世界那么大，我要去看看。。")
        print("2. 老老实实学武功绝学.")
        choice = input("> ")
        if choice == "1":
            print("你刚刚出去2分钟就遇上了黑风寨的土匪，个个武艺高强，把你打死了。。")
        elif choice == "2":
            print("５年后，你学完了门派中所有武林绝学.")
            print("你从密室中拿出来的宝贝也练的炉火纯青。")
            print("你要去外面看一看。but，你刚刚出去2分钟就遇上了黑风寨的土匪，个个武艺高强.")
            print("但你身怀绝技，直接迎了上去，打败了土匪！")
            print("神秘人感到很欣慰，赠你一件宝物---海神三叉戟！（咳咳！不要在意这是什么，你只用知道这是宝物。。。）")
            print("从此你打败天下无敌手.")
            print("武林中留下了你的英名。。。话说你到底叫什么。。没错！这就是一个没有名字的游戏，啊哈哈。。")


            print("全剧，终。。。。")
    elif choice == "6":
        print("你成功加入玉女阁")
        print("1. 世界那么大，我要去看看。。")
        print("2. 老老实实学武功绝学.")
        choice = input("> ")
        if choice == "1":
            PRINT("你刚刚出去2分钟就遇上了黑风寨的土匪，个个武艺高强，把你打死了。。")
        elif choice == "2":
            print("５年后，你学完了门派中所有武林绝学.")
            print("你从密室中拿出来的宝贝也练的炉火纯青。")
            print("你要去外面看一看。but，你刚刚出去2分钟就遇上了黑风寨的土匪，个个武艺高强.")
            print("但你身怀绝技，直接迎了上去，打败了土匪！")
            print("神秘人感到很欣慰，赠你一件宝物---海神三叉戟！（咳咳！不要在意这是什么，你只用知道这是宝物。。。）")
            print("从此你打败天下无敌手.")
            print("武林中留下了你的英名。。。话说你到底叫什么。。没错！这就是一个没有名字的游戏，啊哈哈。。")


            print("全剧，终。。。。")
    elif choice == "7":
        print("你成功加入丐帮")
        print("1. 世界那么大，我要去看看。。")
        print("2. 老老实实学武功绝学.")
        choice = input("> ")
        if choice == "1":
            PRINT("你刚刚出去2分钟就遇上了黑风寨的土匪，个个武艺高强，把你打死了。。")
        elif choice == "2":
            print("５年后，你学完了门派中所有武林绝学.")
            print("你从密室中拿出来的宝贝也练的炉火纯青。")
            print("你要去外面看一看。but，你刚刚出去2分钟就遇上了黑风寨的土匪，个个武艺高强.")
            print("但你身怀绝技，直接迎了上去，打败了土匪！")
            print("神秘人感到很欣慰，赠你一件宝物---海神三叉戟！（咳咳！不要在意这是什么，你只用知道这是宝物。。。）")
            print("从此你打败天下无敌手.")
            print("武林中留下了你的英名。。。话说你到底叫什么。。没错！这就是一个没有名字的游戏，啊哈哈。。")


            print("全剧，终。。。。")
    else:
        adventure_room15()

start()