# Contrato de API - Galera do Vôlei
## Endpoints - Usuários
### 1. **GET /usuarios**
- **Descrição**: Retorna todos os usuários com opções de filtro, ordenação e paginação.
- **URL Params**: None
- **Query Params**:
  - `sexo` (opcional, `string`): Filtra por sexo do usuário.
  - `idade_min` (opcional, `integer`): Filtra por idade mínima do usuário.
  - `idade_max` (opcional, `integer`): Filtra por idade máxima do usuário.
  - `categoria` (opcional, `string`): Filtra por categoria de habilidade do usuário (e.g., iniciante, intermediário, avançado).
  - `order` (opcional, `string`): Ordena os resultados por campo. Formato: `{campo}_{asc|desc}`.
    - Campos suportados: `nome`, `idade`, `categoria`.
    - Exemplo: `order=nome_asc` ou `order=idade_desc`.
  - `page` (opcional, `integer`): Define a página atual dos resultados.
  - `per_page` (opcional, `integer`): Número de usuários por página. 
- **Data Params**: None
- **Headers**:
  - `Content-Type`: `application/json`
  - `Authorization`: `Bearer <OAuth Token>`
- **Response**:
  - **Success**:
    - **Code**: `200 OK`
    - **Content**:
      ```json
      {
          "_metadata": 
          {
              "current_page": "5",
              "per_page": "2",
              "page_count": "2",
              "total_count": "30",
              "order": "idade_desc",
              "links": [
                    {"self": "/usuarios?page=5&per_page=2"},
                    {"first": "/usuarios?page=0&per_page=2"},
                    {"previous": "/usuarios?page=4&per_page=2"},
                    {"next": "/usuarios?page=6&per_page=2"},
                    {"last": "/usuarios?page=26&per_page=2"},
              ]
          },
          "usuarios": [
              {
                  "usuario_id": "1",
                  "nome": "João",
                  "sexo": "masculino",
                  "idade": 25,
                  "categoria": "iniciante",
                  "tipo": "jogador"
              },
              {
                  "usuario_id": "2",
                  "nome": "Maria",
                  "sexo": "feminino",
                  "idade": 30,
                  "categoria": "intermediário",
                  "tipo": "organizador"
              }
          ]
      }
      ```
  - **Error**:
    - **Code**: `400 Bad Request`
    - **Content**:
      ```json
      {
        "error": "Parâmetros invalidos."
      }
      ```
    - **Code**: `401 Unauthorized`
    - **Content**: 
      ```json
      { "error": "Não autorizado." }
      ```

### 2. **GET /usuarios/{id}**
- **Descrição**: Retorna informações de um usuário específico.
- **URL Params**:
  - `usuario_id` (obrigatório, `integer`): ID do usuário.
- **Query Params**: None
- **Data Params**: None
- **Headers**:
  - `Content-Type`: `application/json`
  - `Authorization`: `Bearer <OAuth Token>`
- **Response**:
  - **Success**:
    - **Code**: `200 OK`
    - **Content**:
      ```json
      {
        "usuario_id": 1,
        "nome": "João",
        "sexo": "masculino",
        "idade": "25",
        "categoria": "iniciante",
        "tipo": "jogador",
      }
      ```
  - **Error**:
    - **Code**: `404 Not Found`
    - **Content**: 
      ```json
      {
        "error": "Registro não encontrado."
      }
      ```
    - **Code**: `401 Unauthorized`
    - **Content**:
      ```json
      {
        "error": "Não autorizado."
      }
      ```

### 3. **POST /usuarios**
- **Descrição**: Cria um novo usuário.
- **URL Params**: None
- **Query Params**: None
- **Data Params**:
  - `id` (obrigatório, `integer`): ID do usuário;
  - `nome` (obrigatório, `string`): Nome de usuário;
  - `sexo` (opcional, `string`): Sexo do usuário;
  - `idade` (opcional, `integer`): Idade do usuário;
  - `categoria` (obrigatório, `string`): Categoria de habilidade (iniciante, intermediário, avançado);
  - `tipo` (obrigatório, `string`): Tipo de usuário (organizador, jogador);
- **Headers**:
  - `Content-Type`: `application/json`
  - `Authorization`: `Bearer <OAuth Token>`
