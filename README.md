# Sistema de Ponto de Venda (PDV) - Nível 1

## O que o código faz
O programa simula um sistema de Ponto de Venda (PDV) para registro de compras, aplicando regras de descontos automáticos baseados na idade do cliente e no valor da compra. Ao final do expediente ou encerramento das entradas, ele gera um resumo financeiro com o total de compras efetuadas, total bruto, total líquido com descontos e o valor total de descontos concedidos.

## Como ele faz
O funcionamento do programa segue os seguintes passos:
1. **Entrada e validação da compra**: O sistema solicita o valor da compra. Se o usuário digitar `0`, o loop de atendimento é encerrado. Caso seja informado um valor negativo, solicita uma correção. O valor bruto original é acumulado para as estatísticas.
2. **Entrada e validação da idade**: Solicita a idade do cliente, validando para evitar valores negativos ou irreais (iguais ou superiores a 130).
3. **Aplicação de descontos**:
   - **Desconto para idosos (idade $\ge$ 65)**: Aplica-se primeiramente um desconto de 20% sobre o valor da compra.
   - **Desconto por valor (> 100)**: Se o valor da compra (ou o valor remanescente após o desconto de idoso) for superior a R$ 100,00, é aplicado um desconto adicional de 10%.
   - **Sem desconto**: Caso não atenda aos critérios, o valor integral é mantido.
4. **Armazenamento**: O valor final calculado de cada compra é exibido na tela e armazenado em uma lista.
5. **Resumo do dia**: Após a finalização (`0`), o sistema calcula e exibe:
   - Quantidade total de compras realizadas.
   - Valor bruto total arrecadado (sem descontos).
   - Valor total final com os descontos aplicados.
   - Total acumulado de descontos concedidos.

## Como rodar
Para executar o programa no terminal ou prompt de comando, certifique-se de estar dentro da pasta `nivel_1` e execute:

```bash
python pdv.py
```

## Tabela de Casos de Teste

| Caso | Valor Original (R$) | Idade | Descontos Aplicados | Valor Final (R$) | Explicação |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | R$ 50,00 | 30 | Nenhum (0%) | R$ 50,00 | Idade menor que 65 e valor não ultrapassa R$ 100. |
| **2** | R$ 150,00 | 30 | 10% (compra > 100) | R$ 135,00 | Não tem desconto de idade, recebe 10% pelo valor (150 - 15). |
| **3** | R$ 80,00 | 70 | 20% (idoso) | R$ 64,00 | Recebe 20% de desconto por ter $\ge 65$ anos (80 - 16 = 64). Como 64 $\le$ 100, não há desconto extra. |
| **4** | R$ 200,00 | 70 | 20% + 10% cumulativo | R$ 144,00 | Recebe 20% por idade (200 - 40 = 160). Como 160 > 100, recebe mais 10% sobre 160 (160 - 16 = 144). |
| **5** | R$ 120,00 | 65 | 20% (idoso) | R$ 96,00 | Recebe 20% por idade (120 - 24 = 96). Como 96 não passa de 100, não recebe o segundo desconto. |
| **0** | R$ 0,00 | - | - | - | Encerra o programa e exibe o resumo financeiro. |
