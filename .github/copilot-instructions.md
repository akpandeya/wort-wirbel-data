# Wort Wirbel Data Repository
German language data repository for linguistic processing and analysis tools.

**ALWAYS** reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Repository Overview
This is a data repository containing German language resources, word lists, linguistic data, and related datasets. The repository is designed to be simple and focused on data integrity rather than complex build processes.

## Working Effectively
- Verify repository structure:
  - `ls -la` -- should show README.md and .github directory
  - `cat README.md` -- displays repository description
  - `git status` -- check working directory status
- Validate data integrity:
  - `find . -name "*.txt" -o -name "*.csv" -o -name "*.json" | head -10` -- list data files
  - `wc -l *.txt *.csv 2>/dev/null || echo "No data files found yet"` -- count lines in data files
- Repository maintenance:
  - `git log --oneline -5` -- check recent changes
  - `git branch -a` -- list all branches

## Validation
- **ALWAYS** validate any new data files for:
  - Proper UTF-8 encoding: `file -bi filename.txt` should show `charset=utf-8`
  - No empty lines at end: `tail -n 5 filename.txt`
  - Consistent line endings: `dos2unix -i filename.txt` (should show "no conversion needed")
- **Data file validation scenarios:**
  - Test German text encoding: `echo "Überprüfung äöüß" > test.txt && cat test.txt && rm test.txt`
  - Verify file permissions: `ls -l *.txt *.csv 2>/dev/null | grep -v "^-rw"` (should be empty)
- **ALWAYS** run a complete data validation after making changes:
  - Check for data consistency across all files
  - Verify no binary data is accidentally committed
  - Ensure proper Git LFS usage for large files if needed

## Common Tasks
The following are outputs from frequently run commands. Reference them instead of viewing, searching, or running bash commands to save time.

### Repository root structure
```
ls -la
total 16
drwxr-xr-x 3 runner docker 4096 Sep  1 11:50 .
drwxr-xr-x 3 runner docker 4096 Sep  1 11:49 ..
drwxr-xr-x 7 runner docker 4096 Sep  1 11:50 .git
drwxr-xr-x 2 runner docker 4096 Sep  1 12:00 .github
-rw-r--r-- 1 runner docker   40 Sep  1 11:50 README.md
```

### README content
```
cat README.md
The repot with data for german language
```

## Data Repository Best Practices
- **File naming conventions:**
  - Use lowercase with hyphens: `german-words.txt`, `linguistic-data.csv`
  - Include version numbers for dataset updates: `german-words-v2.txt`
  - Use descriptive names that indicate content and purpose
- **Data organization:**
  - Group related files in subdirectories: `vocabulary/`, `grammar/`, `corpus/`
  - Include metadata files: `data-sources.md`, `license.txt`
  - Maintain changelog for data updates: `CHANGELOG.md`
- **Git practices for data:**
  - Use `.gitattributes` for proper handling of text files: `*.txt text eol=lf`
  - Consider Git LFS for files larger than 100MB
  - Always review diffs before committing data changes
- **Quality assurance:**
  - Document data sources and licensing
  - Include validation scripts for data integrity
  - Test data loading in common formats (UTF-8, CSV parsing)

## Development Guidelines
- **Adding new data files:**
  - Always test encoding: `file -bi newfile.txt`
  - Validate content structure before committing
  - Update documentation to describe new datasets
- **Making changes to existing data:**
  - Back up original data before modifications
  - Document reasons for changes in commit messages
  - Test with small samples before bulk operations
- **Data validation commands:**
  - Check for non-UTF8 characters: `grep -P '[^\x00-\x7F]' filename.txt | head -5`
  - Validate CSV structure: `head -1 filename.csv && tail -1 filename.csv`
  - Count unique entries: `sort filename.txt | uniq | wc -l`

## Future Development Expectations
As this repository grows, expect to add:
- Data processing scripts in Python or other languages
- Automated validation workflows via GitHub Actions
- Documentation for data format specifications
- Example usage scripts and notebooks
- Integration with linguistic analysis tools

## File Structure Reference
Current minimal structure:
```
.
├── .git/           # Git repository data
├── .github/        # GitHub configuration
│   └── copilot-instructions.md
└── README.md       # Basic repository description
```

Expected future structure:
```
.
├── .github/        # GitHub workflows and configs
├── data/           # Raw datasets
│   ├── vocabulary/
│   ├── grammar/
│   └── corpus/
├── docs/           # Documentation
├── scripts/        # Data processing tools
├── tests/          # Validation tests
└── README.md
```

## Troubleshooting
- **Character encoding issues:** Use `iconv -f ISO-8859-1 -t UTF-8 input.txt > output.txt`
- **Large file handling:** Consider `git lfs track "*.txt"` for files >100MB
- **Permission issues:** Run `chmod 644 *.txt *.csv *.md` to fix file permissions
- **Line ending problems:** Use `dos2unix filename.txt` to normalize line endings

Always maintain data integrity and document all changes thoroughly in commit messages and relevant documentation files.