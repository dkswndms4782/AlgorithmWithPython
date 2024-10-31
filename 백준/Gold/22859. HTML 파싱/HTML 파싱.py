import re

text = input()
div_pattern = re.compile(r'<div title="([^"]+)">(.*?)</div>', re.DOTALL)
p_pattern = re.compile(r'<p>(.*?)</p>', re.DOTALL)
del_pattern = re.compile(r'<[^>]+>')

for match in div_pattern.finditer(text):
    title = match.group(1)
    sentence = match.group(2)
    print(f"title : {title}")
    for sen_match in p_pattern.finditer(sentence):
        value = del_pattern.sub('', sen_match.group(1))
        value = re.sub(r'\s+', ' ', value).strip()
        print(value)

