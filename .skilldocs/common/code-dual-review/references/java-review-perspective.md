# Java Code Review Perspective

This checklist defines review points for Java modules and Java-based applications.

## Existing Code Consistency

- Preserve consistency with local code structure and patterns.
- Follow existing naming conventions.
- Keep changes aligned with nearby implementation style.

## Maintainability

- Confirm that variable and method names explain their role clearly.
- Prefer comments that explain intent, constraints, or background.
- Check whether each function has one clear responsibility.
- Avoid tight dependence on another module's internal implementation.
- Avoid unnecessary abstraction, patterns, or indirection.
- Flag nested conditions, long functions, and hard-to-follow control flow.

## Object-Oriented Design

- Check single-responsibility boundaries.
- Prefer asking objects to perform behavior over exposing state for outside handling.
- Prefer intention-revealing methods over generic setters when behavior matters.
- Avoid using inheritance only for code reuse.
- Keep coupling low through interfaces or clear dependency boundaries.

## Layering

- Confirm dependency direction follows the intended architecture.
- Flag lower layers depending on higher-level policy layers.
- Flag circular dependencies.
- Prefer interface-based coupling where it improves testability or boundary clarity.

## Modernization And Structure

- Consider safe Java language features supported by the project runtime.
- Simplify complex logic with standard refactoring patterns when the benefit is clear.
- Keep modernization consistent with local conventions.

## Performance

- Flag unnecessary object creation in hot paths.
- Check whether algorithmic complexity fits expected data size.
- Consider memory use for large projects or large input sets.

## Testing

- Check whether new functions and classes are testable.
- Identify test updates needed for changed logic.
- Confirm tests verify requirements and regression risk directly.

## Database Access

- Check transaction boundaries for bulk operations.
- Flag repeated queries and N+1 access patterns.
- Consider index needs for frequently queried columns.
- Check migration and backward-compatibility risks for persisted data.

## Generated Code Quality

- Check readability and debuggability of generated code.
- Confirm generated output is stable and parseable by downstream tooling.
- Check ordering, section boundaries, include/import handling, and fixture linkage when relevant.

## Error Handling And Logging

- Confirm user-facing errors are actionable.
- Confirm diagnostic logs help debugging.
- Check that resources are cleaned up on exceptional paths.
