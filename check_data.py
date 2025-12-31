import pandas as pd
import numpy as np

# 파일 읽기
df = pd.read_excel('매출_플로우교육.xlsx')

print('=== 컬럼명 ===')
print(df.columns.tolist())

print('\n=== 데이터 타입 ===')
print(df.dtypes)

print('\n=== 상위 10개 데이터 ===')
print(df.head(10))

# 매출 컬럼 찾기
sales_cols = [c for c in df.columns if '매출' in str(c).lower()]
print(f'\n=== 매출 관련 컬럼: {sales_cols} ===')

if sales_cols:
    for sales_col in sales_cols:
        print(f'\n--- {sales_col} 컬럼 분석 ---')
        print(f'데이터 타입: {df[sales_col].dtype}')
        print(f'샘플 데이터 (상위 20개):')
        print(df[sales_col].head(20))
        print(f'\n실제 값 타입 확인 (첫 5개):')
        for i in range(min(5, len(df))):
            val = df[sales_col].iloc[i]
            print(f'{i}: {val} (type: {type(val)}, repr: {repr(val)})')

        # 숫자로 변환 시도
        print(f'\n변환 테스트:')
        if df[sales_col].dtype == 'object':
            test_val = df[sales_col].iloc[0]
            print(f'원본: {test_val}')
            cleaned = str(test_val).replace(',', '').replace('원', '').strip()
            print(f'쉼표/원 제거 후: {cleaned}')
            try:
                numeric = pd.to_numeric(cleaned)
                print(f'숫자 변환 후: {numeric}')
            except Exception as e:
                print(f'변환 에러: {e}')

        print(f'\n통계:')
        print(f'전체 합계: {df[sales_col].sum()}')
        print(f'평균: {df[sales_col].mean()}')
        print(f'최대: {df[sales_col].max()}')
        print(f'최소: {df[sales_col].min()}')

print('\n=== 숫자 컬럼들 ===')
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
print(numeric_cols)
