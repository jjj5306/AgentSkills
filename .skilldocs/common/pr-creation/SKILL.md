# PR Creation

## Purpose

Create a PR description from current branch changes and create the PR when the user requests it and a suitable PR creation tool is available.

Pre-PR review is delegated to `$code-dual-review`. This skill handles PR creation flow, PR description composition, reviewer handling, and final reporting.

## Outputs

- PR title
- PR description
- Dual-review result formatted for the PR body
- PR URL when a PR is created successfully

## Input Contract

This skill runs after both review participants are known.

- Primary reviewer: current agent executing the skill
- Counterpart reviewer: model or agent explicitly named by the user

If the user does not specify a counterpart reviewer, ask once which counterpart review model to use.

Model specification examples:

- `Create a PR with current Codex and Claude Sonnet review.`
- `Generate a PR body using GPT-5 and gemini-2.5-pro as reviewers.`
- `Counterpart reviewer is <model>.`

## Required Template

Review reports and PR description review sections must follow this template:

- `.skilldocs\common\pr-creation\references\pr-review-template.md`

Keep the section names and order. Fill empty sections with `None`.

## Required Delegation

Delegate the pre-PR review to `$code-dual-review`.

- Pass the primary reviewer as the current agent.
- Pass the counterpart reviewer from the user request.
- Pass current branch, target branch, diff range, and requested reviewers when available.
- Extract discussion items, confirmed issues, and test/validation notes from the `$code-dual-review` result.
- Format extracted content with the required template.
- Do not define a separate independent reviewer workflow in this skill.

## Procedure

1. Confirm inputs.
   - Primary reviewer is the current agent.
   - Counterpart reviewer is present in the user request.
   - If counterpart reviewer is missing, ask which counterpart review model to use and continue after the answer.
2. Inspect changes.
   - `git status --short --branch`
   - `git branch --show-current`
   - `git diff <target>...HEAD --stat`
   - `git diff <target>...HEAD`
   - `git log <target>..HEAD --oneline`
   - Use `master` as the target branch when the user does not specify one.
3. Call `$code-dual-review` for current branch changes.
   - State that this is a pre-PR review.
   - State the primary reviewer and counterpart reviewer.
   - Include requested PR reviewers when the user provides them.
   - Include review results in the PR body even when the user asks only for the PR body.
4. Write the PR title and body.
   - Title summarizes the purpose in one line.
   - Body includes a change summary and the required review-result template.
   - Include tests and validation results when available.
5. Create the PR when requested.
   - Prefer an available PR creation tool.
   - Use current branch as source and the confirmed target branch as target.
   - Resolve repository metadata from `git remote -v`.
   - Resolve reviewers to account identifiers when the tool requires it and the data is available.
   - If no PR creation tool is available, output the title and body.

## Completion Report

- When a PR is created, report PR URL, discussion item count, and confirmed issue count.
- When a PR is not created or the user asks only for a body, output the PR title and body.
