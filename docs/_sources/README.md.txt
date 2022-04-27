## How To Build

1. Complete commands:

```shell
**cd .sphinx

sphinx-apidoc --ext-autodoc --force -o  . ../TikTokPrinter

.\make html
```

3. Move generated sphinx `/sphinx/_build/html` folder to root, rename to "docs"
4. Add `.nojekyll` file to new docs folder