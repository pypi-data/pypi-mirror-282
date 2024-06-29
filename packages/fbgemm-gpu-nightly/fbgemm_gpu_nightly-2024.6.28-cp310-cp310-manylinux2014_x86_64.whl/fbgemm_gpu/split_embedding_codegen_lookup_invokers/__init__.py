#!/usr/bin/env python3

# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

# All optimizers
import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_args as lookup_args  # noqa: F401
import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_adagrad as lookup_adagrad  # noqa: F401
import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_adam as lookup_adam  # noqa: F401
import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_lamb as lookup_lamb  # noqa: F401
import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_lars_sgd as lookup_lars_sgd  # noqa: F401
import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_partial_rowwise_adam as lookup_partial_rowwise_adam  # noqa: F401
import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_partial_rowwise_lamb as lookup_partial_rowwise_lamb  # noqa: F401
import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_rowwise_adagrad as lookup_rowwise_adagrad  # noqa: F401
import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_rowwise_adagrad_with_counter as lookup_rowwise_adagrad_with_counter  # noqa: F401
import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_sgd as lookup_sgd  # noqa: F401
import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_none as lookup_none  # noqa: F401

# SSD optimizers (putting them under try-except for BC as they are
# experimental ops which can be removed/updated in the future)
try:
    import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_args_ssd as lookup_args_ssd
    import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_rowwise_adagrad_ssd as lookup_rowwise_adagrad_ssd
except:
    import logging
    logging.warn("fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_args_ssd import failed")