# Automation Routines

The weekly cycle is driven by two Claude routines. Session-scheduled jobs
don't survive the session, so to make these permanent, create scheduled
tasks on claude.ai/code with the prompts below.

## 1. Sunday Night Setup (every Sunday ~8pm)

Scaffolds the week; the student does all graded writing himself.

> Sunday-night setup for the weekly English 11 news-article annotation
> assignment (due Friday). Scaffolding run for a 17-year-old 11th grader
> in Southern California whose main interest is animation (Animation III
> class) — the student writes the summary, annotations, and questions
> himself; do NOT write those for him. Steps: (1) Find topics using the
> Parallel system tools first (Parallel Search MCP if enabled in the
> chat, otherwise the Parallel Task MCP; WebSearch only as fallback).
> Pick 3–5 candidates of current world/local hard news — no celebrity
> fluff or sports — from reputable outlets (AP, NPR, Reuters, LA Times,
> LAist, Hollywood Reporter, Variety, Cartoon Brew, Animation Magazine).
> Required mix: at least one animation/creative-industry story (AI in
> animation/VFX, Animation Guild labor, studio/streaming economics, game
> industry) and the rest chosen for Southern California teen relevance
> (SoCal climate/heat/wildfires, social-media and tech regulation
> affecting teens, courts, science, local news). Skip articles already
> logged. Present candidates as a lettered list (A, B, C, ...) with
> one-line reasons. Flag any candidate that continues a story covered in
> an earlier week ("story arc — follow-up on week of ___"); roughly
> every fourth week, recommend the non-animation candidate as the top
> pick so the semester shows range. (2) List who/what/why/how/should
> question angles per candidate. Also teach 1–2 MLA formatting concepts per week, working
> through docs/mla-lessons.md in order — check off each lesson taught
> and tie it to the week's article when possible. (3) Make a one-page
> Article Pick Sheet PDF (lettered list, MLA mini-lesson box,
> top recommendation + why, URL with print-from-source Ctrl+P
> instructions for the annotated hard copy, question starters,
> checklist — original writing only, never the article's text) and send
> it. (4) Generate a one-card Gamma presentation for the top pick as the
> class-presentation visual and share the edit + export links. (5) Copy
> articles/TEMPLATE.md to articles/YYYY-MM-DD-short-title.md filling in
> only the Part 1 title line (headline - from Source) and URL — the
> template matches the teacher's example; leave all student sections
> blank. (6) Add the week's row to the Notion "Weekly Article Log".
> Also copy articles/PRESENTATION-SCRIPT-TEMPLATE.md's five-beat
> structure into the week's file so the student fills in their script.
> (7) Check last week's Notion row: if Points Earned is empty, include a
> "log last week's points" reminder in the notification. (8) Commit and
> push. (9) Send a phone notification with the lettered candidate list,
> recommendation, MLA mini-lesson, Gamma link, print/annotate reminder,
> and Friday deadline.

## 2. On Article Selection (triggered when the pick is chosen)

> When the week's article is selected from the lettered list, copy
> articles/WRITING-CHECKLIST.md, fill in the article title and week,
> render it as a one-page printable PDF, and send it. Update the week's
> Notion row (Article Title, Source, URL) and the week's file heading.
> The checklist guides the student's writing — never fill in his
> summary, questions, or script.

## 3. Process Improvement Loop (self-paced)

> Review the workflow artifacts (repo docs/template/tools, Notion Weekly
> Article Log, the Sunday routine prompt, pick-sheet PDF and one-slide
> presentation formats), find at most one concrete improvement that
> makes the weekly cycle smoother for the student (clearer template
> prompts, better candidate sourcing, MLA accuracy, presentation
> quality), apply it, commit and push. Never write the student's
> summary/annotations/questions. If nothing needs improving, do nothing
> and report no change.

## Ground rules baked into both routines

- The student writes the summary, annotations, and questions — routines
  scaffold (citations, candidates, formats), never author graded work.
- Never reproduce an article's text; link and cite, print from source.
- Weekly cadence: Sunday pick/setup → Mon–Thu read/annotate/write →
  Friday submit (Google Doc in Schoology + annotated hard copy) and
  present.
