# 학교 건물 피난 통로 구조 안전 진단 프로그램
# 이름 또는 학번:
# 프로젝트 주제: 학교 건물의 대피 통로 안전 점검

# =====================================================================
# 1단계: 데이터 구조 정의 (2차원 리스트)
# 구조: [구역 이름, 복도 너비(cm), 문의 개수, 대피 계단까지의 거리(m)]
# =====================================================================
school_zones = [
    ["3층 2학년 교실복도", 120, 2, 15],
    ["2층 본관-신관 연결통로", 100, 1, 35],
    ["1층 급식실 나가는 통로", 240, 3, 10],
    ["4층 동아리실 복도", 150, 1, 28]
]

# =====================================================================
# 2단계: 함수 정의하기
# =====================================================================

def show_menu(zones):
    print("\n--- [학교 건축 구조 안전 진단 대상 목록] ---")
    for i in range(len(zones)):
        print(f"{i + 1}. {zones[i][0]}")
    print("--------------------------------------------")


def check_safety(zone, students):
    name = zone[0]
    width = zone[1]
    doors = zone[2]
    distance = zone[3]

    score = 100

    # 거리 감점: 25m 초과 시 초과 1m마다 2점 감점
    if distance > 25:
        score -= (distance - 25) * 2

    # 문 병목 감점: 학생/문 > 10명일 때 초과 1명당 3점 감점
    if doors > 0 and (students / doors) > 10:
        score -= (students / doors - 10) * 3

    # 복도 너비 감점
    if width < 120:
        score -= 10
    elif width < 150:
        score -= 5

    # 점수 범위 제한
    if score < 0:
        score = 0
    elif score > 100:
        score = 100

    # 안전 등급
    if score >= 80:
        grade = "안전"
    elif score >= 60:
        grade = "주의"
    else:
        grade = "위험"

    return round(score), grade


def print_report(zone, students, score, grade):
    print("\n============================================")
    print(f"      🏢 건축 피난 구조 진단서 [{zone[0]}]")
    print("============================================")
    print(f"▶ 현재 대피 유도 인원: {students}명")
    print(f"▶ 설계 정보 - 복도 너비: {zone[1]}cm | 문 개수: {zone[2]}개 | 계단 거리: {zone[3]}m")
    print("--------------------------------------------")
    print(f"▶ 구조 안전 점수: {score}점 / 100점")
    print(f"▶ 종합 적합성 등급: [{grade}]")
    print("--------------------------------------------")
    print("💡 건축학적 피드백:")

    if grade == "안전":
        print(" -> 현 건축 구조는 피난 동선 및 수용 인원에 적합하게 설계되었습니다.")
    elif grade == "주의":
        print(" -> 대피 거리가 길거나 병목 위험이 있습니다. 대피 유도 표지판을 증설하세요.")
    else:
        print(" -> [구조 개선 권고] 인원 대비 통로가 취약합니다. 피난 분산 계획을 재수립하십시오.")
    print("============================================\n")


# =====================================================================
# 3단계: 메인 프로그램 흐름 제어 (반복문과 입력)
# =====================================================================
print("🏫 학교 건물 피난 통로 구조 적합성 진단 프로그램을 시작합니다.")

while True:
    show_menu(school_zones)

    try:
        choice = int(input("진단할 구역의 번호를 선택하세요 (종료하려면 0 입력): "))
    except ValueError:
        print("숫자를 입력해주세요. 다시 시도합니다.")
        continue

    if choice == 0:
        print("프로그램을 종료합니다. 안전한 하루 되세요!")
        break

    if choice < 1 or choice > len(school_zones):
        print("잘못된 선택입니다. 목록에 있는 번호를 입력해주세요.")
        continue

    selected_zone = school_zones[choice - 1]

    try:
        students_count = int(input(f"현재 [{selected_zone[0]}]에 있는 인원수를 입력하세요(명): "))
    except ValueError:
        print("올바른 숫자를 입력해주세요. 다시 시도합니다.")
        continue

    final_score, final_grade = check_safety(selected_zone, students_count)
    print_report(selected_zone, students_count, final_score, final_grade)