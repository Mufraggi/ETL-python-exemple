from pydantic import BaseModel, Field
from typing import List, Dict, Optional


class NameModel(BaseModel):
    fr: str
    en: str
    jp: str


class SpriteModel(BaseModel):
    regular: Optional[str]
    shiny: Optional[str]
    gmax: Optional[object] = None


class TypeModel(BaseModel):
    name: str
    image: str


class TalentModel(BaseModel):
    name: str
    tc: bool


class StatsModel(BaseModel):
    hp: int
    atk: int
    def_: int = Field(alias="def")
    spe_atk: int
    spe_def: int
    vit: int


class ResistanceModel(BaseModel):
    name: str
    multiplier: float


class EvolutionModel(BaseModel):
    pre: Optional[List[object]] = None
    next: Optional[List[object]] = None
    mega: Optional[List[object]] = None


class SexeModel(BaseModel):
    male: float
    female: float


class PokemonModel(BaseModel):
    pokedexId: int
    generation: int
    category: str
    name: NameModel
    sprites: SpriteModel
    types: Optional[List[TypeModel]] = None
    talents: Optional[List[TalentModel]] = None
    stats: Optional[StatsModel]
    resistances: Optional[List[ResistanceModel]] = None
    evolution: Optional[EvolutionModel]
    height: Optional[str]
    weight: Optional[str]
    egg_groups: Optional[List[str]]
    sexe: Optional[SexeModel]
    catch_rate: Optional[int]
    level_100: Optional[int]
    forme: Optional[object] = None
