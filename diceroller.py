import click
import random
import json

@click.command()
@click.option("-d", "--dice-type", default="d20")
@click.option("-n", "--num-dice", default=1)
@click.option("-c", "--check")
@click.option("-s", "--save")
@click.option("-k", "--skill")
@click.option("--char", default="lyque")
def roll(dice_type, num_dice, check, save, char, skill):
    with open(f"{char}.json", "r") as inf:
        data = json.load(inf)
        # print(data)
    if check:
        roll_val = d20()
        try:
            mod_val = int(data[check])
            click.echo(roll_val + mod_val)
        except KeyError:
            click.echo(f"No {check} found on character")
    elif save:
        roll_val = d20()
        try:
            mod_val = int(data["save"][save])
            click.echo(roll_val + mod_val)
        except KeyError:
            click.echo(f"No {save} found on character")
    elif skill:
        roll_val = d20()
        try:
            mod_val = int(data["skill"][skill])
            click.echo(roll_val + mod_val)
        except KeyError:
            click.echo(f"No {skill} found on character")
    elif dice_type == "d4":
        for x in range(0, num_dice):
            click.echo(d4())
    elif dice_type == "d6":
        for x in range(0, num_dice):
            click.echo(d6())
    elif dice_type == "d8":
        for x in range(0, num_dice):
            click.echo(d8())
    elif dice_type == "d10":
        for x in range(0, num_dice):
            click.echo(d10())
    elif dice_type == "d12":
        for x in range(0, num_dice):
            click.echo(d12())
    elif dice_type == "d20":
        for x in range(0, num_dice):
            click.echo(d20())
    elif dice_type == "d100":
        for x in range(0, num_dice):
            click.echo(d100())
    else:
        click.echo("Initiative Roll!!!")
        roll_val = d20()
        mod_att = data.get("class", None)
        if not mod_att:
            print("Class attribute not set!")
        else:
            try:
                mod_val = data[mod_att]
                click.echo(roll_val + mod_val)
            except KeyError:
                click.echo(f"No {mod_att} found on character")


def d4():
    return random.randint(1,4)


def d6():
    return random.randint(1,6)


def d8():
    return random.randint(1,8)


def d10():
    return random.randint(1,10)


def d12():
    return random.randint(1,12)


def d20():
    return random.randint(1,20)


def d100():
    return random.randint(1,100)