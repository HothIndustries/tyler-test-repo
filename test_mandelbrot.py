import unittest

from mandelbrot import render_mandelbrot


class MandelbrotTests(unittest.TestCase):
    def test_output_size_matches_dimensions(self):
        output = render_mandelbrot(width=12, height=5, max_iter=20)
        rows = output.splitlines()
        self.assertEqual(5, len(rows))
        self.assertTrue(all(len(row) == 12 for row in rows))

    def test_invalid_dimensions_raise(self):
        with self.assertRaises(ValueError):
            render_mandelbrot(width=0, height=5, max_iter=20)
        with self.assertRaises(ValueError):
            render_mandelbrot(width=10, height=-1, max_iter=20)
        with self.assertRaises(ValueError):
            render_mandelbrot(width=10, height=5, max_iter=0)

    def test_output_is_deterministic(self):
        a = render_mandelbrot(width=20, height=8, max_iter=25)
        b = render_mandelbrot(width=20, height=8, max_iter=25)
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
