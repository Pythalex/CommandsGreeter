# Commands Greeter

A simple greeter with useful commands for linux.

## How to use

To add a greeter on linux, you can add whatever you want at the end of /etc/profile. Each time you will open a new terminal, it will print the text.

## What's the specifity of your greeter ?

The original idea of this repo was to save my own greeters. But it could interest other people as well. I like adding a small box frame around my greeter. I also created a small patcher to easily add special frames and try several themes.

## How to make my own good greater and themes ?

If you want to have something like the example greeter. Just create a txt file with the greeter you would like. For the frame locations, use the following special characters :

    'Ȁ' up left
    'Ȃ' down left
    'Ȅ' up right
    'Ȇ' down right
    'Ȋ' horizontal
    'Ȉ' vertical

Then create or download a box theme of the following format:

    [up left char] [down left char] [up right char] [down right char] [horizontal char] [vertical char]

Then use the patcher script like this:

    python patcher.py greeterfile boxtheme outputfilename

for example :

    greeterfile

    ȀȈȈȈȈȈȈȈȄ
    Ȋ hello Ȋ
    ȂȈȈȈȈȈȈȈȆ


    boxtheme

    ╔ ╚ ╗ ╝ ║ ═


    output

    ╔═══════╗
    ║ hello ║
    ╚═══════╝

Feel free to create beautiful box themes for astounding greeters.