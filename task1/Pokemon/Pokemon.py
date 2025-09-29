import Buff
import random
import Type
class Pokemon:

    def __init__(self,hp,attack,evasion,defense):
        self.hp = hp
        self.current_hp = hp
        self.attack = attack
        self.current_attack = attack
        self.evasion = evasion
        self.current_evasion = evasion
        self.defense = defense
        self.current_defense = defense
        #伤害倍率
        self.attack_factor = 1.0
        #实际受伤倍率
        self.damage_factor = 1.0
        self.counter = 2 #0:被克制 1:克制 2:无克制
        self.buff = []
        self.skill = []
    def activate_counter(self):
        #临时将受伤倍率减半，攻击倍率翻倍
        self.damage_factor /= 2
        self.attack_factor *= 2
        self.counter = 1
    def activate_be_countered(self):
        self.damage_factor *= 2
        self.attack_factor /= 2
        self.counter = 0
    def deactivate_counter(self):
        #恢复受伤倍率和攻击倍率
        if self.counter == 1:
            self.damage_factor *= 2
            self.attack_factor /= 2
            self.counter = 2
        elif self.counter == 0:
            self.damage_factor /= 2
            self.attack_factor *= 2
            self.counter = 2
    def add_buff(self, buff: Buff):
        self.buff.append(buff)
    def remove_buff(self, buff: Buff):
        self.buff.remove(buff)
    def apply_buffs(self):
        for buff in self.buff:
            if buff.duration > 0:
                buff.apply(self)
                buff.duration -= 1
            if buff.duration == 0:
                self.remove_buff(buff)
    def take_damage(self, damage: float, ignore_evasion: bool = False, ignore_defense: bool = False, ignore_defense_factor: bool = False) -> (int,float):
        #返回值(状态,实际伤害) 0闪避 1命中 2格挡(强制扣除1点血量)
        # 先判断是否闪避
        is_evasion_success = True if random.random() <= self.current_evasion else False
        if not ignore_evasion:
            if is_evasion_success:
                return Type.damage_evasion,0
        if not ignore_defense:
            damage = damage - self.current_defense
        if not ignore_defense_factor:
            damage = damage * self.damage_factor
        if damage > 1:
            return Type.damage_success,damage
        else:
            return Type.damage_block,1
    def heal(self,amount):
        #回复血量，不能超过最大血量
        if amount + self.current_hp <= self.hp:
            self.current_hp += amount
        else:
            self.current_hp = self.hp


class GrassPokemon(Pokemon):
    def __init__(self,hp,attack,evasion,defense):
        super().__init__(hp,attack,evasion,defense)
        self.attribute = Type.attr_grass
        #添加属性buff
        grass_buff = Buff.GrassPokemonBuff(self)
        self.add_buff(grass_buff)



a = GrassPokemon()




