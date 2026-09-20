# Cause: `race-condition`

timing or ordering issue in daemon or reader

> Generated from database commit `37e1jc5hc9ma`. 3 analysed issues carry this cause. [Back to index](../index.md)

| Issue | State | Title | Summary |
|---|---|---|---|
| [#197](https://github.com/sezanzeb/input-remapper/issues/197) | CLOSED | Keyboard/mouse not working after reboot on arch based distros | Arch/KDE+Bluetooth: keyboard and mouse stop working after reboot until udev timeout expires. Root: udev rule fires key-mapper-control before the service is ready to accept D-Bus connections; D-Bus call blocks until udev… |
| [#274](https://github.com/sezanzeb/input-remapper/issues/274) | OPEN | Buttons do not work after restart | Logitech MX Anywhere 2 Bluetooth: autoload doesn't work after reboot on Ubuntu. Multiple reporters. Root: udev rule fires with empty DEVNAME for Bluetooth devices; service doesn't find device at the provided path. Worka… |
| [#276](https://github.com/sezanzeb/input-remapper/issues/276) | CLOSED | Crashes after a short amount of time with rapid keypressing. | Razer Tartarus Pro: injection crashes with "tuple has no attribute press_trigger" when rapidly pressing mapped keys. Race condition in keycode_mapper: macro object was replaced by a tuple during press handling. Fixed in… |
