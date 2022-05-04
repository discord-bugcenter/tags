# HelpCenter - tags

Ce dépôt recense la liste des différents "tags" que vous pouvez utiliser via la commande `/tag` de HelpCenter sur le serveur Discord [Bug Center](https://discord.gg/nbmx3XW).

## Organisation du repo

Les tags sont au format [JSON](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation), vous les retrouverez dans le dossier `src`.  
Dans ce dossier, vous distinguerez divers dossiers : ils correspondent à la catégorie de chaque tag.
Chaque fichier JSON correspond à un tag.

Exemple:
Le fichier `src/general/contexte` correspond au tag "contexte" de la catégorie "general".

## Créer / contribuer aux tags

La syntaxe des fichiers de tag est assez simple.
Ils se composent obligatoirement d'un nom (clé : `name`), d'une description (clé : `description`) et d'une réponse (clé : `response`).  

La réponse sera très similaire à la requête faite pour envoyer un message sur Discord (avec par exemple des embeds).

Plus d'informations sur le format des messages : https://discord.com/developers/docs/resources/channel#create-message-jsonform-params

### Les 5 étapes pour contribuer : 

1. Rendez-vous sur [la version "web" de vscode](`https://github.dev/discord-bugcenter/tags).
2. Apportez directement vos modifications. Changez des textes, créez des tags...
3. Allez dans l'onglet `Source control` (Crtl+Shift+G) sur le côté gauche. Cliquez sur la coche 🗸 en haut de l'onglet. Un pop-up apparaît pour vous demandez de créer un fork du projet : faîtes le ! Vous serez ensuite redirigés.
4. En restant sur l'onglet `Source Control`, appuyez sur "Create Pull Request". Mettez un petit titre et une description pour présenter vos changements. Ensuite, appuyez sur "Create".
5. Votre demande de modification a été crée, nous la traiterons dans de plus brefs délais.


*TODO : préciser le fonctionnement des tags en plusieurs langues et la redondance des textes avec `"*"`*.
