# Registro de Testes Manuais --- Projeto Vértice

**Data dos testes:** 29/10/2026\
**Versão:** protótipo funcional inicial\
**Responsável pelos testes:** estudante/desenvolvedor\
**Ambiente:** aplicação Flask executada localmente no Windows, com banco
de dados SQLite.

## Objetivo

Registrar os testes manuais realizados durante o desenvolvimento inicial
do MVP do Projeto Vértice, verificando o cadastro de agendamentos, a
prevenção de conflitos de horário e a persistência dos dados.

## Testes executados

### TM-01 --- Cadastro de agendamento

-   **Objetivo:** verificar se o formulário envia os dados e a aplicação
    confirma o cadastro.
-   **Procedimento:** preencher os campos de cliente, serviço, data e
    horário e enviar o formulário.
-   **Resultado esperado:** a aplicação confirma que o agendamento foi
    salvo.
-   **Resultado observado:** conforme relatado durante o teste, a
    aplicação recebeu os dados e exibiu a confirmação de cadastro.
-   **Status:** Aprovado.

### TM-02 --- Prevenção de conflito de horário

-   **Objetivo:** verificar se a aplicação impede dois agendamentos com
    a mesma data e horário.
-   **Procedimento:** tentar cadastrar outro agendamento usando a mesma
    data e horário de um registro já existente.
-   **Resultado esperado:** a segunda tentativa é rejeitada e a
    aplicação informa que o horário está ocupado.
-   **Resultado observado:** conforme relatado durante o teste, a
    aplicação exibiu a mensagem esperada de conflito.
-   **Status:** Aprovado.

### TM-03 --- Persistência após reiniciar o servidor

-   **Objetivo:** verificar se o registro continua armazenado após
    encerrar e iniciar novamente a aplicação.
-   **Procedimento:** cadastrar um agendamento, interromper o servidor
    Flask, iniciá-lo novamente e tentar cadastrar outro agendamento na
    mesma data e horário.
-   **Resultado esperado:** o banco de dados mantém o registro anterior
    e a nova tentativa de usar o mesmo horário é rejeitada.
-   **Resultado observado:** conforme relatado durante o teste, a
    aplicação reconheceu o conflito mesmo após o reinício do servidor.
-   **Status:** Aprovado.

## Observações e limitações conhecidas

-   Estes são registros de **testes manuais**. Eles não substituem os
    testes automatizados unitários e de integração exigidos no
    desenvolvimento.
-   A regra atual impede dois registros com a mesma combinação exata de
    data e horário. Como o sistema ainda não considera a duração dos
    serviços, não detecta todos os possíveis casos de sobreposição de
    atendimentos.
-   A validação realizada até aqui não comprova, por si só, a
    acessibilidade completa, a segurança ou a qualidade global da
    aplicação.
-   A tela de confirmação do cadastro ainda é simples e será aprimorada
    para manter a identidade visual do Projeto Vértice.
-   Os resultados foram documentados com base nos testes relatados pelo
    desenvolvedor em 29/10/2026.

## Próximas verificações planejadas

-   [ ] Verificar a listagem dos agendamentos salvos.
-   [ ] Criar testes automatizados para regras de cadastro e conflitos.
-   [ ] Configurar a execução automática dos testes por integração
    contínua (CI).
-   [ ] Realizar as rodadas de validação com representante da comunidade
    e registrar o feedback real.
-   [ ] Implementar e documentar melhorias decorrentes da validação.

------------------------------------------------------------------------

Documento inicial de evidências do Projeto Vértice. Atualizar conforme
novos testes forem executados.
