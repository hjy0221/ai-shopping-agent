import streamlit as st
import google.generativeai as genai
import requests
import json
import re

# --- 1. 페이지 설정  ---
st.set_page_config(
    page_title="AI 쇼핑",
    layout="wide",
    page_icon="🛍️"
)

# --- 수정된 2. 사이드바 & 비밀 키 설정 ---
# --- 2. 사이드바: API 키 설정 (하이브리드 방식) ---
with st.sidebar:
    st.header("🔐 API 키 설정")
    
    # 1. Google API Key 처리
    try:
        # 서버(secrets)에 키가 있는지 먼저 확인
        if "GOOGLE_API_KEY" in st.secrets:
            google_api_key = st.secrets["GOOGLE_API_KEY"]
            st.success("✅ Google Key: 서버 설정됨")
        else:
            # secrets 파일은 있는데 키가 없는 경우
            google_api_key = st.text_input("Google API Key", type="password")
    except FileNotFoundError:
        # secrets 파일 자체가 없는 경우 (로컬, 다른 사용자)
        google_api_key = st.text_input("Google API Key", type="password")

    # 2. Naver API Keys 처리
    try:
        if "NAVER_CLIENT_ID" in st.secrets and "NAVER_CLIENT_SECRET" in st.secrets:
            naver_client_id = st.secrets["NAVER_CLIENT_ID"]
            naver_client_secret = st.secrets["NAVER_CLIENT_SECRET"]
            st.success("✅ Naver Key: 서버 설정됨")
        else:
            naver_client_id = st.text_input("Naver Client ID", type="password")
            naver_client_secret = st.text_input("Naver Client Secret", type="password")
    except FileNotFoundError:
        naver_client_id = st.text_input("Naver Client ID", type="password")
        naver_client_secret = st.text_input("Naver Client Secret", type="password")
    
    st.markdown("---")
    st.caption("키가 없으면 작동하지 않습니다.")

# Gemini 설정
genai.configure(api_key=google_api_key)

# --- 3. 네이버 쇼핑 검색 함수 ---
def search_naver_shopping(keyword, display=20):
    url = "https://openapi.naver.com/v1/search/shop.json"
    headers = {
        "X-Naver-Client-Id": naver_client_id,
        "X-Naver-Client-Secret": naver_client_secret
    }
    params = {
        "query": keyword,
        "display": display,
        "sort": "sim"  # 정확도순
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json().get('items', [])
        else:
            st.error(f"네이버 API 오류: {response.status_code}")
            return []
    except Exception as e:
        st.error(f"통신 오류 발생: {e}")
        return []

# --- 4. Gemini: 질문 분석 및 팁 생성 함수 ---
def analyze_query_with_gemini(user_query):
    model = genai.GenerativeModel('gemini-2.5-flash-lite')
    prompt = f"""
    당신은 전문 쇼핑 큐레이터입니다. 사용자의 요청을 분석해서 네이버 쇼핑에 검색할 '최적의 키워드' 1개와 '쇼핑 팁'을 알려주세요.
    
    사용자 요청: "{user_query}"
    
    응답은 반드시 아래 JSON 형식으로만 해주세요:
    {{
        "search_keyword": "네이버에 검색할 단어 (명사 위주)",
        "shopping_tip": "사용자에게 도움되는 따뜻한 조언 한 문장"
    }}
    """
    
    try:
        response = model.generate_content(prompt, generation_config={"response_mime_type": "application/json"})
        return json.loads(response.text)
    except Exception as e:
        st.error(f"AI 분석 중 오류가 발생했습니다: {e}")
        return {"search_keyword": user_query, "shopping_tip": "AI 조언을 불러오지 못했습니다."}

# --- 5. HTML 태그 제거 함수 (네이버 결과 정제용) ---
def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

# --- 6. 메인 화면 UI ---
st.title("🛍️ AI 스마트 쇼핑")
st.markdown("##### 무엇이든 물어보세요! Gemini가 분석하고 네이버에서 찾아옵니다.")

# 검색창
col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    query = st.text_input("검색어 입력", placeholder="예: 요즘 유행하는 30대 남자 집들이 선물 추천해줘", key="search_input")

if query:
    st.divider()
    
    with st.spinner("🤖 Gemini가 고민 중..."):
        # 1. AI 분석
        ai_result = analyze_query_with_gemini(query)
        keyword = ai_result.get("search_keyword", query)
        tip = ai_result.get("shopping_tip", "")
        
    with st.spinner(f"🔍 네이버에서 '{keyword}' 찾는 중..."):
        # 2. 네이버 검색
        items = search_naver_shopping(keyword)

    # --- 결과 화면 ---
    
    # AI 조언 섹션
    st.success(f"💡 **AI의 쇼핑 TIP:** {tip}")
    st.caption(f"적용된 검색어: {keyword}")
    
    st.markdown("### 🛒 검색 결과")
    
    if not items:
        st.warning("검색 결과가 없습니다.")
    else:
        # PC 화면에 맞게 4열 그리드로 배치
        cols = st.columns(4)
        for i, item in enumerate(items):
            with cols[i % 4]:
                with st.container(border=True):
                    # 상품 이미지
                    st.image(item['image'], use_container_width=True)
                    
                    # 상품명 (HTML 태그 제거)
                    title = clean_html(item['title'])
                    st.markdown(f"**{title}**")
                    
                    # 가격 및 카테고리
                    price = int(item['lprice'])
                    st.markdown(f"💰 **{price:,}원**")
                    st.caption(f"{item['category1']} > {item['category2']}")
                    
                    # 구매 링크 버튼
                    st.link_button("구매하러 가기", item['link'], use_container_width=True)

# 하단 푸터
st.markdown("---")
st.caption("Powered by Google Gemini & Naver Search API")
