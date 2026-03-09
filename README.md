
[![Build and test](https://github.com/nfdi4cat/CoreMeta4Cat/actions/workflows/main.yaml/badge.svg)](https://github.com/nfdi4cat/CoreMeta4Cat/actions/workflows/main.yaml)
[![Copier Badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json)](https://github.com/linkml/linkml-project-copier) 


# CoreMeta4Cat

CoreMeta4Cat is a community-driven metadata initiative under NFDI4Cat that defines the minimum information required for reporting catalysis research data. Built on the FAIR principles — Findable, Accessible, Interoperable, and Reusable — it provides a shared language for researchers to describe, share, and discover catalysis datasets across institutions and disciplines.

The model draws its terminology from Voc4Cat, NFDI4Cat's controlled vocabulary for catalysis, ensuring standardized semantic representation. Fields are classified as Mandatory, Recommended, or Optional, helping users meet minimum quality thresholds while leaving room for richer annotation.

CoreMeta4Cat is a living standard. Community feedback — submitted via the Submit Term Feedback button on the GitHub pages — continuously shapes the addition, revision, and removal of data fields.

CoreMeta4Cat is currently developed in parallel as an Excel metadata field template as well as a LinkML schema.

### Excel Template

The Excel file can be found in [docs/assets](docs/assets/FF_20250627_Overview_metadata.xlsx)

### LinkML Schema

The LinkML Schema can be found in [src/catcore/schema/](src/catcore/schema), but we recommend to use the documentation if you are not familiar with reading native LinkML Schema, which can be found on our [GitHub pages](https://nfdi4cat.github.io/CoreMeta4Cat/):

  * [Reaction](https://nfdi4cat.github.io/CoreMeta4Cat/reaction/)
  * [Characterization](https://nfdi4cat.github.io/CoreMeta4Cat/characterization/)
  * [Synthesis](https://nfdi4cat.github.io/CoreMeta4Cat/synthesis/)
  * [Simulation](https://nfdi4cat.github.io/CoreMeta4Cat/simulation/)

## Documentation Website

[nfdi4cat.github.io/CoreMeta4Cat/](nfdi4cat.github.io/CoreMeta4Cat/)

## Repository Structure

* [docs/](docs/) - mkdocs-managed documentation
  * [elements/](docs/elements/) - generated schema documentation
* [examples/](examples/) - Examples of using the schema
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [catcore](src/catcore)
    * [schema/](src/catcore/schema) -- LinkML schema
      (edit this)
    * [datamodel/](src/catcore/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/). To list all pre-defined commands, run `just` or `just --list`.

## Credits

This project uses the template [linkml-project-copier](https://github.com/dalito/linkml-project-copier) published as [doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).
