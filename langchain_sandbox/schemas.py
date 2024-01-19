import pydantic.v1


class GroceriesInput(pydantic.v1.BaseModel):
    groceries: dict[str, dict[str, float]] = pydantic.v1.Field(
        description=(
            "This will contain multiple different groceries. "
            "For each grocery item, we will have a: "
            "quantity [number > 0], "
            "and price [number >= 0] (free means 0)."
        ),
    )
