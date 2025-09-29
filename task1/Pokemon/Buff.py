import Type
class Buff:
    def __init__(self,target):
        self.name = ""
        self.duration = 0
        self.target = target
    def apply(self):
        pass
    def remove(self):
        pass
    def on_take_damage(self): #受到伤害时触发
        pass
    def on_give_attack(self,status:int): #攻击时触发
        pass
    def on_turn_start(self): #回合开始时触发
        pass
    def on_turn_end(self): #回合结束时触发
        self.duration -= 1
        # duration为0时自动删除buff
        if self.duration <= 0:
            self.target.remove_buff(self)


class GrassPokemonBuff(Buff):
    def __init__(self,target):
        super().__init__(target)
        self.name = "GrassPokemonBuff"
        #永久被动，需手动删除
        self.duration = 999
    def on_turn_start(self):
        self.target.heal(self.target.max_hp*0.1)

class FirePokemonBuff(Buff):
    def __init__(self,target):
        super().__init__(target)
        self.name = "FirePokemonBuff"
        self.duration = 999
        self.amount = 0 #层数
        self.max_amount = 4
    def apply(self):
        pass
    def on_give_attack(self,status:int):
        if status == Type.damage_success:
            self.amount = max(self.amount+1,self.max_amount)
