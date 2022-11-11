# dxvk-caches
[DXVK caches to reduce stuttering!](https://github.com/doitsujin/dxvk#state-cache)

Feel free to contribute new caches or for merge with existing ones in:

[_issues_](https://github.com/begin-theadventure/dxvk-caches/issues/): search to see if the issue already exists, if not create a new one (per game), paste the download link or compress with zip and attach;

[_pull requests_](https://github.com/begin-theadventure/dxvk-caches/pulls): paste the download link or compress with zip and attach, change Readme.md (nick, entries and sha512sum) or add it to a proper directory (game or franchise->game) and add empty name.dxvk-cache.md (I'll change it with my download link) if it doesn't exist (new game);

[_Discord_](https://discord.gg/RsYQ4UPwth): compress and send in #your-dxvk-caches channel.

Files are hosted [here](https://sam.nl.tab.digital/s/oZRKz5So2B8gbzY).

For merging and checking I'm using: [dxvk-cache-tool](https://github.com/DarkTigrus/dxvk-cache-tool)

sha512sums apply to .dxvk-cache, not compressed files.

# F A Q
## How to get
To get all caches try [TUTORIAL](https://github.com/begin-theadventure/get-dxvk-caches/blob/main/script/TUTORIAL.md) or just ctrl+f->.dxvk-cache in x directory.
## How to use
Extract .tar.xz file to get .dxvk-cache->paste to x directory.
## Directories
**Wine**: next to .exe or specified path with [environment variable](https://github.com/doitsujin/dxvk#state-cache).

**Steam**: `/path/to/steamapps/shadercache/APPID/DXVK_state_cache` default is `~/.local/share/..` or next to .exe if shader pre-caching is turned off. 

To find out which ID corresponds to a particular game, simply search it on [Steam](https://store.steampowered.com/search/) (app/**ID**/name).
## Security
Read [dxvk/issues/764](https://github.com/doitsujin/dxvk/issues/764)

If you're concerned, use [dxvk-async](https://github.com/Sporif/dxvk-async) instead but it won't give as much of a performance boost as a (especially mature) precompiled state cache.
## Cache versions
Some state cache versions break compatibility and therefore can't be merged with older ones but DXVK can update them including entries however it can't do a downgrade e.g. v15->v10 and in that case it starts with 0 entries.

After v15 I [decided](https://github.com/begin-theadventure/dxvk-caches/discussions/39) to write "State cache version: vX" at the top of the Readme.

Every cache is compatible with versions v10 (v11-14 is v10), unless noted.

*Warning*:

If you want to use DXVK 2.0+ don't use older cache versions (v10 down), read [State cache interactions](https://github.com/doitsujin/dxvk/releases/tag/v2.0) for more info.
