# Auto updating biography of Github
Script for auto-updating the bio / readme.
> [!NOTE]
> It uses:
>- .yml file. For setting up the _free_ and _online_ ubuntu environment.
>- Python script. For getting the current time at Madrid and concatenating the last _changing_ phrase with the other phrases.
>- [Github Actions](https://docs.github.com/es/actions). For automating the script at the ubuntu environment.
>- [Github token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) with personal access and permissions. For accesing my User and getting permissions to change my Biography.
>- [Github secrets](https://docs.github.com/es/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions). For keeping my personal token safe and private.

If you create one for yourself, you can copy this repository. You would only have to change my username at the files (jotaaloud), create your own personal token and putting it in your secrets file, at the same repo.

Feel free to [open an issue](https://github.com/jotaaloud/autoUpdatingBio/issues) at this repository if you have any doubts!

[![Execute the update script](https://github.com/jotaaloud/autoUpdatingBio/actions/workflows/instructions.yml/badge.svg)](https://github.com/jotaaloud/autoUpdatingBio/actions/workflows/instructions.yml)
[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](LICENSE)
