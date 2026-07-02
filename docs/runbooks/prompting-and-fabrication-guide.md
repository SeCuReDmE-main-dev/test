# Prompting And Fabrication Guide

## How To Prompt Codex

Start with the exact workspace, the target plugin, the live mode, and the expected evidence. Ask Codex to mark every claim as confirmed, inferred, or blocked.

## How To Prompt Gemini Or Colab

Open the notebook, copy the strict prompt cell, and paste it into the AI environment. Keep the path and redaction rules visible so the assistant does not drift.

## How To Read Evidence

A result is useful only when it states where the evidence came from, what it proves, and what it does not prove yet.

## How To Avoid Secret Leaks

Never paste `.env` values, tokens, passwords, private keys, cookies, cPanel session URLs, mailbox passwords, or raw private exports. Use status fields and redacted summaries.

## How To Fork A Prompt

Change only the target surface, expected evidence, and final deliverable. Keep the absolute CWD, anti-drift rule, evidence standard, and redaction rule.

## How To Make Your Own Test

Pick one capability, define one target, choose one live mode, and write one pass criterion. If you cannot write the pass criterion, the test is not ready.

## How To Graduate From User To Builder

After you can run tests, combine them into a small workflow: read current state, generate a dry-run plan, capture evidence, publish a redacted notebook, then add a command for reuse.

## Glossary

- Plugin: a Codex capability bundle with skills, commands, and possibly MCP tools.
- RAG: retrieval-augmented context used to preserve evidence and reuse prior knowledge.
- Dry-run: a mutation-shaped plan with execution disabled.
- Live-read: a current state read without mutation.
- Gated-write: a bounded write that is explicitly authorized by a plan and validated afterward.
