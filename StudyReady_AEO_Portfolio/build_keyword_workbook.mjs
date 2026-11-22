import fs from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { Workbook, SpreadsheetFile, FileBlob } from 'file:///C:/Users/BURRAQ%20LAPTOPS/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs';

const base = new URL('.', import.meta.url).pathname;
const read = p => fs.readFile(new URL(p, import.meta.url), 'utf8');
const questionCsv = await read('./research/question_keyword_seed.csv');
const intentCsv = await read('./research/search_intent_map.csv');
const compCsv = await read('./research/competitor_shortlist.csv');
function parseCsv(s){const rows=[];let row=[],v='',q=false;for(let i=0;i<s.length;i++){const c=s[i];if(q&&c==='"'&&s[i+1]==='"'){v+='"';i++;}else if(c==='"'){q=!q;}else if(c===','&&!q){row.push(v);v='';}else if((c==='\n'||c==='\r')&&!q){if(c==='\r'&&s[i+1]==='\n')i++;row.push(v);rows.push(row);row=[];v='';}else v+=c;}if(v||row.length){row.push(v);rows.push(row);}return rows;}
const wb=Workbook.create();
for(const [name,csv] of [['Question Bank',questionCsv],['Intent Map',intentCsv],['Competitors',compCsv]]){
 const sh=wb.worksheets.add(name); sh.getRangeByIndexes(0,0,parseCsv(csv).length,parseCsv(csv)[0].length).values=parseCsv(csv);
}
for (const name of ['Question Bank','Intent Map','Competitors']) {
  const sh=wb.worksheets.getItem(name); sh.showGridLines=false; sh.freezePanes.freezeRows(1);
  const used=sh.getUsedRange();
  const cols=used.columnCount, rows=used.rowCount;
  const head=sh.getRangeByIndexes(0,0,1,cols);
  used.format.wrapText=true;
  used.format.font={name:'Aptos',size:10,color:'#263746'};
  head.format.fill='#12304A'; head.format.font={bold:true,color:'#FFFFFF'}; head.format.wrapText=true;
  head.format.rowHeight=34;
  used.format.autofitColumns();
  used.format.columnWidth=24;
  for(let c=0;c<cols;c++) sh.getRangeByIndexes(0,c,rows,1).format.columnWidth=[31,24,24,30,26,20,44,44][c]||26;
  if (rows>1) sh.getRangeByIndexes(1,0,rows-1,cols).format.rowHeight=37;
}
await wb.recalculate();
const out=await SpreadsheetFile.exportXlsx(wb);
const xlsxPath=fileURLToPath(new URL('./research_keyword_intent_competitor_workbook.xlsx',import.meta.url));
await out.save(xlsxPath);
const check=await SpreadsheetFile.importXlsx(await FileBlob.load(xlsxPath));
const summary=await check.inspect({kind:'workbook,sheet',include:'id,name',maxChars:2000});
console.log(summary.ndjson || summary);
for(const name of ['Question Bank','Intent Map','Competitors']){
 const preview=await check.render({sheetName:name,autoCrop:'all',scale:1,format:'png'});
 await fs.writeFile(fileURLToPath(new URL(`./reports/${name.replaceAll(' ','_')}_preview.png`,import.meta.url)),new Uint8Array(await preview.arrayBuffer()));
}
