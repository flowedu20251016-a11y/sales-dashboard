# 📊 매출 대시보드

Streamlit 기반 매출 분석 및 시각화 대시보드입니다.

## 주요 기능

- 📈 월별 매출 추세 분석
- 📊 전년 대비 매출 비교
- 🔄 동기간 매출 비교
- 📉 누적 매출 분석
- 🎯 카테고리별 매출 분석 (사업부, 브랜드, 캠퍼스)
- 🤖 AI 기반 매출 현황 분석

## 설치 방법

1. 저장소 클론
```bash
git clone <repository-url>
cd chart
```

2. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

## 실행 방법

```bash
streamlit run main.py
```

브라우저에서 자동으로 http://localhost:8501 이 열립니다.

## 사용 방법

1. 사이드바에서 엑셀 또는 CSV 파일 업로드
2. 기간 선택 (연도, 월)
3. 비교 기간 선택
4. 추가 필터 적용 (사업부, 브랜드, 캠퍼스)
5. 대시보드에서 다양한 매출 분석 확인

## 데이터 형식

업로드하는 파일은 다음 컬럼을 포함해야 합니다:
- 연도 (또는 year, 년)
- 월 (또는 month)
- 매출 (또는 sales)
- 사업부 (선택사항)
- 브랜드 (선택사항)
- 캠퍼스/지역 (선택사항)

## 기술 스택

- Python 3.8+
- Streamlit
- Pandas
- Plotly
- NumPy

## 라이선스

MIT License

## 개발자

Created with Claude Code
