# tags
Ce repository ressence la liste des tags qui peuvent être visibles dans la commande /tag sur [Bug Center](https://discord.gg/nbmx3XW).

## Organisation du repo
Les tags sont disponibles, au format json, dans le dossier `src/`.  
Dans ce dossier ce trouve d'autres dossiers : ceux-ci correspondent à la catégorie du tag.  
Chaque fichier json correspond à un tag.  

## Créer / contribuer aux tags
La syntaxe des fichiers tags est assez simple. Ils se composent obligatoirement d'un nom (`name`), d'une description (`description`) et d'une réponse (`response`).  
La réponse sera très similaire à la requête faite pour envoyer un message sur Discord (avec par exemple des embeds).

### Les 5 étapes pour contribuer : 
1. Rendez-vous sur [la version "web" de vscode](`https://github.dev/discord-bugcenter/tags).
2. Apporter directement vos modifications. Changez des textes, créer des commandes...
3. Allez dans l'onglet `Source control` (Crtl+Shift+G) sur le côté gauche. Cliquez sur le petit ✔️ en haut de l'onglet. Une pop-up apparaît pour vous demandez de créer un fork du projet : faîtes le ! Vous serez ensuite redirigés.
4. De nouveau sur l'onglet `Source Control`, appuyez sur "Create Pull Request". Mettez un petit titre et une description pour présenter vos changements. Ensuite, appuyez sur "Create".
5. Voilà, c'est tout !


*TODO : préciser le fonctionnement des tags en plusieurs langues et la redondance des textes avec `"*"`*.
