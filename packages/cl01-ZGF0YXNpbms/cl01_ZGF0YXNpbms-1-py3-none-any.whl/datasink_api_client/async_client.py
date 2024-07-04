import httpx
from urllib.parse import urljoin
from pydantic import BaseModel
from datasink_api_client import models
from typing import List, Dict, Any, Optional, Union


class AsyncDatasinkAPIClient:
    def __init__(self, base_url, credentials):
        self.base_url = base_url
        self.credentials = credentials
        self.session = httpx.AsyncClient(headers={
            'Authorization': f'Basic {self.credentials}',
            'Content-Type': 'application/json'
        })

    async def _request(self, method, endpoint, object_ctor, json=None, **kwargs):
        url = urljoin(self.base_url, endpoint)
        if json is not None:
            if type(json.__class__) == type(BaseModel):
                json = json.model_dump()
            kwargs['json'] = json

        async with self.session:
            response = await self.session.request(method, url, **kwargs)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list):
            return [object_ctor(**item) for item in data]
        return object_ctor(**data)

    async def read_root(self) -> models.ReadRootResponse:
        """Read Root"""
        return await self._request(
            'GET',
            '/',
            object_ctor=models.ReadRootResponse
        )

    async def health_check(self) -> models.HealthCheckResponse:
        """Health Check"""
        return await self._request(
            'GET',
            '/health',
            object_ctor=models.HealthCheckResponse
        )

    async def get_models(self) -> List[models.EmbeddingModel]:
        """Get Models"""
        return await self._request(
            'GET',
            '/models',
            object_ctor=models.EmbeddingModel
        )

    async def create_model(self, embedding_model: models.EmbeddingModel) -> Union[models.EmbeddingModel, models.HTTPValidationError, dict]:
        """Create Model"""
        return await self._request(
            'POST',
            '/models',
            json=embedding_model,
            object_ctor=models.EmbeddingModel
        )

    async def create_embedding(self, embedding_request: models.EmbeddingRequest) -> Union[models.HTTPValidationError, models.EmbeddingResponse, dict, models.ModelNotFoundResponse]:
        """Create Embedding"""
        return await self._request(
            'POST',
            '/embed',
            json=embedding_request,
            object_ctor=models.EmbeddingResponse
        )

    async def get_collections(self) -> List[dict]:
        """Get Collections"""
        return await self._request(
            'GET',
            '/collections',
            object_ctor=dict
        )

    async def create_collection(self, collection_info: Union['CollectionInfo', 'QdrantCollectionInfo']) -> Union[models.HTTPValidationError, models.UnsupportedCollectionTypeResponse, models.QdrantCollectionInfo, dict]:
        """Create Collection"""
        return await self._request(
            'POST',
            '/collections',
            json=collection_info,
            object_ctor=models.QdrantCollectionInfo
        )

    async def update_collection(self, collection_id, partial_collection_info: models.PartialCollectionInfo) -> Union[dict, models.HTTPValidationError, models.CollectionNotFoundResponse]:
        """Update Collection"""
        return await self._request(
            'PATCH',
            f'/collections/{collection_id}',
            json=partial_collection_info,
            object_ctor=dict
        )

    async def delete_collection(self, collection_id) -> Union[dict, models.HTTPValidationError, models.CollectionNotFoundResponse]:
        """Delete Collection"""
        return await self._request(
            'DELETE',
            f'/collections/{collection_id}',
            object_ctor=dict
        )

    async def get_collection(self, collection_id) -> Union[dict, models.HTTPValidationError, models.CollectionNotFoundResponse]:
        """Get Collection"""
        return await self._request(
            'GET',
            f'/collections/{collection_id}',
            object_ctor=dict
        )

    async def query(self, collection_id, query_request: models.QueryRequest) -> Union[dict, models.HTTPValidationError, models.UnsupportedCollectionTypeResponse, models.CollectionNotFoundResponse]:
        """Query"""
        return await self._request(
            'POST',
            f'/collections/{collection_id}/query',
            json=query_request,
            object_ctor=dict
        )

    async def get_collection_entities_list(self, collection_id, limit, offset) -> Union[models.HTTPValidationError, models.CollectionNotFoundResponse, models.CollectionEntityListResponse]:
        """Get Collection Entities List"""
        return await self._request(
            'GET',
            f'/collections/{collection_id}/entities',
            params=dict(limit=limit, offset=offset),
            object_ctor=models.CollectionEntityListResponse
        )

    async def create_collection_entity(self, collection_id, collection_entity: models.CollectionEntity) -> Union[models.CollectionEntityListResponse, dict, models.HTTPValidationError, models.CollectionEntityAlreadyExistsResponse, models.CollectionNotFoundResponse]:
        """Create Collection Entity"""
        return await self._request(
            'POST',
            f'/collections/{collection_id}/entities',
            json=collection_entity,
            object_ctor=models.CollectionEntityListResponse
        )

    async def get_collection_entity(self, collection_id, entity_id) -> Union[models.CollectionEntityResponse, models.HTTPValidationError, models.CollectionOrCollectionEntityNotFoundResponse]:
        """Get Collection Entity"""
        return await self._request(
            'GET',
            f'/collections/{collection_id}/entities/{entity_id}',
            object_ctor=models.CollectionEntityResponse
        )

    async def update_collection_entity(self, collection_id, entity_id, collection_entity: models.CollectionEntity) -> Union[models.CollectionEntityResponse, models.HTTPValidationError, models.CollectionOrCollectionEntityNotFoundResponse]:
        """Update Collection Entity"""
        return await self._request(
            'PUT',
            f'/collections/{collection_id}/entities/{entity_id}',
            json=collection_entity,
            object_ctor=models.CollectionEntityResponse
        )

    async def delete_collection_entity(self, collection_id, entity_id) -> Union[dict, models.HTTPValidationError, models.CollectionNotFoundResponse]:
        """Delete Collection Entity"""
        return await self._request(
            'DELETE',
            f'/collections/{collection_id}/entities/{entity_id}',
            object_ctor=dict
        )

    async def add_data(self, collection_id, data_point: Union['DataPoint', List['DataPoint']]) -> Union[dict, models.HTTPValidationError, models.UnsupportedCollectionTypeResponse, models.CollectionNotFoundResponse]:
        """Add Data"""
        return await self._request(
            'POST',
            f'/collections/{collection_id}/data',
            json=data_point,
            object_ctor=dict
        )
