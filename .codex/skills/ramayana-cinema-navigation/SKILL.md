---
name: ramayana-cinema-navigation
description: Navigate, inspect, automate, and document the Ramayana-ZebpaySIP project in Higgsfield Cinema Studio. Use for any Cinema Studio page, menu, composer, Element, project setting, upload, generation-state, or browser-navigation task, and whenever a newly observed page must be added to the production runbook.
---

# Ramayana Cinema Studio navigation

Read `Ramayana-ZebpaySIP/project/higgsfield-cinema-studio-navigation-runbook.md` before acting. It is the detailed source of truth; do not reconstruct navigation from memory.

## Operating checklist

1. Identify the exact current page and project before clicking.
2. Refresh the accessibility/UI state after every modal, menu, upload, or page transition.
3. Use the authenticated Brave `MythyaVerse` profile only when the user has made it available.
4. Treat Generate, Delete, Share, calls, messages, and membership changes as state-changing boundaries.
5. Obtain immediate approval before any paid Generate action.
6. Capture only the Higgsfield content needed as evidence; exclude unrelated tabs, apps, account identifiers, and secrets.
7. Stop when the requested navigation fact is learned or the approved action is complete.

## Confirmed navigation laws

- Cinema Studio Element CRUD is not exposed by Higgsfield CLI 1.1.19; use the authenticated UI.
- Element Category selection is reliable only after clicking the visible Character, Location, or Prop item and confirming the closed field.
- Element media selections can persist across picker sessions; require exactly `1 selected` before Add to Element.
- Under UI automation, wait briefly after text entry and re-observe before the next action.
- `Turn to video` from an asset detail can route to a generic composer and change the model; use project composer -> Cinema Studio 3.5 -> add/upload picker.
- Duration is a slider; verify the bottom toolbar label.
- After Generate is clicked, the composer and button can remain visible. Confirm a new Processing asset or CLI job ID before any further click.
- Cinema Studio is the project workspace; Cinema Studio 3.5 and Seedance 2.0 are separate engines in its model picker. Verify the active engine label, not only the page title.
- Changing engines can clear the prompt and Elements while retaining an old start frame. Audit and remove stale media after every engine switch.
- In the asset picker, selecting an Element only marks it. Click the bottom `Use` action and then verify its thumbnail and inline `@` tag in the composer.
- For native Windows upload dialogs opened by Higgsfield, `Alt+N` focuses File name; enter the full path and press Enter, then wait for both upload and content-check completion.
- The Seedance 2.0 composer does not expose Cinema Studio 3.5 Genre, Manual Style, or Camera panels. Encode those requirements in the prompt and references.

## Record every new page or state

Update the runbook with:

- starting screen and how it was identified;
- exact action taken;
- confirmed visible result;
- stop condition;
- destructive or credit boundary;
- screenshot or other evidence path;
- reusable learning, clearly separated from inference.

After a meaningful page batch, use `$ramayana-learn`. Update this skill only when the observation changes a reusable navigation law; keep page-by-page detail in the runbook.
