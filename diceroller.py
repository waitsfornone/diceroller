import click
import random
import json
import sys

@click.command()
@click.option("-a", "--advantage", is_flag=True)
@click.option("-d", "--disadvantage", is_flag=True)
@click.option("-c", "--check")
@click.option("-s", "--save")
@click.option("-k", "--skill")
@click.option("-e", "--equipment")
@click.option("-b", "--bless", is_flag=True)
@click.option("--char", default="lyque")
@click.argument("dice_type", nargs=-1)
def roll(dice_type, check, save, char, skill, equipment, advantage, disadvantage, bless):
    with open(f"{char}.json", "r") as inf:
        data = json.load(inf)
        # print(data)
    if check:
        if check in ["save", "skill", "equipment"]:
            click.echo("This is not the command you are looking for!")
            click.echo("See roll --help for more details")
            sys.exit(1)
        try:
            click.echo(dx(20, advantage, disadvantage) + int(data[check]))
        except KeyError:
            click.echo(f"No {check} found on character")
            click.echo(f"Top level are your checks.")
            click.echo(list(data.keys()))
    elif save:
        # gets bless
        try:
            save_roll = dx(20, advantage, disadvantage)
            if bless:
                bless_roll = dx(4)
                save_roll += bless_roll
            click.echo(save_roll + int(data["save"][save]))
        except KeyError:
            click.echo(f"No {save} found on character")
            click.echo(f"Saves on character: {list(data['save'].keys())}")
    elif skill:
        try:
            click.echo(dx(20, advantage, disadvantage) + int(data["skill"][skill]))
        except KeyError:
            click.echo(f"No {skill} found on character")
            click.echo(f"Skills on character: {list(data['skill'].keys())}")
    elif equipment:
        try:
            obj = data["equipment"][equipment]
            hit_roll = dx(20, advantage, disadvantage)
            if bless:
                bless_roll = dx(4)
                hit_roll += bless_roll
            click.echo(f"Hit: {hit_roll + int(obj['hit'])}")
            dmg_roll = multi_roll(obj["dmg_dice"])
            if hit_roll == 20:
                click.echo("CRIT")
                dmg_roll2 = multi_roll(obj["dmg_dice"])
                click.echo(f"Damage: {sum(dmg_roll) + obj['dmg_mod'] + sum(dmg_roll2)}")
            elif hit_roll == 1:
                click.echo("NATURAL 1, YOU MISS!")
            else:
                click.echo(f"Damage: {sum(dmg_roll) + obj['dmg_mod']}")
        except KeyError:
            click.echo(f"{equipment} not found in your equipment!")
            click.echo(f"Equipment on character: {data['equipment'].keys()}")
    elif dice_type:
        # dice_type is now a tuple to make it an optional argument
        # this takes the actual string out of the tuple by index
        click.echo(sum(multi_roll(dice_type[0])))
    else:
        click.echo("Initiative Roll!!!")
        mod_att = data.get("class", None)
        if not mod_att:
            click.echo("Class attribute not set!")
        else:
            try:
                #need to see if Initiative is adv/disadv
                click.echo(dx(20, advantage, disadvantage) + data[mod_att])
            except KeyError:
                click.echo(f"No {mod_att} found on character")


def multi_roll(dice_type):
    pass
    rolled_dice = []
    num_dice, dtype = dice_type.split("d")
    for x in range(0, int(num_dice)):
        rolled_dice.append(dx(int(dtype)))
    return rolled_dice


def dx(num_sides, advantage=False, disadvantage=False):
    roll1 = random.randint(1, num_sides)
    roll2 = random.randint(1, num_sides)
    if advantage and disadvantage:
        click.echo("Error! You can't have both advantage and disadvantage!")
    elif advantage:
        if roll1 > roll2:
            return roll1
        else:
            return roll2
    elif disadvantage:
        if roll1 > roll2:
            return roll2
        else:
            return roll1
    else:
        return roll1
