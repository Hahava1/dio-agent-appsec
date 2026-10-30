# Base de Conhecimento: Segurança de Aplicações (AppSec)

Este documento contém as regras defensivas, frameworks e boas práticas de segurança para análise de código.

## 1. Mapeamento de Vulnerabilidades Comuns (CWE e MITRE ATT&CK)

*   **Injeção de SQL (CWE-89):**
    *   **Tática MITRE:** Initial Access (TA0001)
    *   **Técnica MITRE:** Exploit Public-Facing Application (T1190)
    *   **Regra Defensiva:** Nunca confie em inputs do usuário. É terminantemente proibido o uso de concatenação de strings ou interpolação (ex: f-strings no Python) para montar consultas SQL.
    *   **Mitigação Obrigatória:** Exija o uso de Consultas Parametrizadas (Prepared Statements) suportadas pelo driver do banco de dados (ex: usar `?` no SQLite ou `%s` no psycopg2).

*   **Cross-Site Scripting - XSS (CWE-79):**
    *   **Técnica MITRE:** Drive-by Compromise (T1189)
    *   **Regra Defensiva:** Qualquer dado originado do usuário que for renderizado no navegador deve ser neutralizado.
    *   **Mitigação Obrigatória:** Exija a sanitização de entrada e o Output Encoding (codificação de saída) antes de exibir os dados na tela.

## 2. Princípios de Orientação ao Estudante
*   **Foco na Causa Raiz:** Explique o *porquê* da falha estrutural, mostrando como caracteres especiais (como aspas simples `'` ou traços `--`) alteram a lógica da aplicação.
*   **Zero Respostas Prontas sem Explicação:** Apenas fornecer o código seguro não ensina segurança. Conduza o raciocínio mostrando a diferença entre a string executável e o dado literal.