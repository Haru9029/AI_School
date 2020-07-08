class Info():
    def __init__(self):
        self.list_dics_info = [
            {
            'uid':'simon1234',
            'age' : 26,
            'password' : '1234s',
            'hobby' : 'soccer',
            'hope' : '하루에 하나씩 소화하면서 건강히 제대하겠습니다.'
            },
            {
            'uid': 'moon2508',
            'age' : 18,
            'password' : '2508m',
            'hobby' : 'bowling',
            'hope' : '열심히 하겠습니다'
            },
            {
            'uid' : 'ryu9012',
            'age' : 22,
            'password' : '9012r',
            'hobby' : 'guitar',
            'hope' : '건강제일.'
            },
            {
            'uid' : 'user2178',
            'age' : 19,
            'password' : '2178u',
            'hobby' : 'drawing',
            'hope' : '삼대500'
            }
        ]



    def render(self, info):
        print('---------------------------')
        print('uid :', info['uid'])
        print('hobby :', info['hobby'])
        print('hope :', info['hope'])

    def display_info(self,login_index,is_me=True):  # https://stackoverflow.com/questions/16932825/why-cant-non-default-arguments-follow-default-arguments
        if is_me == True:
            self.render(self.list_dics_info[login_index])
        else:
            for i, dic_info in enumerate(self.list_dics_info):
                if i != login_index:
                    self.render(dic_info)

    def years_info(self):
        for i in range(len(self.list_dics_info)):
            if self.list_dics_info[i]['age'] < 20:
                self.render(self.list_dics_info[i])



#----------------------------------------------------------- 
def Sign_up(uid, age, password, hobby, hope):
    sign_temp = {'uid' : uid,
                 'age' : age,
                 'password' : password,
                 'hobby' : hobby,
                 'hope' : hope}
    Student_info.list_dics_info.append(sign_temp)

    for i in range(len(Student_info.list_dics_info)):
        if Student_info.list_dics_info[i]['uid'] == uid :
            Main_page(i)
            break

def Main_page(login_index) :
    # 2. 관련 데이터 별로 출력해보기! (각각을 하나의 함수로!)
    # - 학생 이름 전부 출력해보기
    # - 20살 미만 학생 open의 쓰기모드를 활용하여 넣어보기
    # - 성인이 아닌 학생 출력하기 (20세 미만..)
    # - 조건문으로 아이디를 안넣으면 쓰기 안되게 막아보기
    # - 모든 로직은 open 을 최대한 활용하기 !
    while(1):
        print('=========== 정보보기 ===========')
        print('1. 내 정보')
        print('2. 다른사람 정보')
        print('3. 미성년자 확인')
        print('0. 나가기')

        select_menu_02 = int(input('메뉴를 선택하세요 : '))

        if select_menu_02 == 1:
            Student_info.display_info(login_index,True)
        elif select_menu_02 == 2:
            Student_info.display_info(login_index,False)
        elif select_menu_02 == 3:
            Student_info.years_info()
        elif select_menu_02 == 0:
            print('로그아웃 합니다 감사합니다.')
            break
        else :
            print('잘못 입력하셨습니다. 다시입력하세요~')
            


select_menu_01 = 0
Student_info = Info()

while(1):
    print('=========== 메 뉴 ===========')
    print('1. 회원가입')
    print('2. 로그인')

    select_menu_01 = int(input('메뉴를 선택하세요 : '))

    if select_menu_01 == 1:
        #회원가입
        while(1):
            input_uid = input('UID : ')
            if 7 < len(input_uid) < 17 : # (uid 8~16자)
                break
            else :
                print('아이디는 8자에서 16자 사이로 입력해주세요')

        while(1):
            input_password = input('비밀번호를 입력하세요 :')
            check_alpha = 0
            check_digit = 0
            for password in input_password:    
                if password.isalpha() == True:
                    check_alpha = 1
                if password.isdigit() == True:
                    check_digit = 1
            if check_alpha==1 & check_digit ==1:
                break
            else :
                print('비밀번호는 숫자와 영문자의 조합으로 입력해주세요')
        while(1) :
            input_age = int(input('나이 : '))
            if input_age < 1 :
                print('태어나신 후에 가입해주세요')
            else :
                break
        input_hobby = input('취미 : ')
        input_hope = input('희망사항 : ')
        Sign_up(input_uid, input_age, input_password, input_hobby, input_hope)
        break
    elif select_menu_01 == 2:
        #로그인
        id = input('아이디를 입력하세요 : ')
        pw = input('비밀번호를 입력하세요 : ')
        flag = 2

        for i in range(len(Student_info.list_dics_info)) :
          if Student_info.list_dics_info[i]['uid'] == id and Student_info.list_dics_info[i]['password'] == pw :
            print(id+"님 어서오세요.")
            flag = 1
            Main_page(i)
            break
          else :
            flag = 0
        
        if flag == 0 :
          print("아이디 또는 비밀번호가 잘못됬습니다")
          
        elif flag != 1 :
          print("오류입니다. 개발자 코드를 확인해주세요")
        break
    else:
        print('잘못 입력하셨습니다. 다시입력하세요~')