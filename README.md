# FM Equity Research

A Python-based tool for generating professional equity research reports in PDF format. This repository provides a framework for financial analysts to create standardized equity research reports with automated data retrieval, analysis, and visualization.

## Project Overview

This project enables users to generate equity research reports for stocks by:
- Retrieving financial data using APIs
- Processing and analyzing financial metrics
- Generating visualizations of price history and comparisons
- Incorporating commentary and DCF models
- Creating a professionally formatted PDF output

## Features

- **PDF Report Generation**: Create well-formatted research reports using FPDF
- **Financial Data Retrieval**: Automatically gather key financial metrics using APIs
- **Custom Recommendations**: Visualize buy/sell/hold recommendations
- **Commentary Integration**: Import narrative analysis from text files
- **DCF Model Integration**: Include extracts from Excel-based DCF models
- **Price History Charts**: Visualize stock performance against market indices
- **Web Scraping**: Include relevant company information from websites
- **Company Selection**: Generate reports for different companies by selecting their ticker symbol

## Getting Started

### Prerequisites

```
python 3.7+
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/FM_equity_research.git
cd FM_equity_research
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

### Required Packages
- matplotlib
- matplotlib-inline
- numpy
- pandas
- requests
- yfinance
- ipywidgets
- fpdf
- lxml

## Usage

1. For team assignments, fork this repository and invite team members as collaborators
2. Review the lecture notebook for detailed implementation guidance
3. Explore the example files to understand the expected inputs and outputs
4. Refer to the FPDF instructions for PDF formatting guidelines

### Running the Project

Open and run the `lecture.ipynb` notebook to understand the process, or implement your own solution based on the task requirements.

## Project Structure

- **example_files/**: Sample data files and output examples
  - API usage examples
  - Sample DCF model
  - Example commentary text
  - Sample PDF output
- **fpdf_instructions/**: Tutorials for PDF generation
  - Basic mechanics
  - Quick guide for implementation
- **images/**: Graphics for inclusion in reports
- **lecture.ipynb**: Main tutorial notebook with implementation instructions
- **task_sheet.ipynb**: Assignment requirements and grading criteria

## Development

For development work:
1. Each team member should work on different features
2. Implement functionality in separate .py files for modular code organization
3. Create a directory structure that supports selection of different companies
4. Test PDF generation with various inputs