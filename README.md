# Wort-Wirbel Data ðŸ‡©ðŸ‡ª

A comprehensive collection of **532 A1-level German vocabulary words** organized for easy access, learning, and development of German language applications. **Extensible to support multiple languages!**

## ðŸŽ¯ Overview

This repository provides structured vocabulary data in JSON format, perfect for:
- Language learning applications
- Vocabulary games and quizzes
- Educational tools and resources
- Data analysis of language patterns
- API development for language learning platforms
- **Automated vocabulary generation from web sources**

## ðŸ“ Structure

```
wort-wirbel-data/
â”œâ”€â”€ README.md                    # This file
â”œâ”€â”€ VOCABULARY.md                # Detailed vocabulary documentation
â”œâ”€â”€ generate_vocabulary.py       # Vocabulary generator script
â”œâ”€â”€ requirements.txt             # Python dependencies
â””â”€â”€ data/
    â””â”€â”€ languages/
        â””â”€â”€ german/              # German language data
            â””â”€â”€ words/
                â”œâ”€â”€ a/           # Words starting with 'a'
                â”‚   â”œâ”€â”€ auto.json
                â”‚   â”œâ”€â”€ apfel.json
                â”‚   â””â”€â”€ ...
                â”œâ”€â”€ b/           # Words starting with 'b'
                â”‚   â”œâ”€â”€ buch.json
                â”‚   â”œâ”€â”€ blau.json
                â”‚   â””â”€â”€ ...
                â””â”€â”€ ...          # Through z/
```

**Future Language Support**: The structure is designed to easily add other languages:
```
data/languages/
â”œâ”€â”€ german/words/...
â”œâ”€â”€ spanish/words/...
â”œâ”€â”€ french/words/...
â””â”€â”€ italian/words/...
```

Each language word is stored as a separate JSON file in the appropriate letter directory.

## ðŸ¤– Vocabulary Generator

The included `generate_vocabulary.py` script can automatically create new vocabulary entries:

### Installation
```bash
# Install Python dependencies
pip install -r requirements.txt
```

### Usage
```bash
# Generate 10 new vocabulary entries (default)
python generate_vocabulary.py

# Generate 25 new entries
python generate_vocabulary.py --count 25

# Generate to custom directory
python generate_vocabulary.py --output "data/languages/spanish/words"

# Allow duplicate entries
python generate_vocabulary.py --allow-duplicates

# Show help
python generate_vocabulary.py --help
```

### Features
- âœ… **Smart article detection** for German nouns (der/die/das)
- âœ… **Automatic example sentence generation**
- âœ… **Duplicate prevention** - won't overwrite existing entries
- âœ… **Filename sanitization** - handles umlauts (Ã¤â†’ae, Ã¶â†’oe, Ã¼â†’ue, ÃŸâ†’ss)
- âœ… **A1-level focus** - generates beginner-appropriate vocabulary
- âœ… **Extensible architecture** - easy to add new data sources
- âœ… **Proper JSON formatting** - includes newlines for GitHub display

## ðŸ“Š Data Format

Each vocabulary entry follows this consistent structure:

```json
{
  "german": "Hund",
  "english": "dog",
  "part_of_speech": "noun",
  "article": "der",
  "example_sentence": "Der Hund bellt."
}
```

### Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `german` | string | The German word (with proper umlauts: Ã¤, Ã¶, Ã¼, ÃŸ) |
| `english` | string | English translation |
| `part_of_speech` | string | Grammatical category (noun, verb, adjective, etc.) |
| `article` | string\|null | German article for nouns (der, die, das) or null for non-nouns |
| `example_sentence` | string | Simple German sentence demonstrating usage |

## ðŸ”¢ Content Statistics

- **Total Words**: 532 A1-level vocabulary entries
- **Coverage**: Core German concepts for beginners
- **Quality**: All entries manually verified for accuracy

### Word Distribution by Starting Letter

| Letter | Count | Letter | Count | Letter | Count |
|--------|-------|--------|-------|--------|-------|
| A | 26 | H | 34 | S | 76 |
| B | 39 | I | 7 | T | 28 |
| C | 3 | J | 8 | U | 10 |
| D | 23 | K | 38 | V | 11 |
| E | 16 | L | 20 | W | 32 |
| F | 31 | M | 32 | Z | 16 |
| G | 24 | N | 23 | - | - |

