---
name: script-video-cinema-navigation
description: Navigate and document an authenticated AI cinema workspace safely. Use when inspecting provider pages, creating reusable elements, staging shots, or updating a page-by-page runbook.
---

# Script Video Cinema Navigation

Operate authenticated cinema interfaces as evolving software. Visible state and current provider schemas override remembered navigation.

## Before interaction

1. Read the project navigation runbook, if present.
2. Read the approved shot or element packet.
3. Take a screenshot or accessibility snapshot before clicking.
4. Identify the exact project, page, modal, model, resolution, duration, audio state, and cost display.

## Navigation method

1. Snapshot.
2. Identify the visible control and current state.
3. Make one reversible interaction.
4. Snapshot the result.
5. Record the discovered path, labels, defaults, limits, autosave behavior, and failure state.

Use a project file such as `project/provider-navigation-runbook.md`. Store facts once at the most specific reusable level; link to them elsewhere.

## Paid boundary

Opening pages, inspecting schemas, uploading approved assets, and staging a prompt are reversible setup. A button that creates a paid job, trains a model, publishes, shares, or deletes requires explicit scope and the relevant approval gate.

Immediately before paid generation, verify model, duration, resolution, references, sound, prompt, live quote, and attempt ID. Then hand control to `$script-video-generate`.

## Learning policy

Record only observed facts. Mark uncertain behavior as a hypothesis with reproduction steps. Promote stable cross-project facts through `$script-video-learn`; keep project-specific IDs and creative decisions in the project.
