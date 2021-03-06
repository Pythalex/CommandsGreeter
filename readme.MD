# Commands Greeter

A simple greeter with useful commands for linux.

    ╔═══════════════════════════════════════════════════════════════════════════════════╗
    ║ SEARCH                                  SSH                                       ║
    ║ ══════                                  ═══                                       ║
    ║ grep pattern file                       ssh user@host                             ║
    ║ grep -r pattern dir                     ssh -p port user@host (using port p)      ║
    ║ command | grep pattern                  ssh -D port user@host (use bind port)     ║
    ║ locate file                             NETWORK                                   ║
    ║ PROCESS                                 ═══════                                   ║
    ║ ═══════                                 whois domain                              ║
    ║ ps aux                                  dig domain = get DNS for domain           ║
    ║ kill pid                                dig -x host = reverse looking             ║
    ║ killall proc                            wget file = download                      ║
    ║ bg = list stopped/backgrouned           wget -c file continue stopped             ║
    ║ fg bring most recent job                SYSTEM                                    ║
    ║ fg -n bring job n                       ══════                                    ║
    ║ COMPRESSION                             date                                      ║
    ║ ═══════════                             cal                                       ║
    ║ tar cf file.tar files compress files    df show disk usage                        ║
    ║ tar xf file.tar untar into cd           du show disk directory space usage        ║
    ║ tar tf file.tar show content            du -sh human readable size in GB          ║
    ║ flags                                   free = show memory and swap usage         ║
    ║ c create          | j bzip2             whereis app ═ show location               ║
    ║ t table of content| k don't ow          SHORTCUTS                                 ║
    ║ x extract         | T files from file   ═════════                                 ║
    ║ f specifies filen | w ask for confirm   ctrl d log out                            ║
    ║ z use zip/gzip    | v verbose           ctrlw erase one word in current line      ║
    ║                                         ctrl u erase whole line                   ║
    ║                                         ctrl r reverse look up of previous command║
    ║                                         !! repeat last command                    ║
    ╚═══════════════════════════════════════════════════════════════════════════════════╝

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
    'Ȉ' vertical
    'Ȋ' horizontal

Then create or download a box theme of the following format:

    [up left char] [down left char] [up right char] [down right char] [horizontal char] [vertical char]

Then use the patcher script like this:

    python patcher.py greeterfile boxtheme outputfilename

for example :

    greeterfile

    ȀȊȊȊȊȊȊȊȄ
    Ȉ hello Ȉ
    ȂȊȊȊȊȊȊȊȆ


    boxtheme

    ╔ ╚ ╗ ╝ ║ ═


    output

    ╔═══════╗
    ║ hello ║
    ╚═══════╝

Feel free to create beautiful box themes for astounding greeters.