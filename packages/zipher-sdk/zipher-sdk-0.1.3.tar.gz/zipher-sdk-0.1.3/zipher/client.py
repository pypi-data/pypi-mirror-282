import os
import json
import requests
from zipher.conf import Conf
from typing import Dict
from databricks.sdk.service.compute import ClusterSpec
from zipher.models import ConfFetcherRequest


class Client:
    def __init__(self, customer_id: str, zipher_api_key: str = ''):
        self.zipher_api_key = zipher_api_key or os.getenv(Conf.zipher_api_key_env_var)
        self.customer_id = customer_id

    def _call_conf_fetcher_api(self, params: ConfFetcherRequest):
        headers = {
            'x-api-key': self.zipher_api_key
        }
        response = requests.get(
            url=Conf.zipher_config_fetcher_api_endpoint,
            headers=headers,
            params=params.model_dump()
        )
        if response.ok:
            return json.loads(response.json()['body'])
        else:
            response.raise_for_status()

    def get_optimized_config(self, job_id: str) -> Dict:
        params = ConfFetcherRequest(customer_id=self.customer_id, job_id=job_id)
        return self._call_conf_fetcher_api(params)

    def get_optimized_config_as_dbx_cluster_spec(self, job_id: str) -> ClusterSpec:
        return ClusterSpec.from_dict(self.get_optimized_config(job_id))

    def update_existing_conf(self, job_id: str, existing_conf: Dict) -> Dict:
        if 'new_cluster' in existing_conf:
            existing_conf = existing_conf['new_cluster']
        params = ConfFetcherRequest(customer_id=self.customer_id, job_id=job_id, merge_with=json.dumps(existing_conf))
        return self._call_conf_fetcher_api(params)

        # optimized_spec = self.get_optimized_config_as_dbx_cluster_spec(job_id=job_id)
        # if 'new_cluster' in existing_conf:
        #     existing_conf = existing_conf['new_cluster']
        # existing_spec = ClusterSpec.from_dict(existing_conf)
        # merged_spec = self.cluster_spec_merger.merge(orig_spec=existing_spec, optimized_spec=optimized_spec)
        # merged_dict = merged_spec.as_dict()

