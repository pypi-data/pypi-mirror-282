from sys import argv
from typing import Type
from entyty import _AbstractEntity as AbstractEntity
import dicepy
import CharActor as ca
import pymunk

from ..dicts import load_dict

_MONSTERS = load_dict('monsters')

class BaseMonster(AbstractEntity):
    _monster_name:      Type[str] = None
    _level:             Type[int] = None
    _hitpoints:         Type[int] = None
    _ability_scores:    Type[dict]= None
    _strength:          Type[int] = None
    _strength_mod:      Type[int] = None
    _dexterity:         Type[int] = None
    _dexterity_mod:     Type[int] = None
    _constitution:      Type[int] = None
    _constitution_mod:  Type[int] = None
    _intelligence:      Type[int] = None
    _intelligence_mod:  Type[int] = None
    _wisdom:            Type[int] = None
    _wisdom_mod:        Type[int] = None
    _charisma:          Type[int] = None
    _charisma_mod:      Type[int] = None
    _armor_class:       Type[int] = None
    _attack_bonus:      Type[int] = None
    _saving_throws:     Type[dict]= None
    _fortitude:         Type[int] = None
    _reflex:            Type[int] = None
    _will:              Type[int] = None
    _damage:            Type[dict]= None
    _dmg_dice:          Type[int] = None
    _dmg_dice_value:    Type[int] = None
    _initiative:        Type[int] = None
    _speed:             Type[dict]= None
    _size:              Type[str] = None
    _type:              Type[str] = None
    _subtype:           Type[str] = None
    _alignment:         Type[str] = None
    _special_abilities: Type[dict]= None
    _description:       Type[str] = None
    _dice_set:          Type[dicepy.Dice.DiceSet] = None
    _grid:              Type[any] = None
    _grid_entity:       Type[any] = None
    _target:            Type[any] = None
                  
    def __init__(
        self,
        monster_name:       Type[str] = None,
        level:              Type[int] = None,
        hitpoints:          Type[int] = None,
        ability_scores:     Type[dict] = None,
        armor_class:        Type[int] = None,
        attack_bonus:       Type[int] = None,
        saving_throws:      Type[dict] = None,
        damage:             Type[dict] = None,
        initiative:         Type[int] = None,
        speed:              Type[dict] = None,
        size:               Type[str] = None,
        monster_type:       Type[str] = None,
        subtype:            Type[str] = None,
        alignment:          Type[str] = None,
        special_abilities:  Type[dict] = None,
        description:        Type[str] = None,
        *argv, **kwargs
    ):
        self.monster_name = monster_name
        self.level = level
        self.hitpoints = hitpoints
        self.ability_scores = ability_scores
        self.armor_class = armor_class
        self.attack_bonus = attack_bonus
        self.saving_throws = saving_throws
        self.dice_set = dicepy.Dice.DiceSet()
        self.damage = damage
        self.initiative = initiative
        self.speed = speed
        self.size = size
        self.monster_type = monster_type 
        self.subtype = subtype
        self.alignment = alignment
        self.special_abilities = special_abilities
        self.description = description
        if kwargs.get('grid', None) is not None:
            from entyty import GridEntity
            self._grid = kwargs['grid']
            self.grid_entity = GridEntity(self.grid, self.monster_name, self)
               
    @property
    def monster_name(self):
        return self._monster_name
    
    @monster_name.setter
    def monster_name(self, monster_name):
        self._monster_name = monster_name
    
    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, level):
        self._level = level
    
    @property
    def hitpoints(self):
        return self._hitpoints
    
    @hitpoints.setter
    def hitpoints(self, hitpoints):
        self._hitpoints = hitpoints
    
    @property
    def ability_scores(self):
        return self._ability_scores
    
    @ability_scores.setter
    def ability_scores(self, ability_scores):
        self._ability_scores = ability_scores
        if ability_scores is None:
            return
        for key, value in ability_scores.items():
            if key == 'strength':
                self.strength = value
            elif key == 'dexterity':
                self.dexterity = value
            elif key == 'constitution':
                self.constitution = value
            elif key == 'intelligence':
                self.intelligence = value
            elif key == 'wisdom':
                self.wisdom = value
            elif key == 'charisma':
                self.charisma = value
                
    @property
    def strength(self):
        return self._strength
    
    @strength.setter
    def strength(self, strength):
        self._strength = strength
        if strength is None:
            return
        self._strength_mod = (strength - 10) // 2
        
    @property
    def strength_mod(self):
        return self._strength_mod
    
    @property
    def dexterity(self):
        return self._dexterity
    
    @dexterity.setter
    def dexterity(self, dexterity):
        self._dexterity = dexterity
        if dexterity is None:
            return
        self._dexterity_mod = (dexterity - 10) // 2
        
    @property
    def dexterity_mod(self):
        return self._dexterity_mod
    
    @property
    def constitution(self):
        return self._constitution
    
    @constitution.setter
    def constitution(self, constitution):
        self._constitution = constitution
        if constitution is None:
            return
        self._constitution_mod = (constitution - 10) // 2
        
    @property
    def constitution_mod(self):
        return self._constitution_mod
    
    @property
    def intelligence(self):
        return self._intelligence
    
    @intelligence.setter
    def intelligence(self, intelligence):
        self._intelligence = intelligence
        if intelligence is None:
            return
        self._intelligence_mod = (intelligence - 10) // 2
        
    @property
    def intelligence_mod(self):
        return self._intelligence_mod
    
    @property
    def wisdom(self):
        return self._wisdom
    
    @wisdom.setter
    def wisdom(self, wisdom):
        self._wisdom = wisdom
        if wisdom is None:
            return
        self._wisdom_mod = (wisdom - 10) // 2
        
    @property
    def wisdom_mod(self):
        return self._wisdom_mod
    
    @property
    def charisma(self):
        return self._charisma
    
    @charisma.setter
    def charisma(self, charisma):
        self._charisma = charisma
        if charisma is None:
            return
        self._charisma_mod = (charisma - 10) // 2
        
    @property
    def charisma_mod(self):
        return self._charisma_mod
    
    @property
    def armor_class(self):
        return self._armor_class
    
    @armor_class.setter
    def armor_class(self, armor_class):
        self._armor_class = armor_class
    
    @property
    def attack_bonus(self):
        return self._attack_bonus
    
    @attack_bonus.setter
    def attack_bonus(self, attack_bonus):
        self._attack_bonus = attack_bonus
    
    @property
    def saving_throws(self):
        return self._saving_throws
    
    @saving_throws.setter
    def saving_throws(self, saving_throws):
        self._saving_throws = saving_throws
        if saving_throws is None:
            return
        for key, value in saving_throws.items():
            if key == 'fortitude':
                self._fortitude = value
            elif key == 'reflex':
                self._reflex = value
            elif key == 'will':
                self._will = value
                
    @property
    def fortitude(self):
        return self._fortitude
    
    @property
    def reflex(self):
        return self._reflex
    
    @property
    def will(self):
        return self._will
    
    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, damage):
        if damage is None:
            return
        for key, value in damage.items():
            if key == 'number_of_dice':
                self._dmg_dice = value
            elif key == 'dice_value':
                self._dmg_dice_value = value
        die = getattr(self.dice_set, f'd{self._dmg_dice_value}')
        self._damage = (self._dmg_dice, die)
        
    @property
    def dmg_dice(self):
        return self._dmg_dice
    
    @property
    def dmg_dice_value(self):
        return self._dmg_dice_value
    
    @property
    def initiative(self):
        return self._initiative
    
    @initiative.setter
    def initiative(self, initiative):
        self._initiative = initiative
    
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, speed):
        self._speed = speed
    
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def monster_type(self):
        return self._monster_type
    
    @monster_type.setter
    def monster_type(self, monster_type):
        self._monster_type = monster_type
    
    @property
    def subtype(self):
        return self._subtype
    
    @subtype.setter
    def subtype(self, subtype):
        self._subtype = subtype
    
    @property
    def alignment(self):
        return self._alignment
    
    @alignment.setter
    def alignment(self, alignment):
        self._alignment = alignment
    
    @property
    def special_abilities(self):
        return self._special_abilities
    
    @special_abilities.setter
    def special_abilities(self, special_abilities):
        self._special_abilities = special_abilities
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        self._description = description
        
    @property
    def dice_set(self):
        return self._dice_set
    
    @dice_set.setter
    def dice_set(self, dice_set):
        self._dice_set = dice_set
        
    @property
    def grid(self):
        return self._grid
    
    @grid.setter
    def grid(self, grid):
        self._grid = grid
        
    @property
    def grid_entity(self):
        return self._grid_entity
    
    @grid_entity.setter
    def grid_entity(self, grid_entity):
        self._grid_entity = grid_entity
        self._create_properties()

    @property
    def target(self):
        return self._target
    
    @target.setter
    def target(self, target):
        self._target = target
        
