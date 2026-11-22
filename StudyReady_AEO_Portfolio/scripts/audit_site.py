from pathlib import Path
from html.parser import HTMLParser
import json, re, csv, xml.etree.ElementTree as ET

BASE=Path(__file__).resolve().parents[1]
SITE=BASE/'site'
class Page(HTMLParser):
 def __init__(self):
  super().__init__(); self.title=''; self.in_title=False; self.in_schema=False; self.in_h1=False; self.in_anchor=False
  self.h1=0; self.h1_text=''; self.main=0; self.links=[]; self.current_anchor=None; self.labels=[]; self.inputs=[]
  self.canonical=''; self.description=''; self.schemas=[]; self.lang=''; self.viewport=False; self.images=[]; self.headings=[]; self.live_regions=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='title': self.in_title=True
  if re.fullmatch(r'h[1-6]',tag): self.headings.append(int(tag[1]))
  if tag=='h1': self.h1+=1; self.in_h1=True
  if tag=='main': self.main+=1
  if tag=='html': self.lang=a.get('lang','')
  if tag=='img': self.images.append(a)
  if tag=='a' and 'href' in a: self.current_anchor={'href':a['href'],'text':'','aria_label':a.get('aria-label','')}; self.in_anchor=True
  if tag=='label' and 'for' in a: self.labels.append(a['for'])
  if tag in ('input','select','textarea') and a.get('id'): self.inputs.append(a['id'])
  if a.get('aria-live'): self.live_regions+=1
  if tag=='link' and a.get('rel')=='canonical': self.canonical=a.get('href','')
  if tag=='meta' and a.get('name')=='description': self.description=a.get('content','')
  if tag=='meta' and a.get('name')=='viewport': self.viewport=True
  if tag=='script' and a.get('type')=='application/ld+json': self.schemas.append(''); self.in_schema=True
 def handle_endtag(self,tag):
  if tag=='title': self.in_title=False
  if tag=='h1': self.in_h1=False
  if tag=='a' and self.current_anchor is not None:
   self.links.append(self.current_anchor); self.current_anchor=None; self.in_anchor=False
  if tag=='script' and self.in_schema: self.in_schema=False
 def handle_data(self,data):
  if self.in_title: self.title+=data
  if self.in_h1: self.h1_text+=data
  if self.in_anchor and self.current_anchor is not None: self.current_anchor['text']+=data
  if self.in_schema: self.schemas[-1]+=data

def local_target(href,source):
 if href.startswith(('#','mailto:','tel:','http:','https:','javascript:')): return None
 path=href.split('#')[0].split('?')[0]
 if not path: return None
 target=SITE/path.lstrip('/') if path.startswith('/') else source.parent/path
 if not path: return None
 return target/'index.html' if target.is_dir() else (SITE/'index.html' if target==SITE else target)

