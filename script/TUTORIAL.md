Easy way to get all .dxvk-cache.

[get-dxvk-caches.sh](https://github.com/begin-theadventure/dxvk-caches/releases/download/1.0.1/get-dxvk-caches.sh)

### GUI:

Download script->edit it->["directoryhere"](https://github.com/begin-theadventure/dxvk-caches#directories)->make it executable->use it.

### Terminal:

_(no need for downloading)_

mkdir dxvk

find ["directoryhere"](https://github.com/begin-theadventure/dxvk-caches#directories) -iname "*dxvk-cache" -exec cp "{}" dxvk \;

**Your caches will be copied to dxvk folder, that's all!**

Credit: TAKYON (commands), [xVanjaZ](https://github.com/xVanjaZ) ([spaces](https://github.com/begin-theadventure/dxvk-caches/commit/38b1e941d7705a4577d39274bb4072e1e39b34e0) fix).
