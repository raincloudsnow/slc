from sys import exit



def start():
	print("历经千辛万苦，一行人来到了佛祖面前")
	print("""佛祖:
是不是很好奇你会怎样飞升
是不是觉得自己玩这个神坑游戏很久了，已经摸清楚套路了
""")
	print("是 or 不是")
	choice = input("> ")
	if choice == "是":
		print("佛祖：我真的佩服你的勇气\n神坑的名头你以为是闹着玩儿的咩！\n你是在蔑视佛祖吗！！！")
		print("佛祖差一点气昏过去，你就差1、、就凉凉了。")
		print("佛祖：calm down calm down\n我可以再给你一个机会\n我们石头剪刀布吧")
		print("石头 or 剪刀 or布")
		choice = input("> ")
		if choice == "石头":
			print("佛祖：布")
			print("佛祖：愿赌服输，再见了")
			exit(0)
		elif choice == "剪刀":
			print("佛祖：我竟然输了\n好吧恭喜你通过了考验\n成功升仙")
			exit(0)
		elif chioce == "布":
			print("佛祖：你竟然和我出一样的！\n你只好重来一次了")
			start()
		else:
			print("佛祖将你这种叛逆的孩子压在了五行山下\n五百年后再出来吧")
			exit(0)
	if choice == "不是":
		print("很好，你还对佛祖保持着敬畏之心")
		print("佛祖：你经历了这么多坑还能承认自己的不足，我真是欣慰啊\n这么好的孩子，恭喜你升仙了")
		exit(0)
	else:
		print("佛祖不想理你并把你再次压在了五行山下\n五百年后再见吧")
		exit(0)



start()
