
import random
import string
alphabet = 26
taisyo = 10
kesson = 0
kesson_list = []

def q_mozi(mozi_list):
    ans = random.sample(mozi_list,10)
    print("対象文字:")
    for i in range(taisyo):
        print(ans[i],end=" ")
    print()
    return ans
def h_mozi(t_mozi):
    x = random.randint(5,9)
    ans = random.sample(t_mozi,x)
    print("表示文字:")
    for i in range(x):
        print(ans[i],end= " ")
    print()
    return ans

if __name__ == "__main__":
    mozi_list = list(string.ascii_uppercase)
    taisyo_mozi = q_mozi(mozi_list)
    hyouzi_mozi = h_mozi(taisyo_mozi)
    for i in taisyo_mozi:
        if (i in hyouzi_mozi):
            continue
        else:
            kesson_list.append(i)
    count = len(kesson_list)
    ans1 = input("欠損文字はいくつあるでしょうか？:")
    if int(ans1) == count:
        print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
        for i in range(count):
            ans2 = input(f"{i+1}つ目の文字を入力して下さい:")
            if ans2 in kesson_list:
                kesson_list.remove(ans2)
            else:
                print("不正解です。またチャレンジしてください")
            if len(kesson_list) ==0:
                print("正解です") 
    