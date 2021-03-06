print("\t멋사 커피 자판기")

print("\t  - 메  뉴 -")
print("\t1 : 아메리카노 1,800원")
print("\t2 : 카페라떼 2,700원")
print("\t3 : 핫초코 2,300원")
print("\n========================================")

# 커피 그림  출력하는 함수
def coffeeArt(order, hot_ice, whipping,cups):
  art = ""
  if hot_ice == "hot":
    art += "🔥"
  elif hot_ice == "ice":
    art += "🧊"
  
  if whipping == "Y":
    art += "🍦"
    
  if order == 1:
    art+="☕"
  elif order == 2:
    art+="🥛"
  elif order == 3:
    art+="🍫"
  return art*cups

coffee_price = 0
whipping = "N"

# 1. 메뉴 선택 
try:
  order = int(input("커피 종류를 선택하세요. 번호 입력 >>> "))
  if order == 1:
    coffee_price = 1800
  elif order == 2:
    coffee_price = 2700
    # 휘핑크림 추가 여부
    whipping = input("휘핑크림 추가해드릴까요? (Y/N) >>> ").upper()
    # y/n을 입력하지 않으면 주문 오류
    if(whipping != "Y" or whipping != "N"):
      print("입력 오류! 주문이 취소되었습니다.")
      quit()
  elif order == 3:
    coffee_price = 2300
    # 휘핑크림 추가 여부
    whipping = input("휘핑크림 추가해드릴까요? (Y/N) >>> ").upper()
    # y/n을 입력하지 않으면 주문 오류
    if(whipping != "Y" or whipping != "N"):
      print("입력 오류! 주문이 취소되었습니다.")
      quit()
      
  # 핫/아이스 여부
  hot_ice = input("hot / ice를 선택하세요. (hot/ice) >>> ").lower()
  # hot/ice를 입력하지 않으면 주문 오류
  if(hot_ice != "hot" and hot_ice != "ice"):
    print("입력 오류! 주문이 취소되었습니다.")
    quit()
    
  # 잔 수 계산
  cups = int(input("몇 잔 드릴까요? >>>"))
  total_price = coffee_price*cups
  
  # 총 금액 계산 + 금액 투입 후 잔돈 계산 알고리즘
  received = int(input("총 금액은 "+str(total_price)+"원입니다. 돈을 투입해주세요 >>> "))
except:
  print("입력 오류! 주문이 취소되었습니다.")
  quit()