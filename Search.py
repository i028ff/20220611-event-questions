def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    
     #探索範囲の左端、の設定
    left = 0
    right = len(sorted_array) - 1
    
    while left <= right:
        #探索範囲の中央値のindexの計算
        mid = (left + right) // 2
        
        #ターゲットと中央値が同じなら中央値のindex返す
        if target_number == sorted_array[mid]:
            return mid
        
        #ターゲットより大きいなら探索の範囲の右側を変える
        elif target_number < sorted_array[mid]:
            right = mid - 1
        
        #ターゲットより小さいなら探索の範囲の左側を変える
        else :
            left = mid + 1

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()