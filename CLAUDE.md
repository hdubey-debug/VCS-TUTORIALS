# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains Manim animation scripts that visualize various text alignment and scoring algorithms used in natural language processing and computational linguistics. Each Python file represents a different animation demonstrating concepts like semantic alignment, narrative alignment, and text matching.

## Key Animation Scripts

- **BMA.py / BMA2.1.py / BMA3.py**: Block Matching Algorithm animations with different visualization approaches
- **Best_Matching.py**: Best matching algorithm visualization
- **SAS1.1.py**: Semantic Alignment Score animation
- **NASD.py**: Narrative Alignment Score - Distance visualization
- **NASL.py**: Narrative Alignment Score - Length animation
- **LAS.py**: Local Alignment Score demonstration
- **VAD1.1.py**: Visual Alignment Demonstration with L-shaped arrows
- **SC.py**: Score Calculation animation

## Development Commands

### Environment Setup
1. python -m venv venv
2. source venv/bin/activate
```

### Running Animations
```bash
# Basic command structure (from README.md example):
python -m manim -pql --disable_caching NASD.py FullConceptAnimation

# General pattern:
python -m manim -pql --disable_caching <script_name.py> FullConceptAnimation
```

### Common Manim Flags
- `-pql`: Preview quality, low resolution (faster rendering)
- `-pqm`: Preview Quality Medium (720p, 30fps)
- `-pqh`: Preview Quality High (1080p, 60fps) - recommended for high quality
- `--disable_caching`: Prevents caching for fresh renders
- `-p`: Preview the animation after rendering
- `-pqk`: Preview Quality 4K (2160p, 60fps) - best quality but large files

## Code Architecture

### Common Structure
All animation scripts follow a consistent pattern:
1. **FullConceptAnimation(Scene)**: Main animation class that extends Manim's Scene
2. **construct()**: Main method containing the animation sequence
3. **Manim imports**: Extensive use of Manim objects (Text, Rectangle, Arrow, VGroup, etc.)

### Animation Patterns
- **Heading Creation**: Title text with underlines, positioned at top
- **Box Visualizations**: Rectangle containers for reference and generated text
- **Cosine Similarity Matrices**: 2D arrays representing similarity scores between text segments
- **Arrow Systems**: Various arrow types (straight, L-shaped, curved) to show relationships
- **Color Coding**: Consistent color schemes (BLUE_E for reference, GREEN_E for generated content)

### Shared Visual Elements
- Text boxes with colored backgrounds and borders
- Similarity score heatmaps using cosine values
- Arrow-based flow diagrams
- Mathematical notation using MathTex
- Animation sequences with timing controls

## Dependencies

The project requires:
- **manim**: Primary animation library
- **numpy**: Used indirectly (imported as `np` in some files)

Note: No requirements.txt or package configuration files are present. Dependencies must be managed manually.