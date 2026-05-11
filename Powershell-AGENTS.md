# AI가 파워쉘 사용 시 유용한 스킬. AGENTS.md에 넣는 것 추천. 이 문장은 지우고 사용하세요.
# PowerShell Failure Reduction Rules

Purpose: reduce first-attempt command failures in Windows + PowerShell environments and minimize wasted retries.

## Working Rules

1. Use native PowerShell syntax from the first attempt for read and discovery tasks.
2. Prefer `LiteralPath` or explicit absolute paths, especially for paths with spaces, non-ASCII characters, or drive letters.
3. Prefer proven read-only command patterns for simple inspection work.
4. Avoid unnecessary shell chaining. Use `PowerShell -> cmd -> python` only when it is actually required.
5. For quoting-sensitive tasks, use shorter commands and minimize argument complexity.
6. Reduce speculative first attempts that are likely to fail.
7. Do not repeat trial runs when sandbox or permission failure is likely.
8. Keep a fixed priority order for file reading and search operations.

## Preferred Patterns

- File listing: `Get-ChildItem`
- Text search: `rg`
- File content: `Get-Content`
- Single item lookup: `Get-Item`
- Path composition: `Join-Path`

## Avoid Patterns

- Applying Unix shell assumptions directly in PowerShell
- Long commands that depend on fragile relative paths or quoting
- Inserting `cmd /c` without a clear need
- Repeating the same failing command pattern with only cosmetic changes

## Execution Heuristics

- Check first: shell syntax, path resolution, quoting, sandbox constraints
- Escalate early: writes or executions that are likely to be blocked by sandbox or permissions
- Parallelize: independent read and discovery commands

## Response Rules

- When PowerShell-related failure is likely, choose the highest-probability command form first.
- After a first failure, do not keep retrying the same class of command. Switch to a form that changes the failure conditions.
