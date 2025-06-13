# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains tutorial materials for Leafmap, a Python package for interactive geospatial mapping. Currently, the repository includes:

- `leafmap_beginner_tutorial.md` - A comprehensive beginner's tutorial in Japanese covering Leafmap installation, basic usage, and practical examples

## Development Notes

Since this is primarily a tutorial repository, there are no specific build or test commands at this time. When adding code examples or expanding the tutorials:

1. Ensure all code examples are tested and working with the latest version of Leafmap
2. Include both Japanese explanations and English code comments for accessibility
3. When creating new tutorial files, follow the existing markdown structure with clear sections and code blocks

## Permissions

The `.claude/settings.local.json` file allows:
- Web fetching from leafmap.org domain
- File system operations (find, ls commands)

This ensures Claude can access official Leafmap documentation when creating or updating tutorials.