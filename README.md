# llmf - LLM Feeder

`llmf` is a CLI tool designed to extract relevant context from a directory and format it for easy input into a Large Language Model (LLM). It collects all file contents (excluding unnecessary files like `node_modules/` and `pnpm-lock.yaml` and more in the future), generates a directory tree, and either outputs the result to a file, clipboard, or standard output.

## 📦 Installation

### Debian / Ubuntu

```sh
echo "deb [trusted=yes] https://guillaumedorschner.github.io/llmfeeder/core/stable/apt/ ./" | sudo tee /etc/apt/sources.list.d/llmf.list
sudo apt update
sudo apt install llmf
```

### RedHat / Fedora

```sh
sudo tee /etc/yum.repos.d/llmf.repo <<EOF
[llmf]
name=LLMFeeder Repository
baseurl=https://yourusername.github.io/llmfeeder/core/stable/rpm/
enabled=1
gpgcheck=0
EOF
sudo dnf install llmf
```

### Examples:

#### 📂 Process a specific directory

```sh
llmf
# or
llmf /path/to/directory
```
