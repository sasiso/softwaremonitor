"""
Copyright [2016] [Satbir Singh]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

class AnEvent(object):
    def __init__(self, dt=0, shape=0, tooltip="NotSet"):
        self._shape = shape
        self._tooltip = tooltip
        self.date_time = dt

    def on_double_click(self):
        pass

    def on_click(self):
        pass
