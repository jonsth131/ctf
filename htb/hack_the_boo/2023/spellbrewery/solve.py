#!/usr/bin/env python3

correct = ["Phantom Firefly Wing", "Ghastly Gourd", "Hocus Pocus Powder", "Spider Sling Silk", "Goblin's Gold", "Wraith's Tear", "Werewolf Whisker", "Ghoulish Goblet", "Cursed Skull", "Dragon's Scale Shimmer",
           "Raven Feather", "Dragon's Scale Shimmer", "Zombie Zest Zest", "Ghoulish Goblet", "Werewolf Whisker", "Cursed Skull", "Dragon's Scale Shimmer", "Haunted Hay Bale", "Wraith's Tear", "Zombie Zest Zest",
           "Serpent Scale", "Wraith's Tear", "Cursed Crypt Key", "Dragon's Scale Shimmer", "Salamander's Tail", "Raven Feather", "Wolfsbane", "Frankenstein's Lab Liquid", "Zombie Zest Zest", "Cursed Skull",
           "Ghoulish Goblet", "Dragon's Scale Shimmer", "Cursed Crypt Key", "Wraith's Tear", "Black Cat's Meow", "Wraith Whisper"]

ingredients = ["Witch's Eye", "Bat Wing", "Ghostly Essence", "Toadstool Extract", "Vampire Blood", "Mandrake Root", "Zombie Brain", "Ghoul's Breath", "Spider Venom", "Black Cat's Whisker",
               "Werewolf Fur", "Banshee's Wail", "Spectral Ash", "Pumpkin Spice", "Goblin's Earwax", "Haunted Mist", "Wraith's Tear", "Serpent Scale", "Moonlit Fern", "Cursed Skull",
               "Raven Feather", "Wolfsbane", "Frankenstein's Bolt", "Wicked Ivy", "Screaming Banshee Berry", "Mummy's Wrappings", "Dragon's Breath", "Bubbling Cauldron Brew", "Gorehound's Howl", "Wraithroot",
               "Haunted Grave Moss", "Ectoplasmic Slime", "Voodoo Doll's Stitch", "Bramble Thorn", "Hocus Pocus Powder", "Cursed Clove", "Wicked Witch's Hair", "Halloween Moon Dust", "Bog Goblin Slime", "Ghost Pepper",
               "Phantom Firefly Wing", "Gargoyle Stone", "Zombie Toenail", "Poltergeist Polyp", "Spectral Goo", "Salamander Scale", "Cursed Candelabra Wax", "Witch Hazel", "Banshee's Bane", "Grim Reaper's Scythe",
               "Black Widow Venom", "Moonlit Nightshade", "Ghastly Gourd", "Siren's Song Seashell", "Goblin Gold Dust", "Spider Web Silk", "Haunted Spirit Vine", "Frog's Tongue", "Mystic Mandrake", "Widow's Peak Essence",
               "Wicked Warlock's Beard", "Crypt Keeper's Cryptonite", "Bewitched Broomstick Bristle", "Dragon's Scale Shimmer", "Vampire Bat Blood", "Graveyard Grass", "Halloween Harvest Pumpkin", "Cursed Cobweb Cotton", "Phantom Howler Fur", "Wraithbone",
               "Goblin's Green Slime", "Witch's Brew Brew", "Voodoo Doll Pin", "Bramble Berry", "Spooky Spellbook Page", "Halloween Cauldron Steam", "Spectral Spectacles", "Salamander's Tail", "Cursed Crypt Key", "Pumpkin Patch Spice",
               "Haunted Hay Bale", "Banshee's Bellflower", "Ghoulish Goblet", "Frankenstein's Lab Liquid", "Zombie Zest Zest", "Werewolf Whisker", "Gargoyle Gaze", "Black Cat's Meow", "Wolfsbane Extract", "Goblin's Gold",
               "Phantom Firefly Fizz", "Spider Sling Silk", "Widow's Weave", "Wraith Whisper", "Siren's Serenade", "Moonlit Mirage", "Spectral Spark", "Dragon's Roar", "Banshee's Banshee", "Witch's Whisper",
               "Ghoul's Groan", "Toadstool Tango", "Vampire's Kiss", "Bubbling Broth", "Mystic Elixir", "Cursed Charm"]

for item in correct:
    value = chr(ingredients.index(item) + 32)
    print(value, end="")
