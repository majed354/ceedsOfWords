"""Build index.html at the repo root from src/families.json and src/template.html.
Run from the repo root:  python3 src/build.py
"""
import json, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = os.path.join(root, 'src')
data = json.load(open(os.path.join(src, 'families.json')))
audio = json.load(open(os.path.join(src, 'audio_manifest.json')))
page = open(os.path.join(src, 'template.html')).read()
page = page.replace('/*__DATA__*/', json.dumps(data, ensure_ascii=False)).replace('/*__AUDIO__*/', json.dumps(audio, separators=(',', ':')))
head = open(os.path.join(src, 'head.html')).read()
i = page.index('</style>') + len('</style>')
open(os.path.join(root, 'index.html'), 'w').write(head + page[:i] + '\n</head>\n<body>\n' + page[i:] + '\n</body>\n</html>\n')
print('built index.html')
