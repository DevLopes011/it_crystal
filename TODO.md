# Tarefas
✅

- Criar os handlers
    - receber os seguintes campos  ✅
        - queryStringParameters  ✅
        - pathParameters  ✅
        - body  ✅
 
- Estudar como funciona o pydantic   ✅
    - Criar schema de entrada de evento lambda  ✅
    - fazer validação de schema  ✅
    - Não pode ter regras de negócio no lambda, apenas receber evento  ✅

- Fazer um teste de cada Handler 
    - Utilizar o Pytest em ambiente de desenvolvedor
        - fazer a instalação com poetry ✅
    - Testar sucesso e falha para cada handler
    - Pensar em tipos de erros que pode cair nas minhas rotas
    - Usar lambda powerTools para fazer logs
    
- REFATORANDO V2
    - Será utilizado apenas uma tabela que se chamará equipments ✅
    - E o relacionado será de um usuário para muitos equipamentos
    - O assetAggregate passará a ter vários equipamentos e um usuário
    - Não teremos mais rotas para alterar assets teremos rotas para alterar equipamentos (Basicamente mudar nomes do CRUD)
    - Criar uma rota para retornar todos os equipamentos de um usuário que será o asset aggregate