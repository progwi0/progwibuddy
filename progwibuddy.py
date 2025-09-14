from ddgs import DDGS
import os
import argparse
import wikipedia

wikipedia.set_lang("en")

version = "1.0"

argumentParse = argparse.ArgumentParser(description="Queries = Arguments. Run this file with arguments as queries.")
argumentParse.add_argument("query", help="This is your query.")
argument = argumentParse.parse_args()

if argument.query.startswith('What is '):
    wis = argument.query[8:]
    print("Progwibuddy: \n", wikipedia.summary(wis, sentences=5), "\nFrom Wikipedia.")
if argument.query.startswith('what is '):
    wis = argument.query[8:]
    print("Progwibuddy: \n", wikipedia.summary(wis, sentences=5), "\nFrom Wikipedia.")
elif argument.query.startswith('Run '):
    run = argument.query[4:]
    print("Progwibuddy: \n")
    os.system(run)
elif argument.query.startswith('run '):
    run = argument.query[4:]
    print("Progwibuddy: \n")
    os.system(run)
elif argument.query.startswith('wikipedia:'):
    wis = argument.query[10:]
    print("Progwibuddy: \n", wikipedia.summary(wis, sentences=5), "\nFrom Wikipedia.")
elif argument.query.startswith('Ver'):
    print("Progwibuddy", version)
    print("Made by progwi0!")
elif argument.query.startswith('ver'):
    print("Progwibuddy", version)
    print("Made by progwi0!")
else:
    print("Progwibuddy: \n")
    with DDGS() as ddgs:
        search = ddgs.text(argument.query, max_results=10)
        for r in search:
            print(r["title"], r["href"])
    print("\nSearched in DuckDuckGo.")