- **Response**:
  - **Success**:
    - **Code**: `201 Created`
    - **Content**:
      ```json
      {
        "usuario_id": 3,
        "nome": "Gabriel",
        "sexo": "masculino",
        "idade": "18",
        "categoria": "iniciante",
        "tipo": "jogador",
      }
      ```
  - **Error**:
    - **Code**: `409 Conflict`
    - **Content**:
      ```json
      {
        "error": "Registro existente."
      }
      ```
    - **Code**: `401 Unauthorized`
    - **Content**: 
      ```json
      {
        "error": "Não autorizado."
      }
      ```

### 4. **PUT /usuarios/{id}**
- **Descrição**: Atualiza informações de um usuário específico.
- **URL Params**:
  - `usuario_id` (obrigatório, `integer`): ID do usuário.
- **Query Params**: None
- **Data Params**:
  - `name` (opcional, `string`): Nome de usuário;
  - `email` (opcional, `string`): E-mail do usuário;
  - `sexo` (opcional, `string`): Sexo do usuário;
  - `idade` (opcional, `integer`): Idade do usuário;
  - `categoria` (opcional, `string`): Categoria de habilidade (iniciante, intermediário, avançado);
  - `tipo` (opcional, `string`): Tipo de usuário (organizador, jogador);
- **Headers**:
  - `Content-Type`: `application/json`
  - `Authorization`: `Bearer <OAuth Token>`
- **Response**:
  - **Success**:
    - **Code**: `20
    - **Content**:
      ```json
      {
        "usuario_id": 1,
        "nome": "João",
        "sexo": "masculino",
        "idade": "25",
        "categoria": "intermediário",
        "tipo": "jogador",
      }
      ```
  - **Error**:
    - **Code**: `404 Not Found`
    - **Content**: 
      ```json
      {
        "error": "Registro não encontrado."
      }
      ```
    - **Code**: `401 Unauthorized`
    - **Content**: 
      ```json
      {
        "error": "Não autorizado."
      }


### 5. **DELETE /usuarios/{id}**
- **Descrição**: Exclui um usuário específico.
- **URL Params**:
  - `usuario_id` (obrigatório, `integer`): ID do usuário.
- **Query Params**: None
- **Data Params**: None
- **Headers**:
  - `Content-Type`: `application/json`
  - `Authorization`: `Bearer <OAuth Token>`
- **Response**:
  - **Success**:
    - **Code**: `204 No Content`
  - **Error**:
    - **Code**: `401 Unauthorized`
    - **Content**: 
      ```json
      {
        "error": "Não autorizado."
      }
      ```
    - **Code**: `404 Not Found`
    - **Content**: 
      ```json
      {
        "error": "Registro não encontrado."
      }

---

## Endpoints - Partidas
### 1. **GET /partidas**
- **Descrição**: Retorna todas as partidas com opções de filtro ordenação e paginação.
- **URL Params**: None
- **Query Params**:
  - `local` (opcional, `string`): Local da partida;
  - `data` (opcional, `date`): Data da partida;
  - `situacao` (opcional, `string`): Situação da partida (nova, em adesão, encerrada, realizada);
  - `categoria` (opcional, `string`): Categoria de habilidade (iniciante, intermediário, avançado);
  - `tipo` (opcional, `string`): Tipo de partida (mista, feminina, masculina);
  - `order` (opcional, `string`): Ordena os resultados por campo. Formato: `{campo}_{asc|desc}`.
    - Campos suportados: `local`, `data`, `situacao`, `categoria`, `tipo`.
    - Exemplo: `order=local_asc` ou `order=data_desc`.
  - `page` (opcional, `integer`): Define a página atual dos resultados.
  - `per_page` (opcional, `integer`): Número de partidas por página. 
- **Data Params**: None
- **Headers**:
  - `Content-Type`: `application/json`
  - `Authorization`: `Bearer <OAuth Token>`
- **Response**:
  - **Success**:
    - **Code**: `200 OK`
    - **Content**:
      ```json
      {
        "_metadata": 
        {
            "current_page": "2",
            "per_page": "2",
            "page_count": "2",
            "total_count": "10",
            "order": "local_asc",
            "links": [
                {"self": "/partidas?page=2&per_page=2"},
                {"first": "/partidas?page=0&per_page=2"},
                {"previous": "/partidas?page=1&per_page=2"},
                {"next": "/partidas?page=3&per_page=2"},
                {"last": "/partidas?page=5&per_page=2"},
            ]
        },
        "partidas": [
            {
                "partida_id": 1,
                "local": "Arena Aqualine",
                "data": "2024-11-07",
                "situacao": "realizada",
                "categoria": "avancado",
                "tipo": "mista",
            },
            {
                "partida_id": 2,
                "local": "Arena Aqualine",
                "data": "2024-10-15",
                "situacao": "encerrada",
                "categoria": "iniciante",
                "tipo": "feminina",
            }
        ]
      }
      ```
  - **Error**:
    - **Code**: `401 Unauthorized`
    - **Content**:
      ```json
      {
        "error": "Não autorizado."
      }
      ```
    - **Code**: `404 Not Found`
    - **Content**:
      ```json
      {
        "error": "Registro não encontrado."
      }
      ```

### 2. **GET /partidas/{partida_id}**
- **Descrição**: Retorna detalhes de uma partida específica.
- **URL Params**:
  - `partida_id` (obrigatório, `integer`): ID da partida.
- **Query Params**: None
- **Data Params**: None
- **Headers**:
  - `Content-Type`: `application/json`
  - `Authorization`: `Bearer <OAuth Token>`
- **Response**:
  - **Success**:
    - **Code**: `200 OK`
    - **Content**: `{ <partida_object> }`
  - **Error**:
    - **Code**: `401 Unauthorized`
    - **Content**: 
      ```json
      {
        "error": "Não autorizado."
      }
      ```
    - **Code**: `404 Not Found`
    - **Content**: 
      ```json
      {
        "error": "Registro não encontrado."
      }
   

