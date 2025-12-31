import pandas as pd
import numpy as np

# main.py와 동일한 로직으로 테스트
df = pd.read_excel('매출_플로우교육.xlsx')

print("=== 1단계: 원본 데이터 ===")
print(f"컬럼들: {df.columns.tolist()}")

# 컬럼 매핑
col_mapping = {}
for col in df.columns:
    col_lower = str(col).lower().strip()
    if '연도' in col_lower or 'year' in col_lower or '년' in col_lower:
        col_mapping['연도'] = col
    elif '월' in col_lower or 'month' in col_lower:
        col_mapping['월'] = col
    elif '구분' == col_lower:
        col_mapping['구분'] = col
    elif '수익코드' in col_lower or 'revenue' in col_lower:
        col_mapping['수익코드'] = col
    elif '사업부' in col_lower or 'division' in col_lower:
        col_mapping['사업부'] = col
    elif '브랜드' in col_lower or 'brand' in col_lower:
        col_mapping['브랜드'] = col
    elif '캠퍼스' in col_lower or '지역' in col_lower or 'campus' in col_lower or 'region' in col_lower:
        col_mapping['캠퍼스'] = col

print(f"\n컬럼 매핑: {col_mapping}")

# 매출 컬럼 찾기
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
print(f"\n숫자 컬럼들 (변환 전): {numeric_cols}")

# 매출 관련 컬럼 매핑
for col in df.columns:
    col_lower = str(col).lower().strip()
    if '매출' in col_lower or 'sales' in col_lower:
        if '매출2' in col_lower or 'sales2' in col_lower or '매출 2' in col_lower:
            col_mapping['매출2'] = col
        elif '매출' in col_lower and '매출2' not in col_mapping:
            col_mapping['매출'] = col

print(f"\n매출 컬럼 매핑 후: {col_mapping}")

# 매출 컬럼이 없으면 숫자 컬럼 중 마지막 것 사용
if '매출' not in col_mapping and numeric_cols:
    col_mapping['매출'] = numeric_cols[-1]
    print(f"⚠️ 매출 컬럼을 찾지 못해 마지막 숫자 컬럼 사용: {numeric_cols[-1]}")

sales_col = col_mapping.get('매출')
print(f"\n=== 2단계: 매출 컬럼 변환 전 ===")
print(f"선택된 매출 컬럼: {sales_col}")
print(f"데이터 타입: {df[sales_col].dtype}")
print(f"샘플 (10개):\n{df[sales_col].head(10)}")

# 매출 컬럼을 숫자로 변환
if '매출' in col_mapping:
    if df[col_mapping['매출']].dtype == 'object':
        print(f"\n=== 3단계: object 타입 -> 숫자 변환 ===")
        df[col_mapping['매출']] = df[col_mapping['매출']].apply(
            lambda x: str(x).replace(',', '').replace('원', '').strip()
            if pd.notna(x) and str(x).strip() not in ['-', '']
            else None
        )
        df[col_mapping['매출']] = pd.to_numeric(df[col_mapping['매출']], errors='coerce')
        print(f"변환 후 데이터 타입: {df[col_mapping['매출']].dtype}")
        print(f"변환 후 샘플 (10개):\n{df[col_mapping['매출']].head(10)}")
    elif df[col_mapping['매출']].dtype in ['int64', 'float64']:
        print(f"\n=== 3단계: 이미 숫자 타입이므로 변환 안 함 ===")

# 연도 처리
if '연도' in col_mapping:
    df['연도_처리'] = df[col_mapping['연도']].apply(
        lambda x: int(x) + 2000 if pd.notna(x) and int(x) < 100 else int(x) if pd.notna(x) else None
    )

print(f"\n=== 4단계: 변환 후 숫자 컬럼 확인 ===")
numeric_cols_after = df.select_dtypes(include=[np.number]).columns.tolist()
print(f"숫자 컬럼들 (변환 후): {numeric_cols_after}")

print(f"\n=== 5단계: 최종 통계 ===")
print(f"매출 컬럼: {sales_col}")
print(f"전체 합계: {df[sales_col].sum():,.0f}원")
print(f"평균: {df[sales_col].mean():,.0f}원")
print(f"2025년 12월 데이터만 필터링:")
df_test = df[(df['연도_처리'] == 2025) & (df[col_mapping['월']] == 12)]
print(f"  - 행 수: {len(df_test)}")
print(f"  - 합계: {df_test[sales_col].sum():,.0f}원")
print(f"  - 샘플:\n{df_test[[col_mapping['연도'], col_mapping['월'], sales_col]].head()}")
