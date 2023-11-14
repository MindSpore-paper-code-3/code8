# Copyright 2021 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================

"""Device adapter for ModelArts"""

from model_utils.config import config

if config.enable_modelarts:
    from model_utils.moxing_adapter import get_device_id, get_device_num, get_rank_id, get_job_id
else:
    from model_utils.local_adapter import get_device_id, get_device_num, get_rank_id, get_job_id

__all__ = ["get_device_id", "get_device_num", "get_rank_id", "get_job_id"]
