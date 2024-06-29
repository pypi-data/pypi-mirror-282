from databricks.sdk.service.compute import ClusterSpec, AwsAttributes


class ClusterSpecMerger:
    def __init__(self):
        self.orig_spec: ClusterSpec = None
        self.optimized_spec: ClusterSpec = None

    def merge(self, orig_spec: ClusterSpec, optimized_spec: ClusterSpec) -> ClusterSpec:
        self.orig_spec = orig_spec
        self.optimized_spec = optimized_spec

        self._merge_autoscaling_config()
        self._merge_spark_cong_config()
        self._merge_aws_attrs()
        self._merge_node_types()
        self._merge_spark_env_vars()

        return self.orig_spec

    def _merge_autoscaling_config(self):
        if self.orig_spec.autoscale is None:
            self.orig_spec.autoscale = self.optimized_spec.autoscale
        else:
            if self.optimized_spec.autoscale is not None:
                self.orig_spec.autoscale.min_workers = self.optimized_spec.autoscale.min_workers
                self.orig_spec.autoscale.max_workers = self.optimized_spec.autoscale.max_workers

    def _merge_spark_cong_config(self):
        self.orig_spec.spark_conf = self.orig_spec.spark_conf or {}
        if self.optimized_spec.spark_conf:
            self.orig_spec.spark_conf.update(self.optimized_spec.spark_conf)

    def _merge_aws_attrs(self):
        self.orig_spec.aws_attributes = self.orig_spec.aws_attributes or AwsAttributes()
        if self.optimized_spec.aws_attributes:
            self.orig_spec.aws_attributes.ebs_volume_count = (self.optimized_spec.aws_attributes.ebs_volume_count or
                                                              self.orig_spec.aws_attributes.ebs_volume_count)
            self.orig_spec.aws_attributes.ebs_volume_size = (self.optimized_spec.aws_attributes.ebs_volume_size or
                                                              self.orig_spec.aws_attributes.ebs_volume_size)
            self.orig_spec.aws_attributes.ebs_volume_throughput = (
                    self.optimized_spec.aws_attributes.ebs_volume_throughput or
                    self.orig_spec.aws_attributes.ebs_volume_throughput)
            self.orig_spec.aws_attributes.ebs_volume_iops = (
                    self.optimized_spec.aws_attributes.ebs_volume_iops or
                    self.orig_spec.aws_attributes.ebs_volume_iops)
            self.orig_spec.aws_attributes.ebs_volume_type = (
                    self.optimized_spec.aws_attributes.ebs_volume_type or
                    self.orig_spec.aws_attributes.ebs_volume_type)
            self.orig_spec.aws_attributes.zone_id = (
                    self.optimized_spec.aws_attributes.zone_id or
                    self.orig_spec.aws_attributes.zone_id)
            self.orig_spec.aws_attributes.first_on_demand = (
                    self.optimized_spec.aws_attributes.first_on_demand or
                    self.orig_spec.aws_attributes.first_on_demand)

    def _merge_node_types(self):
        self.orig_spec.node_type_id = self.optimized_spec.node_type_id or self.orig_spec.node_type_id
        self.orig_spec.driver_node_type_id = self.optimized_spec.driver_node_type_id or self.orig_spec.driver_node_type_id

    def _merge_spark_env_vars(self):
        self.orig_spec.spark_env_vars = self.orig_spec.spark_env_vars or {}
        if self.optimized_spec.spark_env_vars:
            self.orig_spec.spark_env_vars.update(self.optimized_spec.spark_env_vars)
