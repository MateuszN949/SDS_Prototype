from linear_transform import LinearTransformModel


def test_prediction():
    model = LinearTransformModel(
        coefficient=2,
        bias=1,
    )

    assert model.predict(3) == 7