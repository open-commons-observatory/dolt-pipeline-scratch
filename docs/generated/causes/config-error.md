# Cause: `config-error`

wrong user configuration

> Generated from database commit `37e1jc5hc9ma`. 5 analysed issues carry this cause. [Back to index](../index.md)

| Issue | State | Title | Summary |
|---|---|---|---|
| [#17](https://github.com/sezanzeb/input-remapper/issues/17) | CLOSED | Wrong user in systemd daemon | User alarmed that get_user() returned root in systemd daemon on Arch+Wayland+GNOME. Maintainer stated this is expected and normal; the injection uses the user config via D-Bus. Docs gap: expected daemon behavior not doc… |
| [#28](https://github.com/sezanzeb/input-remapper/issues/28) | CLOSED | _gtk_style_provider_private_get_settings assertion failed | GUI crashed on Arch with GTK assertion error. Root cause: user had symlinked sudo to doas which lacks X11 DISPLAY access when used with pkexec. Maintainer added Gtk.init() call but ultimately resolved when user installe… |
| [#123](https://github.com/sezanzeb/input-remapper/issues/123) | CLOSED | Multiple devices with same name share the same macros | Two identical joysticks (Thrustmaster T.16000M) share the same preset files. User confused that selecting device 2 shows device 1's mappings. Maintainer explained design: presets shared by model, different mappings via… |
| [#216](https://github.com/sezanzeb/input-remapper/issues/216) | CLOSED | loading configuration failed | User confused "keymapper" (https://github.com/houmain/keymapper) with input-remapper. Different project, one letter difference in name. Maintainer identified the confusion and closed. |
| [#258](https://github.com/sezanzeb/input-remapper/issues/258) | OPEN | Alphanumeric events not working without prefixing KEY_ | Alphanumeric keys stopped working without KEY_ prefix after migrating config to new install. Root: xmodmap.json was empty (copied from previous system where it may have been populated differently). input-remapper-gtk po… |
