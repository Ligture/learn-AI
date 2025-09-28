import Buff
import random
class Pokemon:
    def __init__(self):
        self.hp = 0
        self.attack = 0
        self.evasion = 0
        self.defense = 0
        #伤害倍率
        self.attack_factor = 1.0
        #实际受伤倍率
        self.defense_factor = 1.0
        self.buff = []
        self.skill = []
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
    def TakeDamage(self, damage: float, ignore_evasion: bool = False, ignore_defense: bool = False, ignore_defense_factor: bool = False) -> (int,float):
        #返回值(状态,实际伤害) 0闪避 1命中 2格挡(强制扣除1点血量)
        # 先判断是否闪避
        evasion_success = True if random.random() <= self.evasion else False
        if not ignore_evasion:
            if evasion_success:
                return 0,0
        if not ignore_defense:
            damage = damage - self.defense
        if not ignore_defense_factor:
            damage = damage * self.defense_factor
        if damage > 1:
            return 1,damage
        else:
            return 2,1




