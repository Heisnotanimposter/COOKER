# 모듈3: 사용자가 입력한 정보에 따라 영양정보를 출력하는 모듈
import module1 as m1 # 모듈1 임포트
import module2 as m2 # 모듈2 임포트
import pandas as pd # 판다스 라이브러리
import matplotlib.pyplot as plt # 맷플롯립 라이브러리

# 사용자가 입력한 음식의 이름을 모듈1에서 받아오는 함수 정의
def get_food_name():
    # 모듈1에서 엔트리에서 음식 이름 가져오기
    food_name = m1.entry.get()
    # 음식 이름 반환하기
    return food_name

# 사용자가 입력한 음식의 이름을 모듈2에 전달하고, 모듈2에서 반환된 영양정보를 받아오는 함수 정의
def get_nutrition_info():
    # 사용자가 입력한 음식의 이름을 가져오기
    food_name = get_food_name()
    # 모듈2에서 영양정보 가져오기
    nutrition_info = m2.get_nutrition_info(food_name)
    # 영양정보 반환하기
    return nutrition_info

# 받아온 영양정보를 적절한 형식으로 가공하는 함수 정의
def process_nutrition_info():
    # 영양정보 가져오기
    nutrition_info = get_nutrition_info()
    # 영양정보를 데이터프레임으로 변환하기
    df = pd.DataFrame([nutrition_info.split("\n")])
    # 데이터프레임의 컬럼 이름 설정하기
    df.columns = ["영양성분", "1인분(100g)당"]
    # 데이터프레임의 인덱스 설정하기
    df.index = [get_food_name()]
    # 데이터프레임의 값들을 숫자로 변환하기
    df["1인분(100g)당"] = df["1인분(100g)당"].str.replace("kcal", "").str.replace("g", "").astype(float)
    # 데이터프레임 반환하기
    return df

# 가공된 영양정보를 표나 그래프로 시각화하는 함수 정의
def visualize_nutrition_info():
    # 데이터프레임 가져오기
    df = process_nutrition_info()
    # 표로 출력하기
    print(df)
    # 그래프로 출력하기
    df.plot(kind="bar", title="음식의 영양성분 비교")
    plt.show()

# 가공된 영양정보를 모듈1에 전달하고, 모듈1에서 화면에 출력하는 함수 정의
def display_nutrition_info():
    # 시각화된 영양정보 가져오기
    nutrition_info = visualize_nutrition_info()
    # 모듈1에서 텍스트 박스에 영양정보 출력하기
    m1.text.delete(1.0, tk.END) # 텍스트 박스 비우기
    m1.text.insert(tk.END, nutrition_info) # 텍스트 박스 채우기
