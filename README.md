# Guru Bot

## Overview

The Guru Bot is a Python-based chatbot designed to offer wisdom and support through curated quotes based on the user's input sentiment. It utilizes sentiment analysis to determine the emotional tone of the user's message and responds with appropriate quotes from a predefined JSON file.

## Features

- **Sentiment Analysis**: The bot analyzes user input to classify it as positive, negative, or neutral using NLTK's VADER sentiment analysis tool.
- **Curated Quotes**: The bot responds with inspiring and thoughtful quotes that match the user's emotional state.
- **Interactive Interface**: Users can interact with the bot through a simple command-line interface.

## Requirements

- Python 3.x
- NLTK library
- JSON file containing quotes

## Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. **Install Required Libraries**
   ```bash
   pip install nltk

3. **Download VADER Lexicon**
   ```python
   import nltk
   nltk.download('vader_lexicon')

## Usage

1. **Run the bot:**
   ```bash
   python guru_bot.py
