---
theme: seriph
title: Beyond Simple Prompts
info: Modern prompting and agent management for everyday AI users
class: text-center
drawings:
  persist: false
transition: slide-left
---

# Beyond Simple Prompts

### Context engineering and managing AI agents for real work

UConn AI Club

---
layout: default
---

# Where most people start

Common everyday prompts:

```text
"Summarize this document for me."
"Write an email explaining our price increase."
"Can you analyze this quarterly report and tell me what stands out?"
```

<v-clicks>

### What goes wrong:
- **Missing context:** The model guesses who your audience is.
- **Vague criteria:** It summarizes what it finds interesting, not what you need.
- **Hallucinations:** Without strict evidence boundaries, it invents plausible facts.
- **Format roulette:** Sometimes you get bullet points, sometimes an essay.

</v-clicks>

---
layout: default
---

# The model frontier (late 2026)

Models have evolved from simple chatbots into autonomous execution engines.

| Lab | Flagship models | What changed |
| :--- | :--- | :--- |
| **OpenAI** | **GPT-6 Astra**, **GPT-6.1 Sol** | Native computer and tool use. Built-in planning. |
| **Anthropic** | **Claude Opus 5.5**, **Sonnet 5.5** | Continuous native thinking. Strict constraint tracking. |
| **Google** | **Gemini 4 Carbon**, **Gemini 3.8 Flash** | Multi-million token context. Grounded evidence citations. |

<div class="mt-4 text-sm text-gray-500">
Takeaway: You do not need to coax these models with conversational tricks. You need to give them structured inputs and clear constraints.
</div>

---
layout: default
---

# Rule 1: Drop "think step by step"

You might have learned phrases like:
- "Think step by step"
- "Take a deep breath and work through this"
- "Show your reasoning line by line"

<v-clicks>

### Why to stop doing this:
- Modern frontier models feature **native test-time compute** (internal reasoning tokens).
- They plan, explore, and self-correct internally before generating text.
- Writing manual chain-of-thought instructions interferes with their internal search process and degrades results.

**Instead:** Focus entirely on your desired **outcome, constraints, and acceptance criteria**.

</v-clicks>

---
layout: default
---

# The 6-part prompt framework

Stop writing one-sentence queries. Structure your requests with these six blocks:

<div class="grid grid-cols-2 gap-4 text-sm mt-4">
<div>

**1. Objective**  
The exact deliverable in one sentence.

**2. Context**  
Target audience, background facts, company standards.

**3. Constraints**  
Hard negative boundaries (what never to say or do).

</div>
<div>

**4. Tools and limits**  
What resources the model can access or modify.

**5. Evidence**  
Source files, transcripts, or data tables to ground claims.

**6. Output format**  
Tables, JSON schemas, or explicit section layouts.

</div>
</div>

---
layout: two-cols
---

# Before: Basic prompt

```text
Look at these vendor reviews 
and write a summary of the 
biggest risks for our leadership 
team.
```

### Result:
- Generic bullet points.
- Mentions minor complaints alongside critical flaws.
- No citations to original sources.
- Polite filler text at the start and end.

::right::

# After: 6-part prompt

```text
[Objective]
Draft a 3-paragraph executive memo 
identifying top vendor compliance risks.

[Context]
Audience: Chief Risk Officer. Standard: SOC 2.

[Constraints]
Do not extrapolate missing filing dates. 
Mark unconfirmed points as [UNVERIFIED]. 
Cut corporate filler and introductory fluff.

[Evidence]
Use only the attached audit PDFs.

[Output format]
Executive Summary, Findings Table (Vendor, 
Risk Tier, Citation), Action Items.
```

---
layout: default
---

# Do's and Don'ts for daily AI use

| Do | Don't |
| :--- | :--- |
| **Specify negative constraints** ("Do not assume missing data"). | **Beg for formats** ("Please make it nice and short"). |
| **Provide source evidence** and demand specific citations. | **Ask open questions** ("What do you think of this?"). |
| **Use structured formats** (tables, bulleted ledgers). | **Tolerate filler** ("Certainly! Here is your summary"). |
| **Put evidence first, task instructions last** for long texts. | **Bury instructions** in the middle of a document dump. |
| **Set explicit roles and audience** (Audience: CFO). | **Rely on vague roleplay** ("Act like a genius wizard"). |

