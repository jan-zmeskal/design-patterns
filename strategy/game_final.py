def get_distance_to_enemy() -> int:
    """Just a mock for demo purposes."""
    return 1


class GameCharacter:
    def __init__(self, name: str) -> None:
        self.name = name
        self.level = 0
        self.strength = self.dexterity = self.intelligence = self.charisma = 5

    @property
    def stats(self) -> dict:
        return {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "intelligence": self.intelligence,
            "charisma": self.charisma,
        }

    def attack(self, mode: str) -> int:
        # Check if valid attack mode was provided
        if mode not in ["branch", "sword", "bow", "dagger"]:
            raise ValueError(f"Unsupported attack mode: {mode}")

        # Compute power based on the attack mode
        if mode == "branch":
            if get_distance_to_enemy() <= 2:
                power = self.strength
            else:
                power = 0
        elif mode == "sword":
            if get_distance_to_enemy() <= 3:
                power = self.strength * 4 if self.strength >= 10 else self.strength * 3
            else:
                power = 0
        elif mode == "bow":
            power = self.dexterity * 3
        elif mode == "dagger":
            if get_distance_to_enemy() <= 1 and self.dexterity >= 7:
                power = self.strength + self.dexterity
            else:
                power = 0

        print(f"{self.name} attacks using {mode} dealing {power} damage")

        return power


def main():
    arthas = GameCharacter(name="Arthas")
    assert arthas.attack("branch") == 5
    assert arthas.attack("sword") == 15
    assert arthas.attack("bow") == 15
    assert arthas.attack("dagger") == 0


if __name__ == "__main__":
    main()
