# Automação do Instagram (n8n)

Dois fluxos para importar no n8n da VPS:

| Arquivo | O que faz |
|---|---|
| `n8n/01_publicar_carrossel.json` | A cada 10 min procura no Notion um post com Status **Agendado** cuja "Data de postagem" já chegou, publica o carrossel no @euforiagrupo (artes JPEG deste repositório) e marca **Postado** com o link. Se algo falhar, marca **Erro na postagem** e escreve o motivo no campo "Erro". |
| `n8n/02_comentarios.json` | A cada 10 min lê os comentários dos posts dos últimos 7 dias. Quem comentar a palavra-chave do post (ex.: VITRINE) recebe a DM com o link do Raio-X e uma resposta pública. Comentários ofensivos ou spam são **ocultados**. |

Configuração: ver a página "Fase 2 | Automação do Instagram" no Notion (Departamento de Marketing).
