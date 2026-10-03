"""Build authored practice questions, with source references and stable option order."""
from pathlib import Path
import json, hashlib, runpy
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'dist/data.js').read_text(encoding='utf8').split('=',1)[1].strip().removesuffix(';'))
questions=[]
inventory=json.loads((ROOT/'scripts/paper-catalogue.json').read_text(encoding='utf8'))
def Q(ch,title,prompt,correct,wrong,explanation):
    source=next(q for q in data['questions'] if q['chapter']==ch and q['title']==title)
    add(ch,prompt,correct,wrong,explanation,source['ref'],'Adapted from a worked PYQ selection',source['id'])
def add(ch,prompt,correct,wrong,explanation,ref,kind,source_id=None):
    assert len(wrong)==3 and correct not in wrong and len(set(wrong))==3
    ident='quiz-'+hashlib.sha256((ch+'|'+prompt).encode()).hexdigest()[:12]
    options=[correct]+wrong
    options.sort(key=lambda o:hashlib.sha256((ident+o).encode()).hexdigest())
    questions.append(dict(id=ident,chapter=ch,prompt=prompt,options=options,answer=options.index(correct),explanation=explanation,ref=ref,kind=kind,workedId=source_id))
def N(ch,year,code,num,prompt,correct,wrong,explanation):
    subject={'p':'Physics','c':'Chemistry','b':'Biology'}[ch[0]]
    p=next(p for p in inventory if p['subject']==subject and p['year']==year and p['set']==code)
    source=next(p for p in data['papers'] if p['subject']==subject and p['year']==year)['source']
    ref=dict(year=year,number=str(num),set=code,file=p['file'],url=source,label=f'{year} · Q{num} · {code}')
    add(ch,prompt,correct,wrong,explanation,ref,'Paraphrased PYQ practice; options may be rewritten')
for subject in ['physics','chemistry','biology','recent']:
    runpy.run_path(str(ROOT/'scripts'/f'quiz_{subject}.py'),init_globals={'Q':Q,'N':N})
assert len({q['id'] for q in questions})==len(questions)
assert all(q['chapter'] in {c['id'] for c in data['chapters']} for q in questions)
assert all(any(q['chapter']==c['id'] for q in questions) for c in data['chapters'])
papers=[]
for p in inventory:
    source=next(x['source'] for x in data['papers'] if x['year']==p['year'] and x['subject']==p['subject'])
    papers.append(dict(id=p['id'],subject=p['subject'],year=p['year'],set=p['set'],file=p['file'],url=source,pages=p['pages'],quizCount=sum(q['ref']['year']==p['year'] and q['ref']['file']==p['file'] and q['chapter'][0]==p['subject'][0].lower() for q in questions)))
payload=dict(questions=questions,papers=papers,coverage='The catalogue lists every PDF found in the nine CBSE main-exam subject archives for 2024–2026, including special versions. Only the authored questions counted as quiz-ready are scored here. Listing a paper does not mean every question in it has been converted or checked. Written-answer questions are adapted into one-point concept checks; these are not official board marks.')
(ROOT/'dist/quiz-data.js').write_text('window.QUIZ_DATA = '+json.dumps(payload,ensure_ascii=False,indent=1)+';\n',encoding='utf8')
print(f'{len(questions)} scored questions; {len(papers)} paper files catalogued')
