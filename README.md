# building an ai agents

### 2 October 2026

> building my own ai agents

this is a small coding agent that i'm building while learning how agentic
systems work. it uses an OpenRouter model to decide which tools to call, then
feeds the result back into the conversation until the model has a final answer.

## explore

- [building an ai agents](#building-an-ai-agents)
  - [what it does](#what-it-does)
  - [setup](#setup)
  - [usage](#usage)
  - [tools](#tools)
  - [stack](#stack)
  - [find me](#find-me)

## what it does

the agent currently has a working directory at `calculator/` and can:

- list files and directories
- read file contents
- execute Python files with optional arguments
- write or overwrite files

the model can call several tools in sequence. for example, it can inspect the
calculator source, change a file, run the tests, and then explain what it did.

## setup

this project uses Python 3.13+ and `uv`.

```bash
uv sync
```

create a `.env` file with an OpenRouter API key:

```env
OPENROUTER_API_KEY=your-key-here
```

## usage

run the agent with a prompt:

```bash
uv run main.py "how does the calculator render results to the console?"
```

use `--verbose` to print token usage, tool arguments, and tool results:

```bash
uv run main.py "run tests.py" --verbose
```

the calculator can also be run directly:

```bash
uv run calculator/main.py "3 + 7 * 2"
```

run the calculator tests with:

```bash
uv run calculator/tests.py
```

## tools

the tool implementations live in `functions/`:

| function | what it does |
| --- | --- |
| `get_files_info` | lists files in a directory |
| `get_file_content` | reads a file, with a 10,000 character limit |
| `run_python_file` | runs a Python file with optional arguments |
| `write_file` | creates or overwrites a file |

the working directory is injected by the agent so the model only supplies
relative paths.

## stack

python + openrouter + openai sdk + uv

## find me

i'm active in boot.dev, you should check me out.

[portfolio website](https://tgr-wjya.up.railway.app/) · [email](mailto:tgrwjya6371+contact@gmail.com) · [linkedin](https://www.linkedin.com/in/tgr-wjya/) · [boot.dev](https://www.boot.dev/u/handmadeinvite39)

---

made with ◉‿◉
