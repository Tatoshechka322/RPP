from discriminant import calculate_discriminant


def test_positive_discriminant():
  assert calculate_discriminant(1, 2, -3) == 16
  assert calculate_discriminant(1, 4, 4) == 0


def test_negative_discriminant():
  assert calculate_discriminant(1, 2, 3) == -8
