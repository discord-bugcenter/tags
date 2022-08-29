# Tags

La principale source des **tags** disponibles sur [Help Center](https://github.com/discord-bugcenter/helpcenter).

Un "tag" est une ressource décrivant un message et son contenu, permettant aux membres
de Bug Center de rapidement pouvoir envoyer des messages d'informations.

## Contribution

### Structure du projet

Le projet est structuré selon certains critères, permettant de pouvoir facilement récupérer
les données utilisées pour un Bot.

Chaque tag correspond à un fichier TOML situé dans un sous-dossier de `src`.
Chaque sous-dossier de `src` correspond à une "catégorie", un moyen de classifier *indirectement*
les tags.

Ainsi, `src/foo/bar.toml` correspond au fichier source d'un tag nommé "bar", de la catégorie "foo".

### Comprendre le schéma d'un tag

Un tag est un fichier [TOML](https://github.com/toml-lang/toml), un langage simple
et puissant permettant la création de données rapidement.

Le schéma même d'un tag est décrit par le fichier [schema.json](schema.json) à la racine du projet.
Ce fichier JSON est la seule source de vérité du schéma d'un tag.

Le fichier schéma suit le standard [JSON Schema](https://json-schema.org/), permettant
à différents outils de proposer de l'autocomplétion et de la validation à partir du contenu du schéma.


Un tag est constitué de cinq propriétés :

- `name`: le nom du tag,
- `description`: une description courte du tag,
- `content`: le contenu message du tag, envoyé comme un message classic sur Discord,
- `embeds`: une liste d'"embeds", étant envoyés comme des Embeds sur Discord,
- `attachments`: des fichiers/images à envoyer avec le message sur Discord.

Par défaut, seul `name` et `description` sont requis.

Par exemple :

```toml
name = "hello_world"
description = "Un tag d'exemple!"
content = """
Contenu du message
sur
plusieurs lignes.
"""
```

### Ajouter/Modifier un tag

Pour ajouter ou modifier un tag, vous devez d'abord créer un fork de ce repo Git, et le clone.
Après cela, il vous suffira de créer un fichier TOML dans un sous-dossier (une catégorie) de `src` si vous 
souhaitez ajouter un tag, sinon il vous suffira de modifier le fichier existant correspondant.

Une fois l'ajout terminé, vous pouvez commit et ouvrir une Merge Request sur ce repo.