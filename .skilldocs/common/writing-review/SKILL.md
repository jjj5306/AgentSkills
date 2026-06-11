# Writing Review

## Core Rule

Review the writing; do not rewrite it. Do not provide replacement paragraphs, before/after examples, or polished final copy unless the user explicitly asks for rewriting.

## Workflow

1. Identify the document type, likely reader, and intended outcome when visible.
2. Review the text across consistency, readability, concision, accuracy, clarity, duplication, structure, emphasis, tone, reader fit, and actionability.
3. Separate confirmed writing issues from facts that need source or freshness verification.
4. Prioritize high-impact findings over exhaustive commentary.
5. Point to the affected section, paragraph, heading, or short phrase. Keep quoted snippets short.
6. Explain why each issue matters to the reader or document goal.
7. Respond in the user's language by default.

When reviewing skills, AGENTS.md files, or workflow instructions, also check whether triggers are clear, scope boundaries are explicit, output contracts are usable, validation steps are executable, and instruction conflicts or duplication could confuse a future agent.

For long, high-stakes, or ambiguous documents, read `.skilldocs\common\writing-review\references\review-checklist.md` before reviewing.

## Subagent Review

Use a subagent when the review target is a skill, AGENTS.md instruction, workflow guide, PR description, ADR, plan, or other document where an independent second pass can catch ambiguity or instruction conflicts.

- Use the CLI Agent Spawn skill for CLI subagent commands.
- Choose the helper agent by current orchestrator: Codex calls Claude Code, and Claude Code calls Codex.
- Build a review packet containing the target text, document purpose, intended reader, and these writing-review criteria.
- Ask the subagent for diagnostic findings only. Do not ask it to rewrite the document.
- Merge the subagent findings with the orchestrator's own review.
- Distinguish confirmed issues from subagent-only concerns that need user judgment.
- If the subagent cannot be started, record the reason and continue with orchestrator-only writing review.

## Output Shape

Use this order unless the user asks for another format:

1. **Overall assessment**: one short paragraph on the document's current quality and main risk.
2. **Key review points**: grouped findings by review dimension. Include only dimensions with meaningful observations.
3. **Priority fixes**: the top 1-3 areas to fix first.
4. **Needs verification**: claims that need fact, source, date, or scope verification.

## Review Dimensions

- **Consistency**: flag conflicting claims, inconsistent scope, mismatched terminology, or conclusions not supported by preceding text.
- **Readability**: flag hard-to-scan structure, overloaded paragraphs, unclear heading hierarchy, or sentence complexity that slows comprehension.
- **Concision**: flag repeated background, redundant qualifiers, over-explained obvious points, or detail that distracts from the main message.
- **Accuracy**: flag incorrect, outdated, overconfident, or unverifiable claims. Mark uncertain claims as verification-needed.
- **Clarity**: flag vague referents, hidden assumptions, unclear actors, missing conditions, or ambiguous next steps.
- **Duplication and structure**: flag repeated sections, scattered related ideas, poor ordering, or conclusions buried too late.
- **Emphasis**: flag important decisions, risks, asks, or constraints that should be more visible.
- **Reader and purpose fit**: flag tone, depth, terminology, or evidence level that does not fit the intended reader and purpose.
- **Actionability**: flag missing owners, decisions, requested actions, acceptance criteria, or follow-up boundaries when the document is meant to drive work.
- **Skill and workflow quality**: for skill files and operational instructions, flag unclear trigger conditions, hidden prerequisites, brittle validation commands, ambiguous stop rules, or duplicated guidance that makes agent execution less reliable.

## Constraints

- Keep the review concise. Do not make the review longer than the source unless the source is very short.
- Prefer concrete, localizable findings over broad style advice.
- Do not invent facts. If external verification is required and not requested, say what needs verification.
- Do not soften real issues into vague suggestions. State the issue directly and briefly.
- Do not comment on every minor grammar or punctuation issue unless the user asks for copyediting.
