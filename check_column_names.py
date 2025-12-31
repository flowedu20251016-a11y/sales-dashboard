import pandas as pd

df = pd.read_excel('매출_플로우교육.xlsx')

print("=== 컬럼명 상세 확인 ===")
for i, col in enumerate(df.columns):
    print(f"{i}: '{col}'")
    print(f"   - 타입: {type(col)}")
    print(f"   - 길이: {len(str(col))}")
    print(f"   - repr: {repr(col)}")
    print(f"   - lower: '{str(col).lower()}'")
    print(f"   - '매출' in lower: {'매출' in str(col).lower()}")
    print()
