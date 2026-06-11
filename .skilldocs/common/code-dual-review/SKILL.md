# Local Code Review

## Purpose

Perform quality review for work in progress or pre-PR changes.

## Suitable Timing

- Early design direction checks
- Mid-implementation checks
- Final self-review before PR creation

## Output

- Primary perspective: current orchestrator agent
- Secondary perspective: helper agent selected through CLI Agent Spawn
- Output artifact: review report
- Out of scope: PR creation, commits, branch changes, file edits

## Review Perspective Document

Always review against the generic Java review perspective document.

- Repository-relative path: `.skilldocs\common\code-dual-review\references\java-review-perspective.md`

If the document cannot be read, report the missing document before reviewing.

## Review Principles

- Review against the loaded review perspective.
- Check consistency with existing code, maintainability, object-oriented design, layering, performance, testability, database access, generated-code quality, error handling, and logging.
- Prioritize real maintenance risks, structural issues, and decisions that need human judgment.
- Leave uncertain domain judgments as questions.

## Review Process

1. Load `.skilldocs\common\code-dual-review\references\java-review-perspective.md`.
2. Inspect changes.
   - `git status --short`
   - `git diff --stat`
   - `git diff` when needed
3. Perform the primary review as the current orchestrator.
4. When a dual review is required, collect the secondary perspective from the helper agent.
5. Separate shared findings, single-perspective findings, and open questions.

## Helper-Agent Review

Use the helper-agent selection rules and CLI commands from CLI Agent Spawn.

- Current orchestrator is Codex: call Claude Code.
- Current orchestrator is Claude Code: call Codex.
- The current orchestrator builds the review packet from `git diff`, relevant files, and the review perspective document.
- Include all required diff and context in the prompt. Do not ask the helper agent to independently explore the codebase.
- Use the helper agent only to collect review observations.
- Do not ask the helper agent to edit files, create commits, change branches, or run tests.
- If the helper agent fails, record the cause and continue with an orchestrator-only review or ask the user whether to retry.

## Single-Reviewer Report Format

```markdown
# Code Review Result

## Findings

### Critical
- **File**: `path/to/file.java:123`
- **Issue**: ...
- **Impact**: ...
- **Recommendation**: ...

### High
- **File**: `path/to/file.java:456`
- **Issue**: ...
- **Impact**: ...
- **Recommendation**: ...

## Questions

## Test Recommendations
```

## Dual-Reviewer Report Format

```markdown
# Dual Code Review Result

## Discussion Items

### [Category] Item title
**File**: `path/to/file:123`

**Orchestrator view**:
- ...

**Helper-agent view**:
- ...

**Decision point**:
- ...

## Confirmed Issues

### [Category] Issue title
**File**: `path/to/file:456`
**Severity**: Critical | High

**Issue**:
- ...

**Impact**:
- ...

**Fix**:
- ...
```
