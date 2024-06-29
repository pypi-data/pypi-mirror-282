from pydantic import BaseModel, Field
import requests


class RestVariantAttributes(BaseModel):
    sku: str | None = None
    count_on_hand: int
    sale_price: str | None = None
    price: str | None = None
    barcode: str
    upc: str | None = None
    advert_id: int
    infinite: bool
    name: str
    master: bool
    item_unit: str | None = None


class RestVariant(BaseModel):
    variant_type: str = Field(..., alias="type")
    id: int
    attributes: RestVariantAttributes


class MarketplacerRestClient:

    def __init__(self, base_url: str, api_key: str):
        self.base_url = f"{base_url}/api/v2/client"
        self.api_key = api_key
        self.headers = {
            "MARKETPLACER-API-KEY": api_key,
            "Content-Type": "application/json",
        }

    def _fetch_variant_page(self, link: str) -> tuple[str | None, list[RestVariant]]:
        """
        Fetches a variant page from the provided link and returns the next page link and a list of RestVariant objects.

        Args:
            link (str): The link to fetch the variant page from.

        Returns:
            tuple[str | None, list[RestVariant]]: A tuple containing the next page link (or None if there is no next page) and a list of RestVariant objects.

        Raises:
            requests.HTTPError: If the response from the server is not successful.

        """
        if not link:
            return

        response = requests.get(link, headers=self.headers)

        if not response.ok:
            response.raise_for_status()

        json_response = response.json()
        json_variants = json_response.get("data", [])

        next_page_link = json_response.get("links", {}).get("next", None)

        return next_page_link, [RestVariant(**variant) for variant in json_variants]

    def fetch_all_variants(self) -> list[RestVariant]:
        """
        Fetches all variants from the server.

        Returns:
            A list of variant objects.
        """
        link = f"{self.base_url}/variants"
        variants: list[RestVariant] = []

        while link:
            link, page_variants = self._fetch_variant_page(link)
            variants.extend(page_variants)

        return variants
