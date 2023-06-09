from fastapi import APIRouter, Body
import random
from uuid import uuid4

router = APIRouter()

adjectives = ["행복한", "슬픈", "화난", "미친", "재밌는", "게으른", "욕심많은", "잠꾸러기", "친절한", "무례한"]
nouns = ["강아지", "고양이", "새", "말", "물고기", "뱀", "사자", "호랑이", "코끼리", "원숭이", "소"]


@router.get("/nickname")
def get_nickname() -> dict[str, str]:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    nickname = f"{adjective} {noun} {str(uuid4())[:8]}"
    return {"nickname": nickname}


@router.post("/existence")
def exist_user_id(user_id: str = Body(embed=True)):
    existing_ids = set()  # 이미 생성된 ID들을 저장하는 set

    # 중복 검사 로직
    if user_id in existing_ids:
        return {"result": True}
    else:
        existing_ids.add(user_id)
        return {"result": False}
