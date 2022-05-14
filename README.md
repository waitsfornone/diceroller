# diceroller
Diceroller CLI for DnD, with character stats

## Character
Included is a sample character sheet that you can use as a template for your own, or just have fun with this Ranger!

## Installation
Download/Clone the repo and run `poetry install`

## Rolling Dice
Roll Initiative! `poetry run roll initiative`

## Commands
Roll any dice -> `roll dice 1d12` `roll dice 4d20` `roll dice 234d52342` (Yes, this technically works!)

Roll a check roll -> `roll check strength`

Roll a save roll -> `roll save wisdom`

Roll a skill check -> `roll skill stealth`

Roll hit and damage rolls for equipped gear (or spells) -> `roll equip longbow`

Roll for a specific character -> `roll --char lyque equip longbow`