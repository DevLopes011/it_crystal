# it_crystal

🧊 Projeto: IT Crystal
IT Crystal é uma aplicação backend serverless escrita em Python 3.13, com foco na organização e controle de equipamentos de TI. O projeto foi desenvolvido aplicando os princípios da Clean Architecture e SOLID, com forte separação de responsabilidades, camadas bem definidas e código altamente testável e extensível.

🎯 Objetivo
Fornecer uma API serverless escalável para gerenciamento de ativos de TI, permitindo o cadastro, consulta, atualização e exclusão de equipamentos, com rastreabilidade do estado físico e associação a colaboradores.

🧠 Arquitetura
✅ Padrões Adotados
Clean Architecture: Separação entre camadas de domínio, casos de uso, controladores (drivers) e infraestrutura (driven).

DDD (Domain-Driven Design): Entidades, value objects, agregados e repositórios.

SOLID:

Single Responsibility: Cada classe tem uma responsabilidade clara (ex: EquipmentUseCase, EquipmentEntity, PhysicalState).

Open/Closed: Estruturas como Enums e Value Objects permitem extensão sem modificação.

Dependency Inversion: Casos de uso dependem de abstrações (como o repositório).

⚙️ Tecnologias e Bibliotecas
Categoria	Tecnologias
Linguagem	Python 3.13
Arquitetura	Clean Architecture, SOLID
AWS Serverless	Lambda, DynamoDB
SDK AWS	Boto3, Boto3 Stubs
Validação e Tipagem	Pydantic v2
Boas Práticas AWS	aws-lambda-powertools
Logging	Loguru
Configuração	python-dotenv
Testes	Pytest

🧱 Camada de Domínio
🧩 Entidades
EquipmentEntity: Representa o equipamento.

UserProfileEntity: Representa o colaborador.

AssetAggregate: Agregado de equipamento.

📦 Value Objects
PhysicalState: Estado físico, defeitos, histórico de reparos.

AddressValueObject: Endereço completo do usuário.

🔠 Enum
EquipmentTypeEnum: Tipos de equipamento (Notebook, Mouse, Teclado etc.).

🔁 Casos de Uso (use_cases)
Implementações da lógica de negócio via a classe EquipmentUseCase, com métodos:

create

get

list

update

delete

Esses casos de uso interagem com o repositório DynamoDB via uma camada de infraestrutura desacoplada.


🧪 Testes
Pytest com tipagem estática via boto3-stubs.

📦 Gerenciamento
Poetry: Gerenciamento de pacotes e ambientes isolados.
