from pathlib import Path

p = Path('index.html')
text = p.read_text(encoding='utf-8')

start = text.index('<nav id="nav">')
end = text.index('</nav>', start) + len('</nav>')

new_nav = '''<nav id="nav" class="nav-groups" aria-label="Navegação principal">
  <div class="nav-group">
    <div class="nav-group-title">Gestão Principal</div>
    <div class="nav-group-buttons">
      <button class="active" data-page="dashboard"><span class="nav-icon">▦</span><span>Dashboard</span></button>
      <button data-page="clientes"><span class="nav-icon">👥</span><span>Clientes</span></button>
      <button data-page="cadastroCliente"><span class="nav-icon">＋</span><span>Cadastrar cliente</span></button>
      <button data-page="planos"><span class="nav-icon">⌁</span><span>Planos</span></button>
      <button data-page="cobrancas"><span class="nav-icon">▤</span><span>Cobranças</span></button>
      <button data-page="recebimentos"><span class="nav-icon">$</span><span>Recebimentos</span></button>
    </div>
  </div>

  <div class="nav-group">
    <div class="nav-group-title">Atendimentos e Contratos</div>
    <div class="nav-group-buttons">
      <button data-page="ordens"><span class="nav-icon">☑</span><span>Ordens de Serviço</span></button>
      <button data-page="contratos"><span class="nav-icon">▧</span><span>Contratos</span></button>
      <button data-page="cliente"><span class="nav-icon">◎</span><span>Área do Cliente</span></button>
    </div>
  </div>

  <div class="nav-group">
    <div class="nav-group-title">Rede e Equipamentos</div>
    <div class="nav-group-buttons">
      <button data-page="pontos"><span class="nav-icon">⌘</span><span>Pontos de Distribuição</span></button>
      <button data-page="equipamentos"><span class="nav-icon">▣</span><span>Equipamentos</span></button>
      <button data-page="tecnicos"><span class="nav-icon">⚒</span><span>Técnicos</span></button>
      <button data-page="despesas"><span class="nav-icon">◫</span><span>Despesas</span></button>
    </div>
  </div>

  <div class="nav-group">
    <div class="nav-group-title">Configurações e Controle</div>
    <div class="nav-group-buttons">
      <button data-page="perfisPermissoes"><span class="nav-icon">◈</span><span>Perfis e Permissões</span></button>
      <button data-page="usuarios"><span class="nav-icon">●</span><span>Usuários</span></button>
      <button data-page="acessosPonto"><span class="nav-icon">◷</span><span>Acessos / Ponto</span></button>
      <button data-page="registros"><span class="nav-icon">☷</span><span>Registros</span></button>
      <button data-page="configObrigatorios"><span class="nav-icon">✓</span><span>Config. Obrigatórios</span></button>
    </div>
  </div>
</nav>'''

text = text[:start] + new_nav + text[end:]

css = '''
/* ===== Navegação organizada em grupos ===== */
#nav.nav-groups{
  display:grid!important;
  grid-template-columns:1fr!important;
  gap:12px!important;
  position:static!important;
  padding:14px 16px!important;
  background:#f5f6f8!important;
  border-bottom:1px solid #ececf0;
}
#nav .nav-group{
  background:#fff;
  border:1px solid #e6e6eb;
  border-radius:14px;
  padding:12px;
  box-shadow:0 2px 8px rgba(0,0,0,.035);
}
#nav .nav-group-title{
  margin:0 0 10px 2px;
  color:#8f0a57;
  font-size:13px;
  font-weight:800;
  letter-spacing:.01em;
}
#nav .nav-group-buttons{
  display:grid;
  grid-template-columns:repeat(6,minmax(0,1fr));
  gap:9px;
}
#nav .nav-group-buttons button{
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
  gap:7px;
  min-height:76px;
  padding:9px 7px;
  border:1px solid #e2e2e7;
  border-radius:10px;
  background:#fff;
  color:#33343a;
  font-size:12px;
  font-weight:700;
  line-height:1.15;
  text-align:center;
  cursor:pointer;
  transition:.15s ease;
}
#nav .nav-group-buttons button:hover{
  border-color:#cfa8bf;
  background:#fcf8fa;
  transform:translateY(-1px);
}
#nav .nav-group-buttons button.active{
  background:#8f0a57!important;
  border-color:#8f0a57!important;
  color:#fff!important;
  box-shadow:0 4px 12px rgba(143,10,87,.16);
}
#nav .nav-icon{
  display:flex;
  align-items:center;
  justify-content:center;
  min-height:24px;
  font-size:20px;
  line-height:1;
  font-weight:800;
}
@media(max-width:1050px){
  #nav .nav-group-buttons{grid-template-columns:repeat(4,minmax(0,1fr));}
}
@media(max-width:700px){
  #nav.nav-groups{padding:10px!important;gap:10px!important;}
  #nav .nav-group{padding:10px;border-radius:12px;}
  #nav .nav-group-title{font-size:12px;margin-bottom:8px;}
  #nav .nav-group-buttons{grid-template-columns:repeat(3,minmax(0,1fr));gap:7px;}
  #nav .nav-group-buttons button{min-height:68px;padding:7px 5px;font-size:11px;}
  #nav .nav-icon{font-size:18px;min-height:21px;}
}
@media(max-width:430px){
  #nav .nav-group-buttons{grid-template-columns:repeat(2,minmax(0,1fr));}
  #nav .nav-group-buttons button{min-height:62px;}
}
'''

marker = '</style>'
if '/* ===== Navegação organizada em grupos ===== */' not in text:
    idx = text.rfind(marker)
    text = text[:idx] + css + text[idx:]

p.write_text(text, encoding='utf-8')
