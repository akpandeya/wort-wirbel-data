# Wort-Wirbel Data: A1 German Vocabulary

This repository contains a comprehensive collection of A1-level German vocabulary words, organized for easy access and learning.

## Structure

The vocabulary is organized in a hierarchical directory structure:

```
data/words/
├── a/
│   ├── auto.json
│   ├── apfel.json
│   └── ...
├── b/
│   ├── buch.json
│   ├── blau.json
│   └── ...
└── ...
```

Each word is stored as a separate JSON file in the appropriate letter directory based on the first letter of the German word.

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
cat data/words/h/hallo.json
```

### Find all nouns
```bash
grep -r '"part_of_speech": "noun"' data/words/
```

### Get all words starting with 'a'
```bash
ls data/words/a/
```

## Quality Assurance

- ✅ All 532 files validated for correct JSON format
- ✅ All required fields present in every entry
- ✅ Proper German special characters preserved
- ✅ Appropriate articles assigned to nouns
- ✅ Authentic German example sentences
- ✅ A1-level vocabulary selection verified

## License

This data is provided for educational purposes and German language learning.