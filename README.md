# Video Content Summarization (VCS) Tutorials

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Manim](https://img.shields.io/badge/manim-community-orange.svg)](https://www.manim.community/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A comprehensive collection of **Manim animation scripts** that visualize advanced text alignment and scoring algorithms used in natural language processing, computational linguistics, and video content analysis. Each animation demonstrates sophisticated mathematical concepts through interactive visual representations.

## 🎯 Project Overview

This repository contains educational animations that illustrate various algorithms and methodologies for measuring textual similarity, narrative alignment, and content scoring. These visualizations are designed to support research in video content summarization, semantic analysis, and automated content evaluation.

### Research Applications
- **Video Content Summarization**: Automated generation and evaluation of video summaries
- **Natural Language Processing**: Text similarity and alignment measurements
- **Computational Linguistics**: Narrative structure analysis and scoring
- **Educational Technology**: Visual learning tools for complex algorithms

## 📊 Algorithm Visualizations

### Core Scoring Algorithms

| Algorithm | File | Description |
|-----------|------|-------------|
| **Block Matching Algorithm** | `BMA_Case1.py`, `BMA_Case2.py`, `BMA_Case3.py` | Multi-case BMA implementations with different optimization strategies |
| **Best Matching Algorithm** | `Best_Matching.py` | Optimal alignment finding between text sequences |
| **Global Alignment Score** | `GAS.py` | Global sequence alignment demonstrations |
| **Local Alignment Score** | `LAS.py` | Local sequence alignment visualization |
| **Narrative Alignment Score - Distance** | `NASD.py` | Distance-based narrative alignment measurements |
| **Narrative Alignment Score - Length** | `NASL.py` | Length-normalized narrative alignment scoring |
| **Score Calculation** | `SC.py` | Comprehensive scoring methodology visualization |
| **Video Comprehension Score** | `VCS.py` | Integrated multi-metric video content evaluation |

### Key Features

- **🎨 Advanced Visualizations**: Sophisticated Manim animations with professional styling
- **📈 Mathematical Precision**: Accurate implementations of scoring algorithms
- **🔄 Interactive Elements**: Dynamic mathematical transformations and constraint visualizations
- **📊 Heatmap Representations**: Cosine similarity matrices and alignment visualizations
- **🎯 Arrow-Based Flow Diagrams**: Clear visual representation of algorithmic processes
- **🎨 Color-Coded Systems**: Consistent visual themes for different components

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/VCS-TUTORIALS.git
   cd VCS-TUTORIALS
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install manim numpy
   ```

### Running Animations

**Basic Usage:**
```bash
python -m manim -pql --disable_caching <script_name.py> FullConceptAnimation
```

**Quality Options:**
- `-pql`: Preview Quality Low (480p, fast rendering)
- `-pqm`: Preview Quality Medium (720p, 30fps)
- `-pqh`: Preview Quality High (1080p, 60fps) - **recommended**
- `-pqk`: Preview Quality 4K (2160p, 60fps) - best quality

**Example Commands:**
```bash
# High-quality NASD animation
python -m manim -pqh --disable_caching NASD.py FullConceptAnimation

# Quick preview of VCS algorithm
python -m manim -pql --disable_caching VCS.py FullConceptAnimation

# 4K quality Best Matching Algorithm
python -m manim -pqk --disable_caching Best_Matching.py FullConceptAnimation
```

## 📁 Project Structure

```
VCS-TUTORIALS/
├── BMA_Case1.py              # Block Matching Algorithm - Case 1
├── BMA_Case2.py              # Block Matching Algorithm - Case 2
├── BMA_Case3.py              # Block Matching Algorithm - Case 3
├── Best_Matching.py          # Best Matching Algorithm
├── GAS.py                    # Global Alignment Score
├── LAS.py                    # Local Alignment Score
├── NASD.py                   # Narrative Alignment Score - Distance
├── NASL.py                   # Narrative Alignment Score - Length
├── SC.py                     # Score Calculation
├── VCS.py                    # Video Comprehension Score
├── media/                    # Generated animation outputs
│   ├── images/               # Static image outputs
│   ├── videos/               # Video animation files
│   └── texts/                # Text rendering cache
├── CLAUDE.md                 # Development guidelines
└── README.md                 # This file
```

## 🎨 Animation Architecture

### Common Design Patterns

All animations follow a consistent architectural approach:

```python
class FullConceptAnimation(Scene):
    def construct(self):
        # 1. Heading and title creation
        # 2. Text box visualizations with colored backgrounds
        # 3. Cosine similarity matrix representations
        # 4. Arrow system for flow visualization
        # 5. Mathematical notation using MathTex
        # 6. Timed animation sequences
```

### Visual Elements

- **📦 Text Containers**: Rectangle-based containers with consistent styling
- **🎯 Similarity Matrices**: 2D heatmap representations of cosine similarities
- **➡️ Flow Arrows**: Multiple arrow types (straight, L-shaped, curved)
- **🎨 Color Schemes**: 
  - `BLUE_E`: Reference text elements
  - `GREEN_E`: Generated content
  - `RED_E`: Highlighting and emphasis
  - `YELLOW`: Flow indicators and connections

## 📖 Algorithm Descriptions

### Video Comprehension Score (VCS)
Integrates multiple alignment metrics (SAS, CAS, NAS) to compute comprehensive video content evaluation scores through sophisticated mathematical operations.

### Block Matching Algorithm (BMA)
Demonstrates various approaches to finding optimal block matches between reference and generated text with different optimization strategies.

### Narrative Alignment Scores
- **NASD**: Distance-based measurements between narrative sequences
- **NASL**: Length-normalized alignment scoring for fair comparison

### Global & Local Alignment Scores
- **GAS**: Global sequence alignment with comprehensive coverage
- **LAS**: Local alignment focusing on specific regions of interest

## 🔧 Development

### Code Style
- Comprehensive documentation with detailed docstrings
- Consistent naming conventions and visual styling
- Modular animation components for reusability
- Mathematical precision in algorithm implementations

### Adding New Animations
1. Follow the established `FullConceptAnimation(Scene)` pattern
2. Use consistent color schemes and visual elements
3. Include comprehensive documentation headers
4. Test with multiple quality settings

## 📚 Research Context

These animations support research in:
- **Automated Video Summarization**: Evaluating quality of generated summaries
- **Content Analysis**: Measuring narrative coherence and semantic alignment
- **Educational Technology**: Visual learning tools for complex algorithms
- **NLP Research**: Understanding text similarity and alignment metrics

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Follow existing code style and documentation patterns
4. Test animations at multiple quality levels
5. Submit a pull request with detailed description

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Mehul Deep**
- Framework: Manim Community v0.19.0
- Focus: Video Content Summarization and NLP Visualization

## 🙏 Acknowledgments

- [Manim Community](https://www.manim.community/) for the excellent animation framework
- Research community for algorithm development and mathematical foundations
- Contributors to natural language processing and computational linguistics research

---

*This repository serves as both an educational resource and a research tool for understanding complex text alignment and scoring algorithms through visual representations.*