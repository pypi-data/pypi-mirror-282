import os
import json
import requests
from zipher.conf import Conf
from zipher.cluster_spec_merger import ClusterSpecMerger
from typing import Dict
from databricks.sdk.service.compute import ClusterSpec


class Client:
    def __init__(self, customer_id: str, zipher_api_key: str = ''):
        self.zipher_api_key = zipher_api_key or os.getenv(Conf.zipher_api_key_env_var)
        self.customer_id = customer_id
        self.cluster_spec_merger = ClusterSpecMerger()

    def get_optimized_config(self, job_id: str) -> Dict:
        headers = {
            'x-api-key': self.zipher_api_key
        }
        params = {
            'customer_id': self.customer_id,
            'job_id': job_id
        }
        response = requests.get(url=Conf.zipher_config_fetcher_api_endpoint, headers=headers, params=params)
        if response.ok:
            return json.loads(response.json()['body'])
        else:
            response.raise_for_status()

    def get_optimized_config_as_dbx_cluster_spec(self, job_id: str) -> ClusterSpec:
        return ClusterSpec.from_dict(self.get_optimized_config(job_id))

    def update_existing_conf(self, job_id: str, existing_conf: Dict) -> Dict:
        optimized_spec = self.get_optimized_config_as_dbx_cluster_spec(job_id=job_id)
        if 'new_cluster' in existing_conf:
            existing_conf = existing_conf['new_cluster']
        existing_spec = ClusterSpec.from_dict(existing_conf)
        merged_spec = self.cluster_spec_merger.merge(orig_spec=existing_spec, optimized_spec=optimized_spec)
        return merged_spec.as_dict()

