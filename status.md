My personal status and progress log file:

1. running main pipeline failed because of hydra config path issue

```
(udacity2) ➜  build-ml-pipeline-for-short-term-rental-prices git:(main) ✗ mlflow run . -P steps=download
```

Result:

```
Cannot find primary config 'config.yaml'. Check that it's in your config search path.

Config search path:
        provider=hydra, path=pkg://hydra.conf
        provider=schema, path=structured://

Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.
2025/10/30 15:56:40 ERROR mlflow.cli: === Run (ID 'fab38d7c789b4f13854756172049e589') failed ===
```

Retry after adding 'config_path="."' to @hydra.main still fails for python 3.13

```
2025/10/30 16:14:05 INFO mlflow.projects.utils: === Fetching project from https://github.com/udacity/build-ml-pipeline-for-short-term-rental-prices#components/get_data into /var/folders/30/t3b584tj4n1dc08h8b56y40h0000gn/T/tmpc9squ25m ===
2025/10/30 16:14:09 INFO mlflow.utils.conda: === Creating conda environment mlflow-3c4ec3dd4a42f8f07e378fedbce985fdcc5cb477 ===
2 channel Terms of Service accepted
Channels:
 - conda-forge
 - defaults
Platform: osx-64
Collecting package metadata (repodata.json): done
Solving environment: failed

LibMambaUnsatisfiableError: Encountered problems while solving:
  - package pyarrow-15.0.0-py38h906a081_0_cpu requires python >=3.8,<3.9.0a0, but none of the providers can be installed

Could not solve for environment specs
The following packages are incompatible
├─ pyarrow =15.0.0 * is installable with the potential options
│  ├─ pyarrow 15.0.0 would require
│  │  └─ python >=3.8,<3.9.0a0 *, which can be installed;
│  ├─ pyarrow 15.0.0 would require
│  │  └─ python >=3.10,<3.11.0a0 *, which can be installed;
│  ├─ pyarrow 15.0.0 would require
│  │  └─ python >=3.11,<3.12.0a0 *, which can be installed;
│  ├─ pyarrow 15.0.0 would require
│  │  └─ python_abi =3.12 *_cp312, which requires
│  │     └─ python =3.12 *_cpython, which can be installed;
│  └─ pyarrow 15.0.0 would require
│     └─ python >=3.9,<3.10.0a0 *, which can be installed;
└─ python =3.13.0 * is not installable because it conflicts with any installable versions previously reported.

Error executing job with overrides: ["main.steps='download'"]
Traceback (most recent call last):
  File "/Users/thilo/udacity/build-ml-pipeline-for-short-term-rental-prices/main.py", line 41, in go
    _ = mlflow.run(
        f"{config['main']['components_repository']}/get_data",
    ...<8 lines>...
        },
    )
  File "/Users/thilo/miniconda3/envs/mlflow-b551409cb0516b9ea0c2361505ae1892a7453fb8/lib/python3.13/site-packages/mlflow/projects/__init__.py", line 358, in run
    submitted_run_obj = _run(
        uri=uri,
    ...<12 lines>...
        docker_auth=docker_auth,
    )
  File "/Users/thilo/miniconda3/envs/mlflow-b551409cb0516b9ea0c2361505ae1892a7453fb8/lib/python3.13/site-packages/mlflow/projects/__init__.py", line 110, in _run
    submitted_run = backend.run(
        uri,
    ...<5 lines>...
        experiment_id,
    )
  File "/Users/thilo/miniconda3/envs/mlflow-b551409cb0516b9ea0c2361505ae1892a7453fb8/lib/python3.13/site-packages/mlflow/projects/backend/local.py", line 176, in run
    conda_env = get_or_create_conda_env(project.env_config_path)
  File "/Users/thilo/miniconda3/envs/mlflow-b551409cb0516b9ea0c2361505ae1892a7453fb8/lib/python3.13/site-packages/mlflow/utils/conda.py", line 293, in get_or_create_conda_env
    conda_env = _create_conda_env_func(
        conda_env_path,
    ...<3 lines>...
        capture_output,
    )
  File "/Users/thilo/miniconda3/envs/mlflow-b551409cb0516b9ea0c2361505ae1892a7453fb8/lib/python3.13/site-packages/mlflow/utils/conda.py", line 115, in _create_conda_env
    process._exec_cmd(
    ~~~~~~~~~~~~~~~~~^
        [
        ^
    ...<9 lines>...
        capture_output=capture_output,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Users/thilo/miniconda3/envs/mlflow-b551409cb0516b9ea0c2361505ae1892a7453fb8/lib/python3.13/site-packages/mlflow/utils/process.py", line 141, in _exec_cmd
    raise ShellCommandException.from_completed_process(comp_process)
mlflow.utils.process.ShellCommandException: Non-zero exit code: 1
Command: ['/Users/thilo/miniconda3/bin/conda', 'env', 'create', '-n', 'mlflow-3c4ec3dd4a42f8f07e378fedbce985fdcc5cb477', '--file', '/var/folders/30/t3b584tj4n1dc08h8b56y40h0000gn/T/tmpc9squ25m/components/get_data/conda.yml']

Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.
2025/10/30 16:14:38 ERROR mlflow.cli: === Run (ID '0fea85b012b94cb593f39ac12e18ddd2') failed ===
```

2. running remote step component 'get data' failed

Console log:

```
Solving environment: failed

LibMambaUnsatisfiableError: Encountered problems while solving:
  - package pyarrow-15.0.0-py38h906a081_0_cpu requires python >=3.8,<3.9.0a0, but none of the providers can be installed

Could not solve for environment specs
The following packages are incompatible
├─ pyarrow =15.0.0 * is installable with the potential options
│  ├─ pyarrow 15.0.0 would require
│  │  └─ python >=3.8,<3.9.0a0 *, which can be installed;
│  ├─ pyarrow 15.0.0 would require
│  │  └─ python >=3.10,<3.11.0a0 *, which can be installed;
│  ├─ pyarrow 15.0.0 would require
│  │  └─ python >=3.11,<3.12.0a0 *, which can be installed;
│  ├─ pyarrow 15.0.0 would require
│  │  └─ python_abi =3.12 *_cp312, which requires
│  │     └─ python =3.12 *_cpython, which can be installed;
│  └─ pyarrow 15.0.0 would require
│     └─ python >=3.9,<3.10.0a0 *, which can be installed;
└─ python =3.13.0 * is not installable because it conflicts with any installable versions previously reported.
```

See github issue: [Pyarrow version 15 not compatible with Python version 3.13](https://github.com/udacity/build-ml-pipeline-for-short-term-rental-prices/issues/73?reload=1)
