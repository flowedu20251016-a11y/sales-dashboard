import pandas as pd
import numpy as np

# main.py와 동일하게 처리
df = pd.read_excel('매출_플로우교육.xlsx')

# 컬럼 매핑
col_mapping = {}
for col in df.columns:
    col_lower = str(col).lower().strip()
    if '연도' in col_lower or 'year' in col_lower or '년' in col_lower:
        col_mapping['연도'] = col
    elif '월' in col_lower or 'month' in col_lower:
        col_mapping['월'] = col
    elif '사업부' in col_lower or 'division' in col_lower:
        col_mapping['사업부'] = col
    elif '브랜드' in col_lower or 'brand' in col_lower:
        col_mapping['브랜드'] = col
    elif '캠퍼스' in col_lower or '지역' in col_lower or 'campus' in col_lower or 'region' in col_lower:
        col_mapping['캠퍼스'] = col

# 매출 컬럼
for col in df.columns:
    col_lower = str(col).lower().strip()
    if '매출' in col_lower or 'sales' in col_lower:
        col_mapping['매출'] = col
        break

sales_col = col_mapping['매출']
print(f"매출 컬럼: {sales_col}")

# 매출 컬럼 변환
if df[sales_col].dtype == 'object':
    df[sales_col] = df[sales_col].apply(
        lambda x: str(x).replace(',', '').replace('원', '').strip()
        if pd.notna(x) and str(x).strip() not in ['-', '']
        else None
    )
    df[sales_col] = pd.to_numeric(df[sales_col], errors='coerce')

# 연도 처리
df['연도_처리'] = df[col_mapping['연도']].apply(
    lambda x: int(x) + 2000 if pd.notna(x) and int(x) < 100 else int(x) if pd.notna(x) else None
)

# NaN 제거
df_clean = df[df[sales_col].notna()].copy()

print(f"\n전체 데이터: {len(df_clean)}행")
print(f"전체 매출 합계: {df_clean[sales_col].sum():,.0f}원")

# 스크린샷과 동일한 조건: 2025년 12월
selected_year = 2025
selected_month = 12

print(f"\n=== 2025년 12월 필터 ===")
main_data = df_clean[(df_clean['연도_처리'] == selected_year) & (df_clean[col_mapping['월']] == selected_month)]
main_sales = main_data[sales_col].sum()
print(f"행 수: {len(main_data)}")
print(f"매출 합계: {main_sales:,.0f}원")
print(f"샘플:\n{main_data[[col_mapping['연도'], col_mapping['월'], sales_col]].head(10)}")

# 2024년 12월
print(f"\n=== 2024년 12월 필터 ===")
comp_data = df_clean[(df_clean['연도_처리'] == 2024) & (df_clean[col_mapping['월']] == 12)]
comp_sales = comp_data[sales_col].sum()
print(f"행 수: {len(comp_data)}")
print(f"매출 합계: {comp_sales:,.0f}원")

# 2023년 12월
print(f"\n=== 2023년 12월 필터 ===")
comp_data2 = df_clean[(df_clean['연도_처리'] == 2023) & (df_clean[col_mapping['월']] == 12)]
comp_sales2 = comp_data2[sales_col].sum()
print(f"행 수: {len(comp_data2)}")
print(f"매출 합계: {comp_sales2:,.0f}원")

# 차이 계산
diff = main_sales - comp_sales
print(f"\n=== 2025 vs 2024 비교 ===")
print(f"2025년: {main_sales:,.0f}원")
print(f"2024년: {comp_sales:,.0f}원")
print(f"증감액: {diff:+,.0f}원")
if comp_sales > 0:
    diff_pct = (diff / comp_sales * 100)
    print(f"증감률: {diff_pct:+.1f}%")
