
import pandas as pd


def 정제(df):
    print("시작        ", len(df))

    # 1. 점수가 비어 있는 행 삭제
    df = df.dropna(subset=["점수"])
    print("빈 칸 제거  ", len(df))

    # 2. 완전히 같은 중복 행 삭제
    df = df.drop_duplicates()
    print("중복 제거   ", len(df))

    # 3. 반과 과목의 앞뒤 공백 제거
    df["반"] = df["반"].str.strip()
    df["과목"] = df["과목"].str.strip()

    # 4. 점수가 0~100 범위인 행만 남기기
    df = df[(df["점수"] >= 0) & (df["점수"] <= 100)]
    print("범위 밖 제거", len(df))

    return df
def 반별평균(df):
    return df.groupby("반")["점수"].mean().round(1)