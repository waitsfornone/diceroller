# diceroller
Diceroller CLI for DnD, with character stats

## Character
Included is a sample character sheet that you can use as a template for your own, or just have fun with this Ranger!

## Installation
Download/Clone the repo and run `poetry install`

## Rolling Dice
Roll Initiative! `poetry run roll`

## Commands
Roll any dice -> -d, --dice-type TEXT `roll -d 1d12`

Roll a check roll -> -c, --check TEXT `roll -c strength`

Roll a save roll -> -s, --save TEXT `roll -s wisdom`

Roll a skill check -> -k, --skill TEXT `roll -k stealth`

Roll hit and damage rolls for equipped gear (or spells) -> -e, --equipment TEXT `roll -e longbow`

Roll for a specific character -> --char TEXT `roll -e longbow --char lyque`