results={'pages':[],'errors':[],'warnings':[]}; onpage=[]; seen_titles={}; seen_canonicals={}
for f in sorted(SITE.rglob('*.html')):
 p=Page(); p.feed(f.read_text(encoding='utf-8'))
 row={'file':str(f.relative_to(SITE)),'title':bool(p.title.strip()),'description':bool(p.description.strip()),'canonical':p.canonical,'canonical_placeholder':('studyready.example' in p.canonical),'h1_count':p.h1,'h1_text':p.h1_text.strip(),'main_count':p.main,'language_declared':bool(p.lang),'viewport_declared':p.viewport,'images_missing_alt':sum('alt' not in im for im in p.images),'schemas':0,'schema_types':[],'schema_consistent':True,'local_links':0,'unnamed_links':0,'broken_local_links':[],'heading_skips':[],'unlabeled_inputs':[],'aria_live_regions':p.live_regions}
 if not p.title.strip(): results['errors'].append(row['file']+': missing title')
 if not p.description.strip(): results['errors'].append(row['file']+': missing description')
 if p.h1!=1: results['errors'].append(row['file']+f': expected one H1, got {p.h1}')
 if p.main!=1: results['errors'].append(row['file']+f': expected one main, got {p.main}')
 if not p.canonical: results['errors'].append(row['file']+': missing canonical')
 if p.canonical:
  if p.canonical in seen_canonicals: results['errors'].append(row['file']+': duplicate canonical with '+seen_canonicals[p.canonical])
  seen_canonicals[p.canonical]=row['file']
 if p.title.strip():
  if p.title.strip() in seen_titles: results['errors'].append(row['file']+': duplicate title with '+seen_titles[p.title.strip()])
  seen_titles[p.title.strip()]=row['file']
 if not p.lang: results['errors'].append(row['file']+': missing document language')
 if not p.viewport: results['errors'].append(row['file']+': missing viewport')
 if row['images_missing_alt']: results['errors'].append(row['file']+': images missing alt text')
 prior=0
 for level in p.headings:
  if prior and level>prior+1: row['heading_skips'].append(f'h{prior} to h{level}')
  prior=level
 if row['heading_skips']: results['errors'].append(row['file']+': heading level skip '+', '.join(row['heading_skips']))
 for link in p.links:
  if not (link['text'].strip() or link['aria_label'].strip()): row['unnamed_links']+=1
 if row['unnamed_links']: results['errors'].append(row['file']+f': {row["unnamed_links"]} link(s) have no accessible name')
 row['unlabeled_inputs']=[x for x in p.inputs if x not in p.labels]
 if row['unlabeled_inputs']: results['errors'].append(row['file']+': inputs lack explicit labels '+', '.join(row['unlabeled_inputs']))
 for raw in p.schemas:
  try:
   data=json.loads(raw); row['schemas']+=1
   nodes=data if isinstance(data,list) else [data]
   types=[x.get('@type') for x in nodes if isinstance(x,dict)]
   row['schema_types'].extend([t for t in types if t])
   for node in nodes:
    if not isinstance(node,dict): continue
    if node.get('@type')=='Article':
     if node.get('headline')!=p.h1_text.strip(): row['schema_consistent']=False
     if node.get('description')!=p.description: row['schema_consistent']=False
     if node.get('mainEntityOfPage')!=p.canonical: row['schema_consistent']=False
    if node.get('@type')=='BreadcrumbList':
     items=node.get('itemListElement',[])
     if not items or items[-1].get('item')!=p.canonical: row['schema_consistent']=False
  except Exception as e: results['errors'].append(row['file']+': invalid JSON-LD '+str(e))
 if not row['schema_consistent']: results['errors'].append(row['file']+': structured data conflicts with visible page metadata')
 for link in p.links:
  href=link['href']
  target=local_target(href,f)
  if target:
   row['local_links']+=1
   if not target.exists(): row['broken_local_links'].append(href)
 if row['broken_local_links']: results['errors'].append(row['file']+': broken links '+', '.join(row['broken_local_links']))
 if f.parent.name=='guides' and f.name!='index.html' and ('Article' not in row['schema_types'] or 'BreadcrumbList' not in row['schema_types']): results['errors'].append(row['file']+': expected Article and BreadcrumbList JSON-LD')
 onpage.append({'Page':row['file'],'Title':p.title.strip(),'Meta description':p.description.strip(),'H1':p.h1_text.strip(),'Canonical':p.canonical,'JSON-LD types':', '.join(row['schema_types']),'Local links':row['local_links'],'Direct answer block':'Yes' if 'class="answer"' in f.read_text(encoding='utf-8') else 'No','Implementation status':'Local prototype; public validation pending'})
 results['pages'].append(row)
sm=SITE/'sitemap.xml'
sitemap_urls=[]
if not sm.exists(): results['errors'].append('missing sitemap.xml')
else:
 try:
  xml=ET.parse(sm).getroot(); sitemap_urls=[n.text for n in xml.findall('.//{*}loc')]
  if any('studyready.example' not in u for u in sitemap_urls): results['errors'].append('sitemap contains non-placeholder or empty URL')
  if set(sitemap_urls)!=set(seen_canonicals): results['errors'].append('sitemap URLs do not match the canonical URLs')
 except Exception as e: results['errors'].append('invalid sitemap XML '+str(e))
robots=(SITE/'robots.txt').read_text(encoding='utf-8') if (SITE/'robots.txt').exists() else ''
if 'Sitemap:' not in robots: results['errors'].append('robots.txt missing sitemap reference')
results['summary']={'html_pages':len(results['pages']),'errors':len(results['errors']),'all_pages_have_metadata':all(x['title'] and x['description'] for x in results['pages']),'all_pages_have_lang_viewport':all(x['language_declared'] and x['viewport_declared'] for x in results['pages']),'schema_matches_visible_page':all(x['schema_consistent'] for x in results['pages']),'sitemap_matches_canonicals':set(sitemap_urls)==set(seen_canonicals),'no_unnamed_links':all(x['unnamed_links']==0 for x in results['pages']),'placeholder_domain_requires_replacement':True,'limitations':['No live host, HTTP response, crawl, indexation, Core Web Vitals, external link status, WCAG conformance, or answer-engine citations tested.']}
out=BASE/'reports'/'local_qa.json'; out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(results,indent=2),encoding='utf-8')
with (BASE/'reports'/'on_page_optimization_register.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=onpage[0].keys()); w.writeheader(); w.writerows(onpage)
print(json.dumps(results['summary'],indent=2)); print('ERRORS:',json.dumps(results['errors']))
raise SystemExit(1 if results['errors'] else 0)