### 3. **POST /partidas**
- **Descrição**: Cria uma nova partida associada a um usuário específico.
- **URL Params**: None
- **Query Params**: None
- **Data Params**:
  - `partida_id` (obrigatório, `integer`): ID da partida.
  - `local` (obrigatório, `string`): Local da partida.
  - `data` (obrigatório, `date`): Data da partida.
  - `situacao` (obrigatório, `string`): Situação da partida (nova, em adesão, encerrada, realizada).
  - `categoria` (obrigatório, `string`): Categoria da partida (iniciante, intermediário, avançado).
  - `tipo` (obrigatório, `string`): Tipo de partida (mista, feminina, masculina).
- **Headers**:
  - `Content-Type`: `application/json`
  - `Authorization`: `Bearer <OAuth Token>`
- **Response**:
  - **Success**:
    - **Code**: `201 Created`
    - **Content**: 
      ```json
      {
        "partida_id": 3,
        "local": "Arena Beach Vôlei Bar",
        "data": "2024-11-22",
        "situacao": "em adesão",
        "categoria": "intermediário",
        "tipo": "feminina",
      }
  - **Error**:
    - **Code**: `401 Unauthorized`
    - **Content**: 
      ```json
      {
        "error": "Não autorizado."
      }
      ```
    - **Code**: `403 Forbidden`
    - **Content**: 
      ```json
      {
        "error": "Somente usuários do tipo organizador podem criar partidas."
      }
    - **Code**: `404 Not Found`
    - **Content**: 
      ```json
      {
        "error": "Registro não encontrado."
      }


### 4. **PUT /partidas/{partida_id}**
- **Descrição**: Atualiza os dados de uma partida especifica.
- **URL Params**:
  - `partida_id` (obrigatório, `integer`): ID da partida que será atualizada
- **Query Params**: None
- **Data Params**:
  - `local` (opcional, `string`): Local da partida.
  - `data` (opcional, `date`): Data da partida.
  - `situacao` (opcional, `string`): Situação da partida (nova, em adesão, encerrada, realizada).
  - `categoria` (opcional, `string`): Categoria da partida (iniciante, intermediário, avançado).
  - `tipo` (opcional, `string`): Tipo de partida (mista, feminina, masculina).
- **Headers**:
  - `Content-Type`: `application/json`
  - `Authorization`: `Bearer <OAuth Token>`
- **Response**:
  - **Success**:
    - **Code**: `200 OK`
    - **Content**: 
      ```json
      {
        "partida_id": 3,
        "local": "Arena Beach Véloz",
        "data": "2024-11-22",
        "situacao": "realizada",
        "categoria": "iniciante",
        "sexo": "feminina",
      }
  - **Error**:
    - **Code**: `401 Unauthorized`
    - **Content**: 
      ```json
      {
        "error": "Não autorizado."
      }
    - **Code**: `403 Forbidden`
    - **Content**: 
      ```json
      {
        "error": "Somente usuários do tipo organizador podem atualizar partidas."
      }
    - **Code**: `404 Not Found`
    - **Content**: 
      ```json
      {
        "error": "Registro não encontrado."
      }

### 5. **DELETE /partidas/{partida_id}**
- **Descrição**: Exclui os dados de uma partida especifica.
- **URL Params**:
  - `partida_id` (obrigatório, `integer`): ID da partida.
- **Query Params**: None
- **Data Params**: None
- **Headers**:
  - `Content-Type`: `application/json`
  - `Authorization`: `Bearer <OAuth Token>`
- **Response**:
  - **Success**:
    - **Code**: `204 No Content`
  - **Error**:
    - **Code**: `401 Unauthorized`
    - **Content**: 
      ```json
      {
        "error": "Não autorizado."
      }
    - **Code**: `403 Forbidden`
    - **Content**: 
      ```json
      {
        "error": "Somente usuários do tipo organizador podem excluir partidas."
      }
    - **Code**: `404 Not Found`
    - **Content**: 
      ```json
      {
        "error": "Registro não encontrado."
      }
    
