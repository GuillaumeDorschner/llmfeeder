Name:           llmf
Version:        0.0.0
Release:        1%{?dist}
Summary:        CLI tool to feed your LLM the necessary context to get help

License:        MIT
URL:            https://github.com/GuillaumeDorschner/llmfeeder
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       bash, tree, xclip

%description
`llmf` is a CLI tool designed to extract relevant context from a directory and format it for easy input into a Large Language Model (LLM).

%prep
%setup -q

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 755 src/llmf %{buildroot}/usr/local/bin/llmf

mkdir -p %{buildroot}/usr/share/man/man1
install -m 644 usr/share/man/man1/llmf.1 %{buildroot}/usr/share/man/man1/llmf.1

%files
/usr/local/bin/llmf
/usr/share/man/man1/llmf.1.gz

%changelog
* Tue Mar 18 2025 Guillaume Dorschner <guillaume.dorschner@icloud.com> - 0.1.0-1
- Initial RPM release
