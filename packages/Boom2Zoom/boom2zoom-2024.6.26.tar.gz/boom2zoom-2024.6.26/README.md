# Boom2Zoom

A CLI tool that extracts assets from a Doom WAD to a directory in [ZDoom archive format](https://zdoom.org/wiki/Using_ZIPs_as_WAD_replacement).

This project was originally started to convert dump Doom texture packs.
It is written in Python and uses [omgifol](https://github.com/devinacker/omgifol) to load data from WADs.


## Features

- Textures and flats are exported to PNGs under the `textures` and `flats` folders respectively.
- Stock textures are filtered out by *content* using a set of known texture digests (more on this below).
- `ANIMATED` and `SWITCHES` are converted into `ANIMDEFS` syntax.
    - Definitions from various Doom-engine games are omitted.
    - Animations are fully defined with `PIC`, but you can opt out and use `RANGE` instead.

## Installation

### Windows <span title="Boom2Zoom is developed on Windows.">♿</span>

A binary is available under releases.
Download and make sure it's in your PATH.
This is the quickest and simplest way to use Boom2Zoom on Windows.

### Pipx

You can use Boom2Zoom via [pipx](https://pipx.pypa.io/stable/).

```shell
pipx install boom2zoom
```

Of course, you can also install it directly with pip if you know what you are doing. Just be careful.

## Quick-start

Let's first test that B2Z is installed correctly:

```shell
boom2zoom --help
```

At a minimum, you need to provide a wad and the directory to dump its assets into.

```shell
boom2zoom OTEX_1.1.wad otex
```

Textures need patches to be exported. B2Z will warn if there are patchy textures.

## Texture Filtering

_Note: When talking about textures, we are strictly speaking about [wall textures](https://doomwiki.org/wiki/Texture)._

Boom2Zoom only checks textures for infringement, not flats!
If there are stock flats in the WAD, they will be exported.

### Details

A WAD with custom textures usually contains redefinitions of stock ones.
You probably do not want these, and they are copyright infringing.
To help you not break the law, Boom2Zoom spots stock textures and won't emit them.
It spots them by seeing if the digest of the texture is the same as a stock one.
This digest comes from hashing the raw pixel values of the texture.

B2Z knows the texture digests of the main Doom games, Freedoom, Heretic, Chex 3, and Hexen.
