# -*- coding:utf-8 -*-

# Copyright (C) 2020. Huawei Technologies Co., Ltd. All rights reserved.
# This program is free software; you can redistribute it and/or modify
# it under the terms of the MIT License.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# MIT License for more details.

"""Defined Configs."""


class BohbPolicyConfig(object):
    """Bohb Policy Config."""

    total_epochs = 81
    epochs_per_iter = 81
    num_samples = 40
    config_count = 1
    repeat_times = 1


class BohbConfig(object):
    """Bobh Config."""

    policy = BohbPolicyConfig
    objective_keys = 'accuracy'