---

## Endpoints - Solicitações
### 1. **GET /partidas/{partida_id}/solicitacoes?status=PENDING**
- **Descrição**: Retorna todas as solicitações pendentes para a participação de uma partida.
- **URL Params**:
  - `partida_id` (obrigatório, `integer`): ID da partida.
- **Query Params**:
  - `status` (opcional, `string`): Filtra por status da solicitação.
- **Data Params**: None
- **Headers**:
  - `Content-Type`: `application/json`
  - `Authorization`: `Bearer <OAuth Token>`
- **Response**:
  - **Success**:
    - **Code**: `200 OK`
    - **Content**: 
      ```json
      {
        "solicitacoes": [
          {
            "solicitacao_id": 1,
            "requester_id": 1,
            "requestee_id": 2,
            "status": "PENDING"
          },
          {
            "solicitacao_id": 2,
            "requester_id": 1,
            "requestee_id": 3,
            "status": "PENDING"
          }
        ]
      }
      ```
  - **Error**:
    - **Code**: `401 Unauthorized`
    - **Content**:
      ```json
      {
        "error": "-nao autorizado."
      }
      ```
    - **Code**: `404 Not Found`
    - **Content**: 
      ```json
      {
        "error": "Registro nao encontrado."
      }

### 2 **POST /partidas/{partida_id}/solicitacoes/**
- **Descrição**: Um usuário envia uma solicitação para participar de uma partida.
- **URL Params**:
  - `partida_id` (obrigatório, `integer`): ID da partida para a qual a solicitação será enviada.
- **Query Params**: None
- **Data Params**:
  - `requester_id` (obrigatório, `integer`): ID de quem está fazendo a solicitação.
  - `requestee_id` (obrigatório, `integer`): ID para quem a solicitação é enviada.
  - `message` (opcional, `string`): Mensagem de descrição da solicitação.
- **Headers**:
  - `Content-Type`: `application/json`
  - `Authorization`: `Bearer <OAuth Token>`
- **Response**:
  - **Success**:
    - **Code**: `201 Created`
    - **Content**: 
      ```json
      {
        "solicitacao_id": "integer",                
        "requester_id": "integer", 
        "requestee_id": "integer",
        "message": "string",          
        "status": "PENDING"         
      }
      ```
  - **Error**:
    - **Code**: `401 Unauthorized`
    - **Content**: 
      ```json
      {
        "error": "Não autorizado."
      }
      ```
    - **Code**: `409 Conflict`
    - **Content**: 
      ```json
      {
        "error": "Solicitação já existente."
      }
      ```


### 3 **PUT partidas/{partida_id}/solicitacoes/{solicitacao_id}?action=(ACCEPT|REJECT)**
- **Descrição**: Um usuário aceita ou rejeita uma solicitação para participar de uma partida.
- **URL Params**:
  - `partida_id` (obrigatório, `integer`): ID da partida para a qual a solicitação foi enviada.
  - `solicitacao_id` (obrigatório, `integer`): ID da solicitação.
- **Query Params**:
  - `action` (obrigatório, `string`): Define a ação a ser tomada na solicitação.
- **Data Params**: None
- **Headers**:
  - `Content-Type`: `application/json`
  - `Authorization`: `Bearer <OAuth Token>`
- **Response**:
  - **Success**:
    - **Code**: `200 OK`
    - **Content**: 
      ```json
      {
        "solicitacao_id": "integer",
        "requester_id": "integer",
        "requestee_id": "integer",
        "message": "string",
        "status": "ACCEPTED || REJECTED"
      }
      ```
      
  - **Error**:
    - **Code**: `401 Unauthorized`
    - **Content**:
      ```json
      {
        "error": "Não autorizado."
      }
      ```
    - **Code**: `404 Not Found`
    - **Content**: 
      ```json
      {
        "error": "Registro nao encontrado."
      }
      ```