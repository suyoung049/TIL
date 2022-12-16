def save(request):
    lsit_1 = [
        "야구",
        "클라이밍",
        "등산",
        "테니스",
        "트래킹",
        "볼링",
        "러닝",
        "스키",
        "보드",
        "헬스",
        "산책",
        "플로깅",
        "자전거",
        "서핑",
        "배드민턴",
        "탁구",
        "골프",
        "스포츠경기",
    ]
    list_2 = [
        "복합문화공간",
        "테마파크",
        "피크닉",
        "드라이브",
        "캠핑",
        "국내여행",
        "해외여행",
    ]
    list_3 = [
        "전시",
        "영화",
        "뮤지컬",
        "공연",
        "디자인",
        "박물관",
        "연극",
        "콘서트",
        "연주회",
        "페스티벌",
    ]

    list_4 = [
        "맛집투어",
        "카페",
        "와인",
        "커피",
        "디저트",
        "맥주",
        "티룸",
        "비건",
        "파인다이닝",
        "요리",
        "페어링",
        "칵테일",
        "위스키",
        "전통주",
    ]
    list_5 = [
        "습관만들기",
        "챌린지",
        "독서",
        "스터디",
        "외국어",
        "재테크",
        "브랜딩",
        "커리어",
        "사이드프로젝트",
    ]
    for i in range(len(lsit_1)):
        tag = Tag()
        tag.tag = lsit_1[i]
        tag.category = "sports"
        tag.save()

    for i in range(len(list_2)):
        tag = Tag()
        tag.tag = list_2[i]
        tag.category = "travel"
        tag.save()
    for i in range(len(list_3)):
        tag = Tag()
        tag.tag = list_3[i]
        tag.category = "art"
        tag.save()
    for i in range(len(list_4)):
        tag = Tag()
        tag.tag = list_4[i]
        tag.category = "food"
        tag.save()
    for i in range(len(list_5)):
        tag = Tag()
        tag.tag = list_5[i]
        tag.category = "develop"
        tag.save()

    return redirect("main")