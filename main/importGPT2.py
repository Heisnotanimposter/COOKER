# 모듈2: 각종 음식에 대한 영양성분정보를 finetuned 정보에 담는 텍스트파일과 그에 적용할 수 있는 gpt 모델
import torch # 파이토치 라이브러리
from transformers import GPT2Tokenizer, GPT2LMHeadModel # 트랜스포머 라이브러리

# gpt 모델과 토크나이저 불러오기
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.load_state_dict(torch.load("finetuned_model.pth")) # finetuned된 모델의 가중치 불러오기
model.eval() # 평가 모드로 설정

# 음식의 이름을 입력받아 해당 음식의 주요 영양성분을 반환하는 함수 정의
def get_nutrition_info(food_name):
    # 입력된 음식의 이름을 토크나이저로 인코딩하기
    input_ids = tokenizer.encode(food_name, return_tensors="pt")
    # gpt 모델로 텍스트 생성하기
    output_ids = model.generate(input_ids, max_length=20, do_sample=True, top_p=0.95)
    # 생성된 텍스트를 디코딩하기
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    # 생성된 텍스트에서 영양성분 부분만 추출하기
    nutrition_info = output_text.split("\n")[1:]
    # 영양성분을 문자열로 변환하기
    nutrition_info = "\n".join(nutrition_info)
    # 영양성분 반환하기
    return nutrition_info
