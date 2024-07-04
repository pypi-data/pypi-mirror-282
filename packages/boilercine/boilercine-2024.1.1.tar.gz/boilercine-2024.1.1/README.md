# boilercine

[![All Contributors](https://img.shields.io/github/all-contributors/blakeNaccarato/boilercine?color=ee8449&style=flat-square)](#contributors)

Convert CINEs for a boiling study.

Install the dependencies of this package manually.

```Shell
pip install --no-deps git+https://github.com/ottomatic-io/pycine@815cfca06cafc50745a43b2cd0168982225c6dca
pip install opencv-python  # Or a different flavor of your choice, e.g. `opencv-contrib-python`
pip install git+https://github.com/blakeNaccarato/boilercine@main
```

I did not add pycine explicitly to requirements because this package relies on an unreleased commit of pycine. Install it without its dependencies to avoid forcing installation of a particular flavor of OpenCV. The `opencv-python` package is a good choice for most users, but you could use `opencv-contrib-python` as well. I reproduce all of its other dependencies as the dependencies of this package.

## Project information

- [Changes](<https://blakeNaccarato.github.io/boilercine/changelog.html>)
- [Docs](<https://blakeNaccarato.github.io/boilercine>)
- [Contributing](<https://blakeNaccarato.github.io/boilercine/contributing.html>)

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- ALL-CONTRIBUTORS-LIST:END -->
