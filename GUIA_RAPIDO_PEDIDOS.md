# 🎯 GUIA RÁPIDO - Sistema de Pedidos e WhatsApp

## ✅ O Que Foi Corrigido

| Problema | Solução | Status |
|----------|---------|--------|
| Botão "Enviar via WhatsApp" não funcionava | Reescrever rota com link wa.me | ✅ RESOLVIDO |
| Botão "Finalizar Pedido" não funcionava | Corrigir formulário e validação | ✅ RESOLVIDO |
| Clientes não apareciam | Passar argumentos em /pedidos | ✅ RESOLVIDO |
| Campo de cliente era text | Converter para select | ✅ RESOLVIDO |

---

## 🚀 Como Usar

### 1. Iniciar Aplicação
```bash
python app.py
```

### 2. Acessar Página
```
http://localhost:5000/pedidos
```

### 3. Fluxo de Pedido

**Passo 1**: Selecionar Cliente
- Dropdown com lista de clientes
- Telefone carrega automaticamente

**Passo 2**: Adicionar Produtos
- Clique em "+ Adicionar Produto"
- Selecione produto e quantidade
- Clique em "Adicionar ao Pedido"
- Repita para mais produtos

**Passo 3**: Finalizar
- Clique em "💳 Finalizar Pedido" OU "📱 Enviar via WhatsApp"

---

## 📱 Botão "Enviar via WhatsApp"

### Como funciona:
1. Salva pedido no banco
2. Gera mensagem formatada
3. Cria link `wa.me` com mensagem
4. Abre WhatsApp Web em nova aba
5. Usuário clica "Enviar" manualmente
6. Limpa formulário

### Mensagem Gerada:
```
*NOVO PEDIDO #42*

👤 *Cliente:* João Silva
📱 *Telefone:* (82) 98109-0042

*📋 Itens do Pedido:*
1. Produto A
   └ Qtd: 2 x R$ 50,00
   └ Subtotal: R$ 100,00

*💰 TOTAL: R$ 175,00*

_Pedido registrado no sistema_
```

---

## 💳 Botão "Finalizar Pedido"

### Como funciona:
1. Valida carrinho (não vazio)
2. Valida cliente (selecionado)
3. Valida telefone (preenchido)
4. Mostra confirmação
5. Salva no banco
6. Exibe ID do pedido
7. Limpa formulário

### Confirmação:
```
✅ Pedido Confirmado!

👤 Cliente: João Silva
📱 Telefone: (82) 98109-0042

✓ Produto A x2 - R$ 100,00
✓ Produto B x1 - R$ 75,00

💰 Total: R$ 175,00

📱 Deseja continuar e salvar o pedido?
```

---

## ⚙️ Configurações

### Número do WhatsApp do Lojista
**Arquivo**: `app/templates/pedidos.html`  
**Linha**: ~734  
**Variável**: `const WHATSAPP_LOJISTA = '5582981090042';`

**Formato**: `55 + código país + DDD + número (sem símbolos)`
- Exemplo: `5582981090042` (Brasil, 82, 981090042)
- ❌ NÃO: `(82) 98109-0042` (com formatação)
- ❌ NÃO: `82981090042` (sem código país)

---

## 📊 Mudanças Técnicas

### Backend (app/routes.py)
- ✅ Rota `/salvar_pedido`: Sem mudanças
- ✅ Rota `/enviar_whatsapp`: **REESCRITA** (Selenium → wa.me URL)
- ✅ Rota `/pedidos`: **CORRIGIDA** (argumento clientes)

### Frontend (app/templates/pedidos.html)
- ✅ Campo customerSelect: **CORRIGIDO** (input → select)
- ✅ Função validateCustomerInfo(): **MELHORADA**
- ✅ Evento whatsappBtn: **CORRIGIDO** (window.open)
- ✅ Evento checkoutBtn: Sem mudanças (funcionava)

---

## 🧪 Testes Rápidos

### Teste 1: Página carrega
```bash
curl http://localhost:5000/pedidos
```
Esperado: HTML da página

### Teste 2: Salvar pedido
```bash
curl -X POST http://localhost:5000/salvar_pedido \
  -H "Content-Type: application/json" \
  -d '{
    "carrinho": [{"produtoId": 1, "nome": "Produto", "quantidade": 1, "valor": 50, "subtotal": 50}],
    "id_cliente": 1,
    "nome_cliente": "Cliente",
    "telefone_cliente": "(82) 98109-0042"
  }'
```
Esperado: `{"status": "sucesso", "id_pedido": ...}`

### Teste 3: Gerar link WhatsApp
```bash
curl -X POST http://localhost:5000/enviar_whatsapp \
  -H "Content-Type: application/json" \
  -d '{
    "whatsapp_numero": "5582981090042",
    "mensagem": "*TESTE*",
    "id_pedido": 1
  }'
```
Esperado: `{"status": "sucesso", "url_whatsapp": "https://wa.me/..."}`

---

## ✅ Checklist Final

Antes de usar, valide:
- ✅ Página de pedidos carrega
- ✅ Dropdown de clientes mostra clientes
- ✅ Campo de telefone está preenchido
- ✅ Botão "+ Adicionar Produto" funciona
- ✅ Produtos aparecem no carrinho
- ✅ Botão "Finalizar Pedido" salva
- ✅ Botão "Enviar via WhatsApp" abre
- ✅ Mensagem está formatada
- ✅ Carrinho limpa após enviar

---

## 📞 Suporte Rápido

### "Botão não funciona"
1. Abra DevTools (F12)
2. Clique no botão
3. Veja o console para erros
4. Se houver erro, copie e reporte

### "WhatsApp não abre"
1. Verifique se tem conta WhatsApp
2. Tente wa.me direto no navegador
3. Verifique número do lojista em `pedidos.html`

### "Pedido não salva"
1. Verifique conexão com banco
2. Execute: `python diagnostic_db.py`
3. Se houver erro, corrija conforme instruções

---

## 📚 Documentação Completa

Arquivos criados/modificados:
- `CORRECAO_PEDIDOS_WHATSAPP.md` - Documentação técnica completa
- `TESTE_PEDIDOS_RESUMO.txt` - Resumo visual (este arquivo)
- `test_pedidos.py` - Script de teste automático

---

**Última atualização**: 6 de dezembro de 2025  
**Status**: ✅ 100% Funcional
