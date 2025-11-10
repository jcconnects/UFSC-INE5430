---
description: Add a new section or subsection to the LaTeX paper (project)
---

You are helping to add a new section or subsection to the LangChain academic paper (main.tex).

## Arguments

Usage: `/add-section [SECTION_NUMBER]`

- `SECTION_NUMBER` (optional): The section/subsection number (e.g., "2.5", "3.2.1")
  - If provided, use this section number
  - If not provided, ask the user for it

## Your Task

1. **Determine the section number**:
   - If argument was provided (e.g., `/add-section 3.2`), use that section number
   - If no argument was provided, ask the user for the section number

2. **Ask the user for additional details** using the AskUserQuestion tool:
   - What type: Section or Subsection?
   - Section/Subsection title
   - Parent section label (if subsection)
   - Estimated length in pages or paragraphs (optional)

3. **Read main.tex** to understand the current structure and find the right insertion point

4. **Create the section structure** following the existing pattern in main.tex:
   - Use proper LaTeX commands (\section{} or \subsection{})
   - Add a \label{} with appropriate naming (sec: or subsec: prefix)
   - Include comment blocks with guidance on what to write
   - Follow the paragraph-by-paragraph structure with line estimates
   - Add separator comments matching the paper's style
   - **MAINTAIN all existing comments** - do not remove or modify existing guidance comments

5. **Insert at the appropriate location** in main.tex using the Edit tool

## CRITICAL: LangChain Documentation Reference

**ALWAYS base section content and guidance on the official LangChain documentation at https://python.langchain.com/**

When creating guidance comments for the new section:
- Reference specific LangChain concepts from the official docs
- Include correct component names, architecture patterns, and terminology
- Suggest relevant citations to LangChain docs in the guidance comments
- Ensure technical accuracy according to the latest LangChain documentation

## Style Guidelines

- Follow the existing comment structure in main.tex
- Include guidance comments like: `% [PARÁGRAFO 1 - X-Y linhas]: Topic description`
- Add separator lines: `% -----------------------------`
- Use proper label naming: `sec:label-name` or `subsec:label-name`
- Include instructions about content, citations, and structure

## Example Structure

```latex
% -----------------------------
% X.Y Section Title
% -----------------------------
\subsection{Section Title}
\label{subsec:section-label}

% [PARÁGRAFO 1 - 4-5 linhas]: What to cover
% - Point 1
% - Point 2
% - Point 3
% - Citar: relevant references

% [PARÁGRAFO 2 - 3-4 linhas]: Additional content
% - More points
% - More guidance
```

After creating the section, inform the user where it was added and provide guidance on what content should be written based on the paper's overall structure.
