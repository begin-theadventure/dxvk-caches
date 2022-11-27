# dxvk-caches
[DXVK caches to reduce stuttering!](https://github.com/doitsujin/dxvk#state-cache)

Feel free to contribute new caches or for merge with existing ones in:

*Note*: don't submit caches that have been upgraded from v10, as this may [cause crashes](https://github.com/doitsujin/dxvk/releases/tag/v2.0) with the latest v15 version.

[_issues_](https://github.com/begin-theadventure/dxvk-caches/issues/): search to see if the issue already exists, if not create a new one (preferably per one game), compress with zip and attach;

[_pull requests_](https://github.com/begin-theadventure/dxvk-caches/pulls): compress with zip and attach, change Readme.md (nick, entries and sha512sum of .dxvk-cache) or (if it's a new cache) add it to the appropriate directory (game or franchise->game) and add an empty name.dxvk-cache.md (I'll change it with my download link) if it doesn't exist (new game);

[_Discord_](https://discord.gg/RsYQ4UPwth): compress and send in #your-dxvk-caches channel.

[DxvkCacheHost](https://dxvkcachehost.codepotatoes.de): it's a site where you can upload your caches, although after adding a new cache if you can open an issue here or send a message on Discord to notify me.

Files are hosted [here](https://sam.nl.tab.digital/s/oZRKz5So2B8gbzY).

For merging and checking I'm using: [dxvk-cache-tool](https://github.com/DarkTigrus/dxvk-cache-tool)

sha512sums apply to .dxvk-cache, not compressed files.

# F A Q
## How to get
To get all caches try [TUTORIAL](https://github.com/begin-theadventure/get-dxvk-caches/blob/main/script/TUTORIAL.md) or just ctrl+f->.dxvk-cache in x directory.
## How to use
Extract .tar.xz file to get .dxvk-cache->paste to x directory.

There are also:

[DXVKoTool](https://github.com/DATL4G/DXVKoTool/releases) application by [DATL4G](https://github.com/DATL4G). Works best for Steam games.

[DxvkCacheHost](https://dxvkcachehost.codepotatoes.de) site by [Crashdummy](https://git.codepotatoes.de/Crashdummy/DxvkCachehost) however it doesn't have every cache from this repo.
## Directories
**Wine**: next to .exe or specified path with [environment variable](https://github.com/doitsujin/dxvk#state-cache).

**Steam**: `/path/to/steamapps/shadercache/APPID/DXVK_state_cache` default is `~/.local/share/..` or next to .exe if shader pre-caching is turned off. 

To find out which ID corresponds to a particular game, simply search it on [Steam](https://store.steampowered.com/search/) (app/**ID**/name).
## Security
Read [dxvk/issues/764](https://github.com/doitsujin/dxvk/issues/764)

If you're concerned, use [dxvk-async](https://github.com/Sporif/dxvk-async) instead but it won't give as much of a performance boost as a (especially mature) precompiled state cache.
## Cache versions
Some state cache versions break compatibility and therefore can't be merged with older ones, but DXVK can update them including entries however it can't do a downgrade e.g. v15->v10 and in that case it starts with 0 entries.

Be aware that using v10 caches (v11-v14 are recognized as v10) with DXVK 2.0+ might result in crashes, for more info read: [State cache interactions](https://github.com/doitsujin/dxvk/releases/tag/v2.0).

v10 caches (up to DXVK 1.10.3) are in [another branch](https://github.com/begin-theadventure/dxvk-caches/tree/v10).