## ðŸš€ Usage Examples

### Load a single word
```bash
# Windows
type data\languages\german\words\h\hallo.json

# Unix/Linux/Mac
cat data/languages/german/words/h/hallo.json
```

### Find all nouns
```bash
# Windows PowerShell
Get-ChildItem -Path "data\languages\german\words" -Filter "*.json" -Recurse | ForEach-Object { if ((Get-Content $_.FullName | ConvertFrom-Json).part_of_speech -eq "noun") { $_.Name } }

# Unix/Linux/Mac
grep -r '"part_of_speech": "noun"' data/languages/german/words/
```

### Get all words starting with 'a'
```bash
# Windows
dir data\languages\german\words\a\

# Unix/Linux/Mac  
ls data/languages/german/words/a/
```

### Load in JavaScript/Node.js
```javascript
const fs = require('fs');
const path = require('path');

// Load a specific word
const word = JSON.parse(fs.readFileSync('data/languages/german/words/h/hallo.json', 'utf8'));
console.log(word);

// Load all German words starting with 'a'
const aWords = fs.readdirSync('data/languages/german/words/a')
  .map(file => JSON.parse(fs.readFileSync(path.join('data/languages/german/words/a', file), 'utf8')));
```

### Load in Python
```python
import json
import os

# Load a specific word
with open('data/languages/german/words/h/hallo.json', 'r', encoding='utf-8') as f:
    word = json.load(f)
    print(word)

# Load all German words starting with 'a'
a_words = []
for filename in os.listdir('data/languages/german/words/a'):
    with open(f'data/languages/german/words/a/{filename}', 'r', encoding='utf-8') as f:
        a_words.append(json.load(f))
```

## ðŸ“ Content Categories

The vocabulary covers essential A1-level topics:

- **Greetings & Politeness**: Hallo, Danke, Bitte, TschÃ¼ss
- **Family & People**: Familie, Mutter, Vater, Kind, Freund
- **Numbers**: 1-1000, ordinal numbers
- **Time**: Days, months, seasons, clock time
- **Colors**: Rot, Blau, GrÃ¼n, Gelb, etc.
- **Body Parts**: Kopf, Hand, Auge, Nase, etc.
- **Food & Drink**: Brot, Wasser, Apfel, Kaffee, etc.
- **Clothing**: Hemd, Hose, Schuh, Jacke, etc.
- **Transportation**: Auto, Bus, Zug, Fahrrad, etc.
- **Places**: Haus, Schule, Stadt, Park, etc.
- **Weather**: Sonne, Regen, Schnee, warm, kalt
- **Animals**: Hund, Katze, Vogel, Fisch, etc.
- **Common Verbs**: sein, haben, gehen, kommen, etc.
- **Adjectives**: groÃŸ, klein, schÃ¶n, gut, etc.

## âœ… Quality Assurance

- âœ… All 532 files validated for correct JSON format
- âœ… All required fields present in every entry
- âœ… Proper German special characters (Ã¤, Ã¶, Ã¼, ÃŸ) preserved
- âœ… Appropriate articles assigned to nouns
- âœ… Authentic German example sentences
- âœ… A1-level vocabulary selection verified
- âœ… Files properly formatted for GitHub display
- âœ… **Automated generation scripts with validation**
- âœ… **Multi-language structure for future expansion**

## ðŸŒ Multi-Language Support

The repository is designed to easily support additional languages:

```bash
# Generate Spanish vocabulary (future feature)
python generate_vocabulary.py --language spanish --output "data/languages/spanish/words"

# Generate French vocabulary (future feature)  
python generate_vocabulary.py --language french --output "data/languages/french/words"
```

Languages can be added by:
1. Creating new directory: `data/languages/[language]/words/`
2. Adapting the generator script for language-specific rules
3. Adding language-specific article/grammar handling

## ðŸ“– Documentation

For detailed vocabulary information and advanced usage, see [VOCABULARY.md](VOCABULARY.md).

## ðŸ¤ Contributing

This is a curated dataset for A1-level German vocabulary. If you find errors or have suggestions for improvements, please open an issue.

## ðŸ“„ License

This data is provided for educational purposes and German language learning. Feel free to use it in your projects to help others learn German!

---

**Viel Erfolg beim Deutschlernen!** ðŸŽ“
