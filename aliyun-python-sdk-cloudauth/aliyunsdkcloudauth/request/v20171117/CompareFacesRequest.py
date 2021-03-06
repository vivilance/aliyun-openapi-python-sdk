# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CompareFacesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2017-11-17', 'CompareFaces','cloudauth')
		self.set_protocol_type('https');

	def get_SourceImageType(self):
		return self.get_query_params().get('SourceImageType')

	def set_SourceImageType(self,SourceImageType):
		self.add_query_param('SourceImageType',SourceImageType)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_TargetImageType(self):
		return self.get_query_params().get('TargetImageType')

	def set_TargetImageType(self,TargetImageType):
		self.add_query_param('TargetImageType',TargetImageType)

	def get_SourceImageValue(self):
		return self.get_query_params().get('SourceImageValue')

	def set_SourceImageValue(self,SourceImageValue):
		self.add_query_param('SourceImageValue',SourceImageValue)

	def get_TargetImageValue(self):
		return self.get_query_params().get('TargetImageValue')

	def set_TargetImageValue(self,TargetImageValue):
		self.add_query_param('TargetImageValue',TargetImageValue)