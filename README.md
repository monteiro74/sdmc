# sdmc
Sistema para Doação de Material de Construção (SDMC)

- [sdmc](#sdmc)
- [1. Introdução](#1-introdução)
- [2. Descrição](#2-descrição)
  - [2.1. Requisitos.](#21-requisitos)
  - [2.2. Funcionais e não-funcionais](#22-funcionais-e-não-funcionais)
- [3. Diagramas](#3-diagramas)
  - [3.1. Diagrama de classe](#31-diagrama-de-classe)
    - [digrama feito no white star (versão 1)](#digrama-feito-no-white-star-versão-1)
    - [3.1.1. Descrição do Diagrama de classe:](#311-descrição-do-diagrama-de-classe)
  - [3.2. Diagrama ER](#32-diagrama-er)
  - [3.3. Diagrama de casos de uso](#33-diagrama-de-casos-de-uso)
  - [3.3. Diagrama de atividade](#33-diagrama-de-atividade)
  - [3.4. Diagrama de componentes](#34-diagrama-de-componentes)
  - [3.5. Diagrama de implantação](#35-diagrama-de-implantação)
  - [4. Histórias de usuário](#4-histórias-de-usuário)
  - [5. Protótipo de telas](#5-protótipo-de-telas)
  - [6. Diagrama de navegação de tela](#6-diagrama-de-navegação-de-tela)



# 1. Introdução

* Contexto: tarefa de casa...
* Motivação: tarefa de casa...

# 2. Descrição

## 2.1. Requisitos.

| Id | Requisitos |
|----|------------|
| 1  | Temos uma instituição sem fins lucrativos |
| 2  | A Instituição tem os seguintes atributos: nome, cnpj, localizaçao, cidade |
| 3 | A Instituição recebe Doação de Materias de construção |
| 4 | A Instituição tem um Depósito |
| 5 | A Instituição recebe Materiais do tipo: tijolo, cimento e telhas |
| 6 | A Instituição tem um Cadastro dos Materiais |
| 7 | A Instituição tem um Cadastro dos doadores |
| 8 | A Instituição tem um Cadastro dos Beneficiários |
| 9 | A Instituição tem um Depósito Temporário de Materiais de construção |
| 10 | A Instituição tem um banco de dados de Doadores, Materiais de construção e Beneficiários |
| 11 | A Instituição tem um pessoal de Staff, Estagiários e Voluntários; o Staff tem diretores e gerentes. |
| 12 | A Instituição tem um "contas a receber" e "contas a pagar", cuidado pela gerência contábil. |
| 13 | A Instituição tem um Regimento Interno (RI). |
| 14 | A Instituição atende apenas no horário da tarde, das 14hs as 18hs. |
| 15 | A Instituição recebe apenas Materais de construção usados na estrutura de casas, não recebe do tipo "materiais de interior" ou "materiais de acabamento". |
| 16 | A Instituição realiza uma Assembléia por ano, em março. |
| 17 | A Instituição realiza Campanhas com data, prazo, responsável e local previamente definidos|
| 18 | As Campanhas são para arrecadar determinados tipos de Materiais de construção como: telhas e tijolos. |
| 19 | Quando o depósito da Instituição esta cheio, os Materiais doados ficam com os Doadores temporariamente, até serem acionados para levar o Material ao Depósito da Instituição. |
| 20 | A Instituição tem um Controle de estoque indicando, qual Material entrou e quem fez a doação. |
| 21 | O controle de estoque indica onde esta armazenado temporariamente o Material até que sejam feita a destinação final deste. |
| 22 | O Controle de estoque também tem os dados de qual Beneficário recebeu os Materiais de contrução, em qual data e hora. |
| 23 | A Instituição tem um caminhão e uma pickup S10. |
| 24 | A Instituição usa o caminhão e a pickup para fazer entregas de materiais de construção, do depósito até os Beneficiários. |
| 25 | Uma ação de doação de Materiais de construção deve ter uma data e hora, previamente agendada com a equipe da Instituição e o Beneficiário. |
| 26 | A Instituição deverá ter um seu Site Institucional uma lista de doares, calendário de doação, datas de assembléis, redimento interno, lista de Beneficionários e formuláiros para os que desejarem doar ou receber materiais de construção. |
| 27 | O Beneficiário deverá apresentar declaração de rendimento ou outro documento equivalente que indique sua situação. |

## 2.2. Funcionais e não-funcionais

> [!TIP]
> Faça uma tabela usando Markdown, com duas colunas, uma coluna indicando o requisito e a outra coluna indicando o tipo de requisito (como "Funcional" ou "Não funcional"), para esta tarefa use a lista abaixo:


| Requisito                                                                                         | Tipo de Requisito |
|---------------------------------------------------------------------------------------------------|-------------------|
| Temos uma instituição sem fins lucrativos                                                        | Funcional         |
| A Instituição tem os seguintes atributos: nome, cnpj, localização, cidade                          | Funcional         |
| A Instituição recebe Doação de Materiais de construção                                            | Funcional         |
| A Instituição tem um Depósito                                                                     | Funcional         |
| A Instituição recebe Materiais do tipo: tijolo, cimento e telhas                                  | Funcional         |
| A Instituição tem um Cadastro dos Materiais                                                       | Funcional         |
| A Instituição tem um Cadastro dos doadores                                                        | Funcional         |
| A Instituição tem um Cadastro dos Beneficiários                                                   | Funcional         |
| A Instituição tem um Depósito Temporário de Materiais de construção                               | Funcional         |
| A Instituição tem um banco de dados de Doadores, Materiais de construção e Beneficiários           | Funcional         |
| A Instituição tem um pessoal de Staff, Estagiários e Voluntários; o Staff tem diretores e gerentes | Funcional         |
| A Instituição tem um "contas a receber" e "contas a pagar", cuidado pela gerência contábil        | Funcional         |
| A Instituição tem um Regimento Interno (RI).                                                      | Funcional         |
| A Instituição atende apenas no horário da tarde, das 14hs as 18hs                                 | Não Funcional     |
| A Instituição recebe apenas Materiais de construção usados na estrutura de casas, não recebe do tipo "materiais de interior" ou "materiais de acabamento" | Não Funcional     |
| A Instituição realiza uma Assembleia por ano, em março.                                           | Não Funcional     |
| A Instituição realiza Campanhas com data, prazo, responsável e local previamente definidos         | Funcional         |
| As Campanhas são para arrecadar determinados tipos de Materiais de construção como: telhas e tijolos | Funcional         |
| Quando o depósito da Instituição está cheio, os Materiais doados ficam com os Doadores temporariamente, até serem acionados para levar o Material ao Depósito da Instituição | Funcional         |
| A Instituição tem um Controle de estoque indicando, qual Material entrou e quem fez a doação      | Funcional         |
| O controle de estoque indica onde está armazenado temporariamente o Material até que sejam feita a destinação final deste | Funcional         |
| O Controle de estoque também tem os dados de qual Beneficiário recebeu os Materiais de construção, em qual data e hora | Funcional         |
| A Instituição tem um caminhão e uma pickup S10                                                   | Funcional         |
| A Instituição usa o caminhão e a pickup para fazer entregas de materiais de construção, do depósito até os Beneficiários | Funcional         |
| Uma ação de doação de Materiais de construção deve ter uma data e hora, previamente agendada com a equipe da Instituição e o Beneficiário | Funcional         |
| A Instituição deverá ter em seu Site Institucional uma lista de doadores, calendário de doação, datas de assembleias, regimento interno, lista de Beneficiários e formulários para os que desejarem doar ou receber materiais de construção | Funcional         |
| O Beneficiário deverá apresentar declaração de rendimento ou outro documento equivalente que indique sua situação | Não Funcional     |





# 3. Diagramas

## 3.1. Diagrama de classe

### digrama feito no white star (versão 1)

![diagrama de classe](https://github.com/monteiro74/sdmc/blob/main/diagrama_de_classe.png)


> [!TIP]
> Faça um diagrama de classe usando Markdown e Mermaid, para os requisitos abaixo:


```mermaid
classDiagram
    class Instituicao {
        +String nome
        +String cnpj
        +String localizacao
        +String cidade
        +String regimentoInterno
        +String horarioAtendimento
        +realizarAssembléia()
        +realizarCampanha()
        +receberDoacao()
        +gerenciarEstoque()
        +gerenciarTransporte()
    }

    class Doacao {
        +String tipoMaterial
        +String dataHora
        +String descricao
    }

    class Deposito {
        +String tipoDeposito
        +boolean estaCheio
        +armazenarMaterial()
        +retirarMaterial()
    }

    class Material {
        +String nome
        +String tipo
        +double quantidade
    }

    class Doadores {
        +String nome
        +String cpfCnpj
        +String endereco
        +doarMaterial()
    }

    class Beneficiarios {
        +String nome
        +String documentoIdentidade
        +String endereco
        +String tipoMaterialRecebido
        +receberMaterial()
    }

    class ControleEstoque {
        +Material material
        +Doadores doador
        +Beneficiarios beneficiario
        +String localArmazenamento
        +String dataHora
        +registrarEntrada()
        +registrarSaida()
    }

    class Veiculo {
        +String modelo
        +String placa
        +entregarMaterial()
    }

    Instituicao "1" --> "1..*" Doacao : recebe
    Instituicao "1" --> "1" Deposito : tem
    Instituicao "1" --> "1..*" Material : recebe
    Instituicao "1" --> "1..*" Doadores : tem
    Instituicao "1" --> "1..*" Beneficiarios : tem
    Instituicao "1" --> "1" ControleEstoque : tem
    Instituicao "1" --> "2" Veiculo : usa
    Doacao "1" --> "1" Material : relacionado
    ControleEstoque "1" --> "1" Material : controla
    ControleEstoque "1" --> "1" Doadores : registra
    ControleEstoque "1" --> "1" Beneficiarios : registra
    Veiculo "1" --> "1" Material : transporta

```

### 3.1.1. Descrição do Diagrama de classe:

Instituicao é a classe principal, representando a entidade que administra a organização, que possui atributos como nome, CNPJ, localização, etc.

Doacao é a classe que representa as doações de materiais feitas para a instituição.

Deposito representa os depósitos (temporários e permanentes) de materiais.

Material armazena os diferentes tipos de materiais, como tijolos e telhas.

Doadores e Beneficiarios são as classes que representam as pessoas que doam e aquelas que recebem os materiais, respectivamente.

ControleEstoque é a classe que gerencia o controle do estoque, registrando entradas e saídas de materiais.

Veiculo refere-se aos veículos utilizados pela instituição para transportar materiais.

## 3.2. Diagrama ER


> [!TIP]
> Faça um diagrama de Entidade Relacionamento usando Markdown e Mermaid, para os requisitos abaixo:


```mermaid

erDiagram
    INSTITUICAO {
        string nome
        string cnpj
        string localizacao
        string cidade
        string regimentoInterno
        string horarioAtendimento
    }

    DOACAO {
        string tipoMaterial
        string dataHora
        string descricao
    }

    DEPOSITO {
        string tipoDeposito
        boolean estaCheio
    }

    MATERIAL {
        string nome
        string tipo
        double quantidade
    }

    DOADOR {
        string nome
        string cpfCnpj
        string endereco
    }

    BENEFICIARIO {
        string nome
        string documentoIdentidade
        string endereco
        string tipoMaterialRecebido
    }

    CONTROLE_ESTOQUE {
        string localArmazenamento
        string dataHora
        string material
        string doador
        string beneficiario
    }

    VEICULO {
        string modelo
        string placa
    }



```




## 3.3. Diagrama de casos de uso


incluir o digrama feito no white star
![]()

## 3.3. Diagrama de atividade

incluir o digrama feito no white star
![]()

## 3.4. Diagrama de componentes

## 3.5. Diagrama de implantação

## 4. Histórias de usuário

## 5. Protótipo de telas

## 6. Diagrama de navegação de tela

