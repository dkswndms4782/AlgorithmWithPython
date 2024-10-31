import re

# HTML에서 <div>와 제목을 추출하는 정규식 패턴
div_pattern = re.compile(r'<div title="([^"]+)">(.*?)</div>', re.DOTALL)
# <p> 태그 안의 텍스트를 추출하는 패턴
p_pattern = re.compile(r'<p>(.*?)</p>', re.DOTALL)
# 태그를 제거하는 패턴
tag_pattern = re.compile(r'<[^>]+>')

# 전체 HTML 입력 받기
html_text = input().strip()

# <div> 태그에 따른 각 문단 처리
for div_match in div_pattern.finditer(html_text):
    title = div_match.group(1)
    content = div_match.group(2)
    print(f"title : {title}")
    
    # 각 <p> 태그의 내용 처리
    for p_match in p_pattern.finditer(content):
        sentence = p_match.group(1)
        sentence = tag_pattern.sub('', sentence)  # 내부 태그 제거
        sentence = re.sub(r'\s+', ' ', sentence).strip()  # 불필요한 공백 정리
        print(sentence)
