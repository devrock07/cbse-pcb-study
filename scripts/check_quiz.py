"""Validate source links, single-answer shape, chapter coverage and offline packaging."""
from pathlib import Path
import json,collections,re
R=Path(__file__).resolve().parents[1]
def read(name):
 return json.loads((R/'dist'/name).read_text(encoding='utf8').split('=',1)[1].strip().removesuffix(';'))
d=read('data.js');q=read('quiz-data.js');rows=q['questions']
assert len({x['id'] for x in rows})==len(rows)
assert len({p['id'] for p in q['papers']})==156
chapters={c['id'] for c in d['chapters']};worked={x['id'] for x in d['questions']}
for x in rows:
 assert x['chapter'] in chapters
 assert len(x['options'])==4 and len(set(x['options']))==4
 assert isinstance(x['answer'],int) and 0<=x['answer']<4
 assert x['explanation'].strip() and x['prompt'].strip()
 assert not x['workedId'] or x['workedId'] in worked
 assert x['ref']['url'].startswith('https://')
 if x['ref']['year'] in [2024,2025,2026]:
  assert any(p['year']==x['ref']['year'] and p['set']==x['ref']['set'] and p['subject'][0].lower()==x['chapter'][0] for p in q['papers'])
assert chapters=={x['chapter'] for x in rows}
for p in q['papers']:
 assert p['quizCount']==sum(x['ref']['year']==p['year'] and x['ref']['file']==p['file'] and x['chapter'][0]==p['subject'][0].lower() for x in rows)
html=(R/'PCB-Boardroom.html').read_text(encoding='utf8')
assert not re.search(r'<script[^>]+src=',html)
assert 'window.QUIZ_DATA' in html and 'function renderQuiz' in html
assert html==(R/'dist/PCB-Boardroom.html').read_text(encoding='utf8')
print('Validated',len(rows),'quiz questions,',len(chapters),'chapters and',len(q['papers']),'paper records.')
print('Questions by year:',dict(sorted(collections.Counter(x['ref']['year'] for x in rows).items())))
print('Minimum questions per chapter:',min(collections.Counter(x['chapter'] for x in rows).values()))
