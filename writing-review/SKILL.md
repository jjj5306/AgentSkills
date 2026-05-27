---
name: writing-review
description: Diagnostic-only writing review for drafts, documents, reports, ADRs, plans, PR descriptions, meeting notes, skill files, AGENTS.md instructions, workflow guides, and internal or user-facing prose. Use when Codex needs to review text for consistency, readability, concision, factual accuracy, precision, duplicated content, structure, emphasis, tone, reader fit, actionability, trigger clarity, or instruction quality without rewriting the text unless explicitly requested.
---

# Writing Review

## Core Rule

Review the writing; do not rewrite it. Do not provide replacement paragraphs, "before/after" examples, or polished final copy unless the user explicitly asks for rewriting.

## Workflow

1. Identify the document type, likely reader, and intended outcome when visible.
2. Review the text across consistency, readability, concision, accuracy, clarity, duplication, structure, emphasis, tone, reader fit, and actionability.
3. Separate confirmed writing issues from facts that need source or freshness verification.
4. Prioritize high-impact findings over exhaustive commentary.
5. Point to the affected section, paragraph, heading, or short phrase. Keep quoted snippets short.
6. Explain why each issue matters to the reader or document goal.
7. Respond in Korean by default when the user writes in Korean.

When reviewing skills, AGENTS.md files, or workflow instructions, also check whether triggers are clear, scope boundaries are explicit, output contracts are usable, validation steps are executable, and instruction conflicts or duplication could confuse a future agent.

For long, high-stakes, or ambiguous documents, read `references/review-checklist.md` before reviewing.

## Output Shape

Use this order unless the user asks for another format:

1. **총평**: one short paragraph on the document's current quality and main risk.
2. **주요 리뷰 포인트**: grouped findings by review dimension. Include only dimensions with meaningful observations.
3. **우선 수정 대상**: the top 1-3 areas to fix first.
4. **확인 필요**: claims that need fact, source, date, or scope verification.

## Review Dimensions

- **정합성**: flag conflicting claims, inconsistent scope, mismatched terminology, or conclusions not supported by preceding text.
- **가독성**: flag hard-to-scan structure, overloaded paragraphs, unclear heading hierarchy, or sentence complexity that slows comprehension.
- **간결성**: flag repeated background, redundant qualifiers, over-explained obvious points, or detail that distracts from the main message.
- **정확성**: flag incorrect, outdated, overconfident, or unverifiable claims. Mark uncertain claims as verification-needed instead of guessing.
- **명확성**: flag vague referents, hidden assumptions, unclear actors, missing conditions, or ambiguous next steps.
- **중복/구조**: flag repeated sections, scattered related ideas, poor ordering, or conclusions buried too late.
- **강조점**: flag important decisions, risks, asks, or constraints that should be more visible.
- **독자/목적 적합성**: flag tone, depth, terminology, or evidence level that does not fit the intended reader and purpose.
- **행동 가능성**: flag missing owners, decisions, requested actions, acceptance criteria, or follow-up boundaries when the document is meant to drive work.
- **스킬/절차 품질**: for skill files and operational instructions, flag unclear trigger conditions, hidden prerequisites, brittle validation commands, ambiguous stop rules, or duplicated guidance that makes agent execution less reliable.

## Constraints

- Keep the review concise. Do not make the review longer than the source unless the source is very short.
- Prefer concrete, localizable findings over broad style advice.
- Do not invent facts. If external verification is required and not requested, say what needs verification.
- Do not soften real issues into vague suggestions. State the issue directly and briefly.
- Do not comment on every minor grammar or punctuation issue unless the user asks for copyediting.
