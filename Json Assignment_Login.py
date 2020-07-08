import json

def main_page(json_student) :
    # 2. 관련 데이터 별로 출력해보기! (각각을 하나의 함수로!)
    # - 학생 이름 전부 출력해보기
    # - 20살 미만 학생 open의 쓰기모드를 활용하여 넣어보기
    # - 성인이 아닌 학생 출력하기 (20세 미만..)
    # - 조건문으로 아이디를 안넣으면 쓰기 안되게 막아보기
    # - 모든 로직은 open 을 최대한 활용하기 !
    while(1):
        print('=========== 정보보기 ===========')
        print('1. 전교생 정보 확인')
        print('2. 미성년자 확인')
        print('0. 나가기')

        select_menu_02 = int(input('메뉴를 선택하세요 : '))

        if select_menu_02 == 1:
            show_all(json_student)
        elif select_menu_02 == 2:
            show_kid(json_student)
        elif select_menu_02 == 0:
            print('페이지에서 로그아웃하여 프로그램을 종료합니다')
            break
        else :
            print('다시 입력해주세요')

def login_student(json_student):
    count = 0
    while(1) :
        id = input('아이디를 입력하세요 : ')
        pw = input('비밀번호를 입력하세요 : ')
        flag = 2

        for i in range(len(json_student)) :
            if json_student[i]['uid'] == id and json_student[i]['password'] == pw :
                print(id+"님 어서오세요")
                flag = 1
                main_page(json_student)
                break
            else :
                flag = 0
        
        if flag == 0 :
            count += 1
            if count < 5 :
                print("아이디 또는 비밀번호가 잘못됬습니다")             
            else :
                print("입력정보가 5회 이상 잘못되었습니다\n프로그램을 종료합니다")
                break
        elif flag != 1 :
            print("개발오류입니다\n개발자 코드를 확인해주세요")
            break

def show_all(json_student):
    print("모든 학생들의 :")
    for i in range(0,len(json_student)):
        print(json_student[i])

def show_kid(json_student):
    print("20살 미만 학생 정보 출력 : ")
    for i in range(0,len(json_student)): # 20살 미만 이름정보 출력
        if(json_student[i]["age"]< 20 ):
             print(json_student[i])

def new_student(json_student, file_path):
    while(1):
        uid = input("UID : ")
        if uid == "" : #공백정보
            print("아이디가 입력되지 않았습니다")
            continue
        elif 7<len(uid)<17 :
            break
        else :
            print("아이디는 8~16자로 입력해야 합니다")
            continue
    while(1) :
        password = input("PW : ")
        if password == "" : #공백정보
            print("비밀번호가 입력되지 않았습니다")
            continue
        check_alpha = 0
        check_digit = 0
        for pw in password:    
            if pw.isalpha() == True:
                check_alpha = 1
            if pw.isdigit() == True:
                check_digit = 1
            if check_alpha==1 & check_digit ==1:
                break
        
        if check_alpha==1 & check_digit==1:
            break    
        else :
            print('비밀번호는 숫자와 영문자의 조합으로 입력해주세요')

    while(1) :
        age = int(input("나이 : "))
        if age < 1 :
            print('태어나신 후에 가입해주세요')
        else :
            break

    json_student.append({"uid" : uid , "password" : password, "age" : age})
    print("OK!")
    with open(file_path,'w',encoding ="UTF8") as json_rewrite:
        json.dump(json_student,json_rewrite,ensure_ascii=False,indent="\t")

    main_page(json_student)


#-----------------------------------------------------------------------------

file_path = "./students_info.json"

with open(file_path,encoding ="UTF8") as json_file:
    json_student = json.load(json_file)

print('=========== 메 뉴 ===========')
print('1. 회원가입')
print('2. 로그인')
print('3. 종료')

select_menu_01 = int(input('메뉴를 선택하세요 : '))

while(1) :
    if select_menu_01 == 1:
        new_student(json_student, file_path) # 새로운 학생 추가
        break
    elif select_menu_01 == 2:
        login_student(json_student)
        break
    elif select_menu_01 == 0:
        print('프로그램을 종료합니다')
        break
    else :
        print('다시 선택해주세요')

