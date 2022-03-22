# tags
Ce repository ressence la liste des tags qui peuvent être visibles dans la commande /tag sur [Bug Center](https://discord.gg/nbmx3XW).

## Organisation du repo
Les tags sont disponibles, au format json, dans le dossier `src/`.  
Dans ce dossier ce trouve d'autres dossiers : ceux-ci correspondent à la catégorie du tag.  
Chaque fichier json correspond à un tag.  

## Créer / contribuer aux tags
La syntaxe des fichiers tags est assez simple. Ils se composent obligatoirement d'un nom (`name`), d'une description (`description`) et d'une réponse (`response`).  
La réponse sera très similaire à la requête faite pour envoyer un message sur Discord (avec par exemple des embeds).

> Ceci n'a pas été testé et le "guide" pour contribuer pourra être amené à changer.

Pour contribuer simplement, vous pouvez vous rendre sur [la version "web" de vscode](`https://github.dev/discord-bugcenter/tags`) et apporter directement vos modifications. Il ne vous restera plus qu'à les "envoyer" à partir de l'onglet "git" sur le côté, en faisant un "commit" de vos changements, puis en ouvrant une "pull request".

*TODO : préciser le fonctionnement des tags en plusieurs langues et la redondance des textes avec `"*"`*.
