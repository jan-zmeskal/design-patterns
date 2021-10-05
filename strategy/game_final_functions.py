from typing import Callable, Tuple


def get_distance_to_enemy() -> int:
    """Just a mock for demo purposes."""
    return 1


def branch_attack_strategy(stats: dict) -> Tuple[str, int]:
    weapon_name = "branch"
    if get_distance_to_enemy() <= 2:
        return weapon_name, stats["strength"]
    return weapon_name, 0


def fireball_attack_strategy(stats: dict) -> Tuple[str, int]:
    return "fireball", stats["intelligence"] + stats["dexterity"] + 1


class GameCharacter:
    def __init__(
        self, name: str, attack_strategy: Callable[[dict], Tuple[str, int]] = None
    ) -> None:
        self.name = name
        self.level = 0
        self.strength = self.dexterity = self.intelligence = self.charisma = 5
        self.attack_strategy = attack_strategy or branch_attack_strategy

    @property
    def stats(self) -> dict:
        return {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "intelligence": self.intelligence,
            "charisma": self.charisma,
        }

    def attack(self) -> int:
        weapon, power = self.attack_strategy(self.stats)

        print(f"{self.name} attacks using {weapon} dealing {power} damage")

        return power


def main():
    arthas = GameCharacter(name="Arthas")
    assert arthas.attack() == 5
    arthas.attack_strategy = fireball_attack_strategy
    assert arthas.attack() == 11


if __name__ == "__main__":
    main()
