import requests
import base64


def _base64_encode_resource_id(resource_name: str, resource_id: int) -> str:
    formatted_string = f"{resource_name}-{resource_id}"
    encoded_string = base64.b64encode(formatted_string.encode()).decode()
    return encoded_string


class MarketplacerGQLClient:

    def __init__(self, gql_url: str, api_key: str):
        self.gql_url = gql_url
        self.api_key = api_key
        self.headers = {
            "MARKETPLACER-API-KEY": api_key,
            "Content-Type": "application/json",
        }

    def update_advert_price(self, advert_id: int, new_price: float):
        pass

    def update_variant_stock(self, variant_id: int, new_stock: int):

        encoded_id = _base64_encode_resource_id("Variant", variant_id)

        mutation = """
            mutation($input: VariantUpdateMutationInput!) {
                variantUpdate(input: $input) {
                variant {
                    legacyId
                    editablePrice
                    countOnHand
                    sku
                }
                errors {
                    field
                    messages
                }
                }
            }
            """

        variables = {
            "input": {
                "clientMutationId": "python-script",
                "variantId": encoded_id,
                "attributes": {"countOnHand": new_stock},
            }
        }

        gql_request = {"query": mutation, "variables": variables}

        response = requests.post(
            url=self.gql_url, json=gql_request, headers=self.headers
        )

        if response.ok:
            return response.json()
        else:
            response.raise_for_status()

    def get_variant_id_by_sku(self, sku: str) -> int:
        pass

    def get_advert_id_by_variant_id(self, variant_id: int) -> int:
        pass

    def get_mutations(self):

        introspection_query = """
            {
                __schema {
                    mutationType {
                        fields {
                            name
                        }
                    }
                }
            }
        """

        response = requests.post(
            url=self.gql_url, json={"query": introspection_query}, headers=self.headers
        )

        if response.status_code == 200:
            result = response.json()
            mutations = result["data"]["__schema"]["mutationType"]["fields"]
            return [mutation["name"] for mutation in mutations]
        else:
            response.raise_for_status()

    def upsert_advert(self, input: dict) -> dict:

        mutation = """
            mutation($input: AdvertUpsertMutationInput!) {
                advertUpsert(input: $input) {
                    advert {
                        id
                        editablePrice
                    }
                    errors {
                        field
                        messages
                    }
                }
            }
        """

        variables = {
            "input": {
                "clientMutationId": "python-script",
                "advertId": str(input["id"]),
                "attributes": {"price": str(input["price"])},
            }
        }

        gql_request = {"query": mutation, "variables": variables}

        response = requests.post(
            url=self.gql_url, json=gql_request, headers=self.headers
        )

        if response.ok:
            return response.json()
        else:
            raise response.raise_for_status()
