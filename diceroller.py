import click
import random
import json

@click.command()
@click.option("-d", "--dice-type")
@click.option("-c", "--check")
@click.option("-s", "--save")
@click.option("-k", "--skill")
@click.option("-e", "--equipment")
@click.option("--char", default="lyque")
def roll(dice_type, check, save, char, skill, equipment):
    with open(f"{char}.json", "r") as inf:
        data = json.load(inf)
        # print(data)
    if check:
        roll_val = dx(20)
        try:
            mod_val = int(data[check])
            click.echo(roll_val + mod_val)
        except KeyError:
            click.echo(f"No {check} found on character")
    elif save:
        roll_val = dx(20)
        try:
            mod_val = int(data["save"][save])
            click.echo(roll_val + mod_val)
        except KeyError:
            click.echo(f"No {save} found on character")
    elif skill:
        roll_val = dx(20)
        try:
            mod_val = int(data["skill"][skill])
            click.echo(roll_val + mod_val)
        except KeyError:
            click.echo(f"No {skill} found on character")
    elif equipment:
        try:
            obj = data["equipment"][equipment]
            hit_roll = dx(20)
            hit_mod = obj["hit"]
            click.echo(f"Hit: {hit_roll + hit_mod}")
            dmg_roll = multi_roll(obj["dmg_dice"])
            dmg_mod = obj["dmg_mod"]
            if hit_roll == 20:
                click.echo("CRIT")
                dmg_roll2 = multi_roll(obj["dmg_dice"])
                click.echo(f"Damage: {sum(dmg_roll) + dmg_mod + sum(dmg_roll2)}")
            else:
                click.echo(f"Damage: {sum(dmg_roll) + dmg_mod}")
        except KeyError:
            click.echo(f"{equipment} not found in your equipment!")
    elif dice_type:
        rolled_dice = multi_roll(dice_type)
        click.echo(sum(rolled_dice))
    else:
        click.echo("Initiative Roll!!!")
        roll_val = dx(20)
        mod_att = data.get("class", None)
        if not mod_att:
            click.echo("Class attribute not set!")
        else:
            try:
                mod_val = data[mod_att]
                click.echo(roll_val + mod_val)
            except KeyError:
                click.echo(f"No {mod_att} found on character")


def multi_roll(dice_type):
    rolled_dice = []
    num_dice, dtype = dice_type.split("d")
    for x in range(0, int(num_dice)):
        rolled_dice.append(dx(int(dtype)))
    return rolled_dice


def dx(num_sides):
    return random.randint(1, num_sides)
