#!/usr/bin/env bash

set -e

conda build .
out_file="$(conda build . --output)"
tar_file="$(basename "$out_file")"
arch_path="$(dirname "$out_file")"
arch_file="$(basename "$arch_path")"
base_path="$(dirname "$arch_path")"
rsync -aRP "$base_path/./$arch_file/$tar_file" "$CONDA_SSH_ALIAS:conda/"
ssh "$CONDA_SSH_ALIAS" "$INDEX_CMD"
