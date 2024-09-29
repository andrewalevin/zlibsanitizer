import unittest

from zlibsanitizer import sanitize



class TestSanitizer(unittest.TestCase):
    def test_sanitizer(self):
        self.assertEqual(
            sanitize("Экономика_для_обычных_людей_Основы_ав_Z_Library"),
            "Экономика_для_обычных_людей_Основы_ав"
        )
        self.assertEqual(
            sanitize("The Cambridge Dictionary of Philosoph... (Z-Library)"),
            "The Cambridge Dictionary of Philosoph..."
        )
        self.assertEqual(
            sanitize("Кант (Гулыга А. В.) (Z-Library)"),
            "Кант (Гулыга А. В.)"
        )
        self.assertEqual(
            sanitize("Понятие_политического_Карл_Шмитт_Z_Library"),
            "Понятие_политического_Карл_Шмитт"
        )
        self.assertEqual(
            sanitize("Surrounded By Bad Bosses (Thomas Erik... (Z-Library)___"),
            "Surrounded By Bad Bosses (Thomas Erik..."
        )

if __name__ == "__main__":
    unittest.main()