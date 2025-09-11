# DSA Problems PDF Generator

## Overview

This is a Python-based PDF generator that creates comprehensive study materials for Data Structures and Algorithms (DSA) problems. The application generates well-formatted PDF documents containing DSA problems with Swift programming language solutions, detailed explanations, and complexity analysis. It's designed as an educational tool for developers studying algorithms and data structures, particularly those working with Swift.

The current version covers 14 essential DSA problems across 5 categories: Arrays (3 problems), Linked Lists (3 problems), Binary Trees (3 problems), Stacks and Queues (2 problems), and Graphs (3 problems). Each problem includes complete Swift solutions, time/space complexity analysis, and detailed explanations.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Core Architecture
- **Single-file application**: The entire application is contained in `main.py`, following a simple monolithic design pattern
- **Object-oriented design**: Uses a main `DSAProblemsPDFGenerator` class to encapsulate all PDF generation functionality
- **Template-based generation**: Employs ReportLab's document template system for consistent formatting and layout

### PDF Generation Framework
- **ReportLab integration**: Uses ReportLab library for professional PDF creation with precise layout control
- **Style management**: Implements custom styling system with predefined paragraph styles for different content types (titles, code blocks, explanations)
- **Document structure**: Utilizes ReportLab's Platypus for high-level document layout with elements like paragraphs, spacers, tables, and page breaks

### Content Organization
- **Modular content structure**: Separates different types of content (problem statements, solutions, complexity analysis) with distinct formatting
- **Code formatting**: Implements syntax highlighting and proper formatting for Swift code blocks
- **Hierarchical layout**: Uses consistent heading hierarchy and spacing for easy navigation

### Design Patterns
- **Builder pattern**: The class builds the PDF document incrementally by adding styled elements to a story list
- **Template method**: Uses consistent methods for formatting different types of content sections
- **Configuration-based styling**: Centralizes all visual formatting decisions in the style setup method

## External Dependencies

### Core Libraries
- **ReportLab**: Primary PDF generation library providing document creation, styling, and layout capabilities
- **Python Standard Library**: Uses `io`, `re`, and `datetime` modules for text processing and date handling

### ReportLab Components
- **Document templates**: `SimpleDocTemplate` for page layout and document structure
- **Content elements**: `Paragraph`, `Spacer`, `PageBreak`, `Table`, `Preformatted` for various content types
- **Styling system**: `getSampleStyleSheet`, `ParagraphStyle` for visual formatting
- **Layout utilities**: Page size definitions, color management, and text alignment tools

### Output Format
- **PDF generation**: Creates A4-sized PDF documents with professional formatting suitable for printing or digital viewing
- **File system**: Outputs to local file system with standard PDF format compatibility