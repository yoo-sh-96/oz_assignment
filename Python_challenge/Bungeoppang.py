class BungeoppangShop: # BungeoppangShop 클래스 생성

    def __init__(self): # __init__이란 객체 생성시 자동으로 실행되는 생성자 매서드 / 매개변수에 self는 자기자신을 가리키기 위해서
        self.stock = {"팥붕어빵": 10, "슈크림붕어빵": 8, "초코붕어빵": 5} #초기 재고상태
        self.prices = {"팥붕어빵": 1000, "슈크림붕어빵": 1200, "초코붕어빵": 1500} # 가격
        self.sales = {"팥붕어빵": 0, "슈크림붕어빵": 0, "초코붕어빵": 0} # 초기 판매개수

    def menu_list(self): # menu_list 호출 시 밑의 print문 실행
        print(f'----------\n메뉴판\n{self.prices}')

    def check_stock(self):
        print("----------\n현재 재고")
        for i in self.stock: # self.stock 딕셔너리의 키값을 하나씩 i에 담아 반복한다.
            print(f'{i} {self.stock[i]}개') # i는 키값, self.stock[i]는 해당 키값의 벨류 ex) i=팥붕어빵, self.stock[i] = self.stock["팥붕어빵"]이므로 10

    def process_order(self, bread_type, bread_count):
        try: # 예외처리문
            if bread_count == '취소': # bread_count가 취소라면 return으로 함수 종료
                return
            bread_count = int(bread_count) # 여기서 오류 발생시 except로 이동
        except ValueError: #위에서 정수가 아닌 다른형태로 입력 시 ValueError 발생으로 밑의 print문 실행 및 return으로 종료
            print("잘못된 입력입니다. 숫자로 적어주세요.")
            return

        else:
            if self.stock[bread_type] >= bread_count: # bread_type과 count는 아래 프린트문에서 입력되는 값과 연결 / self.stock[bread_type]의 벨류값이 count보다 클 경우 실행
                self.stock[bread_type] -= bread_count # 주문한 개수만큼 재고 감소
                self.sales[bread_type] += bread_count # 주문한 개수만큼 판매량 증가
                print(f'----------\n판매완료\n{bread_type}이 {bread_count}개 판매되었습니다.')
                print(f'----------\n총 판매량\n{self.sales}')

            elif self.stock[bread_type] < bread_count: # 재고가 주문량보다 작을 시 실행
                print("재고가 모자랍니다.")

    def admin_mode(self, bread_type, add_stock): # 관리자 모드 
        if add_stock == '뒤로': #뒤로 입력 시 return으로 함수 종료
            return

        try: # 예외처리 문
            self.stock[bread_type] += int(add_stock) # add_stock 만큼 재고개수 증가
        except ValueError: # 위의 값이 정수가아니면 실행
            print("잘못된 입력입니다. 숫자로 적어주세요.")
        else:
            print(f'----------\n재고주문\n{bread_type}이 {add_stock}개 만큼 증가했습니다.')

        self.check_stock() # 현재재고 상태 호출

    def calculate_total_sales(self): # 총 매출 계산 함수
        total_sales = sum(self.sales[i] * self.prices[i] for i in self.prices) # i=self.prices의 키값 / 총매출 = 각각의 판매개수 * 가격을 더한 값
        """
        total_sales = 0
        for i in prices:
            total_sales += self.sales[i] * prices[i]
            total_sales = total_sales + 
        """
        print(f'----------\n총 매출\n{total_sales}원 입니다.')


    def main(self): # 메인모드

        while True: # while문은 트루일때 실행
            check_mode = ["메뉴", "주문", "관리자", "종료"]
            mode = input("모드|메뉴, 주문, 관리자, 종료|") # input으로 모드 선택

            if not mode in check_mode: # check_mode안에 input으로 입력한 값이 없을때 '잘못된 모드입니다.'출력
                print("\n잘못된 모드입니다.")

            else: # 위 if문에서 실행이 안되면
                if mode == "종료": # 모드 선택에서 종료 입력 시
                    self.calculate_total_sales() # 총 매출 함수를 출력하고 밑의 print문 실행 및 break로 종료
                    print("\n시스템이 종료됩니다.")
                    break

                if mode == "메뉴": # 메뉴 모드 선택 시
                    self.menu_list() # 메뉴판 함수 호출

                if mode == "주문": # 주문 모드 선택 시
                    while True: # while문 실행
                        bread_type = input("메뉴를 입력해주세요(메뉴판|팥붕어빵, 슈크림붕어빵, 초코붕어빵, 뒤로|") # bread_type 입력창 생성
                        if bread_type == '뒤로': # 뒤로 선택 시 break 실행으로 while문 종료
                            break
                        if not bread_type in self.stock.keys(): # self.stock 키값에 없는 bread_type이면 "없는 메뉴입니다." 출력
                            print('없는 메뉴입니다.')
                            continue # 계속 실행
                        bread_count = input("메뉴 개수를 입력해주세요. 취소하고 싶으시면 '취소'버튼을 눌러주세요") # 입력창 생성
                        self.process_order(bread_type, bread_count)  # 위의 process_order 함수를 호출

                if mode == "관리자": # 관리자 모드 선택 시
                    while True:
                        admin = input("관리자 모드|재고추가, 재고확인, 뒤로|") # 관리자모드 선택창 생성

                        if admin == "재고추가": # 재고추가 입력 시
                            while True:
                                admin_bread_type = input("추가할 재고 메뉴를 입력해주세요|팥붕어빵, 슈크림붕어빵, 초코붕어빵, 뒤로|") # 입력창 생성
                                if admin_bread_type == '뒤로': # 뒤로 입력 시 break로 종료
                                    break
                                if not admin_bread_type in self.stock.keys(): # self.stock 키값에 없는 admin_bread_type이면 "없는 메뉴입니다." 출력
                                    print('없는 메뉴입니다.')
                                    continue
                                add_stock =  input("얼마나 추가할지 입력해주세요. 뒤로 가길 원하시면 '뒤로'버튼을 눌러주세요") # 입력창을 생성하고
                                self.admin_mode(admin_bread_type, add_stock) # admin_mode 함수 호출

                        if admin == "재고확인": # 재고확인 입력 시
                            self.check_stock() # 재고 상태 호출

                        if admin == '뒤로': # 뒤로 입력 시 
                            break # 종료


bbshop = BungeoppangShop() # BungeoppangShop 클래스의 객체 생성 / 객체 생성으로 처음의 __init__설명과 이어짐, 즉 bbshop = BungeoppangShop() 이걸로 init안의 내용이 자동 실행

if __name__ == "__main__": # 이부분은 지피티로 찾아봐도 이해가 힘듭니다..
     bbshop.main() # 메인 함수 실행
