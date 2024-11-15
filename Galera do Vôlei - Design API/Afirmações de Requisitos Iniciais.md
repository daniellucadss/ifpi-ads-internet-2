# Afirmações de Requisitos Iniciais - Galera do Vôlei
## **Usuário tem um Perfil** com os seguintes atributos:
### **Atributos do Usuário**:
- nome
- sexo
- idade
- categoria
- tipo
- telefone

### **Invariantes**:
- **nome** deve ter entre 3 e 50 caracteres.
- **sexo** deve ser uma das opções: masculino, feminino ou não informado.
- **idade** deve ser um número inteiro entre 18 e 80.
- **categoria** deve ser uma das opções: iniciante, intermediário ou avançado.
- **tipo** deve ser uma das opções: jogador ou organizador.
- **telefone** deve estar em formato válido de número de telefone.

## **Usuário possui um Endereço**:
### **Atributos**:
- rua
- cidade
- estado
- cep

### **Restrição de Relacionamento**:
- Um **Usuário** pode ter um ou mais **Endereços** (relação de 1 para N).

### **Invariantes**:
- **cep** deve ter exatamente 8 dígitos.
- **estado** deve estar em uma lista de estados válidos.

## **Usuário pode criar ou participar de uma Partida**:
### **Atributos da Partida**:
- local
- data
- situacao
- categoria
- tipo

### **Restrição de Relacionamento**:
- Um **Usuário** (Organizador) pode criar várias **Partidas** (relação 1 para N).
- Um **Usuário** (Jogador) pode participar de várias **Partidas** (relação 1 para N).

### **Estados da Partida**:
- Em adesão
- Encerrada
- Realizada

### **Transições de Estado**:
- Em adesão -> Encerrada (quando o organizador encerra a adesão).
- Encerrada -> Realizada (quando a partida é realizada).

### **Invariantes**:
- **data** deve ser uma data válida no futuro.
- **situação** deve ser uma das opções: Em adesão, encerrada ou realizada.
- **categoria** deve ser uma das opções: iniciante, intermediário ou avançado.
- **tipo** deve ser uma das opções: mista, masculina ou feminina.

## Solicitação
### Atributos:
- requester_id
- requestee_id
- message
- status

### Relacionamento:
- Um **Usuário** pode enviar várias Solicitações (relação 1 para N).

### Estados da Solicitação:
- PENDING
- ACCEPTED
- REJECTED

### Invariantes:
- **status** deve ser uma das opções: PENDING, ACCEPTED, REJECTED.
