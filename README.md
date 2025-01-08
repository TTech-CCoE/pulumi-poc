# Prova de Conceito: Pulumi com Python

Este repositório contém uma prova de conceito utilizando [Pulumi](https://pulumi.com) para provisionamento de infraestrutura como código com Python. Esta PoC demonstra como configurar e gerenciar recursos em nuvem de forma programática.

## Objetivo

O objetivo desta PoC é demonstrar a simplicidade e a eficiência do Pulumi em comparação com outras ferramentas de gerenciamento de infraestrutura. Vamos provisionar recursos básicos em um provedor de nuvem (como AWS, Azure ou Google Cloud) utilizando Python.

## Pré-requisitos

Antes de começar, você precisará ter os seguintes itens instalados:

- [Python](https://www.python.org/downloads/) (v3.7 ou superior)
- [Pulumi CLI](https://www.pulumi.com/docs/get-started/install/)
- Acesso a uma conta em um provedor de nuvem (AWS, Azure, GCP)
- [Configure sua conta no Pulumi](https://www.pulumi.com/docs/get-started/install/)

## Configuração do Projeto

Clone este repositório:

```bash
git clone https://github.com/TTech-CCoE/pulumi-poc.git
cd poc-pulumi-python
```

Crie um ambiente virtual e ative-o:

```bash
python -m venv venv
source venv/bin/activate
# Para Windows use: venv\Scripts\activate
```

Instale as dependências necessárias:

```bash
pip install pulumi pulumi_aws  # ou outro provedor de nuvem, conforme necessário
```

Configure as credenciais do seu provedor de nuvem. Consulte a documentação do provedor escolhido para saber como configurar as credenciais.

Login no Pulumi
```bash
pulumi login
```
Para criar um novo projeto, execute:
```bash
pulumi new python
```

Siga as instruções para configurar o projeto.

Defina os Recursos
No arquivo __main__.py, adicione o código necessário para definir os recursos que você deseja provisionar. Um exemplo básico pode ser:

```python
import pulumi
import pulumi_aws as aws

# Exemplo de criação de um bucket S3
bucket = aws.s3.Bucket('meu-bucket')

pulumi.export('bucket_name', bucket.id)
```

Para provisionar os recursos definidos, execute:

```bash
pulumi up
```

Revise as alterações que serão aplicadas e confirme.

Após o provisionamento, você pode verificar os recursos no console do seu provedor de nuvem.

Para remover os recursos provisionados, use:

```bash
pulumi destroy
```

Estrutura do Projeto
Pulumi.yaml: Configuração do projeto Pulumi.
Possível Pulumi.yaml:
```yaml
name: meu-projeto
runtime: python
description: Um projeto de exemplo usando Pulumi com Python
config:
  aws:region: us-west-2
  database: my-database
  apiKey: ${APIC_KEY_ENV_VAR}  # Exemplo de uso de variável de ambiente
```

__main__.py: Código Python que define a infraestrutura a ser provisionada.
requirements.txt: Gerenciamento de dependências do projeto.
Exemplos
Você pode encontrar exemplos de recursos no arquivo __main__.py. Sinta-se à vontade para modificar e experimentar.

Contribuição
Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir um pull request.
