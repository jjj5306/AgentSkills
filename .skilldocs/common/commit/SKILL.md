# Commit Skill

Create a git commit using a structured issue-based commit message convention.

## Workflow

### Step 1: Confirm Issue Identifier

When the user requests a commit, confirm the issue identifier.

- If provided, continue to Step 2.
- If missing, ask once and wait:

```text
Issue identifier?
```

Accepted examples:

- `PROJ-123`
- `ABC-456`
- `NO-ISSUE` when the repository allows commits without issue tracking

### Step 2: Inspect Staged Changes

Run:

```powershell
git diff --staged
git status
```

If no files are staged, report that there is nothing staged to commit.

### Step 3: Write Commit Message

Use this format:

```text
<type>: <issue> <title>

<body>
```

## Type Selection

| Type | Use when |
|------|----------|
| feat | Adding or changing functionality |
| fix | Fixing a bug |
| test | Adding or changing tests |
| refactor | Refactoring code without behavior change |
| style | Formatting or style-only changes |
| docs | Documentation changes |
| chore | Build, tooling, package, or maintenance changes |

## Title Rules

- 50 characters or fewer when practical
- No trailing period
- State what changed clearly

## Body Rules

- Explain what changed and why.
- Omit the body when the title is sufficient.
- Keep body bullets focused on user-visible behavior, maintenance impact, or validation.

## Examples

```text
feat: PROJ-123 split planner prompts by language

- Add language-specific prompt builders
- Improve parser handling for fenced JSON blocks
- Reduce prompt ambiguity for long planning tasks
```

```text
fix: PROJ-456 handle parser fallback failure
```

## Commit Execution

Use a non-interactive commit command.

```powershell
git commit -m @'
<type>: <issue> <title>

<body>
'@
```

## Invocation Examples

```text
Use $commit to commit staged changes.
Use $commit with PROJ-123.
```
