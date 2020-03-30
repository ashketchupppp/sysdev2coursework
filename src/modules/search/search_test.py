import unittest
import os
from search import *

class TestSearchFcuntion(unittest.TestCase):
    def test_valid_entry(self):
        """Test if expeted result is retuned with valid list."""
        movies = [
        {
        "name": "Usual Suspects", 
        "imdb": 7.0,
        "category": "Thriller"
        },
        {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
        },
        {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
        },
        {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
        },
        {
        "name": "Help",
        "imdb": 6.2,
        "category": "Romance"
        },
        {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
        }
        ]
        actualOutput = search_dict(movies, "Colonia", "name")
        expectedOutput = {'name': 'Colonia', 'imdb': 7.4, 'category': 'Romance'}
        self.assertEqual(actualOutput, expectedOutput)
        
    def test_invalid_entry(self):
        """Test if -1 reurned if not in list."""
        movies = [
        {
        "name": "Usual Suspects", 
        "imdb": 7.0,
        "category": "Thriller"
        },
        {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
        },
        {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
        },
        {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
        },
        {
        "name": "Help",
        "imdb": 6.2,
        "category": "Romance"
        },
        {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
        }
        ]
        actualOutput = search_dict(movies, "nothere", "name")
        expectedOutput = [-1]
        self.assertEqual(actualOutput, expectedOutput)
    
    def test_multiple_entry(self):
        """Test if -2 reurned if entry multiple results found."""
        movies = [
        {
        "name": "Usual Suspects", 
        "imdb": 7.0,
        "category": "Thriller"
        },
        {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
        },
        {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
        },
        {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
        },
        {
        "name": "Colonia",
        "imdb": 6.2,
        "category": "Romance"
        },
        {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
        }
        ]
        actualOutput = search_dict(movies, "Colonia", "name")
        expectedOutput = [-2]
        self.assertEqual(actualOutput, expectedOutput)
    
    def test_invalid_key(self):
        """Test if -1 reurned if key is invalid."""
        movies = [
        {
        "name": "Usual Suspects", 
        "imdb": 7.0,
        "category": "Thriller"
        },
        {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
        },
        {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
        },
        {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
        },
        {
        "name": "test",
        "imdb": 6.2,
        "category": "Romance"
        },
        {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
        }
        ]
        actualOutput = search_dict(movies, "Colonia", "nothere")
        expectedOutput = [-1]
        self.assertEqual(actualOutput, expectedOutput)
        
    def test_empty_list(self):
        """Test if -1 reurned if empty dict."""
        movies = []
        actualOutput = search_dict(movies, "Colonia", "nothere")
        expectedOutput = [-1]
        self.assertEqual(actualOutput, expectedOutput)

# this is required to be able to run the tests
if __name__ == '__main__':
    unittest.main()

