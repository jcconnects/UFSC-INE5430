# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an academic paper about **LangChain**, a framework for orchestrating Large Language Models (LLMs). The paper is written in LaTeX using the SBC (Brazilian Computer Society) template for UFSC's INE5430 course. The work is due November 11, 2025, with presentations starting November 18.

**Topic**: LangChain - Framework for Orchestrating Large Language Models
**Format**: SBC template, up to 10 pages, in Brazilian Portuguese
**Authors**: André Thiago Pfleger, Gustavo Girotto, João Pedro Schmidt Cordeiro

## Important Reference

**CRITICAL**: When working with LangChain-related content, ALWAYS follow the official documentation at https://docs.langchain.com/ (as specified in user requirements). This is the authoritative source for LangChain architecture, components, and best practices.

## Building the Document

### Primary Build Method
The user typically uses the **latex-workshop extension in Cursor** to compile main.tex. This extension handles the full build process automatically, including bibliography generation.

### Manual Compilation (if needed)
If manual compilation is required:
```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

The build artifacts are stored in the `build/` directory, including:
- `main.pdf` - Final compiled PDF
- `main.bbl` - BibTeX bibliography output
- `main.synctex.gz` - SyncTeX synchronization file

## Project Structure

### Core Files
- `main.tex` - Main LaTeX document with paper content and structure
- `ref.bib` - Bibliography file with all academic references
- `sbc-template.sty` - SBC template style file (do not modify)
- `README.md` - Course requirements and assignment description

### Paper Structure (as defined in main.tex)

The paper follows this organization:

1. **Resumo** (Portuguese Abstract) - 150-200 words
2. **Abstract** (English) - Translation of Resumo
3. **Section 1: Introdução** - Context, motivation, objectives (1-1.5 pages)
4. **Section 2: Arquitetura do LangChain** - Historical evolution, architecture, LCEL (2-2.5 pages)
   - 2.1 Histórico e Evolução
   - 2.2 Arquitetura Geral
   - 2.3 Abstrações e Interfaces Fundamentais
   - 2.4 LangChain Expression Language (LCEL)
5. **Section 3: Componentes Principais** - Core components (2.5-3 pages)
   - 3.1 Model I/O (LLMs, Chat Models, Prompts, Output Parsers)
   - 3.2 Retrieval (RAG, Embeddings, Vector Stores, Document Loaders)
   - 3.3 Composition (Chains, Agents, Tools)
   - 3.4 Recursos Adicionais (Memory, Callbacks)
6. **Section 4: Aplicações Práticas** - Practical applications (1.5 pages)
   - 4.1 Chatbots Conversacionais
   - 4.2 Sistemas de Question-Answering
   - 4.3 Agentes Autônomos
   - 4.4 Aplicações em Domínios Específicos
7. **Section 5: Análise Comparativa** - Framework comparison (1.5 pages)
   - 5.1 Frameworks Alternativos (LlamaIndex, Semantic Kernel, Haystack)
   - 5.2 Comparação Estruturada
   - 5.3 Vantagens do LangChain
   - 5.4 Limitações e Desafios
8. **Section 6: Conclusão e Trabalhos Futuros** - Conclusions (0.5-1 page)
9. **Bibliografia** - References from ref.bib

## Content Guidelines

### Writing Style
- Language: Brazilian Portuguese (with English abstract)
- Academic tone: formal, objective, technical
- Page limit: 10 pages maximum in SBC format
- Target audience: Computer Science academics and AI practitioners

### Code Listings
Python code examples use the pre-configured `listings` package with:
- Language: Python
- Line numbers on the left
- Syntax highlighting (blue keywords, gray comments, red strings)
- Automatic line breaking
- Frame around code blocks

### Citations
All citations use the `\cite{}` command referencing entries in `ref.bib`. Key references include:
- LangChain official docs: `\cite{langchain2023docs}`
- LangChain GitHub: `\cite{langchain2023github}`
- RAG paper: `\cite{lewis2020retrieval}`
- ReAct pattern: `\cite{yao2023react}`
- GPT-4: `\cite{openai2023gpt4}`
- Russell & Norvig AI book: `\cite{russell2010artificial}`

### Figures and Diagrams
- TikZ is configured for creating architecture diagrams
- See Figure 1 (arquitetura) for the package-based modular architecture diagram
- Use `\begin{figure}[H]` for precise positioning
- Always include `\caption{}` and `\label{fig:name}`

## Bibliography Management

The `ref.bib` file is organized by categories:
1. LangChain official documentation and resources
2. Large Language Models fundamentals
3. Retrieval-Augmented Generation (RAG)
4. Agents and reasoning
5. Prompt engineering
6. Embeddings and vector databases
7. Alternative frameworks
8. Applications and use cases
9. Challenges and limitations

When adding new references:
- Follow existing formatting patterns
- Include access dates for web resources
- Use proper entry types (@article, @misc, @book, @inproceedings)
- Add to the appropriate category with clear comments

## Key LangChain Concepts to Reference

When working on content related to these topics, ensure accuracy per https://docs.langchain.com/:

1. **Core Architecture**: langchain-core, langchain, integrations (langchain-openai, langchain-anthropic), langchain-community
2. **LCEL (LangChain Expression Language)**: Runnable interface, pipe operator (|), composition paradigm
3. **Components**:
   - Model I/O: LLMs, Chat Models, PromptTemplates, Output Parsers
   - Retrieval: RAG, Embeddings, Vector Stores, Document Loaders, Retrievers
   - Composition: Chains, Agents, Tools
   - Additional: Memory systems, Callbacks
4. **Ecosystem**: LangSmith (debugging/monitoring), LangServe (deployment), LangGraph (stateful graph orchestration)
5. **Agent Patterns**: ReAct (Reasoning + Acting), Zero-shot ReAct, Structured Chat, OpenAI Functions

## Common Tasks

### Adding a new section or subsection
1. Follow the structure comments in main.tex
2. Each section has guidance comments indicating content, length, and what to include
3. Maintain the paragraph-by-paragraph structure shown in comments

### Adding new references
1. Add entry to `ref.bib` in appropriate category
2. Use `\cite{key}` in main.tex
3. Rebuild with bibtex to update bibliography

### Updating figures
1. TikZ diagrams are defined inline in main.tex
2. Use the configured styles: package, component, ecosystem
3. Follow the pattern in Figure 1 for consistency

### Checking document status
The paper currently has:
- Abstract completed (both Portuguese and English)
- Introduction completed (Section 1)
- Architecture section partially written (Section 2.1-2.2)
- Rest of the document contains detailed guidance comments for completion

## Git Workflow

Current branch: `main`
Recent commits focus on adding introduction, abstract, and LangChain-specific content.

When committing changes, reference specific sections (e.g., "Add Section 3.1 Model I/O content" or "Update RAG discussion in Section 3.2").
