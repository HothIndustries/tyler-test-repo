"""Render a small ASCII Mandelbrot set in the terminal."""

PALETTE = " .:-=+*#%@"


def _iteration_count(c: complex, max_iter: int) -> int:
    z = 0j
    for i in range(max_iter):
        z = z * z + c
        if abs(z) > 2:
            return i
    return max_iter


def render_mandelbrot(width: int = 80, height: int = 24, max_iter: int = 40) -> str:
    if width <= 0 or height <= 0:
        raise ValueError("width and height must be positive integers")
    if max_iter <= 0:
        raise ValueError("max_iter must be a positive integer")

    rows = []
    for y in range(height):
        imag = (y / (height - 1)) * 2.0 - 1.0 if height > 1 else 0.0
        row = []
        for x in range(width):
            real = (x / (width - 1)) * 3.0 - 2.0 if width > 1 else -0.5
            n = _iteration_count(complex(real, imag), max_iter)
            idx = int((n / max_iter) * (len(PALETTE) - 1))
            row.append(PALETTE[idx])
        rows.append("".join(row))
    return "\n".join(rows)


if __name__ == "__main__":
    print(render_mandelbrot())
