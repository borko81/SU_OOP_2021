from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player import Player


class BattleField:
    @staticmethod
    def fight(attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        if attacker.__class__.__name__ == 'Beginner':
            attacker.health += 40
            for x in attacker.card_repository.cards:
                x.damage_points += 30

        if enemy.__class__.__name__ == 'Beginner':
            enemy.health += 40
            for x in enemy.card_repository.cards:
                x.damage_points += 30

        attacker.health += sum([x.health_points for x in attacker.card_repository.cards])
        enemy.health += sum([x.health_points for x in enemy.card_repository.cards])

        for c in attacker.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return
            enemy.take_damage(c.damage_points)

        for c in enemy.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return
            attacker.take_damage(c.damage_points)


if __name__ == '__main__':
    b = BattleField()
    a = Beginner('A')
    e = Advanced('AA')
    print(type(b.fight).__name__)
