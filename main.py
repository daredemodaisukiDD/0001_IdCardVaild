import random

# 身分證字號第一碼字母對應的數字
letter_to_number = {
    'A': 1, 'B': 0, 'C': 9, 'D': 8, 'E': 7, 'F': 6, 'G': 5, 'H': 4, 'I': 9, 'J': 3, 'K': 2, 'L': 2,
    'M': 1, 'N': 0, 'O': 8, 'P': 9, 'Q': 8, 'R': 7, 'S': 6, 'T': 5, 'U': 4, 'V': 3, 'W': 1, 'X': 3, 'Y': 2, 'Z': 0
}

# 身分證字號驗證函數
def validate_id_card():
    id_card = input("請輸入身分證字號: ")
    
    # 驗證身分證長度
    if len(id_card) != 10:
        print("請確認身分證為10碼")
        return
    
    # 驗證性別代碼
    if int(id_card[1]) not in [1, 2]:
        print("請確認身分證第2碼為1或2")
        return
    
    # 驗證第一碼是否為大寫字母
    if not id_card[0].isupper() or not ('A' <= id_card[0] <= 'Z'):
        print("請確認第一碼為大寫英文字母")
        return

    # 計算總和
    total_sum = letter_to_number[id_card[0]] + int(id_card[9])
    for i in range(1, 9):
        total_sum += int(id_card[i]) * (9 - i)
    
    # 判斷是否合法
    if total_sum % 10 == 0:
        print("合法")
    else:
        print("不合法")

# 身分證字號生成器函數
def generate_id_card():
    # 地區代碼選項
    region_codes = ["A", "B", "O", "C", "D"]

    # 輸入出生地代碼或選擇隨機
    region_code = input("請輸入出生地英文代碼或輸入9隨機: ").upper()
    if region_code == "9":
        region_code = random.choice(region_codes)

    # 輸入性別代碼或選擇隨機
    gender_code = input("請輸入性別代碼(1男性2女性)或輸入9隨機: ").upper()
    if gender_code == "9":
        gender_code = random.randint(1, 2)
    else:
        gender_code = int(gender_code)

    # 計算身分證前兩位
    checksum = letter_to_number[region_code] + gender_code * 8
    print(f"{region_code}{gender_code}", end="")

    # 生成後面7位數字
    for i in range(7):
        random_digit = random.randint(0, 9)
        checksum += random_digit * (7 - i)
        print(random_digit, end="")

    # 計算檢查碼
    print(10 - checksum % 10)

# 主程式函數
def main():
    while True:
        # 顯示選單
        user_choice = input("1.產生器, 2.驗證器, 3.離開: ")
        
        # 根據選擇執行相應的功能
        if user_choice == "1":
            print("1.產生器")
            generate_id_card()
        elif user_choice == "2":
            print("2.驗證器")
            validate_id_card()
        elif user_choice == "3":
            print("3.離開")
            break
        else:
            print("無效的選項，請重新輸入。")

# 執行主程式
if __name__ == "__main__":
    main()
