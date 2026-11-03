# Prompting guidelines and agent management playbook (November 2026)

This repository contains reference guidelines for prompting and managing autonomous agents across general domains (finance, legal, research, operations, and analysis) using late-2026 frontier models: OpenAI GPT-6 (Astra and Sol), Anthropic Claude 5.5 (Opus 5.5 and Sonnet 5.5), and Google Gemini 4 (Carbon, Argon, and Gemini 3.8 Flash).

---

## 1. General prompt framework: the 6-part structure

To direct frontier models across any knowledge domain, partition prompts into six explicit components:

1. **Objective:** State the single primary deliverable and business goal.
2. **Context:** Provide background facts, company standards, target audience, and operating constraints.
3. **Constraints and negative rules:** Define what the model must never do (e.g. "Do not extrapolate missing metrics; mark unconfirmed points as `[UNVERIFIED]`").
4. **Tools and authority limits:** List callable tools and declare what actions require human sign-off.
5. **Evidence and state:** Provide source files, transcripts, or database feeds to ground answers.
6. **Output format:** Define the exact table, JSON schema, or document layout.

---


## 2. Playbook for creating and managing agents

### 1. Enforce single-responsibility agent roles
Do not build a single monolithic assistant to handle complex projects. Split work across specialized sub-agents:
- **Planner / Orchestrator:** Breaks objectives into steps, delegates work, and monitors progress.
- **Worker / Researcher:** Reads source files, executes queries, and extracts facts.
- **Auditor / Critic:** Verifies draft findings against raw source documents before delivery.

### 2. Set explicit autonomy contracts
Agents fail when they pause for trivial confirmations or take destructive actions without approval. Define two clear operational zones:
- **Autonomous zone:** Document search, mathematical calculations, summarization, draft generation, and automated retries on API errors.
- **Human approval gate:** Financial transactions, outbound emails to external clients, record deletions, and permission changes.

Explicit prompt directive: "Execute all research and drafting autonomously. Stop and request approval only before sending outbound messages or modifying persistent database records."

### 3. Maintain persistent task ledgers
Require the agent to output an updated markdown checklist at the beginning of each turn:
- Items completed
- Active task in progress
- Remaining pending items

This prevents context drift over long multi-turn interactions.

### 4. Protect context hygiene
- **Prune tool returns:** Do not retain multi-page raw data payloads in the main context. Have the agent extract key figures and drop raw outputs.
- **Isolate noisy operations:** Delegate web browsing, database scans, and raw log parsing to sub-agents, returning only synthesized findings to the orchestrator.

### 5. Require evidence ledgers and verification loops
- **Mandatory citations:** Require the agent to cite document titles, page numbers, or database record IDs for every factual claim.
- **Auditor pass:** Run an independent evaluation pass with an auditor agent to verify that all statements match primary source records.

### 6. Tiered model routing
- **High-throughput tasks (Gemini 3.8 Flash, GPT-6.1 Sol):** Document indexing, entity extraction, data classification, and routine transformations.
- **High-stakes reasoning (GPT-6 Astra, Claude Opus 5.5, Gemini 4 Carbon):** Complex multi-document synthesis, strategic audits, policy compliance, and final deliverable review.

---

## 3. Slidev presentation

A presentation is available in [slides.md](file:///home/cc/Dev/IdeaProjects/UConn/AIClub/demos/prompting/slides.md).

To run the presentation locally:
```bash
# Start local Slidev presentation server
npx @slidev/cli slides.md
```
Or via npm:
```bash
npm install
npm run dev
```
