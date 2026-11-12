# Modelos "Play em Movimento" (25 modelos de carrossel)

Aprovados pelo Henrique em 12/11/2026 ("todas ficaram excelentes"). A rotina diária do @euforiagrupo passa a usar estes modelos.

## Os modelos
Capas de exemplo em `exemplos/`.

| Nº | Modelo | Função | Use para |
|---|---|---|---|
| 1 | Player | `m_player` (gerar.py) | Processo, bastidor, histórias em etapas |
| 2 | Manchete | `m_manchete` | Notícia com leitura de negócio, análise |
| 3 | Mito × Fato | `m_mito` | Objeções |
| 4 | Roteiro | `m_roteiro` | Como funciona, quem faz o quê |
| 5 | Placar | `m_placar` | Números oficiais, raio-X de YouTuber, dados com fonte |
| 6 | Notificação | `m06` (gerar2.py) | A cena que o cliente quer viver |
| 7 | Recibo | `m07` | O custo de fazer errado |
| 8 | Pare | `m08` | Ângulos "pare de..." |
| 9 | Ingresso | `m09` | Convite para o Raio-X, institucional |
| 10 | Eco | `m10` | Virada de palavra (invisível, visível) |
| 11 | Dicionário | `m11` | Vocabulário da marca |
| 12 | Checklist | `m12` | Listas de sinais, erros, diagnósticos |
| 13 | Calendário | `m13` | Rotina sem resultado |
| 14 | Raio-X | `m14` | Análises e raio-X de perfis |
| 15 | Rec | `m15` | Tudo sobre gravar |
| 16 | Revista | `m16` (gerar3.py) | Grandes nomes: frase forte e a lição |
| 17 | Figurinha | `m17` | Trajetória de empresário em 4 fatos |
| 18 | Dossiê | `m18` | Curiosidades de uma personalidade |
| 19 | Aspas | `m19` | Frase de grande nome, com fonte |
| 20 | Estante | `m20` | Resumo de livro em 3 ideias |
| 21 | Marca-texto | `m21` | A frase que vale o livro |
| 22 | Holofote | `m22` | Insight curto, para salvar |
| 23 | Expectativa × Realidade | `m23` | Meme |
| 24 | Kit | `m24` | Meme do "kit" |
| 25 | Ensaio | `m25` | Reflexão mais profunda |

## Como gerar um post novo
1. Copie a função do modelo para um arquivo novo (ou edite uma cópia de `gerar.py` / `gerar2.py`) e troque só os textos. Cada função monta os slides em HTML e chama `page("nome", [slides])`.
2. `python3 gerar2.py` (ele importa o `gerar.py`) escreve `modelo-*.html` nesta pasta.
3. `SAIDA=/caminho/de/saida node foto.js` fotografa cada slide em PNG e JPG 1080x1350.
4. Copie os `slide_XX.jpg` para `carrosseis/AAAA-MM-DD_slug/` e siga o fluxo normal (Calendário no Notion).

Precisa do `Archivo.ttf` (variável) ao lado do `gerar.py`, em `gerador/container/` ou em `/mnt/project-files/dossie/thumb-materiais/`. A Inter vem do sistema. O Playwright é o do Node do ambiente.

## Regras
- Não repetir o mesmo modelo na mesma semana; alternar fundos preto, laranja e off-white.
- Olhar todos os slides antes de agendar. Títulos longos estouram: reduza o `font-size` do bloco.
- Para mais slides, repita o bloco de miolo do modelo.
- Palavra do "Comente" única por post. As dos exemplos são ilustrativas.
- Valem as regras de sempre: números oficiais, sem rosto do Henrique, sem "canal" para o que construímos, sem citar IA, CTA do Raio-X sem minutos.
- Cores chapadas da marca Play. Tons de apoio: grafite #141312, fumaça #26221F, areia #DDD6CB, cinza #8A827A.
- Texto do CTA: os exemplos dizem "com os nossos consultores"; a rotina diária usa a redação vigente dela (hoje "com a nossa equipe"). Troque na função `cta` e nos CTAs do gerar.py.
- Modelos 16 a 19 (personalidades): foto só em post sobre a própria pessoa, em preto e branco, com crédito "Foto: site" no slide e fontes dos fatos no miolo. Fotos em `fotos/` (ver `fotos/CREDITOS.txt`); use `foto('arquivo.jpg', estilo)` e `credito('site')` do gerar3.py. Fato, número e frase de pessoa só com fonte checada. A pessoa é o assunto, nunca dá a entender que indica a gente.
- Modelos 20 e 21 (livros): só livro que foi lido ou tem resumo confiável; cite título e autor.
