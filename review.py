# 1주일 내용 10문제로 끝내기

# 1. 파이썬 조건문을 활용하여 장발장은 빵을 못먹게 하기
# - 실행 예시 : "장발장 차례 입니다, 빵을 드릴 수 없습니다."
# - 실행 예시 : "홍길동 차례 입니다, 빵을 하나 드리겠습니다."

people = ['홍길동', '성진', '심청이', '장발장', '심봉사']

for member in people :
    print(member + '의 차례입니다.')
    if member == '장발장':
        print('빵을 지급하지 않습니다.')
    else:
        print('빵을 1개 지급합니다.')

# --------------------------------------------------------

# 2. 1번 문제의 구현된 부분을 함수로 바꾸기
# - 조건 : 입력값(사람 한 명씩) 을 받아서 빵을 먹으면 안되는 사람이면 0을, 먹어도 되면 1을 반환하기
# - 실행 예시 : "홍길동은 빵을 먹을 수 있는 사람 입니다."
# - 실행 예시 : "장발장은 빵을 먹을 수 없는 사람 입니다."
# 반복문을 활용하여 5 명 전원 다 출력 할 것

# --------------------------------------------------------
def racist(member):
    print(member + '의 차례입니다.')
    if member == '장발장':
        return 0
    else:
        return 1

for member in people:
    if racist(member):
        print('빵을 1개 지급합니다.')
    else:
        print('빵을 지급받을 권한이 없습니다.')


# 3. 지역변수와 전역변수 이해하기

# 아래의 코드는 num_stamp 라는 전역변수를 함수 내에서 global 명령을 통해 수정가능하게 억지로 만든상태이다.
# 하지만, 함수의 기능과 본질을 생각하면 아래의 예시는 굉장히 바람직하지 못하다!
# global 명령은 안쓰는 것이 좋다!
# 그렇다면, global 명령을 사용하지 않고 아래의 로직을 함수의 입력값과 반환값을 활용하여 수정해보기!

num_stamp = 0  # 쿠폰 스탬프가 찍힌 횟수 (전역변수)


def stamp(st):
    """쿠폰 스탬프가 찍힌 횟수를 증가시키고, 화면에 출력한다."""
    #global num_stamp           # num_stamp는 전역변수다
    st = st + 1  # 오류가 발생하지 않는다 (global 안쓰면 오류 발생함)
    print(st)
    return st


num_stamp = stamp(num_stamp)  # 화면에 1이 출력된다
num_stamp = stamp(num_stamp)  # 화면에 2가 출력된다


# --------------------------------------------------------

# 4. 클래스 이용하기
# 요구사항
# - 교통수단 클래스 만들기 (속성 : 이름, 가격, 출발시간, 도착시간 / 기능 : 출발시간, 도착시간 보기)
# - 비행기 클래스 만들기
# 속성 : 이름, 가격, 출발시간, 도착시간, 수하물 가능여부
# 기능 : 출발시간, 도착시간 보기, 수하물 맡기기(수하물이 가능하면 "수하물을 맡겼습니다!"출력, 불가능하면 "이 비행기는 수하물을 못맡깁니다!" 출력)
# - 기차 클래스 만들기
# 속성 : 이름, 가격, 출발시간, 도착시간, 좌석등급
# 기능 : 출발시간, 도착시간 보기, 좌석등급 보기

# 클래스를 상속을 활용해서 효율적으로 만들어 볼것! (메소드 오버라이딩)
# 두 개 이상의 인스턴스를 비행기, 기차 각각 만들어 볼것

class take:
    name = '이름'
    price = '가격'
    departure = '출발시간'
    arrival = '도착시간'

    def show(self,name):
        print('출발시간: '+self.departure)
        print('도착시간: '+self.arrival)

class plain(take):
    def __init__(self,name,price,departure,arrival,transit):
        self.name = name
        self.price = price
        self.departure = departure
        self.arrival = arrival
        self.transit = transit
    
    def show(self):
        print('출발시간: '+self.departure)
        print('도착시간: '+self.arrival)
        if self.transit:
            print("물건을 적재했습니다!")
        else:
            print("이 비행기는 수하물을 실을 수 없습니다.")

class train(take):
    def __init__(self,name,price,departure,arrival,seatclass):
        self.name = name
        self.price = price
        self.departure = departure
        self.arrival = arrival
        self.seatclass = seatclass
    
    def show(self):
        print('출발시간: '+self.departure)
        print('도착시간: '+self.arrival)
        if self.seatclass == 'economy':
            print("기본석입니다.")
        elif self.seatclass == 'business':
            print("2등석입니다.")
        elif self.seatclass == 'first':
            print("1등석입니다.")
        else:
            print("입석입니다.")

KTX = train('KTX',40000,'06:30','08:00','economy')
KOREA_AIR = plain('KOREA_AIR',100000,'8:20','12:50',True)

KTX.show()
KOREA_AIR.show()
# --------------------------------------------------------

# 5. 문자열 이용하기


# 파이썬 io 하는거 2 문제
