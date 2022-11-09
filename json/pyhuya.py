#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..') 
from base.spider import Spider
import json

class Spider(Spider):
	def getName(self):
		return "虎牙"
	def init(self,extend=""):
		pass
	def isVideoFormat(self,url):
		pass
	def manualVideoCheck(self):
		pass
	def homeContent(self,filter):
		result = {}
		cateManual = {
			"一起看": "一起看",
			"三国杀": "三国杀",
			"网游竞技": "网游竞技",
"英雄联盟": "英雄联盟",
"王者荣耀": "王者荣耀",
"英雄联盟电竞经理": "英雄联盟电竞经理",
"一起看": "一起看",
"星秀": "星秀",
"暗黑破坏神：不朽": "暗黑破坏神：不朽",
"暗区突围": "暗区突围",
"生死狙击2": "生死狙击2",
"户外": "户外",
"金铲铲之战": "金铲铲之战",
"和平精英": "和平精英",
"英雄联盟手游": "英雄联盟手游",
"天天吃鸡": "天天吃鸡",
"lol云顶之弈": "lol云顶之弈",
"剑侠世界3": "剑侠世界3",
"不良人3": "不良人3",
"二次元": "二次元",
"穿越火线": "穿越火线",
"主机游戏": "主机游戏",
"美食": "美食",
"综合手游": "综合手游",
"暴雪专区": "暴雪专区",
"颜值": "颜值",
"CF手游": "CF手游",
"交友": "交友",
"地下城与勇士": "地下城与勇士",
"新游广场": "新游广场",
"体育": "体育",
"棋牌桌游": "棋牌桌游",
"我的世界": "我的世界",
"炉石传说": "炉石传说",
"魔兽世界": "魔兽世界",
"QQ飞车手游": "QQ飞车手游",
"DOTA2": "DOTA2",
"方舟": "方舟",
"跑跑卡丁车手游": "跑跑卡丁车手游",
"火影忍者手游": "火影忍者手游",
"球球大作战": "球球大作战",
"CS:GO": "CS:GO",
"DOTA1": "DOTA1",
"QQ飞车": "QQ飞车",
"问道": "问道",
"魔兽争霸3": "魔兽争霸3",
"逆战": "逆战",
"梦三国": "梦三国",
"三国杀": "三国杀",
"网游竞技": "网游竞技",
"手游休闲": "手游休闲",
"娱乐天地": "娱乐天地",
"放映厅": "放映厅",
"单机热游": "单机热游",
"组队": "组队",
"二次元手游": "二次元手游",
"吃喝玩乐": "吃喝玩乐",
"原神": "原神",
"MMORPG": "MMORPG",
"互动点播": "互动点播",
"动作游戏": "动作游戏",
"永劫无间": "永劫无间",
"原创": "原创",
"虎牙地方": "虎牙地方",
"传奇": "传奇",
"御龙在天": "御龙在天",
"军事游戏": "军事游戏",
"传奇类游戏": "传奇类游戏",
"射击综合游戏": "射击综合游戏",
"幻塔": "幻塔",
"战争冲突": "战争冲突",
"虎牙领主争霸": "虎牙领主争霸",
"王者模拟战": "王者模拟战",
"坦克世界": "坦克世界",
"一起玩": "一起玩",
"传奇手游": "传奇手游",
"天龙八部手游": "天龙八部手游",
"虎牙文化": "虎牙文化",
"明日之后": "明日之后",
"Dread Hunger": "Dread Hunger",
"艾尔登法环": "艾尔登法环",
"永恒之塔": "永恒之塔",
"英魂之刃": "英魂之刃",
"第五人格": "第五人格",
"COD手游": "COD手游",
"虚拟偶像": "虚拟偶像",
"音乐": "音乐",
"彩虹岛Online": "彩虹岛Online",
"趣分享": "趣分享",
"逃离塔科夫": "逃离塔科夫",
"狼人杀手游": "狼人杀手游",
"探索": "探索",
"剑灵": "剑灵",
"Apex英雄": "Apex英雄",
"炉石战棋": "炉石战棋",
"DNF手游": "DNF手游",
"欢乐麻将": "欢乐麻将",
"天涯明月刀手游": "天涯明月刀手游",
"怀旧游戏": "怀旧游戏",
"冒险岛": "冒险岛",
"俄罗斯钓鱼4": "俄罗斯钓鱼4",
"欢乐斗地主": "欢乐斗地主",
"神武4手游": "神武4手游",
"起凡：群雄逐鹿": "起凡：群雄逐鹿",
"部落：上升": "部落：上升",
"御龙在天手游": "御龙在天手游",
"体育游戏": "体育游戏",
"神武4电脑版": "神武4电脑版",
"诛仙3": "诛仙3",
"CFHD": "CFHD",
"热血江湖": "热血江湖",
"枪神纪": "枪神纪",
"QQ三国": "QQ三国",
"英雄杀": "英雄杀",
"九阴真经": "九阴真经",
"三国志战略版": "三国志战略版",
"天天狼人": "天天狼人",
"NBA2KOL系列": "NBA2KOL系列",
"征途": "征途",
"多乐棋牌": "多乐棋牌",
"问道手游": "问道手游",
"寻仙": "寻仙",
"龙之谷": "龙之谷",
"草根传奇": "草根传奇",
"阴阳师": "阴阳师",
"暗黑破坏神": "暗黑破坏神",
"直播购": "直播购",
"忍者必须死3": "忍者必须死3",
"DayZ独立版": "DayZ独立版",
"荒野行动PC版": "荒野行动PC版",
"斗战神": "斗战神",
"迷你世界": "迷你世界",
"逆水寒": "逆水寒",
"恐惧之间": "恐惧之间",
"斗罗大陆：魂师对决": "斗罗大陆：魂师对决",
"战舰世界": "战舰世界",
"反恐精英Online": "反恐精英Online",
"狼人杀": "狼人杀",
"妄想山海": "妄想山海",
"旅游": "旅游",
"刀剑英雄": "刀剑英雄",
"流放之路": "流放之路",
"摔跤城大乱斗": "摔跤城大乱斗",
"诛仙世界": "诛仙世界",
"QQ华夏": "QQ华夏",
"奶块": "奶块",
"生死狙击": "生死狙击",
"部落冲突": "部落冲突",
"魔兽世界怀旧服": "魔兽世界怀旧服",
"香肠派对": "香肠派对",
"恐鬼症": "恐鬼症",
"创造与魔法": "创造与魔法",
"完美世界手游": "完美世界手游",
"率土之滨": "率土之滨",
"星球大战系列": "星球大战系列",
"SKY光遇": "SKY光遇",
"铁甲雄兵": "铁甲雄兵",
"JJ棋牌": "JJ棋牌",
"派对": "派对",
"大唐无双零": "大唐无双零",
"梦幻新诛仙": "梦幻新诛仙",
"巅峰战舰": "巅峰战舰",
"星际战甲": "星际战甲",
"崩坏3": "崩坏3",
"欧洲卡车模拟": "欧洲卡车模拟",
"绿茵信仰": "绿茵信仰",
"狼人杀官方": "狼人杀官方",
"逃跑吧！少年": "逃跑吧！少年",
"征途2": "征途2",
"新倩女幽魂": "新倩女幽魂",
"天涯明月刀": "天涯明月刀",
"天天象棋": "天天象棋",
"倩女幽魂手游": "倩女幽魂手游",
"武侠乂手游": "武侠乂手游",
"怪物猎人：崛起": "怪物猎人：崛起",
"中国象棋": "中国象棋",
"怪物猎人物语": "怪物猎人物语",
"饥荒": "饥荒",
"失落的方舟": "失落的方舟",
"天谕手游": "天谕手游",
"重返帝国": "重返帝国",
"梦想世界3": "梦想世界3",
"大话西游2": "大话西游2",
"互动剧游": "互动剧游",
"万国觉醒": "万国觉醒",
"完美端游系列": "完美端游系列",
"斗破苍穹手游": "斗破苍穹手游",
"新笑傲江湖": "新笑傲江湖",
"多多自走棋": "多多自走棋",
"天天酷跑": "天天酷跑",
"天翼决": "天翼决",
"甜蜜之家": "甜蜜之家",
"守望先锋": "守望先锋",
"弹弹堂手游": "弹弹堂手游",
"反恐行动online": "反恐行动online",
"新剑侠情缘手游": "新剑侠情缘手游",
"英魂之刃口袋版": "英魂之刃口袋版",
"云上城之歌": "云上城之歌",
"FIFA Online系列": "FIFA Online系列",
"奇迹MU：觉醒": "奇迹MU：觉醒",
"千年3": "千年3",
"无期迷途": "无期迷途",
"造梦西游OL": "造梦西游OL",
"SCUM": "SCUM",
"超击突破": "超击突破",
"港诡实录": "港诡实录",
"丝路传说2": "丝路传说2",
"纸人": "纸人",
"无神之界": "无神之界",
"战争雷霆": "战争雷霆",
"剑网3": "剑网3",
"武林外传一世琴缘": "武林外传一世琴缘",
"命运2": "命运2",
"最强NBA": "最强NBA",
"QQ自由幻想": "QQ自由幻想",
"时空猎人3": "时空猎人3",
"逆水寒手游": "逆水寒手游",
"星际争霸": "星际争霸",
"航海王热血航线": "航海王热血航线",
"王牌竞速": "王牌竞速",
"战地5": "战地5",
"精灵盛典：黎明": "精灵盛典：黎明",
"永恒纪元：戒": "永恒纪元：戒",
"神泣": "神泣",
"骑马与砍杀系列": "骑马与砍杀系列",
"只狼：影逝二度": "只狼：影逝二度",
"北凉悍刀行": "北凉悍刀行",
"洛克王国": "洛克王国",
"植物大战僵尸": "植物大战僵尸",
"三国战纪2": "三国战纪2",
"跑跑卡丁车": "跑跑卡丁车",
"全民枪战2": "全民枪战2",
"远征Online梦想版": "远征Online梦想版",
"诛仙手游": "诛仙手游",
"方舟手游": "方舟手游",
"混沌起源": "混沌起源",
"雷曼：传奇": "雷曼：传奇",
"怪物猎人世界": "怪物猎人世界",
"育碧游戏": "育碧游戏",
"FIFA足球世界": "FIFA足球世界",
"黎明觉醒": "黎明觉醒",
"荒野乱斗": "荒野乱斗",
"007：传奇": "007：传奇",
"天下": "天下",
"极限竞速：地平线": "极限竞速：地平线",
"龙之谷2手游": "龙之谷2手游",
"蛋仔派对": "蛋仔派对",
"虎牙球球": "虎牙球球",
"Badlanders": "Badlanders",
"激战2": "激战2",
"征途2手游": "征途2手游",
"剑灵：革命": "剑灵：革命",
"绝世仙王": "绝世仙王",
"超激斗梦境": "超激斗梦境",
"航海王：燃烧意志": "航海王：燃烧意志",
"红警OL": "红警OL",
"使命召唤系列": "使命召唤系列",
"QQ幻想": "QQ幻想",
"岛": "岛",
"消逝的光芒2": "消逝的光芒2",
"海岛奇兵": "海岛奇兵",
"战意": "战意",
"三国志": "三国志",
"荒野大镖客2": "荒野大镖客2",
"黑色沙漠": "黑色沙漠",
"极光世界 弑神传": "极光世界 弑神传",
"音乐游戏": "音乐游戏",
"九灵神域": "九灵神域",
"QQ幻想世界": "QQ幻想世界",
"Lost Light（萤火突击国际服）": "Lost Light（萤火突击国际服）",
"新飞飞(FlyFF)": "新飞飞(FlyFF)",
"深空之眼": "深空之眼",
"新斗罗大陆": "新斗罗大陆",
"坦克大战": "坦克大战",
"三国战纪": "三国战纪",
"猎人：荒野的召唤": "猎人：荒野的召唤",
"真·三国无双OL": "真·三国无双OL",
"VALORANT": "VALORANT",
"风云": "风云",
"贪玩蓝月": "贪玩蓝月",
"决战平安京": "决战平安京",
"拳皇命运": "拳皇命运",
"其他单机": "其他单机",
"QQ仙侠传": "QQ仙侠传",
"奥拉星": "奥拉星",
"荣耀新三国": "荣耀新三国",
"寻仙手游": "寻仙手游",
"罗布乐思": "罗布乐思",
"盗贼之海": "盗贼之海",
"一念逍遥": "一念逍遥",
"一梦江湖": "一梦江湖",
"实况足球": "实况足球",
"Among Us": "Among Us",
"热血江湖手游": "热血江湖手游",
"皇室战争": "皇室战争",
"FIFA Online4": "FIFA Online4",
"糖豆人：终极淘汰赛": "糖豆人：终极淘汰赛",
"轩辕传奇": "轩辕传奇",
"哈利波特：魔法觉醒": "哈利波特：魔法觉醒",
"无尽的拉格朗日": "无尽的拉格朗日",
"明日方舟": "明日方舟",
"都市：天际线": "都市：天际线",
"醉逍遥": "醉逍遥",
"使命召唤：战区": "使命召唤：战区",
"王牌战争：文明重启": "王牌战争：文明重启",
"诺亚传说": "诺亚传说",
"黑色沙漠手游": "黑色沙漠手游",
"真三国无双霸": "真三国无双霸",
"希望OL": "希望OL",
"梦三国手游": "梦三国手游",
"斗罗大陆": "斗罗大陆",
"天谕": "天谕",
"梦幻诛仙手游": "梦幻诛仙手游",
"大话西游手游": "大话西游手游",
"新剑侠情缘": "新剑侠情缘",
"天天吃鸡手机版": "天天吃鸡手机版",
"九霄缳神记": "九霄缳神记",
"夜族崛起": "夜族崛起",
"雀魂麻将": "雀魂麻将",
"魂斗罗：归来": "魂斗罗：归来",
"游戏王：决斗链接": "游戏王：决斗链接",
"天命西游": "天命西游",
"笑傲江湖": "笑傲江湖",
"QQ炫舞": "QQ炫舞",
"帝国时代4": "帝国时代4",
"征途手游": "征途手游",
"漫威超级战争": "漫威超级战争",
"奥奇传说手游": "奥奇传说手游",
"双人成行": "双人成行",
"完美世界：诸神之战": "完美世界：诸神之战",
"指尖四川麻将": "指尖四川麻将",
"幽灵线：东京": "幽灵线：东京",
"庆余年手游": "庆余年手游",
"拳皇98终极之战OL": "拳皇98终极之战OL",
"剑侠世界": "剑侠世界",
"海底大作战": "海底大作战",
"单机手游": "单机手游",
"全面战争：三国": "全面战争：三国",
"鸿图之下": "鸿图之下",
"刺客信条": "刺客信条",
"青云诀2": "青云诀2",
"火影忍者OL": "火影忍者OL",
"泡泡堂": "泡泡堂",
"装甲战争": "装甲战争",
"QQ炫舞手游": "QQ炫舞手游",
"星辰变": "星辰变",
"战术小队": "战术小队",
"枪火重生": "枪火重生",
"洛奇英雄传": "洛奇英雄传",
"真三国无双": "真三国无双",
"起凡游戏三国争霸": "起凡游戏三国争霸",
"死亡之夜": "死亡之夜",
"极品飞车系列": "极品飞车系列",
"堡垒之夜": "堡垒之夜",
"任天堂专区": "任天堂专区",
"霸王2": "霸王2",
"魔戒：中土大战": "魔戒：中土大战",
"APEX手游": "APEX手游",
"猫和老鼠": "猫和老鼠",
"文明与征服": "文明与征服",
"幻世九歌": "幻世九歌",
"灵魂筹码": "灵魂筹码",
"仁王2": "仁王2",
"帝国时代系列": "帝国时代系列",
"梦幻诛仙2": "梦幻诛仙2",
"少年三国志2": "少年三国志2",
"摩尔庄园": "摩尔庄园",
"魔力宝贝": "魔力宝贝",
"球球英雄": "球球英雄",
"坦克世界闪击战": "坦克世界闪击战",
"决胜三国": "决胜三国",
"风云岛行动": "风云岛行动",
"仙境传说RO": "仙境传说RO",
"剑侠世界2手游": "剑侠世界2手游",
"时空召唤": "时空召唤",
"全面战争": "全面战争",
"鬼泣": "鬼泣",
"鬼谷八荒": "鬼谷八荒",
"地铁跑酷": "地铁跑酷",
"决斗之城": "决斗之城",
"我的勇者": "我的勇者",
"QQ华夏手游": "QQ华夏手游",
"黑暗与光明手游": "黑暗与光明手游",
"腾讯桌球": "腾讯桌球",
"帝国神话": "帝国神话",
"王牌战士": "王牌战士",
"赛尔号": "赛尔号",
"奥奇传说": "奥奇传说",
"模拟农场": "模拟农场",
"火线精英": "火线精英",
"天堂 W": "天堂 W",
"仙剑奇侠传七": "仙剑奇侠传七",
"古剑奇谭OL": "古剑奇谭OL",
"千古风流": "千古风流",
"释厄英雄": "释厄英雄",
"影之刃3": "影之刃3",
"太荒初境": "太荒初境",
"奥比岛：梦想国度": "奥比岛：梦想国度",
"机动都市阿尔法": "机动都市阿尔法",
"奥拉星手游": "奥拉星手游",
"电竞传奇": "电竞传奇",
"轩辕传奇手游": "轩辕传奇手游",
"军棋": "军棋",
"新大话西游3": "新大话西游3",
"斗罗大陆-斗神再临": "斗罗大陆-斗神再临",
"使命召唤：黑色行动4": "使命召唤：黑色行动4",
"猎魂觉醒": "猎魂觉醒",
"第九大陆": "第九大陆",
"对马岛之魂": "对马岛之魂",
"剑网1：归来": "剑网1：归来",
"疾风之刃": "疾风之刃",
"神武2": "神武2",
"口袋觉醒": "口袋觉醒",
"天堂": "天堂",
"流星群侠传": "流星群侠传",
"我叫MT4": "我叫MT4",
"飙酷车神": "飙酷车神",
"看门狗：军团": "看门狗：军团",
"绝区零": "绝区零",
"全球使命": "全球使命",
"泰坦陨落": "泰坦陨落",
"武魂2": "武魂2",
"三国之刃": "三国之刃",
"深海迷航": "深海迷航",
"宝可梦：剑盾": "宝可梦：剑盾",
"冒险男爵": "冒险男爵",
"龙武手游": "龙武手游",
"传奇天下": "传奇天下",
"热血江湖2": "热血江湖2",
"魔侠传": "魔侠传",
"火炬之光：无限": "火炬之光：无限",
"封印者": "封印者",
"新盗墓笔记": "新盗墓笔记",
"一拳超人：最强之男": "一拳超人：最强之男",
"剑侠情缘2剑歌行": "剑侠情缘2剑歌行",
"凡人修仙传Online": "凡人修仙传Online",
"非人学园": "非人学园",
"全球行动": "全球行动",
"仙剑奇侠传五": "仙剑奇侠传五",
"流放者柯南": "流放者柯南",
"封神榜（国际版）": "封神榜（国际版）",
"热血街篮": "热血街篮",
"石油骚动": "石油骚动",
"奇葩战斗家": "奇葩战斗家",
"传世无双": "传世无双",
"流星蝴蝶剑": "流星蝴蝶剑",
"武装突袭": "武装突袭",
"蛇蛇争霸": "蛇蛇争霸",
"环世界": "环世界",
"极品飞车Online": "极品飞车Online",
"霸刀群侠传online": "霸刀群侠传online",
"保卫萝卜3": "保卫萝卜3",
"渡神记": "渡神记",
"EVE星战前夜：无烬星河": "EVE星战前夜：无烬星河",
"幽灵行动：荒野": "幽灵行动：荒野",
"永恒轮回": "永恒轮回",
"三国志：幻想大陆": "三国志：幻想大陆",
"虎牙吃鸡": "虎牙吃鸡",
"天使之战": "天使之战",
"绿色征途": "绿色征途",
"炫舞时代": "炫舞时代",
"霓虹深渊": "霓虹深渊",
"四海兄弟": "四海兄弟",
"无尽传奇": "无尽传奇",
"归家异途": "归家异途",
"魔力宝贝：旅人": "魔力宝贝：旅人",
"逆境求生": "逆境求生",
"猫之城": "猫之城",
"英雄三国": "英雄三国",
"新游推荐": "新游推荐",
"赤壁": "赤壁",
"成吉思汗怀旧版": "成吉思汗怀旧版",
"无人深空": "无人深空",
"战争怒吼": "战争怒吼",
"街机游戏": "街机游戏",
"一刀流": "一刀流",
"米加小镇": "米加小镇",
"剑网3指尖对弈": "剑网3指尖对弈",
"风云龙战天下": "风云龙战天下",
"时空猎人": "时空猎人",
"天国：拯救": "天国：拯救",
"荣耀大天使": "荣耀大天使",
"龙与家园": "龙与家园",
"橙光": "橙光",
"斗罗大陆：武魂觉醒": "斗罗大陆：武魂觉醒",
"元气骑士": "元气骑士",
"无尽神域": "无尽神域",
"新水浒Q传": "新水浒Q传",
"月圆之夜": "月圆之夜",
"台球大师": "台球大师",
"圣境传说": "圣境传说",
"梦幻龙族II": "梦幻龙族II",
"仙魔决": "仙魔决",
"欢喜斗地主": "欢喜斗地主",
"未来之役": "未来之役",
"天使纪元": "天使纪元",
"天堂2：血盟": "天堂2：血盟",
"三国群英传7": "三国群英传7",
"玄中记": "玄中记",
"我在江湖之神魔道": "我在江湖之神魔道",
"战地之王": "战地之王",
"热血三国": "热血三国",
"刀塔传奇": "刀塔传奇",
"神雕侠侣2": "神雕侠侣2",
"成吉思汗3": "成吉思汗3",
"全球使命3": "全球使命3",
"九界": "九界",
"劲舞团": "劲舞团",
"皇帝成长计划2": "皇帝成长计划2",
"乱世王者": "乱世王者",
"火星求生": "火星求生",
"Party Animals": "Party Animals",
"这是我的战争": "这是我的战争",
"山海经之魔蛙传说": "山海经之魔蛙传说",
"DJMAX三部曲": "DJMAX三部曲",
"足球小将": "足球小将",
"重生细胞": "重生细胞",
"狂野飙车9：竞速传奇": "狂野飙车9：竞速传奇",
"漫威蜘蛛侠": "漫威蜘蛛侠",
"文明6": "文明6",
"反恐精英Online 2": "反恐精英Online 2",
"街头篮球": "街头篮球",
"圣斗士星矢(腾讯)": "圣斗士星矢(腾讯)",
"战舰世界闪击战": "战舰世界闪击战",
"漫漫长夜": "漫漫长夜",
"缺氧": "缺氧",
"星露谷物语": "星露谷物语",
"蘑菇战争2": "蘑菇战争2",
"神之浩劫": "神之浩劫",
"虎豹骑": "虎豹骑",
"全面战争：阿提拉": "全面战争：阿提拉",
"皇家塔防": "皇家塔防",
"泰拉瑞亚手游": "泰拉瑞亚手游",
"乱世逐鹿": "乱世逐鹿",
"戴森球计划": "戴森球计划",
"提灯与地下城": "提灯与地下城",
"禁闭求生": "禁闭求生",
"动物派对手游": "动物派对手游",
"新世界": "新世界",
"喷射战士3": "喷射战士3",
"无限法则": "无限法则",
"魔渊之刃": "魔渊之刃",
"十二之天系列": "十二之天系列",
"魔之精灵": "魔之精灵",
"马里奥专区": "马里奥专区",
"星之海洋5": "星之海洋5",
"死亡细胞": "死亡细胞",
"狩猎时刻": "狩猎时刻",
"欢乐升级": "欢乐升级",
"围棋": "围棋",
"失落的王座": "失落的王座",
"全境封锁": "全境封锁",
"伤害世界": "伤害世界",
"超神传": "超神传",
"恶魔之魂": "恶魔之魂",
"战双：帕弥什": "战双：帕弥什",
"剑网3：指尖江湖": "剑网3：指尖江湖",
"雨中冒险": "雨中冒险",
"哈迪斯": "哈迪斯",
"自由幻想手游": "自由幻想手游",
"反恐精英": "反恐精英",
"斗破仙途": "斗破仙途",
"蜘蛛侠系列": "蜘蛛侠系列",
"魔法门之英雄无敌系列": "魔法门之英雄无敌系列",
"武魂": "武魂",
"骑士物语": "骑士物语",
"剑与家园": "剑与家园",
"三界争锋": "三界争锋",
"金星登陆器": "金星登陆器",
"SD敢达Online": "SD敢达Online",
"马里奥赛车8": "马里奥赛车8",
"最终幻想系列": "最终幻想系列",
"烽火三国": "烽火三国",
"永劫无间手游": "永劫无间手游",
"航海王：启航": "航海王：启航",
"女鬼桥：开魂路": "女鬼桥：开魂路",
"武侠乂": "武侠乂",
"龙武": "龙武",
"造梦西游4手机版": "造梦西游4手机版",
"火影忍者：究极风暴系列": "火影忍者：究极风暴系列",
"Steamcraft": "Steamcraft",
"忍者村大战2": "忍者村大战2",
"新挑战": "新挑战",
"圣斗士星矢ol": "圣斗士星矢ol",
"仙之痕手游": "仙之痕手游",
"挨饿荒野": "挨饿荒野",
"攻城掠地": "攻城掠地",
"龙之国物语": "龙之国物语",
"戎马丹心之汉匈决战": "戎马丹心之汉匈决战",
"仙剑奇侠传OL手游": "仙剑奇侠传OL手游",
"群侠传": "群侠传",
"美丽水世界": "美丽水世界",
"斩魂": "斩魂",
"闪克": "闪克",
"蚁族崛起": "蚁族崛起",
"口袋妖怪": "口袋妖怪",
"全民斩仙": "全民斩仙",
"航海世纪": "航海世纪",
"野兽传奇": "野兽传奇",
"龙与地下城Online": "龙与地下城Online",
"小缇娜的奇幻之地": "小缇娜的奇幻之地",
"紫塞秋风": "紫塞秋风",
"荒野行动": "荒野行动",
"保卫萝卜2": "保卫萝卜2",
"战神": "战神",
"黄易群侠传2": "黄易群侠传2",
"全面战争：竞技场": "全面战争：竞技场",
"玄真道": "玄真道",
"蜀山剑侠传": "蜀山剑侠传",
"古剑奇谭3": "古剑奇谭3",
"有杀气童话2": "有杀气童话2",
"神将三国": "神将三国",
"原始征途": "原始征途",
"斗斗堂": "斗斗堂",
"领地人生": "领地人生",
"小森生活": "小森生活",
"塞尔达传说：荒野之息": "塞尔达传说：荒野之息",
"国战ONLINE": "国战ONLINE",
"真武传": "真武传",
"轩辕剑外传：云之遥": "轩辕剑外传：云之遥",
"禅游斗地主": "禅游斗地主",
"梦幻模拟战": "梦幻模拟战",
"大唐2": "大唐2",
"重力": "重力",
"蜀山神话": "蜀山神话",
"微软模拟飞行2020": "微软模拟飞行2020",
"狙击手：幽灵战士": "狙击手：幽灵战士",
"飞龙在天传奇": "飞龙在天传奇",
"闪烁之光": "闪烁之光",
"火影小时代": "火影小时代",
"狂刃": "狂刃",
"复仇者联盟": "复仇者联盟",
"神佑释放": "神佑释放",
"全球使命（国际版）": "全球使命（国际版）",
"环形战争": "环形战争",
"新射雕群侠传": "新射雕群侠传",
"远古战争国度（古域之战）": "远古战争国度（古域之战）",
"龙族幻想": "龙族幻想",
"剑侠情缘手游": "剑侠情缘手游",
"剑与远征手游": "剑与远征手游",
"创世理想乡": "创世理想乡",
"幻想神域": "幻想神域",
"警匪杀": "警匪杀",
"地城之光": "地城之光",
"新惊天动地": "新惊天动地",
"一剑斩仙": "一剑斩仙",
"FF14": "FF14",
"不良人2": "不良人2",
"坎公骑冠剑": "坎公骑冠剑",
"瑞奇与叮当": "瑞奇与叮当",
"最终幻想：起源": "最终幻想：起源",
"玄天之剑": "玄天之剑",
"逃脱者2": "逃脱者2",
"远征军：征服者": "远征军：征服者",
"黑暗领域2": "黑暗领域2",
"精灵与萤火意志": "精灵与萤火意志",
"三国": "三国",
"神界2": "神界2",
"诺亚之心": "诺亚之心",
"梦想世界3手游": "梦想世界3手游",
"一起玩农场": "一起玩农场",
"EVE Online": "EVE Online",
"龙族血统": "龙族血统",
"切尔诺贝利突击队": "切尔诺贝利突击队",
"蜀门": "蜀门",
"鹿鼎记": "鹿鼎记",
"五子棋": "五子棋",
"格斗游戏": "格斗游戏",
"环绕走廊": "环绕走廊",
"天穗之咲稻姬": "天穗之咲稻姬",
"重写三国志": "重写三国志",
"Factorio": "Factorio",
"废品机械师": "废品机械师",
"血染钟楼": "血染钟楼",
"神魔": "神魔",
"逆战手游": "逆战手游",
"大唐仙妖劫": "大唐仙妖劫",
"猎杀：恶魔熔炉": "猎杀：恶魔熔炉",
"头文字D": "头文字D",
"暗黑血统2": "暗黑血统2",
"奥日与黑暗森林": "奥日与黑暗森林",
"吞食天地3": "吞食天地3",
"风暴英雄": "风暴英雄",
"最后一炮": "最后一炮",
"人类一败涂地": "人类一败涂地",
"轩辕剑三：天之痕": "轩辕剑三：天之痕",
"黑暗地带：51区": "黑暗地带：51区",
"异能都市": "异能都市",
"订阅": "订阅",
"直播": "直播",
"赛事": "赛事",
"网游": "网游",
"单机": "单机",
"娱乐": "娱乐",
"手游": "手游",
"QQ飞车全国公开赛端游赛道": "QQ飞车全国公开赛端游赛道",
"暴雪游戏频道": "暴雪游戏频道",
"LCK夏季赛": "LCK夏季赛",
"英雄联盟": "英雄联盟",
"LOL云顶之弈": "LOL云顶之弈",
"穿越火线": "穿越火线",
"DNF": "DNF",
"射击综合": "射击综合",
"炉石传说": "炉石传说",
"DOTA2": "DOTA2",
"魔兽争霸3": "魔兽争霸3",
"CS:GO": "CS:GO",
"逆战": "逆战",
"生死狙击2": "生死狙击2",
"QQ飞车": "QQ飞车",
"天天吃鸡": "天天吃鸡",
"主机游戏": "主机游戏",
"我的世界": "我的世界",
"方舟": "方舟",
"永劫无间": "永劫无间",
"逃离塔科夫": "逃离塔科夫",
"怀旧游戏": "怀旧游戏",
"互动点播": "互动点播",
"Dread Hunger": "Dread Hunger",
"星秀": "星秀",
"户外": "户外",
"二次元": "二次元",
"一起看": "一起看",
"美食": "美食",
"颜值": "颜值",
"交友": "交友",
"体育": "体育",
"组队": "组队",
"王者荣耀": "王者荣耀",
"和平精英": "和平精英",
"LOL电竞经理": "LOL电竞经理",
"LOL手游": "LOL手游",
"新游广场": "新游广场",
"金铲铲之战": "金铲铲之战",
"暗区突围": "暗区突围",
"火影忍者手游": "火影忍者手游",
"CF手游": "CF手游",
"棋牌休闲": "棋牌休闲",
"原神": "原神",
"综合手游": "综合手游",
"暗黑破坏神：不朽": "暗黑破坏神：不朽",
"环形战争": "环形战争",
"二次元手游": "二次元手游",
"下载客户端": "下载客户端",
"我要直播": "我要直播"


			
		}
		classes = []
		for k in cateManual:
			classes.append({
				'type_name': k,
				'type_id': cateManual[k]
			})

		result['class'] = classes
		if (filter):
			result['filters'] = self.config['filter']
		return result
	def homeVideoContent(self):
		result = {}
		return result
	def categoryContent(self,tid,pg,filter,extend):
		result = {}
		url = 'http://live.yj1211.work/api/live/getRecommendByPlatformArea?platform=huya&size=20&area={0}&page={1}'.format(tid, pg)
		rsp = self.fetch(url)
		content = rsp.text
		jo = json.loads(content)
		videos = []
		vodList = jo['data']
		for vod in vodList:
			aid = (vod['roomId']).strip()
			title = vod['roomName'].strip()
			img = vod['roomPic'].strip()
			remark = (vod['categoryName']).strip()
			videos.append({
				"vod_id": aid,
				"vod_name": title,
				"vod_pic": img,
				"vod_remarks": remark
			})
		result['list'] = videos
		result['page'] = pg
		result['pagecount'] = 9999
		result['limit'] = 90
		result['total'] = 999999
		return result
	def detailContent(self,array):
		aid = array[0]
		url = "http://live.yj1211.work/api/live/getRoomInfo?platform=huya&roomId={0}".format(aid)
		rsp = self.fetch(url)
		jRoot = json.loads(rsp.text)
		jo = jRoot['data']
		title = jo['roomName']
		pic = jo['roomPic']
		desc = str(jo['online'])
		dire = jo['ownerName']
		typeName = jo['categoryName']
		remark = jo['categoryName']
		vod = {
			"vod_id": aid,
			"vod_name": title,
			"vod_pic": pic,
			"type_name": typeName,
			"vod_year": "",
			"vod_area": "",
			"vod_remarks": remark,
			"vod_actor": '在线人数:' + desc,
			"vod_director": dire,
			"vod_content": ""
		}
		playUrl = '原画' + '${0}#'.format(aid)
		vod['vod_play_from'] = '虎牙直播'
		vod['vod_play_url'] = playUrl

		result = {
			'list': [
				vod
			]
		}
		return result
	def searchContent(self,key,quick):
		result = {}
		return result
	def playerContent(self,flag,id,vipFlags):
		result = {}

		url = 'https://mp.huya.com/cache.php?m=Live&do=profileRoom&roomid={0}'.format(id)
		rsp = self.fetch(url)
		jRoot = json.loads(rsp.text)
		jo = jRoot['data']
		ja = jo['stream']['baseSteamInfoList'][0]['sStreamName']
		url = 'http://txtest-xp2p.p2p.huya.com/src/' + ja + '.xs?ratio=4000'

		result["parse"] = 0
		result["playUrl"] = ''
		result["url"] = url
		result["header"] = {
			"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
		}
		result["contentType"] = 'video/x-flv'
		return result

	config = {
		"player": {},
		"filter": {}
	}
	header = {}

	config = {
		"player": {},
		"filter": {}
	}
	header = {}
	def localProxy(self,param):
		action = {
			'url':'',
			'header':'',
			'param':'',
			'type':'string',
			'after':''
		}
		return [200, "video/MP2T", action, ""]
