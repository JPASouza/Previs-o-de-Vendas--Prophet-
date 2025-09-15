# Análise Exploratória de Dados - Vendas Produto Alfa

## Visão Geral da Série Temporal
- Tendência: Estável ao longo do tempo
- Sazonalidade: Não há padrão sazonal claro visível
- Volatilidade: Alta variação diária nas vendas
- Outliers: Picos e quedas bruscas frequentes
- Demanda: Mantém-se em torno de 200–400 unidades por dia

## Análise por Dia da Semana
- Finais de semana têm maior volume de vendas
  - Sábado e Domingo apresentam as maiores médias
- Segunda a Sexta: Volumes mais baixos e relativamente estáveis
- Domingo é o dia com maior média de vendas entre todos os dias

## Impacto das Promoções
- Promoção Ativa:
  - Mediana significativamente mais alta
  - Maior variabilidade nas vendas
  - Presença de outliers superiores
- Sem Promoção:
  - Mediana mais baixa
  - Menor variabilidade nos dados
  - Distribuição mais concentrada
- Conclusão: Promoções aumentam significativamente o volume médio de vendas

## Impacto dos Feriados
- Feriados não necessariamente aumentam vendas
  - Mediana similar sugere que o volume médio não difere significativamente
- Consistência operacional
  - Feriados apresentam menor variabilidade
  - Possivelmente por terem comportamento mais previsível
- Oportunidade identificada
  - Considerar estratégias de promoção específicas para feriados

## Estatísticas Descritivas
- Período analisado: 730 dias (2 anos de dados diários)
- Métricas principais:
  - Média de vendas: 292 unidades por dia
  - Mediana: 285,5 unidades (distribuição relativamente equilibrada)
  - Desvio padrão: 137 (alta variabilidade entre os dias)
  - Mínimo: 50 unidades (dias de vendas muito baixas)
  - Máximo: 594 unidades (dias de pico elevado)
- Distribuição interquartílica:
  - 25% dos dias: menos de 178 unidades
  - 75% dos dias: menos de 399 unidades
  - Indica ampla variação entre os dias típicos

## Recomendações
1. Desenvolver estratégias específicas para maximizar vendas nos finais de semana
2. Otimizar campanhas promocionais considerando a alta efetividade demonstrada
3. Criar estratégias específicas para feriados, visando aumentar o volume de vendas
4. Investigar causas dos dias com vendas muito baixas (50 unidades) para mitigação
5. Planejar estoque considerando a alta variabilidade diária nas vendas
