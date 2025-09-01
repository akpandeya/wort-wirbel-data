#!/usr/bin/env python3
"""
Wort-Wirbel Vocabulary Generator
Generates German A1-level vocabulary entries from web sources
"""

import json
import os
import requests
import time
import re
from typing import Dict, List, Optional, Tuple
from pathlib import Path
import argparse
from dataclasses import dataclass
import transliterate


@dataclass
class VocabularyEntry:
    """Represents a vocabulary entry"""
    german: str
    english: str
    part_of_speech: str
    article: Optional[str]
    example_sentence: str


class GermanVocabularyGenerator:
    """Generates German vocabulary entries from various web sources"""

    def __init__(self, output_dir: str = "data/languages/german/words"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Common German articles for nouns
        self.articles = ["der", "die", "das"]

        # A1-level topics to focus on
        self.a1_topics = [
            "family", "colors", "numbers", "food", "animals", "body",
            "clothes", "house", "weather", "time", "transport", "school",
            "work", "emotions", "greetings", "activities"
        ]

    def clean_german_word(self, word: str) -> str:
        """Clean and normalize German word"""
        # Remove extra whitespace and convert to proper case
        word = word.strip()
        if word:
            word = word[0].upper() + word[1:].lower()
        return word

    def get_filename_safe_word(self, german_word: str) -> str:
        """Convert German word to filename-safe format"""
        # Replace umlauts and special characters for filenames
        replacements = {
            'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'ß': 'ss',
            'Ä': 'Ae', 'Ö': 'Oe', 'Ü': 'Ue'
        }

        filename = german_word.lower()
        for german_char, replacement in replacements.items():
            filename = filename.replace(german_char, replacement)

        # Remove any remaining non-alphanumeric characters
        filename = re.sub(r'[^a-z0-9]', '', filename)
        return filename

    def determine_article(self, german_word: str, part_of_speech: str) -> Optional[str]:
        """Determine the German article for a noun (simplified heuristic)"""
        if part_of_speech.lower() != "noun":
            return None

        word_lower = german_word.lower()

        # Common patterns for article determination (simplified)
        # These are heuristics and may not be 100% accurate
        if word_lower.endswith(('ung', 'heit', 'keit', 'schaft', 'ion')):
            return "die"
        elif word_lower.endswith(('chen', 'lein', 'ment', 'um')):
            return "das"
        elif word_lower.endswith(('er', 'ling', 'ig')):
            return "der"

        # Default fallback - would need a proper dictionary for accuracy
        return "der"  # Most common article

    def generate_example_sentence(self, entry: VocabularyEntry) -> str:
        """Generate a simple example sentence"""
        german = entry.german
        article = entry.article
        pos = entry.part_of_speech.lower()

        # Simple sentence templates based on part of speech
        if pos == "noun" and article:
            templates = [
                f"{article} {german} ist schön.",
                f"Ich sehe {article.replace('der', 'den').replace('die', 'die').replace('das', 'das')} {german}.",
                f"{article} {german} ist hier."
            ]
        elif pos == "verb":
            templates = [
                f"Ich {german}.",
                f"Wir {german} gern.",
                f"Sie {german} heute."
            ]
        elif pos == "adjective":
            templates = [
                f"Das ist {german}.",
                f"Er ist sehr {german}.",
                f"Die Blume ist {german}."
            ]
        else:
            templates = [f"Das ist {german}."]

        return templates[0]  # Return first template for simplicity

    def fetch_vocabulary_from_dict_api(self, word: str) -> Optional[VocabularyEntry]:
        """Fetch vocabulary data from a dictionary API"""
        try:
            # Using a free dictionary API (example - you may need to find a German-specific one)
            url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                if data and len(data) > 0:
                    entry_data = data[0]
                    meanings = entry_data.get('meanings', [])

                    if meanings:
                        part_of_speech = meanings[0].get('partOfSpeech', 'noun')
                        definitions = meanings[0].get('definitions', [])

                        if definitions:
                            # This is a simplified example - you'd need a proper translation service
                            # For now, creating a placeholder structure
                            return None  # API doesn't provide German translations

        except Exception as e:
            print(f"Error fetching from API for {word}: {e}")

        return None

    def create_manual_entry(self, german: str, english: str, part_of_speech: str) -> VocabularyEntry:
        """Create a vocabulary entry manually"""
        article = self.determine_article(german, part_of_speech)

        entry = VocabularyEntry(
            german=german,
            english=english,
            part_of_speech=part_of_speech,
            article=article,
            example_sentence=""
        )

        entry.example_sentence = self.generate_example_sentence(entry)
        return entry

    def save_entry(self, entry: VocabularyEntry) -> bool:
        """Save vocabulary entry to JSON file"""
        try:
            # Determine the directory based on first letter
            first_letter = entry.german[0].lower()
            letter_dir = self.output_dir / first_letter
            letter_dir.mkdir(exist_ok=True)

            # Create filename
            filename = self.get_filename_safe_word(entry.german) + ".json"
            filepath = letter_dir / filename

            # Create JSON data
            data = {
                "german": entry.german,
                "english": entry.english,
                "part_of_speech": entry.part_of_speech,
                "article": entry.article,
                "example_sentence": entry.example_sentence
            }

            # Save to file
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                f.write('\n')  # Add newline for GitHub display

            print(f"Saved: {entry.german} -> {filepath}")
            return True

        except Exception as e:
            print(f"Error saving entry {entry.german}: {e}")
            return False

    def generate_a1_vocabulary_batch(self) -> List[VocabularyEntry]:
        """Generate a batch of A1-level vocabulary entries"""
        # Sample A1 vocabulary - in a real implementation, you'd fetch from proper sources
        sample_words = [
            ("Katze", "cat", "noun"),
            ("laufen", "to run", "verb"),
            ("rot", "red", "adjective"),
            ("Schule", "school", "noun"),
            ("trinken", "to drink", "verb"),
            ("groß", "big", "adjective"),
            ("Fenster", "window", "noun"),
            ("sprechen", "to speak", "verb"),
            ("klein", "small", "adjective"),
            ("Küche", "kitchen", "noun"),
            ("fahren", "to drive", "verb"),
            ("schnell", "fast", "adjective"),
            ("Garten", "garden", "noun"),
            ("essen", "to eat", "verb"),
            ("neu", "new", "adjective"),
        ]

        entries = []
        for german, english, pos in sample_words:
            entry = self.create_manual_entry(german, english, pos)
            entries.append(entry)

        return entries

    def check_existing_words(self) -> set:
        """Get set of existing words to avoid duplicates"""
        existing = set()

        for letter_dir in self.output_dir.iterdir():
            if letter_dir.is_dir():
                for json_file in letter_dir.glob("*.json"):
                    try:
                        with open(json_file, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                            existing.add(data.get('german', '').lower())
                    except Exception as e:
                        print(f"Error reading {json_file}: {e}")

        return existing

    def generate_vocabulary(self, count: int = 10, avoid_duplicates: bool = True):
        """Generate vocabulary entries"""
        print(f"Generating {count} vocabulary entries...")

        existing_words = self.check_existing_words() if avoid_duplicates else set()
        entries = self.generate_a1_vocabulary_batch()

        saved_count = 0
        for entry in entries:
            if saved_count >= count:
                break

            if avoid_duplicates and entry.german.lower() in existing_words:
                print(f"Skipping duplicate: {entry.german}")
                continue

            if self.save_entry(entry):
                saved_count += 1
                existing_words.add(entry.german.lower())

            # Small delay to be respectful to APIs
            time.sleep(0.1)

        print(f"Successfully generated {saved_count} vocabulary entries!")


def main():
    """Main function to run the vocabulary generator"""
    parser = argparse.ArgumentParser(description="Generate German A1 vocabulary entries")
    parser.add_argument("--count", "-c", type=int, default=10,
                       help="Number of vocabulary entries to generate (default: 10)")
    parser.add_argument("--output", "-o", type=str, default="data/languages/german/words",
                       help="Output directory for vocabulary files")
    parser.add_argument("--allow-duplicates", action="store_true",
                       help="Allow duplicate entries (default: skip duplicates)")

    args = parser.parse_args()

    generator = GermanVocabularyGenerator(args.output)
    generator.generate_vocabulary(
        count=args.count,
        avoid_duplicates=not args.allow_duplicates
    )


if __name__ == "__main__":
    main()
