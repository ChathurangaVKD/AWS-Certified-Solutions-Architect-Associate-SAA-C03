const {JSDOM}=require("jsdom");const fs=require("fs");const dir=process.argv[2];
let html=fs.readFileSync(dir+"index.html","utf8").replace('<script src="questions.js"></script>',"<script>"+fs.readFileSync(dir+"questions.js","utf8")+"</script>");
const d=new JSDOM(html,{runScripts:"dangerously",url:"http://localhost/",pretendToBeVisual:true,beforeParse(w){w.matchMedia=()=>({matches:false});w.scrollTo=()=>{};w.HTMLElement.prototype.scrollIntoView=()=>{};}});const w=d.window;
const $=s=>w.document.querySelector(s),sleep=ms=>new Promise(r=>setTimeout(r,ms));w.addEventListener("error",e=>console.log("ERR",e.message));
(async()=>{
console.log("topics",w.document.querySelectorAll('[data-m=domain]').length);
$('[data-m=full]').click();console.log($('.tag').textContent,$('.timer').textContent);
for(let i=0;i<65;i++){ w.document.dispatchEvent(new w.KeyboardEvent("keydown",{key:"a"})); w.document.dispatchEvent(new w.KeyboardEvent("keydown",{key:"ArrowRight"})); }
$('#end2').click(); await sleep(20); $('.modal button.primary').click(); await sleep(20);
console.log($('.ring').textContent, w.document.querySelectorAll('.dom').length, $('.card p.muted.small:last-child')?.textContent);
$('#home').click();$('[data-m=weak]').click();console.log($('.ttl').textContent);$('.opt').click();$('#check').click();console.log($('.expl').textContent.slice(0,60));
$('#quit').click();$('[data-m=domain][data-d="Compute"]').click();console.log($('.ttl').textContent,$('.tag:nth-child(2)').textContent);
})();
