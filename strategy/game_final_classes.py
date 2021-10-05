from abc import ABC, abstractmethod


def get_distance_to_enemy() -> int:
    """Just a mock for demo purposes."""
    return 1


class AttackStrategy(ABC):
    weapon_name = ""

    @abstractmethod
    def perform_attack(self, stats: dict) -> int:
        """Determine attack power based on character's stats."""

    def __str__(self) -> str:
        return self.weapon_name


class BranchAttackStrategy(AttackStrategy):
    weapon_name = "branch"

    def perform_attack(self, stats: dict) -> int:
        if get_distance_to_enemy() <= 2:
            return stats["strength"]
        return 0


class SwordAttackStrategy(AttackStrategy):
    weapon_name = "sword"

    def perform_attack(self, stats: dict) -> int:
        if get_distance_to_enemy() <= 3:
            strength = stats["strength"]
            return strength * 4 if strength >= 10 else strength * 3
        return 0


class BowAttackStrategy(AttackStrategy):
    weapon_name = "bow"

    def perform_attack(self, stats: dict) -> int:
        return stats["dexterity"] * 3


class FireballAttackStrategy(AttackStrategy):
    weapon_name = "fireball"

    def perform_attack(self, stats: dict) -> int:
        return stats["intelligence"] + stats["dexterity"] + 1


class GameCharacter:
    def __init__(self, name: str, attack_strategy: AttackStrategy = None) -> None:
        self.name = name
        self.level = 0
        self.strength = self.dexterity = self.intelligence = self.charisma = 5
        self.attack_strategy = attack_strategy or BranchAttackStrategy()

    @property
    def stats(self) -> dict:
        return {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "intelligence": self.intelligence,
            "charisma": self.charisma,
        }

    def attack(self) -> int:
        power = self.attack_strategy.perform_attack(stats=self.stats)

        print(
            f"{self.name} attacks using {self.attack_strategy} dealing {power} damage"
        )

        return power


def main():
    arthas = GameCharacter(name="Arthas")
    assert arthas.attack() == 5
    arthas.attack_strategy = BowAttackStrategy()
    assert arthas.attack() == 15
    arthas.attack_strategy = FireballAttackStrategy()
    assert arthas.attack() == 11


if __name__ == "__main__":
    main()