---
layout: default
---

# Moving from prompts to agents

A prompt produces a single answer. An **agent** performs a multi-step job.

```
Goal: "Review 15 vendor contracts and flag non-compliant indemnification clauses."
```

<v-clicks>

### What an agent does:
1. Inspects the file directory.
2. Reads contract 1, extracts clauses, notes citations.
3. Compares findings against company compliance rules.
4. Repeats for contracts 2 through 15.
5. Flags ambiguities and compiles the final report.

</v-clicks>

---
layout: default
---

# The three agent roles

Do not ask one agent to do everything. Separate responsibilities into three distinct roles:

<div class="grid grid-cols-3 gap-4 mt-6 text-sm">
<div class="p-3 border rounded">

### 1. Orchestrator
- Breaks high-level goals into sub-tasks.
- Assigns work to specialized sub-agents.
- Tracks overall progress.

</div>
<div class="p-3 border rounded">

### 2. Worker
- Queries databases or reads files.
- Extracts facts and performs calculations.
- Has read-only access to prevent accidents.

</div>
<div class="p-3 border rounded">

### 3. Auditor
- Reviews worker output against primary sources.
- Checks for missed constraints and errors.
- Delivers the verified final output.

</div>
</div>

---
layout: default
---

# Managing autonomy: when to pause

Agents fail when they either stop every two seconds or make destructive changes unprompted.

<div class="grid grid-cols-2 gap-6 mt-4">
<div>

### Autonomous zone (No pauses)
- Searching internal files and reading documents.
- Calculating metrics and transforming data.
- Drafting text, tables, and memos.
- Retrying an API call that timed out.

</div>
<div>

### Human gate (Must pause and ask)
- Sending emails or messages to clients.
- Overwriting or deleting existing database records.
- Moving money or executing payments.
- Changing system permissions or credentials.

</div>
</div>

<div class="mt-4 p-2 bg-gray-100 rounded text-xs text-gray-700">
Instruction phrasing: "Execute all research and drafting autonomously. Stop and ask for approval only before sending outbound messages or modifying stored records."
</div>

---
layout: default
---

# Preventing agent memory loss

When agents run multi-step tasks across several turns, they can lose focus.

### Fix 1: The persistent task ledger
Require the agent to begin every turn with a running checklist:
```markdown
- [x] Extracted revenue and expenses from Q1-Q3 files
- [/] Calculating debt service coverage ratios (in progress)
- [ ] Draft risk summary memorandum
```

### Fix 2: Context pruning
Do not keep 50 pages of raw search results in the conversation window. Have the worker agent extract the five needed facts, then drop the raw file from memory.

---
layout: default
---

# Picking the right model for the job

Match model power to task difficulty to save budget and cut wait times.

<div class="grid grid-cols-2 gap-6 mt-6">
<div>

### Workhorse tier (Fast & Cheap)
**Gemini 3.8 Flash / GPT-6.1 Sol**
- Parsing invoices and receipts.
- Extracting names, dates, and amounts.
- Categorizing customer feedback.
- Routine text formatting.

</div>
<div>

### Frontier reasoning tier (Deep)
**GPT-6 Astra / Claude Opus 5.5 / Gemini 4**
- Resolving conflicting legal clauses.
- Complex strategic planning and policy audits.
- Multi-document risk analysis.
- Final executive deliverable sign-off.

</div>
</div>

---
layout: center
class: text-center
---

# Summary checklist for tomorrow

<div class="text-left max-w-xl mx-auto space-y-3 text-sm">

1. **Use the 6 parts:** Objective, Context, Constraints, Tools, Evidence, Format.
2. **Cut the coaching:** Delete "think step by step" and let reasoning models plan.
3. **Set negative constraints:** Tell the model what **not** to do.
4. **Isolate roles:** Let one agent gather facts, and another audit the results.
5. **Define stop gates:** Allow autonomous drafting, but require sign-off for actions.

</div>

<div class="mt-8 text-xs text-gray-400">
UConn AI Club | Demos & Guidelines
</div>
