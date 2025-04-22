import boto3
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class DynamoUpdateService:
    def __init__(self, table_name: str):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(table_name)

    def update_item(self, item_id: str, update_data: dict) -> dict:
        if not update_data:
            raise ValueError("Nenhum dado para atualizar.")

        update_data.pop("id", None)

        update_expression = "SET " + ", ".join(f"#{k} = :{k}" for k in update_data.keys())
        print(update_expression)
        expression_attribute_values = {f":{k}": v for k, v in update_data.items()}
        expression_attribute_names= {f"#{k}": k for k in update_data.keys()}

        try:
            logger.info(f"Atualizando item {item_id} com dados: {update_data}")
            response = self.table.update_item(
                Key={"id": item_id},
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values,
                ExpressionAttributeNames=expression_attribute_names,
                ConditionExpression="attribute_exists(id)",
                ReturnValues="ALL_NEW"
            )
            
            logger.info(f"Update realizado com sucesso: {response}")
            return response["Attributes"]

        except Exception as e:
            logger.error(f"Erro ao atualizar item {item_id}: {e}")
            raise Exception("Erro ao atualizar item no DynamoDB")
