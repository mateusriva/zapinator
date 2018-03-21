"""Contains special words which are specially zapinated, or not."""

discard_tokens = ["que", "de"]
"""Tokens that shall never be zapinated. NEVER."""

specific_tokens = {"brasil" : ["🇧🇷"], "festa" : ["🎆", "🎇", "✨", "🎈", "🎉", "🎊"], "top" : ["👌"], "zap" : ["📞", "♣"]}
"""Wordlist of special tokens"""

mood_emoji = {"happy": ["😀","😁","😂","😃","😄","😅","😆","😉","😊","😋","😎","☺","😛","😜","😝", "👌"], "angry": ["😤", "😖", "🙁", "😩", "😦", "😡", "🤬"]}
"""list of emojis by mood"""
