from fastapi import FastAPI
import random
from uuid import uuid4

app = FastAPI()

adjectives = ["행복한", "슬픈", "화난", "미친", "재밌는", "게으른", "욕심많은", "잠꾸러기", "친절한", "무례한"]
nouns = ["강아지", "고양이", "새", "말", "물고기", "뱀", "사자", "호랑이", "코끼리", "원숭이", "소"]


@app.get("/users/nickname")
def get_nickname() -> dict[str, str]:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    nickname = f"{adjective} {noun} {str(uuid4())[:8]}"
    return {"nickname": nickname}


@app.post("/users/id/existence")
def exist_user_id(request: dict):
    existing_ids = set()  # 이미 생성된 ID들을 저장하는 set
    user_id = request.get("userId")

    # 중복 검사 로직
    if user_id in existing_ids:
        return {"result": True}
    else:
        existing_ids.add(user_id)
        return {"result": False}


# @app.post("/users/sign-up")
# def sign_up(request: dict):
#     # 회원가입 로직
#     user_id = request.get('userId')
#     nickname = request.get('nickname')
#     password = request.get('password')
#     existing_ids = set() # 이미 생성된 ID들을 저장하는 set

#     # 중복 검사 로직
#     if user_id in existing_ids:
#         return {"result": False, "message": "User ID already exists."}

#     # 닉네임 검사 로직
#     if not is_valid_nickname(nickname):
#         return {"result": False, "message": "Invalid nickname format."}

#     # 비밀번호 검사 로직
#     if not is_valid_password(password):
#         return {"result": False, "message": "Invalid password format."}

#     # 회원 정보 저장 로직
#     save_user_info(user_id, nickname, password)
#     existing_ids.add(user_id)
#     return {"result": True, "message": "Sign up successful."}
