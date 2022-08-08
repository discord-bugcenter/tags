from typing import Any

from pydantic import AnyHttpUrl, BaseModel, Extra, Field, root_validator


class TagEmbedFieldPayload(BaseModel, extra=Extra.forbid):
    name: str = Field(..., description="The name of the field.")
    value: str = Field(..., description="The value of the field.")
    inline: bool = Field(False, description="Whether the field should be displayed inline.")


class TagEmbedPayload(BaseModel, extra=Extra.forbid):
    title: str = Field(..., description="The title of the embed.")
    description: str | None = Field(None, description="The description of the embed.")
    image: AnyHttpUrl | None = Field(None, description="The image of the embed.")
    thumbnail: AnyHttpUrl | None = Field(None, description="The thumbnail of the embed.")
    fields: list[TagEmbedFieldPayload] = Field(default_factory=list, description="The fields of the embed.")


class TagAttachmentsPayload(BaseModel, extra=Extra.forbid):
    filename: str = Field(..., description="The filename of the attachment.")
    description: str | None = Field(None, description="The description of the attachment.")
    url: AnyHttpUrl = Field(..., description="The url of the attachment.")


class TagPayload(BaseModel, extra=Extra.forbid):
    name: str = Field(..., description="The name of the tag.")
    description: str = Field(..., description="The description of the tag.")
    content: str | None = Field(None, description="The content of the tag.")

    embeds: list[TagEmbedPayload] = Field(default_factory=list, description="The embeds of the tag.")
    attachments: list[TagAttachmentsPayload] = Field(default_factory=list, description="The attachments of the tag.")

    @root_validator()
    def validate_attachments(cls, values: dict[str, Any]) -> dict[str, Any]:
        if not values["content"] and not values["embeds"]:
            raise ValueError("Tag must have either content or embeds, or both.")
        return values


with open("test.json", "w") as f:
    f.write(TagPayload.schema_json(indent=4))
