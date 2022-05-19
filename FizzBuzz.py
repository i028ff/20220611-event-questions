for num in range(1, 101):
    string = ''

    # ここから記述
    if (num % 3 == 0) & (num % 5 == 0):
        string = 'FizzBuzz'       #3の倍数かつ5の倍数ならFizzBuzzを返す
        
    elif (num % 3 == 0):
        string = 'Fizz'           #3の倍数ならFizzを返す
    
    elif (num % 5 == 0):
        string = 'Buzz'           #5の倍数ならBuzzを返す
    
    else: 
        string = str(num)         #それ以外なら数字を返す
    # ここまで記述

    print(string)