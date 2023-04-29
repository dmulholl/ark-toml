# TOML Metadata for Ark

[1]: https://github.com/dmulholl/ark

This [Ark][1] plugin adds support for TOML file headers as an alternative to YAML.

    ~~~
    title = "Page Title"
    author = "John Doe"
    ~~~

You can install the plugin from the package index using `pip`:

    $ pip install ark-toml

Activate the plugin by adding `ark_toml` to the extensions list in your site's `config.py` file:

    extensions = ['ark_toml']

The plugin identifies TOML file headers by checking for three opening and closing tildes, `~`.
