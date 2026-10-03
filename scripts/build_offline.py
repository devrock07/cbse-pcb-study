"""Package the static app as a single HTML file; no third-party dependencies."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
dist=root/'dist'
html=(dist/'index.html').read_text(encoding='utf8')
html=html.replace('<link rel="stylesheet" href="style.css">','<style>'+(dist/'style.css').read_text(encoding='utf8')+'</style>')
for name in ['data','app']:
    html=html.replace(f'<script src="{name}.js"></script>','<script>'+(dist/f'{name}.js').read_text(encoding='utf8').replace('</script','<\\/script')+'</script>')
for target in [root/'PCB-Boardroom.html',dist/'PCB-Boardroom.html']:
    target.write_text(html,encoding='utf8')
print('Built offline webpage:',len(html.encode('utf8')),'bytes')
