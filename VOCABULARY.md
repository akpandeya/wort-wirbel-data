# Wort-Wirbel Data: A1 German Vocabulary

This repository contains a comprehensive collection of A1-level German vocabulary words, organized for easy access and learning. **Now with multi-language support and automated generation capabilities!**

## Structure

The vocabulary is organized in a language-specific hierarchical directory structure:

```
data/languages/german/words/
â”œâ”€â”€ a/
â”‚   â”œâ”€â”€ auto.json
â”‚   â”œâ”€â”€ apfel.json
â”‚   â””â”€â”€ ...
â”œâ”€â”€ b/
â”‚   â”œâ”€â”€ buch.json
â”‚   â”œâ”€â”€ blau.json
â”‚   â””â”€â”€ ...
â””â”€â”€ ...
```

Each word is stored as a separate JSON file in the appropriate letter directory based on the first letter of the German word.

**Multi-Language Ready**: The structure supports future expansion to other languages:
```
data/languages/
â”œâ”€â”€ german/words/...
â”œâ”€â”€ spanish/words/...
â”œâ”€â”€ french/words/...
â””â”€â”€ [other-languages]/words/...
```

## Vocabulary Generator

The repository includes `generate_vocabulary.py` for automated vocabulary creation:

### Features
- **Smart German article detection** (der/die/das) using linguistic patterns
- **Automatic example sentence generation** with proper grammar
- **Duplicate prevention** - won't overwrite existing entries
- **Filename sanitization** - converts umlauts for file system compatibility
- **A1-level focus** - generates beginner-appropriate vocabulary
- **Web API integration ready** - extensible to fetch from online dictionaries

### Usage
```bash
# Install dependencies
pip install -r requirements.txt

# Generate 10 new entries
python generate_vocabulary.py

# Generate more entries
python generate_vocabulary.py --count 25
```

## Data Format

Each vocabulary entry contains the following fields:

```json
{
  "german": "Hund",
  "english": "dog",
  "part_of_speech": "noun",
  "article": "der",
  "example_sentence": "Der Hund bellt."
}
```

### Fields Description

- **german**: The German word (with proper special characters like ä, ö, ü, ß)
- **english**: English translation
- **part_of_speech**: Grammatical category (noun, verb, adjective, etc.)
- **article**: German article for nouns (der, die, das) or null for non-nouns
- **example_sentence**: A simple German sentence demonstrating usage

## Content Overview

The collection includes **532 A1-level German vocabulary words** covering:

### Core Categories
- **Basic Expressions**: Greetings, please/thank you, yes/no
- **Family & People**: Family members, professions, personal relationships
- **Numbers**: 1-1000, ordinal numbers
- **Time**: Days, months, seasons, time expressions
- **Colors**: Basic color vocabulary
- **Body Parts**: Essential body vocabulary
- **Food & Drink**: Common foods, beverages, kitchen items
- **Clothing**: Basic clothing and accessories
- **Transportation**: Vehicles and travel-related terms
- **Places**: Home, school, city, nature locations
- **Weather & Nature**: Weather conditions, natural features
- **Animals**: Common domestic and wild animals
- **Common Verbs**: Essential action words and modal verbs
- **Adjectives**: Descriptive words for size, color, quality
- **Grammar Words**: Prepositions, conjunctions, pronouns

### Distribution by Letter
- A: 26 words | B: 39 words | C: 3 words | D: 23 words
- E: 16 words | F: 31 words | G: 24 words | H: 34 words
- I: 7 words | J: 8 words | K: 38 words | L: 20 words
- M: 32 words | N: 23 words | O: 9 words | P: 12 words
- R: 14 words | S: 76 words | T: 28 words | U: 10 words
- V: 11 words | W: 32 words | Z: 16 words

## Usage Examples

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

## Quality Assurance

- ✅ All 532 files validated for correct JSON format
- ✅ All required fields present in every entry
- ✅ Proper German special characters preserved
- ✅ Appropriate articles assigned to nouns
- ✅ Authentic German example sentences
- ✅ A1-level vocabulary selection verified
- ✅ **Automated generation with validation scripts**
- ✅ **Multi-language structure for extensibility**

## Future Enhancements

The vocabulary generator can be extended to:
- **Fetch from online German dictionaries** (Dict.cc, DWDS, etc.)
- **Integrate with translation APIs** (Google Translate, DeepL)
- **Add pronunciation data** (IPA, audio file links)
- **Include difficulty ratings** (A1, A2, B1, etc.)
- **Support other languages** (Spanish, French, Italian)

## License

This data is provided for educational purposes and German language learning.