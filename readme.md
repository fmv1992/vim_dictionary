![https://travis-ci.org/fmv1992/vim_dictionary.svg?branch=dev]
# Vim_dictionary

Add a dictionary functionality to your vim. It requires vim8 and the features `+channel` and `+python3`.

Example:

    Dictionary noxious

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

# Requirements

It requires vim8 and the features `+channel` and `+python3`.
It requires python3 to be installed as well.

# Installing

Install this plugin with your favorite plugin manager or use vim8 recommended package structure.

See `:tab help packages` in vim for details.

    cd ~/.vim/pack/foo/start
    git clone https://github.com/fmv1992/vim_dictionary
    cd vim_dictionary
    make install

This will download [Project Gutenberg ebook Webster's Unabridged Dictionary](http://www.gutenberg.org/ebooks/29765) and place it under `./download`.

# Customizing

# Troubleshooting

## Advanced

## Testing

1. Stress test.
1. First word.
1. Last word.
1. Random words.

## TODO

1. BUG: sometimes vim hangs and the server is not killed...
1. Write a decent help file.
1. Write a small makefile.
    1. Check eligibility for plugin installation.
    1. Download dictionary.
    1. Execute tests.
1. Fold everything!
1. Write python docstrings.
