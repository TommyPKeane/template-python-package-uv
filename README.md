# tommy teaches tommy: Template Repository - Custom Python Package

__tommy teaches tommy__ (_and anyone else who cares to read all this_) about how to create and manage your own custom Python Package in a standalone repository with this GitHub Template Repository.

Here, we're using `pyenv`, `direnv`, `uv`, `ruff`, and `pytest` to manage an isolated local development environment with formatting, linting, and unit-testing.

This is just a template repo, so there's going to be minimal code, and if you use this directory you'll want to follow the `REFACTOR_AFTER_CLONING.md` documentation for detailed explanations on what to change and how to use this repository.

Per the `LICENSE` file, this repository is setup with an MIT License for Free and Open-Source usage in personal, academic, or professional settings. This license was mainly chosen because there's really not anything unique here, it's mainly just about setting-up tooling and then lots of README ramblings that most people would probably want to delete anyways. So feel free to use this however you want, and build off of it for any projects you have, either personally or professionally (at your job).

<!-- MarkdownTOC -->

- [Environment Setup and Install](#environment-setup-and-install)
- [Ubuntu 24.04 \(Linux\)](#ubuntu-2404-linux)
- [macOS with `brew`](#macos-with-brew)
- [Windows 11](#windows-11)
- [Developer Setup](#developer-setup)
    - [Updating `ruff` and other `uv` Tools](#updating-ruff-and-other-uv-tools)
    - [Updating Dependencies \(and `uv.lock` File\)](#updating-dependencies-and-uvlock-file)
    - [Recreating the `uv.lock` File](#recreating-the-uvlock-file)
- [Python Package Processes](#python-package-processes)
    - [Run and Debug with Unit-Testing _via_ `pytest`](#run-and-debug-with-unit-testing-via-pytest)
    - [Locally Build the Python Package as a `.whl` \(Wheel\)](#locally-build-the-python-package-as-a-whl-wheel)
- [References](#references)

<!-- /MarkdownTOC -->


<a id="environment-setup-and-install"></a>
## Environment Setup and Install

<a id="ubuntu-2404-linux"></a>
## Ubuntu 24.04 (Linux)

> _TBD..._

<a id="macos-with-brew"></a>
## macOS with `brew`

On macOS (or Linux) if using `brew` (https://brew.sh), you can install `direnv` and `pyenv` with the commands:

```bash
brew install direnv
```

and

```bash
brew install pyenv
```

And if you want a full compilation/install for Python, you'd likely also want to make sure you use `brew` to install these libraries:

- `brew install gcc`
- `brew install openssl`
- `brew install zlib`
- `brew install make`
- `brew install cmake`
- `brew install readline`
- `brew install tcl-tk`
- `brew install ncurses`

And then you can install `uv` and `ruff` (via `uv`) with:

```bash
brew install uv
```

then

```bash
uv tool install ruff
```

and then make sure the tools are in your `PATH` with

```bash
uv tool update-shell
```

and then if you're using `bash` you can make sure your shell is updated in the current terminal session with:

```bash
source ~/.bashrc
```

<a id="windows-11"></a>
## Windows 11

> _TBD..._


<a id="developer-setup"></a>
## Developer Setup

> ***Last Tested with:***
> - `uv 0.8.17 (Homebrew 2025-09-10)`
> - `ruff 0.13.0`


1. Make sure you have the Python Version installed:
    ```bash
    pyenv install
    ```
1. Create the local Project Environment:
    ```bash
    direnv allow
    ```
1. Confirm your Python executable is in the local `.direnv` directory:
    ```bash
    which python
    ```
1. Make sure the latest version of `pip` is installed:
    ```bash
    pip install --upgrade pip
    ```
1. Install the Python dependencies and setup the local Package with `uv` by relying on the already active `direnv` and `pyenv` local virtual environment:
    ```bash
    uv sync --active --frozen
    ```

`uv` recommends to use their built-in `venv` management for Virtual Environments, but with this example we're showing how to rely on `direnv` and `pyenv`, which can be a bit more featureful and stable as `uv` is still in active development.

This also allows you to compare/contrast this setup and the processes with a similar setup using `poetry` also shown in this repository for `poetry` version `v1.8` and `poetry` version `v2.0`, as there are some nuanced differences between all three of these approaches.

<a id="updating-ruff-and-other-uv-tools"></a>
### Updating `ruff` and other `uv` Tools

When you install a "tool" with `ruff`, you won't be managing it directly through `brew`, so the `brew` steps for updates won't work:

1. `brew update`
1. `brew upgrade`

instead, you would use the following to update `ruff`:

```bash
uv tool upgrade ruff
```

or you can update anything you have installed as a tool via `uv` with:

```bash
uv tool upgrade --all
```

<a id="updating-dependencies-and-uvlock-file"></a>
### Updating Dependencies (and `uv.lock` File)

You can run:

```bash
uv sync --active --upgrade
```

<a id="recreating-the-uvlock-file"></a>
### Recreating the `uv.lock` File

If you decide to delete the `uv.lock` file, you'll want to recreate it for other developers (and your future self) to stay aligned, so you should run:

```bash
uv sync --active
```

Then once the `uv.lock` file is created, you and other developers should always use:

```bash
uv sync --active --frozen
```

to make sure you only install from  the `uv.lock` file versions when cloning the repository.

<a id="python-package-processes"></a>
## Python Package Processes

<a id="run-and-debug-with-unit-testing-via-pytest"></a>
### Run and Debug with Unit-Testing _via_ `pytest`

> _TBD..._

<a id="locally-build-the-python-package-as-a-whl-wheel"></a>
### Locally Build the Python Package as a `.whl` (Wheel)

> _TBD..._

<a id="references"></a>
## References

- https://docs.astral.sh/uv/
- https://docs.astral.sh/ruff/
- https://docs.astral.sh/uv/concepts/projects/dependencies/
- https://www.cosmicpython.com/
- https://www.pygame.org/
- https://gameprogrammingpatterns.com/state.html
- https://blog.frost.kiwi/dual-kawase/
