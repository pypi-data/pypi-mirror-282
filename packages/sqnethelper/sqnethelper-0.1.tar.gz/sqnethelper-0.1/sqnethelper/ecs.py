
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest, StartInstanceRequest, StopInstanceRequest

class ECSManager:
    def __init__(self, access_key, access_secret, region):
        self.client = AcsClient(access_key, access_secret, region)

    def list_instances(self):
        request = DescribeInstancesRequest.DescribeInstancesRequest()
        response = self.client.do_action_with_exception(request)
        return response

    def start_instance(self, instance_id):
        request = StartInstanceRequest.StartInstanceRequest()
        request.set_InstanceId(instance_id)
        response = self.client.do_action_with_exception(request)
        return response

    def stop_instance(self, instance_id):
        request = StopInstanceRequest.StopInstanceRequest()
        request.set_InstanceId(instance_id)
        response = self.client.do_action_with_exception(request)
        return response
