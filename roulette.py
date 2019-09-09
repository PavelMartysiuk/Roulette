import random
print ("Рулетка")
def spin():
    ran=random.randint(1,100)
    if ran in range(1,41):
        ran_color="Красный"
        return(ran_color)
    elif ran in range(41,85):
        ran_color="Черный"
        return(ran_color)
    elif ran in range (85,101):
        ran_color="Зеленый"
        return(ran_color)
def helpy():
    print("Выберите цвет \n1)Красный \n2)Черный \n3)Зеленый")
    coloruser=input('введите цвет').title()
    return(coloruser)

def choosecolor(coloruser):
    if coloruser=="Красный" or "Черный" or "Зеленый":
        print("Вы выбрали",coloruser)
    else:
        helpy()
def money(color,coloruser):
    balance = 100
    print(f'Ваш баланс:{balans}')
    rate=int(input("Введите сумму, которую хотите поставить"))
    if rate < balance:
        balance -= rate
        if coloruser==color=="Зеленый":
            win=rate*2
            balance +=win
            print("Вы победили, ваш выигрыш:",win)
        elif coloruser==color=="Красный" or coloruser==color=="Черный":
            win=rate*1.2
            balance+=win
            print("Вы победили,ваш выигрыш:",win)
        else :
            print("Вы проиграли, выпал",color)
    else:
        raise('Balans Error')
if __name__ == '__main__':
    while True:
        coloruser = helpy()
        choosecolor(coloruser)
        ran_color = spin()
        money(ran_color,coloruser)
