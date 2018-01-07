![](https://travis-ci.org/fmv1992/vim_dictionary.svg?branch=dev)

# Vim_dictionary

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

# Requirements

* Vim >= 8.0
    * `+channel` support
    * `+python3` support

* `python3` itself.

# Installing

Install this plugin with your favorite plugin manager or use vim8's recommended package structure.

See `:tab help packages` in vim for details.

    cd ~/.vim/pack/foo/start
    git clone https://github.com/fmv1992/vim_dictionary
    cd vim_dictionary
    make install

`make install` will:

1. Download [Project Gutenberg ebook Webster's Unabridged Dictionary](http://www.gutenberg.org/ebooks/29765) and place it under `./download`.
1. Kindly generate helpfiles so you can `:help vim_dictionary` to find out more!

# Customizing

Three variables are customizable:

1. The height of the window with the lookup result.

        let g:vimdictionary_winheight = 10

1. The `winminheight` for the window with the lookup result.

        let g:vimdictionary_winminheight = 5

1. The persistence of the python3 server process if you have no vim instances running (it may speed up the initialization of your vim a little bit).

        let g:vimdictionary_persistent_server = 1

# Ideas for the future

1. Add windows support (make paths platform independent basically).
1. Expand possible dictionaries.
1. Support "pluggable" dictionaries (create a known python API for it).
1. Support bilingual dictionaries/thesaurus.

# License

[GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html).

<!---
# Advanced

## Testing

1. [✓] Stress test.
1. [✓] First word.
1. [✓] Last word.
1. [✓] Random words.

--->
## TODO

* If vim is called via root other it creates the dictionary file '/tmp/vim_dictionary.log' which cannot be overwritten.
* Add the option to let the python3 server idle even without vim instances.
