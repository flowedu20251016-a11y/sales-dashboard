import pandas as pd
import numpy as np

# 파일 읽기
df = pd.read_excel('매출_플로우교육.xlsx')

# 매출 컬럼 찾기
sales_col = [c for c in df.columns if '매출' in str(c).lower()][0]

print(f'원본 데이터 타입: {df[sales_col].dtype}')
print(f'원본 샘플 (10개):')
print(df[sales_col].head(10))

# 변환
df[sales_col] = df[sales_col].apply(
    lambda x: str(x).replace(',', '').replace('원', '').strip()
    if pd.notna(x) and str(x).strip() not in ['-', '']
    else None
)
df[sales_col] = pd.to_numeric(df[sales_col], errors='coerce')

print(f'\n변환 후 데이터 타입: {df[sales_col].dtype}')
print(f'변환 후 샘플 (10개):')
print(df[sales_col].head(10))

print(f'\n변환 후 통계:')
print(f'전체 합계: {df[sales_col].sum():,.0f}원')
print(f'평균: {df[sales_col].mean():,.0f}원')
print(f'최대: {df[sales_col].max():,.0f}원')
print(f'최소: {df[sales_col].min():,.0f}원')
print(f'NaN 개수: {df[sales_col].isna().sum()}개')