class Monster(BaseMonster):
    def __init__(self, entry_number: Type[int] = None, **kwargs):
        if entry_number is not None:
            monster_data = Monster.load_monster(entry_number)
            if kwargs.get('grid', None) is not None:
                monster_data['grid'] = kwargs['grid']
            super().__init__(**monster_data)
        else:
            super().__init__(**kwargs)

    def _create_properties(self):
        setattr(self, 'grid', self._grid)
        setattr(self.__class__, 'grid', property(lambda self: self._grid))
        properties = {
            'cell': self.grid_entity.cell,
            'cell_name': self.grid_entity.cell_name,
            'cell_history': self.grid_entity.cell_history,
            'last_cell': self.grid_entity.last_cell,
            'x': self.grid_entity.x,
            'y': self.grid_entity.y,
            'position': pymunk.Vec2d(self.grid_entity.position[0], self.grid_entity.position[1]),
            'path': self.grid_entity.path
        }
        for attr, value in properties.items():
            setattr(self, attr, value)
            setattr(self.__class__, attr, property(lambda self, attr=attr: getattr(self.grid_entity, attr)))
   
    @staticmethod
    def load_monster(entry_number: Type[int] = None):
        return _MONSTERS[str(entry_number)]
    
    def move(self, direction: str = None, cell: object | str = None):
        FROM = self.cell.designation
        if cell is not None:
            if isinstance(cell, str):
                cell = self.grid[cell]    
            self.grid_entity.move(cell, teleport = True)
            return
        if direction is not None and direction in {
            'north_west',
            'north',
            'north_east',
            'east',
            'south_east',
            'south',
            'south_west',
            'west',
        }:
            return self._extracted_from_move_18(direction, FROM)

    def _extracted_from_move_18(self, direction, FROM):
        move = self.grid_entity.move_in_direction(direction)
        TO = self.cell.designation
        if not move:
            return move
        return f'{FROM} --> {TO}'

    def set_target(self, target: object):
        self.target = target
    
    def _attack_figure(self):
        if self.target is None:
            return 'No target.'
        attack_roll = self.dice_set.d20.roll()
        if attack_roll == 20:
            damage = sum(self.damage[1].roll() for _ in range(self.damage[0]))
            damage += self.Strength.modifier
            damage *= 2
            self.target.hp -= damage
            return f'Critical hit! {damage} damage dealt.'
        elif attack_roll == 1:
            return 'Critical miss!'
        elif attack_roll + self.Strength.modifier >= self.target.armor_class:
            damage = sum(self.damage[1].roll() for _ in range(self.damage[0]))
            damage += self.Strength.modifier
            self.target.hp -= damage
            return f'{damage} damage dealt.'
        else:
            return 'Miss!'
