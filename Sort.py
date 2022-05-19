def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    
    #探索範囲の両端の選定
    left = 0
    right = len(array) - 1

    while left < right:
        
         #基準値以上の値がでるまで左側から探索
        while (array[left] < pivot):
            left += 1
        
        #基準値未満の値がでるまで右側から探索
        while (array[right] >= pivot) & (left < right):
            right -= 1
        
        #対象の2つを入れ替え
        if left < right:
            array[left], array[right] = array[right], array[left]

    #2つの配列に分ける
    if len(array) >= 3:
        if left == 0:
            return sort(array[::-1])
        else:
            array1 = array[:left]
            array2 = array[left:]
            
            return sort(array1) ,sort(array2)
        
    else:
        array1 = [array[0]]
        array2 = [array[1]]
        
        return sort(array1) ,sort(array2)


    # ここまで記述

if __name__ == '__main__':
    main()
