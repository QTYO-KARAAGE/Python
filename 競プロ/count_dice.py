import random 

a_max = 4
b_min = 5
b_max = 7
c_min = 8
c_max = 9
d_min = 10 

count = 10

quit = 'y'

while (quit != 'n'):
    #確率の計算
    result = random.randint(1, count)
    
    #変数resultの値がAからDのどれに当てはまるのかの条件分岐
    if 1 <= result <= a_max :
        print('結果：A \n A：{}個 B：{}個 C：{}個 D：{}個'.format(a_max, b_max - a_max, c_max - b_max, count - c_max))
        a_max += 1
        b_min += 1
        b_max += 1
        c_min += 1
        c_max += 1
        d_min += 1
    elif b_min <= result <= b_max :
        print('結果：B \n A：{}個 B：{}個 C：{}個 D：{}個'.format(a_max, b_max - a_max, c_max - b_max, count - c_max))
        b_max += 1
        c_min += 1
        c_max += 1
        d_min += 1
    elif c_min <= result <= c_max :
        print('結果：C \n A：{}個 B：{}個 C：{}個 D：{}個'.format(a_max, b_max - a_max, c_max - b_max, count - c_max))
        c_max += 1
        d_min += 1
    else :
        print('結果：D \n A：{}個 B：{}個 C：{}個 D：{}個'.format(a_max, b_max - a_max, c_max - b_max, count - c_max))
        #Dに当てはまった場合、変数countをインクリメントするだけなので条件分岐後の計算はない
    
    #合計数の追加
    count += 1
    
    #コンティニューするか決める
    quit = input('continue? [y/n]：')

