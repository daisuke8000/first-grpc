# from typing import List, Optional
#
# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
#
# class Baker(BaseModel):
#
#     class Menu(BaseModel):
#         CLASSIC: str = "classic"
#         BANANA_AND_WHIP: str = "banana_and_whip"
#         BACON_AND_CHEESE: str = "bacon_and_cheese"
#         MIX_BERRY: str = "mix_berry"
#         BAKED_MARSHMALLOW: str = "baked_marshmallow"
#         SPICY_CURRY: str = "spicy_curry"
#
#     def bake_pancake(self, menu: str) -> str:
#         req =