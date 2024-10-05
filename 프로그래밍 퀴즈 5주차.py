# quiz 1
def add(num1, num2, num3, num4):
    return num1 + num2 + num3 + num4

def multiply(num1, num2, num3, num4):
    return num1 * num2 * num3 * num4

print(add(2, 3, 4, 5))  # 출력: 14
print(multiply(2, 3, 4, 5))  # 출력: 120

# quiz 2
def odd_or_even(num):
    if num % 2 == 0:
        return "짝수"
    else:
        return "홀수"


print(odd_or_even(3))  # 출력: 홀수
print(odd_or_even(4))  # 출력: 짝수

# quiz 3
def average(lst):
    total = 0
    count = 0
    for number in lst:
        total += number
        count += 1
    return total / count if count > 0 else 0

print(average([1, 2, 3, 4, 5]))  # 출력: 3.0

# quiz 4
class GameCharacter:
    def __init__(self, id, gender, profession):
        self.id = id
        self.gender = gender
        self.profession = profession

    def attack(self):
        print("공격!")

character = GameCharacter("hero01", "여자", "전사")
character.attack()  # 출력: 공격!

# quiz 5
class RealEstate:
    def __init__(self, location, area, building_type, price, year_built):
        self.location = location
        self.area = area
        self.building_type = building_type
        self.price = price
        self.year_built = year_built

    def display_info(self):
        print(f"위치: {self.location}")
        print(f"평수: {self.area}")
        print(f"건물 종류: {self.building_type}")
        print(f"가격: {self.price}")
        print(f"건축 연도: {self.year_built}")

property = RealEstate("서울", 85, "아파트", 50000000, 2020)
property.display_info()


