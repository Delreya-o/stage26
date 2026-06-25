# Présentation
***
**Objectif** : créer un petit site répertoriant des livres

**Motivation** : apprendre à géré Django, Vue.js avec d'autres outils comme MariaDB dans le cadre d'un stage
### Phase 1 : Mise en place du backend & frontend

### Phase 2 : Création et affichage de formulaires
# Installation
***
#### OpenBao
> https://github.com/openbao/openbao/releases/tag/v2.6.0-beta20260622
```
tar xzf <archive-openbao>.tar.gz
sudo mv bao /usr/local/bin/
sudo chmod +x /usr/local/bin/bao
```

#### MariaDB
> https://medium.com/code-zen/django-mariadb-85cc9daeeef8
```
sudo apt install mariadb-server
```

- Créer un utilisateur
```
CREATE OR REPLACE USER user@localhost IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON myprojectdb.* TO 'user'@'localhost';
FLUSH PRIVILEGES;
```

# Lancement
***
> [!Note]
> **Environnement**
> ```
> python3 -m venv .venv
> source .venv/bin/activate
> pip install -r requirements.txt
> ```

**BDD**
```bash
sudo systemctl start openbao
sudo systemctl start mariadb.service
```

**Lancer l'UI**
```bash
python3 mylibrary/manage.py runserver
```

# Création d'un superuser
***
```bash
python3 mylibrary/manage.py createsuperuser
```
--> `user`, `user@email.fr`, `password`