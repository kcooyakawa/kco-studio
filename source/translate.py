import re, json, sys
sys.path.insert(0,'/home/claude/gen')
from en_map import EN
def translate(t, en_pdf_id=None, pt_pdf_id='597bb175a3988fe9ae7b1313dc471c6c'):
    i=t.index('<x-dc>'); j=t.index('</x-dc>')
    tpl=t[i:j]
    def tr_text(m):
        pre,body,post=m.group(1),m.group(2),m.group(3)
        if '{{' in body:
            parts=re.split(r'(\{\{.*?\}\})',body)
            out=[]
            for p in parts:
                if p.startswith('{{'): out.append(p); continue
                s=p.strip()
                if s in EN:
                    lead=p[:len(p)-len(p.lstrip())]; trail=p[len(p.rstrip()):]
                    out.append(lead+EN[s]+trail)
                else: out.append(p)
            return pre+''.join(out)+post
        s=body.strip()
        if s in EN: return pre+body.replace(s,EN[s])+post
        return m.group(0)
    tpl=re.sub(r'(>)([^<>]+)(<)',tr_text,tpl)
    def tr_attr(m):
        k,v=m.group(1),m.group(2)
        return f'{k}="{EN[v]}"' if v in EN else m.group(0)
    tpl=re.sub(r'\b(alt|aria-label|title)="([^"]*)"',tr_attr,tpl)
    tpl=tpl.replace('<a class="kco-nav kco-lang" href="en/" hreflang="en" lang="en" aria-label="English version">EN</a>','<a class="kco-nav kco-lang" href="../" hreflang="pt-BR" lang="pt-BR" aria-label="Versão em português">PT</a>')
    tpl=tpl.replace('download="Kco_Oyakawa_CV_2026.pdf"','download="Kco_Oyakawa_Resume_2026.pdf"')
    if en_pdf_id: tpl=tpl.replace(pt_pdf_id,en_pdf_id).replace('download="Kco_Oyakawa_Servicos_e_Valores_2026.pdf"','download="Kco_Oyakawa_Services_and_Rates_2026.pdf"')
    t=t[:i]+tpl+t[j:]
    # JS
    a=t.index('data-dc-script'); a=t.index('>',a)+1; b=t.index('</script>',a)
    js=t[a:b]
    def tr_sq(m):
        s=m.group(1)
        if s in EN: return "'"+EN[s].replace("\\","\\\\").replace("'","\\'").replace("\\\\n","\\n")+"'"
        return m.group(0)
    js=re.sub(r"'((?:[^'\\\n]|\\.)*)'",tr_sq,js)
    def tr_dq(m):
        s=m.group(1)
        if s in EN: return '"'+EN[s]+'"'
        return m.group(0)
    js=re.sub(r'"((?:[^"\\\n]|\\.)*)"',tr_dq,js)
    t=t[:a]+js+t[b:]
    t=t.replace('<html lang="pt-BR">','<html lang="en">')
    return t
if __name__=='__main__':
    src=open(sys.argv[1]).read(); out=translate(src, sys.argv[3] if len(sys.argv)>3 else None)
    open(sys.argv[2],'w').write(out)
