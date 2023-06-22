'''コマンド引数の数字を読み取りFizzBuzzを解く'''
import sys

#関数定義パート
def tofizzbuzz(n):
    '''FizzBuzzを解く関数'''
    if(n % 3 == 0 and n % 5 == 0):
        str="FizzBuzz"
    elif(n % 3 == 0):
        str = "Fizz"
    elif(n % 5 == 0):
        str = "Buzz"
    else:
        str=n

    return str

#実行パート
if __name__ == '__main__':
    argv = sys.argv

    if(len(argv) != 3):
        #引数があるかチェックしなければメッセージを出力して終了
        print("使い方: python %s 整数１" %argv[0])
        sys.exit()

    try:
        x = int(argv[1]) #文字列として入力された引数を整数に変換
        print(tofizzbuzz(x))
    except ValueError:
        print("整数を引数に指定してください")
        sys.exit()