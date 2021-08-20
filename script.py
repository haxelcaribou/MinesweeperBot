#!/usr/bin/python3

import discord
import secrets
import random


client = discord.Client()


size = 11
num_mines = 16
blank_emote = "blaank"
bomb_emote = "a"

rows = size
columns = size

status = "Minesweeper"


def generate_board(rows, columns):
    board = [[0 for i in range(0, rows)] for j in range(0, columns)]

    board_coordinates = [(x, y) for x in range(0, columns)
                         for y in range(0, rows)]
    mine_coordinates = random.sample(board_coordinates, num_mines)

    for mine in mine_coordinates:
        x, y = mine
        board[x][y] = 9
        neighbors = [(x - 1, y), (x - 1, y + 1), (x, y - 1), (x + 1, y - 1),
                     (x + 1, y), (x + 1, y + 1), (x, y + 1), (x - 1, y - 1)]
        for n in neighbors:
            if 0 <= n[0] <= columns - 1 and 0 <= n[1] <= rows - 1 and n not in mine_coordinates:
                board[n[0]][n[1]] += 1

    return board


def convert():
    message = ""
    emotes = [blank_emote, "one", "two", "three", "four",
              "five", "six", "seven", "eight", bomb_emote]

    for row in board:
        for square in row:
            message += "||:"
            message += emotes[square]
            message += ":||"
        message += "\n"

    return message


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(status))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channel = message.channel

    message_content = message.clean_content.lower()

    if message_content.startswith("!~ "):


client.run(secrets.token)
