# oTree

## Live demo
http://demo.otree.org/

## Homepage
http://www.otree.org/

## About

oTree is a Django-based framework for implementing multiplayer decision strategy games.
Many of the details of writing a web application are abstracted away,
meaning that the code is focused on the logic of the game.
oTree programming is accessible to programmers without advanced experience in web app development.

This repository contains the games; the oTree core libraries are [here](https://github.com/oTree-org/otree-core).

## Quick start

```
pip install -r requirements_base.txt
otree resetdb
otree runserver
```

## Heroku
This version of oTree is being continuously tested on TravisCI and
deployed on Heroku at http://leeps-otree.herokuapp.com.

To get into the machine run the following commands:
```
heroku login
heroku run bash --app leeps-otree
```

If site asks to run ```otree resetdb``` run the following commands:
```
heroku login
heroku run otree resetdb --app leeps-otree
```

## Contact
chris@otree.org (you can also add me on Skype by searching this email address; please mention oTree in your contact request)

**Please contact me if any part of oTree does not work for you (or is unclear).**

## Contributors

* Juan B. Cabral (http://jbcabral.org/, https://github.com/leliel12)
* Gregor Muellegger (http://gremu.net/, https://github.com/gregmuellegger)
* Alexander Schepanovski (https://github.com/Suor/)
* Alexander Sandukovskiy
* Som Datye

## Mailing list
[Help & discussion mailing list](https://groups.google.com/forum/#!forum/otree)

# Docs

http://otree.readthedocs.org

# Status

![RTD Badge](https://readthedocs.org/projects/otree/badge/?version=latest)
