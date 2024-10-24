# New World Database Data Extractor

### Comment ça marche ?
L'outil extrait automatiquement la liste des items, perks et compétences présentes sur le site nwdb.info.

Afin d'utiliser l'outil, il faut python 3 d'installé sur la machine et installer les dépendances du projet
`pip install -r requirements.txt`

Il faut ensuite renomer _**.env.dist**_ en **.env** et remplir les variables demandées.

Les variables correspondent au lien vers l'API, ainsi que le compte utilisateur admin que vous avez défini.

### Exemple de fichier .env :

```
API_URL="https://api.new-world-tools.fr"
API_USERNAME="admin"
API_PASSWORD="password"
```
