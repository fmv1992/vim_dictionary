![](https://travis-ci.org/fmv1992/vim_dictionary.svg?branch=dev)

# Vim_dictionary

Enable dictionary capabilities within vim.

## Screencast

See it in action:

[![asciicast](https://asciinema.org/a/s9Gk1QCcPBwjM4OAxViNIlUoR.png)](https://asciinema.org/a/s9Gk1QCcPBwjM4OAxViNIlUoR)

## Description

Add a dictionary functionality to your vim. It requires vim8 and the features `+channel` and `+python3`.

Example:

    :Dictionary noxious

Will give you:

    NOXIOUS
    Nox"ious, a. Etym: [L. noxius, fr. noxa harm; akin to nocere to harm,
    hurt. Cf. Nuisance, Necromancy.]

    1. Hurtful; harmful; baneful; pernicious; injurious; destructive;
    unwholesome; insalubrious; as, noxious air, food, or climate;
    pernicious; corrupting to morals; as, noxious practices or examples.
    Too frequent an appearance in places of public resort is noxious to
    spiritual promotions. Swift.

    2. Guilty; criminal. [R.]
    Those who are noxious in the eye of the law. Abp. Bramhall.

    Syn.
    -- Noisome; hurtful; harmful; injurious; destructive; pernicious;
    mischievous; corrupting; baneful; unwholesome; insalubrious. See
    Noisome.
    -- Nox"ious*ly, adv.
    -- Nox"ious*ness, n.

That's it, this is a [KISS](https://en.wikipedia.org/wiki/KISS_principle) plugin.

You can check for details [here](https://github.com/fmv1992/vim_dictionary/blob/dev/doc/vim_dictionary.txt#L72).

## Requirements

*   Vim >= 8.0
    *   `+channel` support.
    *   `+python3` support.

*   `python3` itself.

*   `wiktionaryparser` for optional online and multi-lingual support.

## Installing

Install this plugin with your favorite plugin manager or use vim8's recommended package structure.

See `:tab help packages` in vim for details.

    cd ~/.vim/pack/foo/start
    git clone https://github.com/fmv1992/vim_dictionary
    cd vim_dictionary
    make install

`make install` will:

1. Download [Project Gutenberg ebook Webster's Unabridged Dictionary](http://www.gutenberg.org/ebooks/29765) and place it under `./download`.

1. Kindly generate helpfiles so you can `:help vim_dictionary` to find out more!

## Customizing

After installing you can check out the available customizations with: `:help vim_dictionary-variables`.

## Debugging

Close all your vim instances and execute:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
python3 ./vim_dictionary/vim_dictionary_server.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See the live log. Also see the output file on `/tmp/vim_dictionary.log`.

### Known bugs

1.  This program does not work in [cygwin](https://cygwin.com/). Something about permission errors when starting the python TCP server:

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Traceback (most recent call last):
        File "./vim_dictionary/vim_dictionary_server.py", line 126, in <module>
            server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
        File "/usr/lib/python3.6/socketserver.py", line 450, in __init__
            self.socket_type)
        File "/usr/lib/python3.6/socket.py", line 144, in __init__
            _socket.socket.__init__(self, family, type, proto, fileno)
        PermissionError: [Errno 1] Operation not permitted
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    and getting sockets in `channel_open()` in vim:

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        E898: socket() in channel_open(): Operation not permitted
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Ideas for the future

After installing see the `:help vim_dictionary-next-steps`.

## License

[GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html).

[comment]: # ( vim: set filetype=markdown fileformat=unix wrap spell spelllang=en_us: )
