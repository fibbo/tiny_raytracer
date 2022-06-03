class SceneBase:
    def __str__(self):
        raise NotImplementedError(
            "This function should be implemented in derived classes."
        )

    def to_json(self):
        raise NotImplementedError(
            "This function should be implemented in derived classes."
        )

    def from_json(self, json):
        raise NotImplementedError(
            "This function should be implemented in derived classes."
        )
