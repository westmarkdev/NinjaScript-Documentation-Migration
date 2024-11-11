# NinjaScript Documentation Migration

## Project Overview

This project aims to migrate and enhance NinjaScript product documentation from NinjaTrader's traditional knowledge base to a modern content management system using Sanity.io and Markdoc. The goal is to improve accessibility, consistency, and integration of NinjaScript documentation.

- Source_Files 

## Key Features

- Migration of ~2000 Markdown files to Sanity CMS
- Automated content cleaning and formatting
- Custom schema for structured content in Sanity
- Batch processing pipeline for efficient migration
- Quality assurance through automated linting and manual review

## Repository Structure

  - `source_files/`: Raw and linted input files
  - `docs/`: Processed and final output files
  - `scripts/`: Python and JavaScript processing scripts

## Getting Started

### Prerequisites

- Node.js and npm
- Python 3.x
- Sanity CLI

### Quick Start

1. Clone the repository
2. Install dependencies: `npm install`
3. Preview the migration pipeline: `node .\scripts\migrate.js
4. Run the Sanity migration pipeline: `python node .\scripts\migrate.js --execute

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## Contact

- Project Manager: [@Brett]
- Consultant: [@Matthew]

## Additional Resources

- [Project Documentation](docs/plan.md)
- [Sanity Documentation](https://www.sanity.io/docs)
- [Markdoc Documentation](https://markdoc.dev/)
