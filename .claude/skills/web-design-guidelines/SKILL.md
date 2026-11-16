---
name: web-design-guidelines
description: Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practices".
metadata:
  author: vercel
  version: "1.0.0"
  argument-hint: <file-or-pattern>
---

# Web Interface Guidelines

Review files for compliance with Web Interface Guidelines.

## How It Works

1. Read the guidelines from `guidelines.md` in this skill's folder (local pinned copy)
2. Read the specified files (or prompt user for files/pattern)
3. Check against all rules in the fetched guidelines
4. Output findings in the terse `file:line` format

## Guidelines Source

Local pinned copy: `guidelines.md` (next to this SKILL.md), taken from
https://github.com/vercel-labs/web-interface-guidelines (`command.md`, MIT) on 2026-11-02.
Do not fetch the rules from the network: use the local copy, so the rules cannot change unreviewed.
To update them, a person downloads the new `command.md`, reviews it and replaces `guidelines.md`.

## Usage

When a user provides a file or pattern argument:
1. Read `guidelines.md` from this skill's folder
2. Read the specified files
3. Apply all rules from the fetched guidelines
4. Output findings using the format specified in the guidelines

If no files specified, ask the user which files to review.
