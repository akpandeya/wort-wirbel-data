# Wort-Wirbel Data 🇩🇪

A comprehensive collection of **532 A1-level German vocabulary words** organized for easy access, learning, and development of German language applications. **Extensible to support multiple languages!**

## 🎯 Overview

This repository provides structured vocabulary data in JSON format, perfect for:
- Language learning applications
- Vocabulary games and quizzes
- Educational tools and resources
- Data analysis of language patterns
- API development for language learning platforms
- **Automated vocabulary generation from web sources**

##  Structure

```
wort-wirbel-data/
 README.md                    # This file
 VOCABULARY.md                # Detailed vocabulary documentation
 generate_vocabulary.py       # Vocabulary generator script
 requirements.txt             # Python dependencies
 data/
     languages/
         german/              # German language data
             words/
                 a/           # Words starting with 'a'
                    auto.json
                    apfel.json
                    ...
                 b/           # Words starting with 'b'
                    buch.json
                    blau.json
                    ...
                 ...          # Through z/
```

**Future Language Support**: The structure is designed to easily add other languages:
```
data/languages/
 german/words/...
 spanish/words/...
 french/words/...
 italian/words/...
```

Each language word is stored as a separate JSON file in the appropriate letter directory.

## 🤖 Vocabulary Generator

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
- ✅ **Smart article detection** for German nouns (der/die/das)
- ✅ **Automatic example sentence generation**
- ✅ **Duplicate prevention** - won't overwrite existing entries
- ✅ **Filename sanitization** - handles umlauts (äâ†’ae, öâ†’oe, üâ†’ue, ßâ†’ss)
- ✅ **A1-level focus** - generates beginner-appropriate vocabulary
- ✅ **Extensible architecture** - easy to add new data sources
- ✅ **Proper JSON formatting** - includes newlines for GitHub display

## Š Data Format

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
| `german` | string | The German word (with proper umlauts: ä, ö, ü, ß) |
| `english` | string | English translation |
| `part_of_speech` | string | Grammatical category (noun, verb, adjective, etc.) |
| `article` | string\|null | German article for nouns (der, die, das) or null for non-nouns |
| `example_sentence` | string | Simple German sentence demonstrating usage |

## Content Statistics

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

## 🚀 Usage Examples

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

## Content Categories

The vocabulary covers essential A1-level topics:

- **Greetings & Politeness**: Hallo, Danke, Bitte, Tschüss
- **Family & People**: Familie, Mutter, Vater, Kind, Freund
- **Numbers**: 1-1000, ordinal numbers
- **Time**: Days, months, seasons, clock time
- **Colors**: Rot, Blau, Grün, Gelb, etc.
- **Body Parts**: Kopf, Hand, Auge, Nase, etc.
- **Food & Drink**: Brot, Wasser, Apfel, Kaffee, etc.
- **Clothing**: Hemd, Hose, Schuh, Jacke, etc.
- **Transportation**: Auto, Bus, Zug, Fahrrad, etc.
- **Places**: Haus, Schule, Stadt, Park, etc.
- **Weather**: Sonne, Regen, Schnee, warm, kalt
- **Animals**: Hund, Katze, Vogel, Fisch, etc.
- **Common Verbs**: sein, haben, gehen, kommen, etc.
- **Adjectives**: groß, klein, schön, gut, etc.

## ✅ Quality Assurance

- ✅ All 532 files validated for correct JSON format
- ✅ All required fields present in every entry
- ✅ Proper German special characters (ä, ö, ü, ß) preserved
- ✅ Appropriate articles assigned to nouns
- ✅ Authentic German example sentences
- ✅ A1-level vocabulary selection verified
- ✅ Files properly formatted for GitHub display
- ✅ **Automated generation scripts with validation**
- ✅ **Multi-language structure for future expansion**

## 🌍 Multi-Language Support

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

## Documentation

For detailed vocabulary information and advanced usage, see [VOCABULARY.md](VOCABULARY.md).

## 🤝 Contributing

This is a curated dataset for A1-level German vocabulary. If you find errors or have suggestions for improvements, please open an issue.

## License

This data is provided for educational purposes and German language learning. Feel free to use it in your projects to help others learn German!

---

**Viel Erfolg beim Deutschlernen!**
