# CLI Agent Spawn

## Purpose

Define reusable PowerShell commands for running Codex CLI and Claude Code CLI helper agents.

## Inputs

- Working directory
- Prompt file
- Agent: `codex` or `claude-code`
- Model
- Optional log file

## Codex CLI

Run from the target working directory and pass the prompt file through stdin.

```powershell
Set-Location -LiteralPath '<worktree>'
Get-Content -LiteralPath '<prompt-file>' -Raw | codex exec --model '<model>' -
```

## Claude Code CLI

Run from the target working directory and pass the prompt file in print mode.

```powershell
Set-Location -LiteralPath '<worktree>'
Get-Content -LiteralPath '<prompt-file>' -Raw | claude --model '<model>' -p
```

## Claude Code Regression Subject Run

When running a subject agent in an isolated experimental worktree, make the permission mode explicit.

```powershell
Set-Location -LiteralPath '<worktree>'
Get-Content -LiteralPath '<prompt-file>' -Raw | claude --safe-mode --disable-slash-commands --model '<model>' --permission-mode bypassPermissions -p
```

Subject-agent output records one final status line.

- `RESULT: implemented`
- `RESULT: failed - <reason>`

## Parallel Regression Runs

Run each experiment group in a separate worktree. Use the same subject agent and model, with separate prompt and log files per group.

When the orchestrator supports parallel execution, start both subject calls concurrently. When running directly in PowerShell, start both jobs first, then wait for both to finish.

```powershell
$firstJob = Start-Job -ScriptBlock {
  param($Worktree, $PromptFile, $Model, $LogFile)
  Set-Location -LiteralPath $Worktree
  $started = Get-Date
  $sw = [System.Diagnostics.Stopwatch]::StartNew()
  $output = Get-Content -LiteralPath $PromptFile -Raw |
    claude --safe-mode --disable-slash-commands --model $Model --permission-mode bypassPermissions -p 2>&1
  $exitCode = $LASTEXITCODE
  $sw.Stop()
  $output | Set-Content -LiteralPath $LogFile -Encoding UTF8
  [ordered]@{
    name = 'experiment-a'
    exitCode = $exitCode
    elapsedMs = $sw.ElapsedMilliseconds
    startedAt = $started.ToString('o')
    endedAt = (Get-Date).ToString('o')
    logFile = $LogFile
  }
} -ArgumentList '<worktree-a>', '<prompt-a>', '<model>', '<experiment-a.log>'

$secondJob = Start-Job -ScriptBlock {
  param($Worktree, $PromptFile, $Model, $LogFile)
  Set-Location -LiteralPath $Worktree
  $started = Get-Date
  $sw = [System.Diagnostics.Stopwatch]::StartNew()
  $output = Get-Content -LiteralPath $PromptFile -Raw |
    claude --safe-mode --disable-slash-commands --model $Model --permission-mode bypassPermissions -p 2>&1
  $exitCode = $LASTEXITCODE
  $sw.Stop()
  $output | Set-Content -LiteralPath $LogFile -Encoding UTF8
  [ordered]@{
    name = 'experiment-b'
    exitCode = $exitCode
    elapsedMs = $sw.ElapsedMilliseconds
    startedAt = $started.ToString('o')
    endedAt = (Get-Date).ToString('o')
    logFile = $LogFile
  }
} -ArgumentList '<worktree-b>', '<prompt-b>', '<model>', '<experiment-b.log>'

Wait-Job -Job $firstJob, $secondJob
$firstResult = Receive-Job -Job $firstJob
$secondResult = Receive-Job -Job $secondJob
Remove-Job -Job $firstJob, $secondJob
```

Collect exit code, elapsed time, final log line, `git status --short`, and `git diff` for each run after both jobs finish.

## Helper Agent Selection

Helper-agent calls use an agent different from the current orchestrator.

- Current orchestrator is Codex: call Claude Code.
- Current orchestrator is Claude Code: call Codex.
- For reviews, writing reviews, and validation calls, pass an orchestrator-built prompt file to the selected agent using the regular CLI command.

## Operating Rules

- Use native PowerShell commands on Windows.
- When a target is known, start with `Set-Location -LiteralPath '<worktree>'`.
- Store prompts in files and pass them with `Get-Content -Raw`.
- Do not ask helper agents to edit files, create commits, change branches, or run tests unless the task explicitly defines a subject-agent regression run.
- If a helper-agent command fails, record the failure cause and change the next attempt only when it changes the failure condition.
- Regression subject agents may edit files in isolated worktrees.
- Regression subject agents do not create commits, change branches, or run tests unless the experiment explicitly requires it.
