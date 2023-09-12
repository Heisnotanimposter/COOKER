 # 모듈1: 사용자에게 보여주는 프론트엔드
import tkinter as tk # GUI 라이브러리
import module2 as m2 # 모듈2 임포트

# GUI 생성
window = tk.Tk()
window.title("음식 영양정보 조회")
window.geometry("300x200")

# 라벨 생성
label1 = tk.Label(window, text="음식 이름을 입력하세요:")
label1.pack()

# 엔트리 생성
entry = tk.Entry(window)
entry.pack()

# 텍스트 박스 생성
text = tk.Text(window)
text.pack()

# 버튼 클릭 이벤트 함수 정의
def button_click():
    # 엔트리에서 음식 이름 가져오기
    food_name = entry.get()
    # 모듈2에서 영양정보 가져오기
    nutrition_info = m2.get_nutrition_info(food_name)
    # 텍스트 박스에 영양정보 출력하기
    text.delete(1.0, tk.END) # 텍스트 박스 비우기
    text.insert(tk.END, nutrition_info) # 텍스트 박스 채우기

# 버튼 생성
button = tk.Button(window, text="조회하기", command=button_click)
button.pack()

# GUI 실행
window.mainloop()
