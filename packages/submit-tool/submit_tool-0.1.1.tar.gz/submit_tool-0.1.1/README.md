# A simple CLI tool to faciliate config-based jobs

## Background

When submitting a job that requires queueing (for example, in SLURM), the configure files used in the commands are not used at the moment the job was submitted. Changing the configuration files right after the submission may cause unexpected consequences when the job is really launched (read the wrong configuration files).

The simple tool provided by this extension is to copy detected scripts and configurations in a temporary directories and to redirect the arguments to those in the temporary directories (by default is `~/.submit-tool/<random_str>/`).

## Installation

```bash
pip install submit-tool
```

## Usage

```
submit-tool <original command>
```

## Supported extensions

- `sh`
- `json`
- `yaml`
- `yml`
- `toml`
- `ini`